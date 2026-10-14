#!/usr/bin/env python3
"""
ai_takeup.py - do Indian-language users take up AI features? Implements docs/analysis_plan_ai_takeup.md
(registered 6 Oct 2026, commit 87621fa) exactly; any deviation is listed in that file.

    python analysis/ai_takeup.py aggregate             # review text -> aggregate counts (needs reviews_lang.csv)
    python analysis/ai_takeup.py estimate --placebo 100   # from the aggregate file only; repeat to 1,000 draws
    python analysis/ai_takeup.py validation            # hand-check sample for the outcome (needs review text)
    python analysis/ai_takeup.py explore-h3            # exploratory: is the H3 star gap a review-length effect?

`aggregate` reads play_reviews/data/reviews_lang.csv (local only) and writes
play_reviews/data/ai_mentions_app_lang_month.csv: per app x month x language label, the number of reviews,
of reviews mentioning AI (M1, M2) and the sum of star ratings. No text. `estimate` needs only that file and
data/launch_dates.csv, so the results can be replicated from the repository.

Hypotheses (two-sided, 5%):
  H1  share of reviews mentioning AI rises after an app's AI launch          share ~ post | app + month + language
  H2  the rise differs between Indian-language and English reviews             share ~ post x Indian | app x month
                                                                               + app x language + language x month
  H3  Indian-language reviewers rate differently within the same app-month    stars ~ Indian | app x month
Review-level linear probability models, estimated on cell means weighted by the number of reviews (identical
point estimates). Coefficients in percentage points (H1, H2) or stars (H3).
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estimate import drop_zero_groups, plot_event, plot_placebo, ri_pvalue  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "play_reviews" / "data"
AGG = DATA / "ai_mentions_app_lang_month.csv"
OUT = ROOT / "results" / "ai_takeup"
INDIAN_CODES = {"hin", "mar", "guj", "pan", "ben", "tam", "tel", "kan", "mal", "ori", "asm", "urd", "oth"}

# ---------------------------------------------------------------- outcome: keyword lists (fixed by the plan)
nfc = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
LATIN_GENERIC = ["a.i.", "artificial intelligence", "artificial inteligence", "chatbot", "chat bot", "chat-bot",
                 "bot", "gpt", "chatgpt", "chat gpt", "virtual assistant", "voice assistant", "digital assistant",
                 "machine learning"]
INDIC_GENERIC = ["एआई", "ए आई", "ए.आई", "आर्टिफिशियल", "कृत्रिम बुद्धिमत्ता", "चैटबॉट", "चैट बॉट", "चॅटबॉट", "बॉट",
                 "એઆઈ", "এআই", "ஏஐ", "ఏఐ", "ಎಐ", "എഐ", "ਏਆਈ", "ଏଆଇ", "اے آئی"]
APP_TERMS = {  # feature names, counted only in the app that launched the feature
    "com.BigHaat": ["crop doctor"],
    "com.syngenta.growerconnectapp": ["crop doctor"],
    "com.itc.maars": ["krishi mitra", "कृषि मित्र"],
    "com.prompt.ma.maapplicationfinalAmul": ["sarlaben", "sarla ben", "सरलाबेन", "સરલાબેન"],
    "com.nic.project.pmkisan": ["kisan e-mitra", "kisan e mitra", "kisan emitra", "किसान ई-मित्र", "किसान ई मित्र"],
    "com.sirpi.dvaracattlehealth": ["e-tag", "etag", "muzzle"],
    "agri.tnagri": ["pest identification", "identify pest"],
}
M2_LATIN = ["photo", "pic", "picture", "image", "scan", "camera", "voice", "bol kar", "bolkar", "bol ke"]
M2_INDIC = ["फोटो", "फ़ोटो", "तस्वीर", "स्कैन", "कैमरा", "आवाज", "आवाज़", "बोलकर", "बोल कर"]


def _is_latin(term):
    return all(ord(c) < 0x250 for c in term)


def _pattern(terms, case_insensitive=True):
    """Latin terms match at word boundaries (spaces inside a term match any whitespace); other scripts match
    as substrings."""
    parts = []
    for t in terms:
        t = nfc(t)
        if _is_latin(t):
            body = r"\s+".join(re.escape(w) for w in t.split(" "))
            parts.append(rf"(?<![A-Za-z0-9]){body}(?![A-Za-z0-9])")
        else:
            parts.append(re.escape(t))
    return re.compile("|".join(parts), re.IGNORECASE if case_insensitive else 0)


AI_CAPS = re.compile(r"(?<![A-Za-z0-9])AI(?![A-Za-z0-9])")  # "AI" in capitals, as a separate word
M1_GENERIC = _pattern(LATIN_GENERIC + INDIC_GENERIC)
M1_APP = {pkg: _pattern(terms) for pkg, terms in APP_TERMS.items()}
M2_EXTRA = _pattern(M2_LATIN + M2_INDIC)


def mentions(text, package):
    """(m1, m2): does the review mention AI under the primary (M1) and broad (M2) definition?"""
    if not isinstance(text, str) or not text:
        return 0, 0
    t = nfc(text)
    m1 = bool(AI_CAPS.search(t) or M1_GENERIC.search(t) or (package in M1_APP and M1_APP[package].search(t)))
    m2 = m1 or bool(M2_EXTRA.search(t))
    return int(m1), int(m2)


# ---------------------------------------------------------------- step 1: aggregate (needs review text)
def review_months(df):
    """Month in Indian time and the window used by build_panel.py (Jan 2016 to the last full month)."""
    ist = pd.to_datetime(df["at_utc"], utc=True) + pd.Timedelta(hours=5, minutes=30)
    month = ist.dt.tz_localize(None).dt.to_period("M")
    fetched = pd.to_datetime(df["fetched_utc"], utc=True).max() + pd.Timedelta(hours=5, minutes=30)
    end = fetched.tz_localize(None).to_period("M") - 1
    return month, pd.Period("2016-01", "M"), end


def term_counts(df):
    """Diagnostic (not part of the registered tests): reviews matched by each keyword, by language group.
    Feature names are searched only in their own app's reviews."""
    grp = df["lang_main"].map(lambda c: "indian" if c in INDIAN_CODES else ("english" if c == "eng" else "other"))
    text = df["content"].fillna("").map(nfc)
    terms = ([("M1", "AI (capitals)", AI_CAPS, None)] +
             [("M1", t, _pattern([t]), None) for t in LATIN_GENERIC + INDIC_GENERIC] +
             [("M1", t, _pattern([t]), pkg) for pkg, ts in APP_TERMS.items() for t in ts] +
             [("M2 only", t, _pattern([t]), None) for t in M2_LATIN + M2_INDIC])
    rows = []
    for lst, term, pat, pkg in terms:
        scope = (df["package"] == pkg) if pkg else pd.Series(True, index=df.index)
        hit = text[scope].map(lambda x: bool(pat.search(x)))
        c = grp[scope][hit].value_counts()
        rows.append({"list": lst, "term": term, "app": pkg or "all", "english": int(c.get("english", 0)),
                     "indian": int(c.get("indian", 0)), "other": int(c.get("other", 0))})
    return pd.DataFrame(rows)


def aggregate(inp, out, terms_out=None):
    df = pd.read_csv(inp, dtype={"reviewId": str}, encoding="utf-8-sig",
                     usecols=["package", "reviewId", "at_utc", "fetched_utc", "score", "content", "lang", "lang_main"])
    df = df[df["at_utc"].notna()].copy()
    df["month"], start, end = review_months(df)
    df = df[(df["month"] >= start) & (df["month"] <= end)].copy()
    mm = [mentions(c, p) for c, p in zip(df["content"], df["package"])]
    df["m1"], df["m2"] = [m[0] for m in mm], [m[1] for m in mm]
    df["stars_n"] = df["score"].notna().astype(int)
    df["stars_sum"] = df["score"].fillna(0)
    df["month"] = df["month"].astype(str)
    g = (df.groupby(["package", "month", "lang_main", "lang"], dropna=False)
           .agg(n=("reviewId", "size"), m1=("m1", "sum"), m2=("m2", "sum"),
                stars_sum=("stars_sum", "sum"), stars_n=("stars_n", "sum")).reset_index())
    g.to_csv(out, index=False)
    if terms_out:
        terms_out.parent.mkdir(parents=True, exist_ok=True)
        term_counts(df).to_csv(terms_out, index=False)
    print(f"{out.name}: {len(g):,} cells, {int(g['n'].sum()):,} reviews, {g['package'].nunique()} apps "
          f"({start} to {end}); M1 matches {int(g['m1'].sum()):,}, M2 matches {int(g['m2'].sum()):,}")
    return g


# ---------------------------------------------------------------- step 2: estimation (aggregate file only)
def load_cells(agg, langs_main=None, mixed_indian=False):
    """Collapse to app x month x Indian/English cells. mixed_indian: mixed reviews count as Indian."""
    a = pd.read_csv(agg, dtype={"month": str}, keep_default_na=False, na_values=[""])
    if langs_main:
        a = a[a["lang_main"].isin(langs_main)]
    code = a["lang"] if mixed_indian else a["lang_main"]
    a = a.assign(indian=code.map(lambda c: 1 if c in INDIAN_CODES else (0 if c == "eng" else np.nan)))
    a = a[a["indian"].notna()]
    return (a.groupby(["package", "month", "indian"], as_index=False)[["n", "m1", "m2", "stars_sum", "stars_n"]]
             .sum().astype({"indian": int}))


def sample(cells, launch_path, include_only=True):
    """Apply include = 1 and panel_end from launch_dates.csv; return cells and the launch dict."""
    lau = pd.read_csv(launch_path, dtype=str).fillna("")
    if include_only:
        keep = set(lau.loc[lau["include"].str.strip() == "1", "package"])
        cells = cells[cells["package"].isin(keep)]
        end = {r.package: r.panel_end.strip() for r in lau.itertuples() if r.panel_end.strip()}
        cap = cells["package"].map(end)
        cells = cells[cap.isna() | (cells["month"] <= cap.fillna(""))]
    launch = {r.package: r.ai_launch_month.strip() for r in lau.itertuples()
              if r.ai_launch_month.strip() and r.package in set(cells["package"])}
    return cells.copy(), launch


def prepare(cells, launch):
    d = cells.copy()
    d["t"] = pd.PeriodIndex(d["month"], freq="M").asi8
    lt = {k: pd.Period(v, "M").ordinal for k, v in launch.items()}
    d["launch_t"] = d["package"].map(lt)
    d["post"] = (d["t"] >= d["launch_t"]).astype(int)
    d["treat"] = d["post"] * d["indian"]
    d["rel_q"] = np.floor((d["t"] - d["launch_t"]) / 3).clip(-4, 4).fillna(-1).astype(int)
    return d


H1_FML = "share ~ post | package + month + indian"
H2_FML = "share ~ treat | package^month + package^indian + indian^month"


def _ols(d, fml, y, coef):
    import pyfixest as pf
    dd = d[d["n"] > 0].assign(share=lambda x: 100 * x[y] / x["n"])
    fit = pf.feols(fml, data=dd, weights="n", vcov={"CRV1": "package"})
    r = fit.tidy().loc[coef]
    return {"coef": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"], "ci_low": r["2.5%"], "ci_high": r["97.5%"],
            "n_reviews": int(dd["n"].sum()), "n_apps": dd["package"].nunique(),
            "n_treated": dd.loc[dd["launch_t"].notna(), "package"].nunique()}


def fit_h1(d, y="m1"):
    return _ols(d, H1_FML, y, "post")


def fit_h2(d, y="m1"):
    return _ols(d, H2_FML, y, "treat")


def fit_ppml(d, y, h):
    """Poisson on mention counts with log(total reviews) as exposure."""
    import pyfixest as pf
    dd = d[d["n"] > 0].assign(log_n=lambda x: np.log(x["n"]))
    fml, coef = (f"{y} ~ post | package + month + indian", "post") if h == "H1" else \
                (f"{y} ~ treat | package^month + package^indian + indian^month", "treat")
    if h == "H2":  # drop_zero_groups works on a "language" column
        dd = drop_zero_groups(dd.assign(language=dd["indian"]), y)
    fit = pf.fepois(fml, data=dd, offset="log_n", vcov={"CRV1": "package"})
    r = fit.tidy().loc[coef]
    return {"coef": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"], "ci_low": r["2.5%"], "ci_high": r["97.5%"],
            "n_reviews": int(dd["n"].sum()), "n_apps": dd["package"].nunique(),
            "n_treated": dd.loc[dd["launch_t"].notna(), "package"].nunique()}


def fit_h3(cells):
    import pyfixest as pf
    dd = cells[cells["stars_n"] > 0].assign(stars=lambda x: x["stars_sum"] / x["stars_n"])
    fit = pf.feols("stars ~ indian | package^month", data=dd, weights="stars_n", vcov={"CRV1": "package"})
    r = fit.tidy().loc["indian"]
    eng = dd[dd["indian"] == 0]
    return {"coef": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"], "ci_low": r["2.5%"], "ci_high": r["97.5%"],
            "n_reviews": int(dd["stars_n"].sum()), "n_apps": dd["package"].nunique(), "n_treated": np.nan,
            "english_mean_stars": float((eng["stars_sum"].sum()) / eng["stars_n"].sum())}


def fit_event(d, h, y="m1"):
    import pyfixest as pf
    dd = d[d["n"] > 0].assign(share=lambda x: 100 * x[y] / x["n"])
    fml = ("share ~ i(rel_q, ref=-1) | package + month + indian" if h == "H1" else
           "share ~ i(rel_q, indian, ref=-1) | package^month + package^indian + indian^month")
    tb = pf.feols(fml, data=dd, weights="n", vcov={"CRV1": "package"}).tidy().reset_index()
    tb["quarter"] = tb["Coefficient"].str.extract(r"rel_q::(-?\d+)").astype(int)
    tb = tb.rename(columns={"Estimate": "beta", "Std. Error": "se", "2.5%": "ci_low", "97.5%": "ci_high"})
    ref = pd.DataFrame([{"quarter": -1, "beta": 0.0, "se": 0.0, "ci_low": 0.0, "ci_high": 0.0}])
    return pd.concat([tb[["quarter", "beta", "se", "ci_low", "ci_high"]], ref]).sort_values("quarter")


def placebo(d, n_launch, reps, seed, y="m1", min_side=6):
    """Same rule as estimate.placebo: give n_launch random apps a launch month drawn inside their own data
    window (at least min_side months each side); refit H1 and H2."""
    rng = np.random.default_rng(seed)
    win = d.groupby("package")["t"].agg(["min", "max"])
    ok = win[(win["max"] - win["min"]) >= 2 * min_side]
    k = min(n_launch, len(ok))
    base = d.drop(columns=["launch_t", "post", "treat", "rel_q"])
    out = []
    for r in range(reps):
        chosen = rng.choice(ok.index.to_numpy(), size=k, replace=False)
        fake = {pkg: pd.Period(ordinal=int(rng.integers(ok.loc[pkg, "min"] + min_side, ok.loc[pkg, "max"] - min_side + 1)),
                               freq="M").strftime("%Y-%m") for pkg in chosen}
        dp = prepare(base, fake)
        out.append({"draw_seed": seed, "draw": r, "h1": fit_h1(dp, y)["coef"], "h2": fit_h2(dp, y)["coef"]})
    return pd.DataFrame(out)


def primary_outcome(d):
    """Decision rule fixed in the plan: M1 is primary only if it matches at least 200 reviews in treated apps
    after their launch (counted in the estimation sample: English and Indian-language reviews, up to panel_end)."""
    post_mentions = int(d.loc[d["post"] == 1, "m1"].sum())
    return ("m1" if post_mentions >= 200 else "m2"), post_mentions


OUTCOME_LABEL = {"m1": "AI terms (M1)", "m2": "AI, photo, scan or voice terms (M2)"}


def fmt_p(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def estimate(a):
    a.out.mkdir(parents=True, exist_ok=True)
    cells, launch = sample(load_cells(a.agg), a.launch)
    d = prepare(cells, launch)
    y, post_mentions = primary_outcome(d)
    lines = ["# AI take-up by language: results", "",
             "Implements `docs/analysis_plan_ai_takeup.md` (registered 6 Oct 2026). Coefficients for H1 and H2 are in",
             "percentage points of reviews mentioning AI; H3 is in stars (1–5).", "",
             f"Decision rule: {post_mentions:,} M1 mentions in treated apps after launch "
             f"({'at least' if y == 'm1' else 'fewer than'} 200), so the primary outcome is {y.upper()}: the review",
             f"contains {OUTCOME_LABEL[y]}.", ""]

    rows = [{"hypothesis": "H1", "spec": "main", "outcome": y, **fit_h1(d, y)},
            {"hypothesis": "H2", "spec": "main", "outcome": y, **fit_h2(d, y)}]
    h3_all = fit_h3(load_cells(a.agg))
    h3_17 = fit_h3(cells)
    rows += [{"hypothesis": "H3", "spec": "all 46 apps", "outcome": "stars", **h3_all},
             {"hypothesis": "H3", "spec": "17-app sample", "outcome": "stars", **h3_17}]

    # randomization inference for H1 and H2
    pl_path = a.out / "placebo.csv"
    pl = pd.read_csv(pl_path) if pl_path.exists() else pd.DataFrame(columns=["draw_seed", "draw", "h1", "h2"])
    if a.placebo:
        seed = 2000 + (int(pl["draw_seed"].nunique()) if len(pl) else 0)
        pl = pd.concat([pl, placebo(d, len(launch), a.placebo, seed, y)], ignore_index=True)
        pl.to_csv(pl_path, index=False)
    for r in rows[:2]:
        col = "h1" if r["hypothesis"] == "H1" else "h2"
        r["p_ri"] = ri_pvalue(pl[col], r["coef"]) if len(pl) else np.nan
        r["n_placebo"] = len(pl)

    # robustness (all fixed in the plan; clustered p-values)
    other = "m2" if y == "m1" else "m1"
    variants = [
        ("Poisson counts, exposure = reviews", d, y, "ppml"),
        ("Mixed reviews count as Indian", prepare(*sample(load_cells(a.agg, mixed_indian=True), a.launch)), y, "ols"),
        ("Hindi and Marathi vs English only", prepare(*sample(load_cells(a.agg, langs_main=["eng", "hin", "mar"]), a.launch)), y, "ols"),
        ("Excluding PMKISAN", d[d["package"] != "com.nic.project.pmkisan"], y, "ols"),
        ("Excluding Dvara Surabhi", d[d["package"] != "com.sirpi.dvaracattlehealth"], y, "ols"),
        ("Window of 12 months around launch", d[d["launch_t"].isna() | ((d["t"] - d["launch_t"]).abs() <= 12)], y, "ols"),
        (f"{other.upper()} instead of {y.upper()}", d, other, "ols"),
    ]
    for name, dv, yy, kind in variants:
        for h in ("H1", "H2"):
            res = fit_ppml(dv, yy, h) if kind == "ppml" else (fit_h1(dv, yy) if h == "H1" else fit_h2(dv, yy))
            rows.append({"hypothesis": h, "spec": name, "outcome": yy, **res})
    est = pd.DataFrame(rows)
    est.to_csv(a.out / "estimates.csv", index=False)

    # event studies and figures
    what = "mentioning AI" if y == "m1" else "with AI, photo,\nscan or voice terms"
    for h, lab in (("H1", f"Change in reviews {what} (pp)"),
                   ("H2", f"Indian minus English change, reviews\n{what} (pp)")):
        es = fit_event(d, h, y)
        es.to_csv(a.out / f"event_study_{h.lower()}.csv", index=False)
        plot_event(es, a.out / f"event_study_{h.lower()}.png", ylabel=lab)
    if len(pl):
        main = est[est["spec"] == "main"].set_index("hypothesis")
        for h in ("H1", "H2"):
            plot_placebo(pl.rename(columns={h.lower(): "beta"}), main.loc[h, "coef"], a.out / f"placebo_{h.lower()}.png",
                         ri_pvalue(pl[h.lower()], main.loc[h, "coef"]), xlabel="Placebo estimate (percentage points)")

    # descriptive: mention rates before and after launch in treated apps, by language
    tr = d[d["launch_t"].notna()]
    desc = tr.groupby(["post", "indian"])[["n", y]].sum().reset_index()
    desc["rate_pct"] = 100 * desc[y] / desc["n"]
    lines += [f"## Share of reviews with {OUTCOME_LABEL[y]} in treated apps (%)", "",
              "| Period | English | Indian-language |", "|---|---|---|"]
    for p_, lab in ((0, "Before launch"), (1, "After launch")):
        r_ = desc[desc["post"] == p_].set_index("indian")
        lines.append(f"| {lab} | {r_.loc[0, 'rate_pct']:.2f} ({int(r_.loc[0, y]):,} of {int(r_.loc[0, 'n']):,}) | "
                     f"{r_.loc[1, 'rate_pct']:.2f} ({int(r_.loc[1, y]):,} of {int(r_.loc[1, 'n']):,}) |")
    lines += ["", "## Main estimates", "", "| Hypothesis | Sample | Estimate | 95% CI (clustered) | p (clustered) | p (randomization) |",
              "|---|---|---|---|---|---|"]
    for r in est[est["spec"].isin(["main", "all 46 apps", "17-app sample"])].itertuples():
        ri = f"{r.p_ri:.3f} ({int(r.n_placebo):,} draws)" if pd.notna(getattr(r, "p_ri", np.nan)) else ""
        unit = " stars" if r.hypothesis == "H3" else " pp"
        lines.append(f"| {r.hypothesis} | {r.spec} | {r.coef:+.3f}{unit} | [{r.ci_low:+.3f}, {r.ci_high:+.3f}] | {fmt_p(r.p)} | {ri} |")
    lines += ["", f"H3: English reviews average {h3_all['english_mean_stars']:.2f} stars (all 46 apps).", "",
              "## Robustness (clustered p-values)", "", "| Hypothesis | Variant | Outcome | Estimate | p |", "|---|---|---|---|---|"]
    for r in est[~est["spec"].isin(["main", "all 46 apps", "17-app sample"])].itertuples():
        unit = " (log points)" if r.spec.startswith("Poisson") else " pp"
        lines.append(f"| {r.hypothesis} | {r.spec} | {r.outcome.upper()} | {r.coef:+.3f}{unit} | {fmt_p(r.p)} |")
    (a.out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


# ---------------------------------------------------------------- exploratory (not in the plan; needs review text)
LENGTH_BINS, LENGTH_LABELS = [0, 1, 2, 5, 10, 20, np.inf], ["1", "2", "3-5", "6-10", "11-20", "21+"]


def explore_h3_length(inp, out):
    """Exploratory check of H3, fixed before it was run: is the star gap a review-length effect? Short reviews
    ("good", "nice") are mostly labelled English and mostly 5 stars. (a) H3 with word-count-bin fixed effects;
    (b) H3 on reviews of at least 5 words. All 46 apps, app x month fixed effects, clustered by app."""
    import pyfixest as pf
    df = pd.read_csv(inp, dtype={"reviewId": str}, encoding="utf-8-sig",
                     usecols=["package", "at_utc", "fetched_utc", "score", "content", "lang_main"])
    df = df[df["at_utc"].notna()].copy()
    df["month"], start, end = review_months(df)
    df = df[(df["month"] >= start) & (df["month"] <= end) & df["score"].notna()].copy()
    df["indian"] = df["lang_main"].map(lambda c: 1 if c in INDIAN_CODES else (0 if c == "eng" else np.nan))
    df = df[df["indian"].notna()].copy()
    df["words"] = df["content"].fillna("").str.split().str.len()
    df["len_bin"] = pd.cut(df["words"], LENGTH_BINS, labels=LENGTH_LABELS).astype(str)
    df["month"] = df["month"].astype(str)
    by_len = (df.groupby(["package", "month", "indian", "len_bin"], as_index=False)
                .agg(n=("score", "size"), stars=("score", "mean")))
    long = (df[df["words"] >= 5].groupby(["package", "month", "indian"], as_index=False)
              .agg(n=("score", "size"), stars=("score", "mean")))
    rows = []
    for name, dd, fml in (("H3 as registered (for comparison)", by_len, "stars ~ indian | package^month"),
                          ("(a) plus review-length fixed effects", by_len, "stars ~ indian | package^month + len_bin"),
                          ("(b) reviews of at least 5 words", long, "stars ~ indian | package^month")):
        r = pf.feols(fml, data=dd, weights="n", vcov={"CRV1": "package"}).tidy().loc["indian"]
        rows.append({"check": name, "coef": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"],
                     "ci_low": r["2.5%"], "ci_high": r["97.5%"], "n_reviews": int(dd["n"].sum()),
                     "n_apps": dd["package"].nunique()})
    res = pd.DataFrame(rows)
    shares = (df.groupby(["indian", "len_bin"]).size().unstack(0).reindex(LENGTH_LABELS)
                .pipe(lambda x: 100 * x / x.sum()).round(1).rename(columns={0: "english_pct", 1: "indian_pct"}))
    stars_by = df.groupby(["len_bin", "indian"])["score"].mean().unstack().reindex(LENGTH_LABELS).round(2)
    shares["english_mean_stars"], shares["indian_mean_stars"] = stars_by[0], stars_by[1]
    out.mkdir(parents=True, exist_ok=True)
    res.to_csv(out / "exploratory_h3_length.csv", index=False)
    shares.reset_index().to_csv(out / "exploratory_review_length.csv", index=False)
    print(res.to_string(index=False)); print(shares.to_string())
    return res, shares


# ---------------------------------------------------------------- validation sample (needs review text)
def validation(inp, launch_path, out, y="m2", n=75, seed=7):
    """Hand-check sample for the primary outcome y, from the estimation sample (include = 1, up to panel_end):
    n matches and n post-launch non-matches in treated apps, each for English and Indian-language reviews."""
    df = pd.read_csv(inp, dtype={"reviewId": str}, encoding="utf-8-sig",
                     usecols=["package", "reviewId", "at_utc", "fetched_utc", "content", "lang_main"])
    df = df[df["at_utc"].notna()].copy()
    df["month"], start, end = review_months(df)
    df = df[(df["month"] >= start) & (df["month"] <= end)].copy()
    lau = pd.read_csv(launch_path, dtype=str).fillna("")
    lau = lau[lau["include"].str.strip() == "1"]
    cap = {r.package: pd.Period(r.panel_end.strip(), "M") for r in lau.itertuples() if r.panel_end.strip()}
    df = df[df["package"].isin(set(lau["package"]))]
    df = df[[p not in cap or m <= cap[p] for p, m in zip(df["package"], df["month"])]]
    lt = {r.package: pd.Period(r.ai_launch_month, "M") for r in lau.itertuples() if r.ai_launch_month.strip()}
    df["indian"] = df["lang_main"].map(lambda c: 1 if c in INDIAN_CODES else (0 if c == "eng" else np.nan))
    df = df[df["indian"].notna()].copy()
    mm = [mentions(c, p) for c, p in zip(df["content"], df["package"])]
    df["m1"], df["m2"] = [m[0] for m in mm], [m[1] for m in mm]
    df["post_treated"] = [p in lt and m >= lt[p] for p, m in zip(df["package"], df["month"])]
    parts = []
    for grp, pool in (("matched", df[df[y] == 1]), ("unmatched_post", df[(df[y] == 0) & df["post_treated"]])):
        for ind in (0, 1):
            sub = pool[pool["indian"] == ind]
            parts.append(sub.sample(min(n, len(sub)), random_state=seed).assign(group=grp))
    v = pd.concat(parts).sample(frac=1, random_state=seed).reset_index(drop=True)
    v.insert(0, "sample_id", range(1, len(v) + 1))
    v["human_mentions_ai"] = ""
    v["human_note"] = ""
    v[["sample_id", "package", "reviewId", "content", "human_mentions_ai", "human_note", "lang_main", "group",
       "m1", "m2"]].to_csv(out, index=False, encoding="utf-8-sig")
    print(f"Saved {len(v)} reviews to {out} ({v.groupby(['group', 'indian']).size().to_dict()}). Fill "
          "human_mentions_ai with 1 if the review refers to an AI feature (chatbot, AI advisor, photo or voice "
          "diagnosis), else 0. Hide the columns after human_note while coding.")
    return v


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["aggregate", "estimate", "validation", "explore-h3"])
    ap.add_argument("--reviews", type=Path, default=DATA / "reviews_lang.csv")
    ap.add_argument("--agg", type=Path, default=AGG)
    ap.add_argument("--launch", type=Path, default=ROOT / "data" / "launch_dates.csv")
    ap.add_argument("--placebo", type=int, default=0, help="placebo draws to add (appended to placebo.csv)")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    if a.step == "aggregate":
        aggregate(a.reviews, a.agg, a.out / "term_counts.csv")
    elif a.step == "estimate":
        estimate(a)
    elif a.step == "explore-h3":
        explore_h3_length(a.reviews, a.out)
    else:
        y, _ = primary_outcome(prepare(*sample(load_cells(a.agg), a.launch)))
        validation(a.reviews, a.launch, DATA / "ai_mention_validation.csv", y)


if __name__ == "__main__":
    main()
