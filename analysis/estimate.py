#!/usr/bin/env python3
"""
estimate.py - Poisson (PPML) estimates of the AI-launch effect on Indian-language reviews.

    python analysis/estimate.py                                   # real data, default paths
    python analysis/estimate.py --panel data/sim/panel_app_lang_month.csv --launch data/sim/launch_dates.csv --out results/sim
    python analysis/estimate.py --placebo 100                     # add 100 placebo draws (rerun to add more)
    python analysis/estimate.py --exclude-overlap 3               # drop apps with a funding round or M&A within 3 months of launch
    python analysis/estimate.py --leave-one-out                   # also re-fit dropping each treated app in turn
    python analysis/estimate.py --categories "Input marketplace + advisory;Advisory / crop health" --out results/input_advisory

Model (one row per app a, language l, month t; Undetermined / No text rows dropped):
    E[n_alt] = exp( beta * AI_at * Indian_l  +  app x month FE  +  language x month FE  +  app x language FE )
AI_at = 1 from the app's AI launch month on. App x month fixed effects absorb everything that moves an
app's total reviews (marketing, funding, outages); language x month effects absorb India-wide shifts in
who reviews apps; app x language effects absorb each app's usual language mix. beta is the change in
Indian-language reviews relative to English ones after launch: 100*(exp(beta)-1) percent.
Standard errors are clustered by app. The placebo draws reassign launches to random apps and months
(randomization inference), which stays valid with few treated apps.

Inputs
    --panel   play_reviews/data/panel_app_lang_month.csv   (from build_panel.py)
    --launch  data/launch_dates.csv   package, ai_launch_month (YYYY-MM or blank), include (1/0),
                                     panel_end (optional YYYY-MM: last month to use for that app)
    --firm-events data/firm_events.csv  package, event_month (for --exclude-overlap)
Outputs in --out (default results/): main_estimates.csv, main_table.csv/.tex (tables.py),
event_study.csv/.png/.pdf, placebo.csv/.png/.pdf, summary.md, leave_one_out.csv (with --leave-one-out).
Figures are sized for one journal column (90 mm).
"""
import argparse
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
FE = "package^month + language^month + package^language"
MEASURES = ["n_main", "n_mixed_ind", "n_script", "n_play"]
MEASURE_LABEL = {"n_main": "Main (mixed reviews count as English)", "n_mixed_ind": "Mixed reviews count as Indian",
                 "n_script": "Indian script only", "n_play": "Google Play language tag"}
FIG_W = 3.54   # inches: one column of an Elsevier journal page (90 mm)
PAPER_RC = {"font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7,
            "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
            "xtick.major.size": 2.5, "ytick.major.size": 2.5,
            "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42}


def month_index(s):
    return pd.PeriodIndex(s.astype(str), freq="M").asi8


def load(panel_path, launch_path):
    p = pd.read_csv(panel_path, dtype={"month": str})
    p = p[p["indian"].isin([0, 1])].copy()
    p["indian"] = p["indian"].astype(int)
    lau = pd.read_csv(launch_path, dtype=str).fillna("")
    if "include" not in lau:
        lau["include"] = "1"
    keep = set(lau.loc[lau["include"].str.strip().isin(["1", "1.0", "yes", "Yes"]), "package"])
    dropped = sorted(set(p["package"]) - keep)
    p = p[p["package"].isin(keep)].copy()
    if "panel_end" in lau:   # last month to use for an app (ownership change, shutdown, abandoned app)
        end = {r.package: pd.Period(r.panel_end.strip(), "M").ordinal for r in lau.itertuples() if r.panel_end.strip()}
        cap = p["package"].map(end)
        p = p[cap.isna() | (month_index(p["month"]) <= cap)].copy()
    launch = {r.package: r.ai_launch_month.strip() for r in lau.itertuples() if r.ai_launch_month.strip()}
    return p, launch, dropped


def prepare(p, launch):
    d = p.copy()
    d["t"] = month_index(d["month"])
    lt = {k: pd.Period(v, "M").ordinal for k, v in launch.items()}
    d["launch_t"] = d["package"].map(lt)
    d["post"] = (d["t"] >= d["launch_t"]).astype(int)          # NaN launch -> False
    d["treat"] = d["post"] * d["indian"]
    rel_q = np.floor((d["t"] - d["launch_t"]) / 3).clip(-4, 4)  # quarters since launch, ends binned
    d["rel_q"] = rel_q.fillna(-1).astype(int)                   # never-treated apps sit in the reference bin
    return d


def drop_zero_groups(d, y):
    """Groups whose outcome is all zero carry no information in PPML; drop them before fitting."""
    for _ in range(3):
        n0 = len(d)
        for g in (["package", "language"], ["package", "month"], ["language", "month"]):
            s = d.groupby(g)[y].transform("sum")
            d = d[s > 0]
        if len(d) == n0:
            break
    return d


def fit_main(d, y):
    import pyfixest as pf
    dd = drop_zero_groups(d, y)
    if dd["treat"].nunique() < 2:
        return None
    fit = pf.fepois(f"{y} ~ treat | {FE}", data=dd, vcov={"CRV1": "package"})
    r = fit.tidy().loc["treat"]
    return {"measure": y, "beta": r["Estimate"], "se": r["Std. Error"], "p": r["Pr(>|t|)"],
            "ci_low": r["2.5%"], "ci_high": r["97.5%"], "effect_pct": 100 * (np.exp(r["Estimate"]) - 1),
            "n_obs": len(dd), "n_apps": dd["package"].nunique(),
            "n_treated": dd.loc[dd["launch_t"].notna(), "package"].nunique(), "n_reviews": int(dd[y].sum())}


def fit_event(d, y):
    import pyfixest as pf
    dd = drop_zero_groups(d, y)
    fit = pf.fepois(f"{y} ~ i(rel_q, indian, ref=-1) | {FE}", data=dd, vcov={"CRV1": "package"})
    tb = fit.tidy().reset_index()
    tb["quarter"] = tb["Coefficient"].str.extract(r"rel_q::(-?\d+)").astype(int)
    tb = tb.rename(columns={"Estimate": "beta", "Std. Error": "se", "2.5%": "ci_low", "97.5%": "ci_high"})
    ref = pd.DataFrame([{"quarter": -1, "beta": 0.0, "se": 0.0, "ci_low": 0.0, "ci_high": 0.0}])
    return pd.concat([tb[["quarter", "beta", "se", "ci_low", "ci_high"]], ref]).sort_values("quarter")


def placebo(d, launch, y, reps, seed, min_side=6):
    """Give len(launch) randomly chosen apps a launch month drawn at random inside their own data
    window (at least min_side months on each side), refit, and keep the placebo beta."""
    rng = np.random.default_rng(seed)
    win = d.groupby("package")["t"].agg(["min", "max"])
    ok = win[(win["max"] - win["min"]) >= 2 * min_side]
    k = min(len(launch), len(ok))
    out = []
    base = d.drop(columns=["launch_t", "post", "treat", "rel_q"])
    for r in range(reps):
        chosen = rng.choice(ok.index.to_numpy(), size=k, replace=False)
        fake = {}
        for pkg in chosen:
            lo, hi = ok.loc[pkg, "min"] + min_side, ok.loc[pkg, "max"] - min_side
            fake[pkg] = pd.Period(ordinal=int(rng.integers(lo, hi + 1)), freq="M").strftime("%Y-%m")
        res = fit_main(prepare(base, fake), y)
        if res:
            out.append({"draw_seed": seed, "draw": r, "beta": res["beta"]})
    return pd.DataFrame(out)


def keep_categories(p, launch, packages_path, cats):
    """Keep apps whose category in packages.csv starts with one of `cats` (a list of prefixes)."""
    pk = pd.read_csv(packages_path, dtype=str).fillna("")
    keep = set(pk.loc[pk["category"].apply(lambda c: any(c.startswith(x) for x in cats)), "package"])
    return p[p["package"].isin(keep)].copy(), {k: v for k, v in launch.items() if k in keep}


def leave_one_out(d, y):
    """Main estimate re-fitted without each treated app in turn."""
    out = []
    for pkg in sorted(d.loc[d["launch_t"].notna(), "package"].unique()):
        res = fit_main(d[d["package"] != pkg], y)
        if res:
            out.append({"dropped": pkg, "platform": d.loc[d["package"] == pkg, "platform"].iloc[0] if "platform" in d else pkg,
                        "beta": res["beta"], "se": res["se"], "p": res["p"], "effect_pct": res["effect_pct"],
                        "n_treated": res["n_treated"]})
    return pd.DataFrame(out)


def ri_pvalue(placebo_betas, beta):
    """Two-sided randomization-inference p-value: share of placebo estimates at least as large as |beta|."""
    return float((np.abs(np.asarray(placebo_betas)) >= abs(beta)).mean())


def overlap_exclusions(launch, events_path, k):
    ev = pd.read_csv(events_path, dtype=str).fillna("")
    ev = ev[(ev["package"] != "") & (ev["event_month"] != "")]
    out = {}
    for pkg, m in launch.items():
        e = ev.loc[ev["package"] == pkg, "event_month"]
        if e.empty:
            continue
        gaps = (pd.PeriodIndex(e, freq="M").asi8 - pd.Period(m, "M").ordinal)
        near = int(np.abs(gaps).min())
        if near <= k:
            out[pkg] = near
    return out


def save_figure(fig, path):
    """PNG at print resolution, plus a vector PDF with the same name for the manuscript."""
    import logging
    logging.getLogger("fontTools").setLevel(logging.WARNING)   # PDF font embedding is chatty
    fig.savefig(path, dpi=600)
    fig.savefig(Path(path).with_suffix(".pdf"))


def plot_event(es, path):
    """Quarterly effects with 95% intervals; black and white, one journal column wide."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    es = es.sort_values("quarter")
    est, ref = es[es["quarter"] != -1], es[es["quarter"] == -1]
    qs = list(range(int(es["quarter"].min()), int(es["quarter"].max()) + 1))
    labels = [str(q).replace("-", "−") for q in qs]
    labels[0], labels[-1] = "≤" + labels[0], "≥" + labels[-1]   # end quarters are binned
    with plt.rc_context(PAPER_RC):
        fig, ax = plt.subplots(figsize=(FIG_W, 2.3))
        ax.axhline(0, color="0.6", lw=0.6, zorder=0)
        ax.axvline(-0.5, color="0.6", lw=0.6, ls=(0, (3, 2)), zorder=0)
        ax.errorbar(est["quarter"], est["beta"], yerr=[est["beta"] - est["ci_low"], est["ci_high"] - est["beta"]],
                    fmt="o", color="black", ms=3.5, lw=0.8, capsize=1.8, capthick=0.8)
        ax.plot(ref["quarter"], ref["beta"], "o", mfc="white", mec="black", ms=3.5, mew=0.8)
        ax.annotate("ref.", (-1, 0), xytext=(0, -5), textcoords="offset points", ha="center", va="top",
                    fontsize=6.5, color="0.3")
        ax.set_xticks(qs, labels)
        ax.set_xlabel("Quarters since AI launch")
        ax.set_ylabel("Effect on Indian-language\nreviews (log points)")
        fig.tight_layout(pad=0.3)
        save_figure(fig, path)
        plt.close(fig)


def plot_placebo(pl, beta, path, p_ri=None):
    """Histogram of placebo estimates with the actual estimate marked; one journal column wide."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    lim = 1.1 * max(float(np.abs(pl["beta"]).max()), abs(beta))
    with plt.rc_context(PAPER_RC):
        fig, ax = plt.subplots(figsize=(FIG_W, 2.2))
        counts, _, _ = ax.hist(pl["beta"], bins=np.linspace(-lim, lim, 31), color="0.82", edgecolor="0.35", lw=0.4)
        ax.axvline(beta, color="black", lw=1.2)
        ax.set_xlim(-lim, lim)
        ax.set_ylim(0, 1.3 * counts.max())
        left = beta > 0  # label on the side of the line with more room
        ax.annotate("Estimate", (beta, 1), xycoords=("data", "axes fraction"), xytext=(-3 if left else 3, -1),
                    textcoords="offset points", ha="right" if left else "left", va="top", fontsize=7)
        if p_ri is not None:  # above the plot, so it never collides with the bars or the label
            ax.set_title(f"Randomization-inference p = {p_ri:.3f} ({len(pl):,} placebo draws)", fontsize=7, loc="right", pad=3)
        ax.set_xlabel("Placebo estimate (log points)")
        ax.set_ylabel("Placebo draws")
        fig.tight_layout(pad=0.3)
        save_figure(fig, path)
        plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--panel", type=Path, default=ROOT / "play_reviews" / "data" / "panel_app_lang_month.csv")
    ap.add_argument("--launch", type=Path, default=ROOT / "data" / "launch_dates.csv")
    ap.add_argument("--firm-events", type=Path, default=ROOT / "data" / "firm_events.csv")
    ap.add_argument("--measures", default=",".join(MEASURES))
    ap.add_argument("--placebo", type=int, default=0, help="placebo draws to add (appended to placebo.csv)")
    ap.add_argument("--exclude-overlap", type=int, default=-1,
                    help="drop treated apps with a funding round or M&A within this many months of launch")
    ap.add_argument("--categories", default="",
                    help="keep only apps whose category in --packages starts with one of these (separate with ';')")
    ap.add_argument("--packages", type=Path, default=ROOT / "play_reviews" / "packages.csv")
    ap.add_argument("--leave-one-out", action="store_true",
                    help="also re-estimate the main measure dropping each treated app in turn (leave_one_out.csv)")
    ap.add_argument("--out", type=Path, default=ROOT / "results")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)

    p, launch, dropped = load(a.panel, a.launch)
    notes = [f"Apps left out (include=0 or not in {a.launch.name}): {len(dropped)}"]
    if a.exclude_overlap >= 0:
        ex = overlap_exclusions(launch, a.firm_events, a.exclude_overlap)
        p = p[~p["package"].isin(ex)]
        launch = {k: v for k, v in launch.items() if k not in ex}
        notes.append(f"Dropped for a firm event within {a.exclude_overlap} months of launch: "
                     + (", ".join(f"{k} ({v} mo)" for k, v in ex.items()) or "none"))
    if a.categories:
        cats = [c.strip() for c in a.categories.split(";") if c.strip()]
        p, launch = keep_categories(p, launch, a.packages, cats)
        notes.append(f"Only apps whose category starts with: {'; '.join(cats)} ({p['package'].nunique()} apps)")
    d = prepare(p, launch)
    measures = [m.strip() for m in a.measures.split(",") if m.strip() in d.columns]

    rows = [r for r in (fit_main(d, m) for m in measures) if r]
    main_tab = pd.DataFrame(rows)
    main_tab.to_csv(a.out / "main_estimates.csv", index=False)
    if main_tab.empty:
        raise SystemExit("No treatment variation: check launch_dates.csv (dates and include=1).")

    y0 = measures[0]
    es = fit_event(d, y0)
    es.to_csv(a.out / "event_study.csv", index=False)
    plot_event(es, a.out / "event_study.png")

    pl_path = a.out / "placebo.csv"
    pl_old = pd.read_csv(pl_path) if pl_path.exists() and a.placebo else pd.DataFrame(columns=["draw_seed", "draw", "beta"])
    if a.placebo:
        seed = 1000 + int(pl_old["draw_seed"].nunique()) if len(pl_old) else 1000
        pl = pd.concat([pl_old, placebo(d, launch, y0, a.placebo, seed)], ignore_index=True)
        pl.to_csv(pl_path, index=False)
    else:
        pl = pd.read_csv(pl_path) if pl_path.exists() else pl_old
    beta0 = float(main_tab.loc[main_tab["measure"] == y0, "beta"].iloc[0])
    lines = ["# Results", "", *notes, "",
             "| Measure | Effect (%) | beta | SE | p | 95% CI (beta) | Apps (treated) | Obs |",
             "|---|---|---|---|---|---|---|---|"]
    for r in main_tab.itertuples():
        lines.append(f"| {MEASURE_LABEL.get(r.measure, r.measure)} | {r.effect_pct:+.1f} | {r.beta:.3f} | {r.se:.3f} | "
                     f"{r.p:.3f} | [{r.ci_low:.3f}, {r.ci_high:.3f}] | {r.n_apps} ({r.n_treated}) | {r.n_obs:,} |")
    if len(pl):
        p_ri = ri_pvalue(pl["beta"], beta0)
        lines += ["", f"Randomization inference ({len(pl)} placebo draws, {MEASURE_LABEL.get(y0, y0)}): p = {p_ri:.3f}"]
        plot_placebo(pl, beta0, a.out / "placebo.png", p_ri)
    if a.leave_one_out:
        loo = leave_one_out(d, y0)
        loo.to_csv(a.out / "leave_one_out.csv", index=False)
        if len(loo):
            lo, hi = loo.loc[loo["effect_pct"].idxmin()], loo.loc[loo["effect_pct"].idxmax()]
            lines += ["", f"Leave one treated app out ({MEASURE_LABEL.get(y0, y0)}): effect from {lo.effect_pct:+.1f}% "
                      f"(without {lo.platform}) to {hi.effect_pct:+.1f}% (without {hi.platform})"]
    pre = es[es["quarter"] < -1]
    if len(pre):
        lines += ["", "Pre-launch quarters (should be near zero): "
                  + ", ".join(f"q{int(q)}: {b:+.3f} (se {s:.3f})" for q, b, s in zip(pre["quarter"], pre["beta"], pre["se"]))]
    (a.out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    from tables import write_main_table
    write_main_table(a.out)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
