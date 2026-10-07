"""Reply-gap analysis: reply window, review-level variables, and recovery of a known gap."""
import argparse
import itertools

import numpy as np
import pandas as pd
import pytest

from replies import reply_window, review_frame


def test_reply_window():
    at = pd.Series(["2026-08-31T18:45:00+00:00", "2026-09-15T08:00:00+00:00"])
    fetched = pd.Series(["2026-10-05T22:58:20+00:00", "2026-10-06T00:46:33+00:00"])
    month, end, min_days = reply_window(at, fetched)
    assert str(end) == "2026-08" and 35 <= min_days < 36
    assert month.astype(str).tolist() == ["2026-09", "2026-09"]      # 18:45 UTC on 31 Aug is 00:15 on 1 Sep in India


def test_review_frame(tmp_path):
    rows = [  # content, lang_main, lang, form, stars, at, reply, replied at
        ("good", "eng", "eng", "english", 5, "2024-03-01T10:00:00+00:00", "Thank you for your feedback", "2024-03-03T10:00:00+00:00"),
        ("यह ऐप बहुत अच्छा है किसानों के लिए", "hin", "hin", "native", 4, "2024-03-02T10:00:00+00:00",
         "धन्यवाद, हम आपकी मदद करेंगे", "2024-03-02T22:00:00+00:00"),
        ("app kaam nahi kar raha hai bhai", "hin", "hin", "roman", 1, "2024-03-05T10:00:00+00:00",
         "Sorry for the trouble, please contact us", "2024-03-01T10:00:00+00:00"),        # edited after the reply
        ("bekar app", "hin", "hin", "roman", 1, "2024-03-06T10:00:00+00:00", None, None),
        ("ok", "eng", "eng", "english", 3, "2026-09-10T10:00:00+00:00", None, None),     # after the window
    ]
    df = pd.DataFrame(rows, columns=["content", "lang_main", "lang", "form", "score", "at_utc", "replyContent", "repliedAt_utc"])
    df["package"], df["reviewId"] = "a", [f"r{i}" for i in range(len(df))]
    df["fetched_utc"] = "2026-10-05T22:58:20+00:00"
    inp = tmp_path / "reviews_lang.csv"
    df.to_csv(inp, index=False)
    f, end, _ = review_frame(inp)
    f = f.set_index("reviewId")
    assert str(end) == "2026-08" and "r4" not in f.index
    assert f["replied"].tolist() == [1, 1, 1, 0]
    assert f["valid"].tolist() == [1, 1, 0, 0] and f["edited_after"].tolist() == [0, 0, 1, 0]
    assert f.loc["r0", "sum_log_days"] == pytest.approx(np.log1p(2.0))
    assert f.loc["r0", "len_bin"] == "1" and f.loc["r1", "len_bin"] == "6-10" and f.loc["r1", "native"] == 1
    assert f.loc["r0", "reply_lang"] == "eng" and f.loc["r1", "reply_lang"] == "hin"
    assert f["matched"].tolist() == [1, 1, 0, 0] and f["same_lang"].tolist() == [1, 1, 0, 0]


def fake_aggregate(path, gap_gov=-5.0, gap_other=-15.0, seed=5):
    """Cells with a known gap in reply rates (pp), confounded as in the real data: Indian-language reviews are
    longer, and long reviews are answered more often."""
    rng = np.random.default_rng(seed)
    apps = [f"sim.app{i:02d}" for i in range(10)]
    months = pd.period_range("2019-01", "2021-12", freq="M").astype(str)
    langs = [("eng", "eng", 0), ("hin", "hin", 1), ("hin", "hin", 0), ("tam", "tam", 1), ("eng", "hin", 0)]
    g = pd.DataFrame(list(itertools.product(apps, months, range(len(langs)), [1, 3, 5], ["1", "6-10", "21+"])),
                     columns=["package", "month", "li", "stars", "len_bin"])
    g["lang_main"], g["lang"], g["native"] = zip(*[langs[i] for i in g["li"]])
    ind = (g["lang_main"] != "eng").to_numpy()
    short = (g["len_bin"] == "1").to_numpy()
    lam = np.where(ind, np.where(short, 2, 6), np.where(short, 12, 3))
    g["n"] = rng.poisson(lam)
    gov = g["package"].isin(apps[:4]).to_numpy()
    p = (0.45 + 0.20 * (g["stars"] == 1) - 0.25 * short + 0.02 * g["package"].str[-1].astype(int)
         + ind * np.where(gov, gap_gov, gap_other) / 100)
    g["replied"] = rng.binomial(g["n"], p.clip(0.01, 0.99))
    g["edited_after"] = rng.binomial(g["replied"], 0.05)
    g["valid"] = g["replied"] - g["edited_after"]
    g["sum_log_days"] = g["valid"] * (1.0 + 0.3 * ind) + rng.normal(0, 0.5, len(g)) * np.sqrt(g["valid"])
    g["reply_det"] = g["replied"] - rng.binomial(g["replied"], 0.02)
    g["matched"] = rng.binomial(g["reply_det"], np.where(ind, 0.2, 0.95))
    g["reply_indian"] = np.where(ind, g["matched"], g["reply_det"] - g["matched"])
    g["same_lang"] = g["matched"]
    g.drop(columns="li").to_csv(path, index=False)
    pk = pd.DataFrame({"package": apps, "platform": [f"App {i}" for i in range(10)],
                       "owner_type": ["Government"] * 4 + ["Startup"] * 6,
                       "category": ["Input marketplace + advisory"] * 5 + ["Advisory / crop health"] * 5})
    lau = pd.DataFrame({"package": apps, "ai_launch_month": ["2020-01", "", "2020-06", "", "2021-01", "", "", "2020-03", "", ""],
                        "include": "1", "panel_end": ""})
    return pk, lau


def test_recovers_known_gap(tmp_path):
    pytest.importorskip("pyfixest")
    from replies import add_app_info, fit_gap, fit_split, load
    agg, pkp = tmp_path / "agg.csv", tmp_path / "packages.csv"
    pk, _ = fake_aggregate(agg)
    pk.to_csv(pkp, index=False)
    d = add_app_info(load(agg), pkp)
    r1 = fit_gap(d)
    assert -13.5 < r1["coef"] < -9.0 and r1["p"] < 0.01                     # true average gap: -11 pp
    raw = fit_gap(d, fe="package^month")
    assert raw["coef"] > r1["coef"] + 5                                        # length confound hides much of it
    assert 0.2 < fit_gap(d, "R2")["coef"] < 0.4
    assert -80 < fit_gap(d, "R3")["coef"] < -70
    assert 12 < fit_gap(d, "R3b")["coef"] < 18     # Indian-language replies: 20% to Indian reviews, 5% to English
    rows, p_eq = fit_split(d, "R1", "gov", ["government", "other"])
    est = {r["level"]: r["coef"] for r in rows}
    assert -8 < est["government"] < -2 and -18 < est["other"] < -12 and p_eq < 0.01


def test_estimate_end_to_end(tmp_path):
    pytest.importorskip("pyfixest")
    from replies import estimate
    agg, pkp, lp, out = tmp_path / "agg.csv", tmp_path / "packages.csv", tmp_path / "launch.csv", tmp_path / "res"
    pk, lau = fake_aggregate(agg)
    pk.to_csv(pkp, index=False)
    lau.to_csv(lp, index=False)
    a = argparse.Namespace(agg=agg, launch=lp, packages=pkp, out=out, placebo=2)
    estimate(a)
    estimate(a)                                                                 # placebo draws accumulate
    pl = pd.read_csv(out / "placebo_r4.csv")
    assert len(pl) == 4 and pl["draw_seed"].nunique() == 2
    est = pd.read_csv(out / "estimates.csv")
    assert set(est["question"]) == {"R1", "R2", "R3", "R3b", "R4"}
    assert (est["section"] == "robustness").sum() == 8
    assert len(pd.read_csv(out / "leave_one_out.csv")) == 10
    for f in ("summary.md", "app_gaps.pdf", "event_study_r4.png", "placebo_r4.pdf"):
        assert (out / f).exists()
