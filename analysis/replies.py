#!/usr/bin/env python3
"""
replies.py - do agtech apps answer Indian-language farmers less often? Implements docs/analysis_plan_replies.md
(registered 7 Oct 2026, commit 517bc83) exactly; any deviation is listed in that file.

    python analysis/replies.py aggregate              # review text -> aggregate counts (needs reviews_lang.csv)
    python analysis/replies.py estimate --placebo 100  # from the aggregate file only; repeat to 1,000 draws
    python analysis/replies.py validation             # hand-check sample of reply languages (needs review text)

Questions (two-sided, 5%). All have app x month, star-rating and review-length fixed effects; clustered by app.
  R1 (primary)  replied ~ Indian                                                     percentage points
  R2            log(1 + days to reply) ~ Indian, among replied reviews               log points
  R3            reply in the review's language group ~ Indian, among replied reviews  percentage points
  R4            replied ~ AI launch x Indian, plus app x language and language x month fixed effects;
                17-app sample; randomization inference
Review-level models are estimated by weighted least squares on cell means (app x month x language x stars x
length bin), weighted by the number of reviews: the point estimates are identical.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "play_reviews"))
from ai_takeup import INDIAN_CODES, LENGTH_BINS, LENGTH_LABELS, prepare, sample  # noqa: E402
from estimate import FIG_W, PAPER_RC, plot_event, plot_placebo, ri_pvalue, save_figure  # noqa: E402

DATA = ROOT / "play_reviews" / "data"
AGG = DATA / "replies_app_lang_month.csv"
OUT = ROOT / "results" / "replies"
PACKAGES = ROOT / "play_reviews" / "packages.csv"
START, MIN_DAYS = pd.Period("2016-01", "M"), 35
IST = pd.Timedelta(hours=5, minutes=30)
KEYS = ["package", "month", "lang_main", "lang", "native", "stars", "len_bin"]
COUNTS = ["n", "replied", "valid", "sum_log_days", "edited_after", "reply_det", "reply_indian", "matched", "same_lang"]
FE = "package^month + stars + len_bin"
PMKISAN = "com.nic.project.pmkisan"


def group_of(code):
    return "ind" if code in INDIAN_CODES else ("eng" if code == "eng" else None)


# ---------------------------------------------------------------- step 1: review-level variables (needs text)
def reply_window(at_utc, fetched_utc):
    """Months in Indian time. The window ends with the last month whose final day is at least MIN_DAYS before
    the earliest scrape, so every review had at least MIN_DAYS days to receive a reply."""
    month = (pd.to_datetime(at_utc, utc=True) + IST).dt.tz_localize(None).dt.to_period("M")
    fetched = (pd.to_datetime(fetched_utc, utc=True).min() + IST).tz_localize(None)
    end = fetched.to_period("M") - 1
    while end.end_time + pd.Timedelta(days=MIN_DAYS) > fetched:
        end -= 1
    return month, end, (fetched - end.end_time) / pd.Timedelta(days=1)


def review_frame(inp, models=ROOT / "play_reviews" / "models", label_replies=True):
    cols = ["package", "reviewId", "at_utc", "fetched_utc", "score", "content", "lang", "lang_main", "form",
            "replyContent", "repliedAt_utc"]
    df = pd.read_csv(inp, dtype={"reviewId": str}, encoding="utf-8-sig", usecols=cols)
    df = df[df["at_utc"].notna() & df["score"].notna()].copy()
    df["month"], end, min_days = reply_window(df["at_utc"], df["fetched_utc"])
    df = df[(df["month"] >= START) & (df["month"] <= end)].copy()
    df["stars"] = df["score"].astype(int)
    words = df["content"].fillna("").astype(str).str.split().str.len()
    df["len_bin"] = pd.cut(words, LENGTH_BINS, labels=LENGTH_LABELS).astype(str).where(words > 0, "0")
    df["native"] = df["form"].isin(["native", "native+latin"]).astype(int)
    reply = df["replyContent"].fillna("").astype(str).str.strip()
    df["replied"] = (reply != "").astype(int)
    days = (pd.to_datetime(df["repliedAt_utc"], utc=True) - pd.to_datetime(df["at_utc"], utc=True)) / pd.Timedelta(days=1)
    df["days"] = days.where(df["replied"] == 1)
    df["valid"] = ((df["replied"] == 1) & (days >= 0)).astype(int)
    df["edited_after"] = ((df["replied"] == 1) & (days < 0)).astype(int)
    df["sum_log_days"] = np.where(df["valid"] == 1, np.log1p(days.clip(lower=0).fillna(0)), 0.0)
    df["reply_lang"] = ""
    if label_replies:
        import detect_language as DL
        from wordfreq import zipf_frequency
        DL.zipf_frequency = zipf_frequency                   # set by detect_language.main() when run directly
        Labeller, clean = DL.Labeller, DL.clean
        lab = Labeller(models, use_ftn=True, use_ftr=False, quiet=True)   # the settings used for the reviews
        cleaned = reply.map(clean)
        uniq = list(dict.fromkeys(cleaned[df["replied"] == 1]))
        res = lab.label_unique(uniq)
        df["reply_lang"] = [res[t]["lang_main"] if r == 1 else "" for t, r in zip(cleaned, df["replied"])]
    rev, rep = df["lang_main"].map(group_of), df["reply_lang"].map(group_of)
    df["reply_det"] = ((df["replied"] == 1) & rep.notna()).astype(int)
    df["reply_indian"] = ((df["reply_det"] == 1) & (rep == "ind")).astype(int)
    df["matched"] = ((df["reply_det"] == 1) & (rep == rev)).astype(int)
    df["same_lang"] = ((df["reply_det"] == 1) & (df["reply_lang"] == df["lang_main"])).astype(int)
    df["month"] = df["month"].astype(str)
    return df, end, min_days


def unadjusted(df):
    """Raw figures by review language (main measure), from review-level data."""
    rows = []
    for g, lab in (("eng", "English"), ("ind", "Indian-language")):
        s = df[df["lang_main"].map(group_of) == g]
        r = s[s["replied"] == 1]
        rows.append({"language": lab, "reviews": len(s), "reply_rate_pct": 100 * s["replied"].mean(),
                     "median_days_to_reply": r.loc[r["valid"] == 1, "days"].median(),
                     "edited_after_reply_pct_of_replied": 100 * r["edited_after"].mean(),
                     "reply_language_undetermined_pct": 100 * (1 - r["reply_det"].mean()),
                     "reply_in_indian_language_pct": 100 * r["reply_indian"].sum() / max(r["reply_det"].sum(), 1),
                     "reply_in_same_language_pct": 100 * r["same_lang"].sum() / max(r["reply_det"].sum(), 1)})
    return pd.DataFrame(rows)


def aggregate(inp, out, results=OUT):
    df, end, min_days = review_frame(inp)
    g = df.groupby(KEYS, dropna=False).agg(n=("reviewId", "size"), **{c: (c, "sum") for c in COUNTS[1:]}).reset_index()
    g.to_csv(out, index=False)
    results.mkdir(parents=True, exist_ok=True)
    unadjusted(df).to_csv(results / "unadjusted.csv", index=False)
    print(f"{out.name}: {len(g):,} cells, {int(g['n'].sum()):,} reviews, {g['package'].nunique()} apps "
          f"({START} to {end}; the last reviews had {min_days:.1f} days to receive a reply)")
    return g


# ---------------------------------------------------------------- step 2: estimation (aggregate file only)
def load(agg, mixed_indian=False):
    a = pd.read_csv(agg, dtype={"month": str, "len_bin": str}, keep_default_na=False, na_values=[""])
    code = a["lang"] if mixed_indian else a["lang_main"]
    a = a.assign(code=code, indian=code.map(lambda c: {"ind": 1, "eng": 0}.get(group_of(c), np.nan)))
    return a[a["indian"].notna()].astype({"indian": int}).reset_index(drop=True)


OUTCOMES = {"R1": ("replied", "n", 100.0), "R2": ("sum_log_days", "valid", 1.0), "R3": ("matched", "reply_det", 100.0),
            "R3b": ("reply_indian", "reply_det", 100.0)}   # R3b is exploratory (see the plan's Deviations)


def _frame(d, q, weight=None):
    num, den, scale = OUTCOMES[q]
    dd = d[d[den] > 0].copy()
    dd["y"] = scale * dd[num] / dd[den]
    dd["den"] = dd[den]
    dd["w"] = dd[den] if weight is None else weight(dd)
    return dd


def _row(fit, coef, dd):
    r = fit.tidy().loc[coef]
    return {"coef": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"], "ci_low": r["2.5%"],
            "ci_high": r["97.5%"], "n_reviews": int(dd["den"].sum()), "n_apps": dd["package"].nunique()}


def fit_gap(d, q="R1", fe=FE, weight=None):
    import pyfixest as pf
    dd = _frame(d, q, weight)
    fit = pf.feols(f"y ~ indian | {fe}", data=dd, weights="w", vcov={"CRV1": "package"})
    return _row(fit, "indian", dd)


def fit_poisson(d):
    """Robustness 8: reply counts per cell, exposure = reviews; app-months with no reply carry no information."""
    import pyfixest as pf
    dd = d[d["n"] > 0].assign(log_n=lambda x: np.log(x["n"]), den=lambda x: x["n"])
    dd = dd[dd.groupby(["package", "month"])["replied"].transform("sum") > 0]
    fit = pf.fepois(f"replied ~ indian | {FE}", data=dd, offset="log_n", vcov={"CRV1": "package"})
    return _row(fit, "indian", dd)


def _wald(fit, names):
    """p-value that the listed coefficients are equal (clustered covariance)."""
    from scipy import stats
    b = fit.coef().loc[names].to_numpy()
    idx = [list(fit.coef().index).index(n) for n in names]
    V = np.asarray(fit._vcov)[np.ix_(idx, idx)]
    R = np.eye(len(names))[:-1] - np.eye(len(names), k=1)[:-1]
    rb = R @ b
    w = float(rb @ np.linalg.solve(R @ V @ R.T, rb))
    return float(stats.chi2.sf(w, len(names) - 1))


def fit_split(d, q, col, levels, min_indian=100):
    """Gap within each level of `col`. For a split that applies to both languages (app type, star group), all
    fixed effects are interacted with the level, so each estimate equals the one from its own subsample; for a
    split of Indian-language reviews (Hindi vs other, script vs romanized), each subgroup is compared with all
    English reviews. Levels with fewer than min_indian Indian-language observations are skipped."""
    import pyfixest as pf
    dd = _frame(d, q)
    within_indian = col in ("hindi", "native")
    names, keep = [], []
    for lv in levels:
        sel = (dd[col] == lv) & (dd["indian"] == 1)
        if dd.loc[sel, "w"].sum() < min_indian:
            continue
        nm = f"ind_{col}_{lv}".replace("-", "_")
        dd[nm] = sel.astype(int)
        names.append(nm)
        keep.append(lv)
    if not names:
        return [], np.nan
    if within_indian:
        fe = FE
    else:
        g = "|" + dd[col].astype(str)
        dd["pm_g"] = dd["package"] + "|" + dd["month"] + g
        dd["stars_g"] = dd["stars"].astype(str) + g
        dd["len_g"] = dd["len_bin"].astype(str) + g
        fe = "pm_g + stars_g + len_g"
        dd = dd[dd[col].isin(keep)]
    fit = pf.feols(f"y ~ {' + '.join(names)} | {fe}", data=dd, weights="w", vcov={"CRV1": "package"})
    rows = []
    for lv, nm in zip(keep, names):
        sub = dd[(dd[col] == lv) | ((dd["indian"] == 0) & within_indian)]
        rows.append({"level": lv, **_row(fit, nm, sub)})
    return rows, (_wald(fit, names) if len(names) > 1 else np.nan)


def add_app_info(d, packages=PACKAGES):
    pk = pd.read_csv(packages, dtype=str).fillna("")
    gov = dict(zip(pk["package"], np.where(pk["owner_type"].str.strip() == "Government", "government", "other")))
    mkt = dict(zip(pk["package"], np.where(pk["category"].str.contains("Input marketplace"), "marketplace", "other")))
    return d.assign(gov=d["package"].map(gov).fillna("other"), market=d["package"].map(mkt).fillna("other"),
                    star_grp=np.select([d["stars"] <= 2, d["stars"] == 3], ["negative", "neutral"], "positive"),
                    hindi=np.where(d["code"] == "hin", "hindi", "other"),
                    native=np.where(d["native"] == 1, "script", "romanized"))


def app_gaps(d, packages=PACKAGES, min_each=100):
    """Robustness 10: the gap app by app (apps with at least min_each reviews in each language group);
    within one app, standard errors are clustered by month."""
    import pyfixest as pf
    names = pd.read_csv(packages, dtype=str).set_index("package")["platform"].to_dict()
    rows = []
    for pkg, s in d.groupby("package"):
        cnt = s.groupby("indian")["n"].sum()
        if cnt.get(0, 0) < min_each or cnt.get(1, 0) < min_each:
            continue
        dd = _frame(s, "R1")
        if dd["y"].std() == 0:
            continue
        fit = pf.feols("y ~ indian | month + stars + len_bin", data=dd, weights="w", vcov={"CRV1": "month"})
        rows.append({"package": pkg, "app": names.get(pkg, pkg), **_row(fit, "indian", dd),
                     "english_reply_rate_pct": 100 * s.loc[s["indian"] == 0, "replied"].sum() / cnt[0]})
    return pd.DataFrame(rows).sort_values("coef")


def plot_app_gaps(g, beta, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    with plt.rc_context(PAPER_RC):
        fig, ax = plt.subplots(figsize=(FIG_W, 0.6 + 0.16 * len(g)))
        y = np.arange(len(g))
        ax.errorbar(g["coef"], y, xerr=[g["coef"] - g["ci_low"], g["ci_high"] - g["coef"]], fmt="o", color="black",
                    ms=3, lw=0.8, capsize=1.5)
        ax.axvline(0, color="0.6", lw=0.6)
        ax.axvline(beta, color="black", lw=0.6, ls="--")
        ax.set_yticks(y, g["app"])
        ax.set_xlabel("Reply rate, Indian-language minus\nEnglish reviews (percentage points)")
        fig.tight_layout(pad=0.3)
        save_figure(fig, path)
        plt.close(fig)


# R4: the gap and AI launches (same structure as the main composition model)
R4_FE = "package^month + package^indian + indian^month + stars + len_bin"


def fit_r4(d):
    import pyfixest as pf
    dd = _frame(d, "R1")
    fit = pf.feols(f"y ~ treat | {R4_FE}", data=dd, weights="w", vcov={"CRV1": "package"})
    out = _row(fit, "treat", dd)
    out["n_treated"] = dd.loc[dd["launch_t"].notna(), "package"].nunique()
    return out


def fit_r4_event(d):
    import pyfixest as pf
    dd = _frame(d, "R1")
    tb = pf.feols(f"y ~ i(rel_q, indian, ref=-1) | {R4_FE}", data=dd, weights="w",
                  vcov={"CRV1": "package"}).tidy().reset_index()
    tb["quarter"] = tb["Coefficient"].str.extract(r"rel_q::(-?\d+)").astype(int)
    tb = tb.rename(columns={"Estimate": "beta", "Std. Error": "se", "2.5%": "ci_low", "97.5%": "ci_high"})
    ref = pd.DataFrame([{"quarter": -1, "beta": 0.0, "se": 0.0, "ci_low": 0.0, "ci_high": 0.0}])
    return pd.concat([tb[["quarter", "beta", "se", "ci_low", "ci_high"]], ref]).sort_values("quarter")


def placebo_r4(d, n_launch, reps, seed, min_side=6):
    """Same rule as estimate.placebo: n_launch random apps get a launch month drawn inside their own data window
    (at least min_side months each side)."""
    rng = np.random.default_rng(seed)
    win = d.groupby("package")["t"].agg(["min", "max"])
    ok = win[(win["max"] - win["min"]) >= 2 * min_side]
    k = min(n_launch, len(ok))
    base = d.drop(columns=["launch_t", "post", "treat", "rel_q"])
    out = []
    for r in range(reps):
        chosen = rng.choice(ok.index.to_numpy(), size=k, replace=False)
        fake = {p: pd.Period(ordinal=int(rng.integers(ok.loc[p, "min"] + min_side, ok.loc[p, "max"] - min_side + 1)),
                             freq="M").strftime("%Y-%m") for p in chosen}
        out.append({"draw_seed": seed, "draw": r, "beta": fit_r4(prepare(base, fake))["coef"]})
    return pd.DataFrame(out)


def fmt_p(p):
    return "" if pd.isna(p) else ("<0.001" if p < 0.001 else f"{p:.3f}")


def estimate(a):
    a.out.mkdir(parents=True, exist_ok=True)
    d = add_app_info(load(a.agg), a.packages)
    rows = []

    def add(section, q, spec, res, **extra):
        rows.append({"section": section, "question": q, "spec": spec, **res, **extra})

    # main questions
    unit = {"R1": "pp", "R2": "log points", "R3": "pp"}
    for q in ("R1", "R2", "R3"):
        add("main", q, "main", fit_gap(d, q), unit=unit[q])
        add("main", q, "app x month fixed effects only", fit_gap(d, q, fe="package^month"), unit=unit[q])

    # exploratory, not in the plan: R3's "matched" outcome mixes an app's default reply language with switching
    # language; R3b asks how much more likely the reply is in an Indian language when the review is in one
    for spec, fe in (("main", FE), ("app x month fixed effects only", "package^month")):
        add("exploratory", "R3b", spec, fit_gap(d, "R3b", fe=fe), unit="pp")

    # heterogeneity (R1, R2, R3 where samples allow)
    splits = [("gov", ["government", "other"], "Government apps vs others"),
              ("market", ["marketplace", "other"], "Input-marketplace apps vs others"),
              ("star_grp", ["negative", "neutral", "positive"], "By star rating"),
              ("hindi", ["hindi", "other"], "Hindi vs other Indian languages (each vs English)"),
              ("native", ["script", "romanized"], "Indian script vs romanized (each vs English)")]
    for q in ("R1", "R2", "R3"):
        for col, levels, name in splits:
            res, p_eq = fit_split(d, q, col, levels)
            for r in res:
                lv = r.pop("level")
                add("heterogeneity", q, f"{name}: {lv}", r, unit=unit[q], p_equal=p_eq)

    # robustness for R1
    a_all = pd.read_csv(a.agg).groupby("package")[["replied", "n"]].sum()   # all reviews, any language
    replying = a_all.index[a_all["replied"] / a_all["n"] >= 0.10]
    app_total = d.groupby("package")["n"].transform("sum")
    d_edit = d.assign(n=d["n"] - d["edited_after"], replied=d["replied"] - d["edited_after"])
    robust = [
        ("1. Stars and length fixed effects by app", lambda: fit_gap(d, fe="package^month + package^stars + package^len_bin")),
        ("2. Mixed reviews count as Indian", lambda: fit_gap(add_app_info(load(a.agg, mixed_indian=True), a.packages))),
        ("3. Excluding PMKISAN", lambda: fit_gap(d[d["package"] != PMKISAN])),
        ("4. Each app weighted equally", lambda: fit_gap(d, weight=lambda x: x["n"] / app_total.loc[x.index])),
        ("5. Apps replying to at least 10% of reviews", lambda: fit_gap(d[d["package"].isin(replying)])),
        ("6. Excluding reviews edited after the reply", lambda: fit_gap(d_edit)),
        ("7. Reviews from January 2020 on", lambda: fit_gap(d[d["month"] >= "2020-01"])),
        ("8. Poisson, reply counts (log points)", lambda: fit_poisson(d)),
    ]
    for name, f in robust:
        add("robustness", "R1", name, f(), unit="log points" if name.startswith("8.") else "pp")
    beta = rows[0]["coef"]
    loo = []
    for pkg in sorted(d["package"].unique()):
        r = fit_gap(d[d["package"] != pkg])
        loo.append({"dropped": pkg, "coef": r["coef"], "ci_low": r["ci_low"], "ci_high": r["ci_high"], "p": r["p"]})
    loo = pd.DataFrame(loo)
    loo.to_csv(a.out / "leave_one_out.csv", index=False)
    far = loo.iloc[(loo["coef"] - beta).abs().argmax()]
    gaps = app_gaps(d, a.packages)
    gaps.to_csv(a.out / "app_gaps.csv", index=False)
    plot_app_gaps(gaps, beta, a.out / "app_gaps.png")

    # R4: AI launches, 17-app sample, randomization inference
    cells, launch = sample(d, a.launch)
    d4 = prepare(cells, launch)
    r4 = fit_r4(d4)
    pl_path = a.out / "placebo_r4.csv"
    pl = pd.read_csv(pl_path) if pl_path.exists() else pd.DataFrame(columns=["draw_seed", "draw", "beta"])
    if a.placebo:
        seed = 3000 + (int(pl["draw_seed"].nunique()) if len(pl) else 0)
        pl = pd.concat([pl, placebo_r4(d4, len(launch), a.placebo, seed)], ignore_index=True)
        pl.to_csv(pl_path, index=False)
    r4["p_ri"] = ri_pvalue(pl["beta"], r4["coef"]) if len(pl) else np.nan
    r4["n_placebo"] = len(pl)
    add("main", "R4", "AI launch x Indian (17 apps)", r4, unit="pp")
    es = fit_r4_event(d4)
    es.to_csv(a.out / "event_study_r4.csv", index=False)
    plot_event(es, a.out / "event_study_r4.png", ylabel="Change in Indian minus English\nreply rate (pp)")
    if len(pl):
        plot_placebo(pl, r4["coef"], a.out / "placebo_r4.png", r4["p_ri"], xlabel="Placebo estimate (percentage points)")

    est = pd.DataFrame(rows)
    est.to_csv(a.out / "estimates.csv", index=False)
    write_summary(a.out, est, loo, far, gaps, beta)


def write_summary(out, est, loo, far, gaps, beta):
    L = ["# Developer replies by review language: results", "",
         "Implements `docs/analysis_plan_replies.md` (registered 7 Oct 2026). R1 and R3 are in percentage points,",
         "R2 in log points (0.10 is about 10% longer). All models hold fixed the app and month, the star rating and the",
         "review length, unless stated; 95% intervals and p-values are clustered by app.", ""]
    un = out / "unadjusted.csv"
    if un.exists():
        u = pd.read_csv(un).set_index("language")
        L += ["## Raw figures (no adjustment)", "", "| | English | Indian-language |", "|---|---|---|"]
        for c, lab, f in (("reviews", "Reviews", "{:,.0f}"), ("reply_rate_pct", "Replied (%)", "{:.1f}"),
                          ("median_days_to_reply", "Median days to reply", "{:.1f}"),
                          ("edited_after_reply_pct_of_replied", "Replied reviews edited after the reply (%)", "{:.1f}"),
                          ("reply_language_undetermined_pct", "Replies of undetermined language (%)", "{:.1f}"),
                          ("reply_in_indian_language_pct", "Replies in an Indian language (% of determined)", "{:.1f}"),
                          ("reply_in_same_language_pct", "Replies in the review's own language (% of determined)", "{:.1f}")):
            L.append(f"| {lab} | {f.format(u.loc['English', c])} | {f.format(u.loc['Indian-language', c])} |")
        L.append("")
    L += ["## Main estimates", "", "| Question | Specification | Estimate | 95% CI | p | p (randomization) | Reviews | Apps |",
          "|---|---|---|---|---|---|---|---|"]
    for r in est[est["section"] == "main"].itertuples():
        ri = f"{r.p_ri:.3f} ({int(r.n_placebo):,} draws)" if pd.notna(getattr(r, "p_ri", np.nan)) else ""
        L.append(f"| {r.question} | {r.spec} | {r.coef:+.2f} {r.unit} | [{r.ci_low:+.2f}, {r.ci_high:+.2f}] | "
                 f"{fmt_p(r.p)} | {ri} | {r.n_reviews:,} | {r.n_apps} |")
    L += ["", "## Exploratory (not in the plan): does the reply switch to an Indian language?", "",
          "R3b: how much more likely a reply is to be in an Indian language when the review is in one, within the same",
          "app and month. Defined after R3 was seen; see the plan's Deviations.", "",
          "| Specification | Estimate | 95% CI | p | Replies | Apps |", "|---|---|---|---|---|---|"]
    for r in est[est["section"] == "exploratory"].itertuples():
        L.append(f"| {r.spec} | {r.coef:+.2f} {r.unit} | [{r.ci_low:+.2f}, {r.ci_high:+.2f}] | {fmt_p(r.p)} | "
                 f"{r.n_reviews:,} | {r.n_apps} |")
    L += ["", "## Heterogeneity", "", "| Question | Split | Estimate | 95% CI | p | p (groups equal) |", "|---|---|---|---|---|---|"]
    for r in est[est["section"] == "heterogeneity"].itertuples():
        L.append(f"| {r.question} | {r.spec} | {r.coef:+.2f} {r.unit} | [{r.ci_low:+.2f}, {r.ci_high:+.2f}] | "
                 f"{fmt_p(r.p)} | {fmt_p(r.p_equal)} |")
    L += ["", "## Robustness of R1", "", "| Check | Estimate | 95% CI | p |", "|---|---|---|---|"]
    for r in est[est["section"] == "robustness"].itertuples():
        L.append(f"| {r.spec} | {r.coef:+.2f} {r.unit} | [{r.ci_low:+.2f}, {r.ci_high:+.2f}] | {fmt_p(r.p)} |")
    L += [f"| 9. Leaving out one app at a time | {loo['coef'].min():+.2f} to {loo['coef'].max():+.2f} pp | "
          f"largest change: without `{far['dropped']}` ({far['coef']:+.2f}) | |",
          f"| 10. App by app ({len(gaps)} apps with at least 100 reviews in each language) | "
          f"{(gaps['coef'] < 0).sum()} negative, {(gaps['coef'] > 0).sum()} positive; "
          f"{((gaps['ci_high'] < 0)).sum()} significantly negative, {((gaps['ci_low'] > 0)).sum()} significantly positive | "
          "`app_gaps.pdf` | |", ""]
    (out / "summary.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


# ---------------------------------------------------------------- validation sample (needs review text)
def validation(inp, out, n=50, seed=7):
    df, _, _ = review_frame(inp)
    s = df[(df["lang_main"].map(group_of) == "ind") & (df["reply_det"] == 1)].copy()
    s["group"] = np.where(s["reply_indian"] == 1, "reply_labelled_indian", "reply_labelled_english")
    parts = [g.sample(min(n, len(g)), random_state=seed) for _, g in s.groupby("group")]
    v = pd.concat(parts).sample(frac=1, random_state=seed).reset_index(drop=True)
    v.insert(0, "sample_id", range(1, len(v) + 1))
    v["review_text"], v["reply_text"] = v["content"], v["replyContent"]
    v["human_reply_lang"], v["human_note"] = "", ""
    v[["sample_id", "package", "reviewId", "review_text", "reply_text", "human_reply_lang", "human_note",
       "lang_main", "reply_lang", "group"]].to_csv(out, index=False, encoding="utf-8-sig")
    print(f"Saved {len(v)} replies to {out} ({v['group'].value_counts().to_dict()}). Write the reply's language "
          "code in human_reply_lang (eng, hin, mar, guj, ... or und). Hide the columns after human_note while coding.")
    return v


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["aggregate", "estimate", "validation"])
    ap.add_argument("--reviews", type=Path, default=DATA / "reviews_lang.csv")
    ap.add_argument("--agg", type=Path, default=AGG)
    ap.add_argument("--launch", type=Path, default=ROOT / "data" / "launch_dates.csv")
    ap.add_argument("--packages", type=Path, default=PACKAGES)
    ap.add_argument("--placebo", type=int, default=0, help="placebo draws for R4 to add (appended)")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    if a.step == "aggregate":
        aggregate(a.reviews, a.agg, a.out)
    elif a.step == "estimate":
        estimate(a)
    else:
        validation(a.reviews, DATA / "reply_language_validation.csv")


if __name__ == "__main__":
    main()
