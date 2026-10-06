"""AI take-up analysis: keyword rules as registered, aggregation, and recovery of a known effect."""
import argparse

import numpy as np
import pandas as pd
import pytest

from ai_takeup import aggregate, mentions

PMKISAN, BIGHAAT = "com.nic.project.pmkisan", "com.BigHaat"


@pytest.mark.parametrize("text,pkg,expected", [
    ("The AI advice was correct", "x", (1, 1)),
    ("very nice ai", "x", (0, 0)),                      # "AI" counts only in capitals
    ("AIR quality and FAIR price", "x", (0, 0)),        # ... and only as a separate word
    ("A.I. based app", "x", (1, 1)),
    ("Chatbot replies fast", "x", (1, 1)),
    ("chat   bot is slow", "x", (1, 1)),                 # spaces inside a term match any whitespace
    ("the Bot is useless", "x", (1, 1)),
    ("robot and bottle", "x", (0, 0)),                   # word boundaries for Latin terms
    ("used chatgpt instead", "x", (1, 1)),
    ("crop doctor is good", BIGHAAT, (1, 1)),
    ("crop doctor is good", "x", (0, 0)),                # feature names count only in their own app
    ("kisan e-mitra solved it", PMKISAN, (1, 1)),
    ("went to e-mitra kiosk", PMKISAN, (0, 0)),          # plain e-Mitra is not counted
    ("एआई से पूछा", "x", (1, 1)),
    ("ऐप में चैटबॉट है", "x", (1, 1)),
    ("upload photo of leaf", "x", (0, 1)),               # M2 only
    ("फोटो डालो", "x", (0, 1)),
    ("photos", "x", (0, 0)),                             # whole words only, as registered
    ("", "x", (0, 0)),
    (np.nan, "x", (0, 0)),
])
def test_mentions(text, pkg, expected):
    assert mentions(text, pkg) == expected


def test_aggregate_months_and_window(tmp_path):
    rows = [  # package, at_utc, score, content, lang, lang_main
        ("a", "2023-03-31T20:00:00+00:00", 5, "AI is good", "eng", "eng"),       # 01:30 IST on 1 April
        ("a", "2023-04-10T08:00:00+00:00", 3, "बहुत अच्छा", "hin", "hin"),
        ("a", "2023-04-11T08:00:00+00:00", 1, "photo nahi hua", "hin", "eng"),   # mixed review
        ("a", "2026-10-01T08:00:00+00:00", 4, "AI", "eng", "eng"),               # after the last full month
        ("a", "2015-12-01T08:00:00+00:00", 4, "AI", "eng", "eng"),               # before Jan 2016
    ]
    df = pd.DataFrame(rows, columns=["package", "at_utc", "score", "content", "lang", "lang_main"])
    df["reviewId"] = [f"r{i}" for i in range(len(df))]
    df["fetched_utc"] = "2026-10-06T00:46:33+00:00"
    inp, out = tmp_path / "reviews_lang.csv", tmp_path / "agg.csv"
    df.to_csv(inp, index=False)
    g = aggregate(inp, out).set_index(["month", "lang_main", "lang"])
    assert set(g.index.get_level_values("month")) == {"2023-04"}
    assert g.loc[("2023-04", "eng", "eng"), ["n", "m1", "m2", "stars_sum"]].tolist() == [1, 1, 1, 5]
    assert g.loc[("2023-04", "eng", "hin"), ["n", "m1", "m2"]].tolist() == [1, 0, 1]
    assert "content" not in pd.read_csv(out).columns
    from ai_takeup import term_counts
    tc = term_counts(df).set_index("term")
    assert tc.loc["AI (capitals)", ["english", "indian"]].tolist() == [3, 0]
    assert tc.loc["photo", ["english", "indian"]].tolist() == [1, 0]


def fake_aggregate(path, effect_eng=4.0, effect_ind=2.0, gap_stars=-0.3, seed=11):
    """App x month x language counts with known take-up: the post-launch rise in the share mentioning AI is
    effect_eng pp in English and effect_ind pp in Indian-language reviews."""
    rng = np.random.default_rng(seed)
    months = pd.period_range("2019-01", "2023-12", freq="M").astype(str)
    launch = {f"sim.app{i:02d}": m for i, m in enumerate(["2020-06", "2021-01", "2021-07", "2022-01", "2022-06", "2023-01"])}
    rows = []
    for i in range(14):
        pkg = f"sim.app{i:02d}"
        for m in months:
            post = pkg in launch and m >= launch[pkg]
            for lang, lang_main, mean_n, eff in (("eng", "eng", 60, effect_eng), ("hin", "hin", 40, effect_ind),
                                                 ("tam", "tam", 10, effect_ind), ("hin", "eng", 8, effect_eng),
                                                 ("und", "und", 5, 0.0)):
                n = int(rng.poisson(mean_n))
                p = 0.01 + post * eff / 100
                m1 = int(rng.binomial(n, p))
                stars = 4.0 + gap_stars * (lang_main not in ("eng", "und"))
                rows.append({"package": pkg, "month": m, "lang_main": lang_main, "lang": lang, "n": n, "m1": m1,
                             "m2": m1 + int(rng.binomial(n - m1, 0.02)),
                             "stars_sum": float(np.clip(rng.normal(stars, 0.8, n), 1, 5).sum()), "stars_n": n})
    pd.DataFrame(rows).to_csv(path, index=False)
    lau = pd.DataFrame({"package": [f"sim.app{i:02d}" for i in range(14)]})
    lau["ai_launch_month"] = lau["package"].map(launch).fillna("")
    lau["include"] = "1"
    lau["panel_end"] = ""
    lau.loc[lau["package"] == "sim.app13", "panel_end"] = "2021-12"
    return lau


def test_recovers_known_effects(tmp_path):
    pytest.importorskip("pyfixest")
    from ai_takeup import fit_h1, fit_h2, fit_h3, load_cells, prepare, sample
    agg, lp = tmp_path / "agg.csv", tmp_path / "launch.csv"
    fake_aggregate(agg).to_csv(lp, index=False)
    cells, launch = sample(load_cells(agg), lp)
    assert cells.loc[cells["package"] == "sim.app13", "month"].max() == "2021-12"   # panel_end applied
    d = prepare(cells, launch)
    h1, h2 = fit_h1(d), fit_h2(d)
    assert 2.0 < h1["coef"] < 4.5 and h1["p"] < 0.01        # weighted average of the two rises
    assert -3.2 < h2["coef"] < -0.8                          # Indian minus English: -2 pp
    h3 = fit_h3(cells)
    assert -0.4 < h3["coef"] < -0.2 and h3["n_treated"] != h3["n_treated"]


def test_estimate_end_to_end(tmp_path):
    pytest.importorskip("pyfixest")
    from ai_takeup import estimate
    agg, lp, out = tmp_path / "agg.csv", tmp_path / "launch.csv", tmp_path / "res"
    fake_aggregate(agg).to_csv(lp, index=False)
    a = argparse.Namespace(agg=agg, launch=lp, out=out, placebo=2)
    estimate(a)
    estimate(a)                                              # placebo draws accumulate with a new seed
    pl = pd.read_csv(out / "placebo.csv")
    assert len(pl) == 4 and pl["draw_seed"].nunique() == 2
    est = pd.read_csv(out / "estimates.csv")
    assert len(est) == 4 + 14 and est.loc[est["spec"] == "main", "n_placebo"].eq(4).all()
    for f in ("summary.md", "event_study_h1.csv", "event_study_h2.png", "placebo_h2.pdf"):
        assert (out / f).exists()


def test_validation_sample(tmp_path):
    from ai_takeup import validation
    rows = []
    for i in range(40):
        for pkg, month in (("a", "2022-06"), ("a", "2023-06"), ("b", "2023-06"), ("c", "2023-06")):
            for lang, txt in (("eng", "upload photo here" if i % 2 else "good app"), ("hin", "फोटो" if i % 2 else "अच्छा")):
                rows.append((pkg, f"{pkg}{month}{lang}{i}", f"{month}-10T08:00:00+00:00", txt, lang))
    df = pd.DataFrame(rows, columns=["package", "reviewId", "at_utc", "content", "lang_main"])
    df["fetched_utc"] = "2026-10-06T00:46:33+00:00"
    inp, lp, out = tmp_path / "r.csv", tmp_path / "l.csv", tmp_path / "v.csv"
    df.to_csv(inp, index=False)
    pd.DataFrame({"package": ["a", "b", "c"], "ai_launch_month": ["2023-01", "", ""], "include": ["1", "1", "0"],
                  "panel_end": ["", "", ""]}).to_csv(lp, index=False)
    v = validation(inp, lp, out, y="m2", n=30)
    assert set(v["package"]) <= {"a", "b"}                               # include = 0 apps left out
    um = v[v["group"] == "unmatched_post"]
    assert (um["package"] == "a").all() and um["reviewId"].str.contains("2023-06").all()
    assert (v.loc[v["group"] == "matched", "m2"] == 1).all() and len(v) == 30 + 30 + 20 + 20   # pools of 20 cap the non-matches
    assert pd.read_csv(out, encoding="utf-8-sig")["human_mentions_ai"].isna().all()
