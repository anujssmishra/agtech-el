#!/usr/bin/env python3
"""
simulate_panel.py - a fake app x language x month panel with a known AI effect.

Used to test the estimation code and to compute statistical power before the real data
exist. The layout matches play_reviews/build_panel.py output, so estimate.py runs on either.

    python analysis/simulate_panel.py --out data/sim --effect 0.15

How the counts are generated (log of the expected count, then negative-binomial noise):
    app size x app growth x app-month shock     (absorbed by app x month fixed effects)
  + app's language mix                          (absorbed by app x language fixed effects)
  + a common rise in Indian-language reviews    (absorbed by language x month fixed effects)
  + log(1 + effect) on Indian-language reviews after the app's AI launch
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

LANGS = ["English", "Hindi", "Marathi", "Gujarati", "Punjabi", "Bengali", "Tamil", "Telugu", "Kannada",
         "Malayalam", "Odia", "Assamese", "Urdu"]
# relative weight of each Indian language in a typical app's Indian-language reviews (Hindi-heavy)
INDIAN_WEIGHTS = [6, 2, 1.5, 1, 1, 1, 1, 1, 0.7, 0.7, 0.5, 0.7]


def simulate(n_apps=40, n_treated=15, start="2017-01", end="2026-08", effect=0.15, seed=0,
             mean_reviews=60.0, size_sd=1.0, english_share=0.6, indian_trend=0.004,
             dispersion=2.0, min_pre=12, min_post=6):
    """Return (panel, launches). mean_reviews = average written reviews per app-month, all languages."""
    rng = np.random.default_rng(seed)
    months = pd.period_range(start, end, freq="M")
    T = len(months)
    beta = np.log1p(effect)
    frames, launches = [], []
    for a in range(n_apps):
        pkg = f"sim.app{a:02d}"
        first = int(rng.integers(0, max(1, T - (min_pre + min_post) - 12)))
        size = mean_reviews * np.exp(rng.normal(0, size_sd) - size_sd ** 2 / 2)
        eng = float(np.clip(rng.beta(6 * english_share, 6 * (1 - english_share)), 0.05, 0.95))
        mix = np.concatenate([[eng], (1 - eng) * rng.dirichlet(INDIAN_WEIGHTS)])
        launch = None
        if a < n_treated and T - min_post > first + min_pre:
            launch = int(rng.integers(first + min_pre, T - min_post))
        launches.append({"package": pkg, "ai_launch_month": months[launch].strftime("%Y-%m") if launch is not None else "",
                         "include": 1, "panel_role": "Treated (simulated)" if launch is not None else "Comparison (simulated)"})
        t = np.arange(first, T)
        growth = rng.normal(0.01, 0.01)
        app_month = np.log(size) + growth * (t - first) + rng.normal(0, 0.3, len(t))
        ind = np.array([l > 0 for l in range(len(LANGS))])
        logmu = (app_month[:, None] + np.log(mix)[None, :]
                 + (indian_trend * (t[:, None] - T / 2)) * ind[None, :])
        if launch is not None:
            logmu += beta * ((t >= launch)[:, None] & ind[None, :])
        mu = np.exp(logmu)
        lam = rng.gamma(dispersion, mu / dispersion) if dispersion else mu
        n = rng.poisson(lam)
        frames.append(pd.DataFrame({
            "package": pkg, "platform": pkg,
            "panel_role": launches[-1]["panel_role"],
            "month": np.repeat(months[t].strftime("%Y-%m"), len(LANGS)),
            "language": np.tile(LANGS, len(t)),
            "indian": np.tile(ind.astype(int), len(t)),
            "n_main": n.ravel(),
        }))
    panel = pd.concat(frames, ignore_index=True)
    for m in ("n_mixed_ind", "n_script", "n_play"):
        panel[m] = panel["n_main"]
    return panel, pd.DataFrame(launches)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=Path("data/sim"))
    ap.add_argument("--apps", type=int, default=40)
    ap.add_argument("--treated", type=int, default=15)
    ap.add_argument("--effect", type=float, default=0.15, help="proportional rise in Indian-language reviews after launch")
    ap.add_argument("--mean-reviews", type=float, default=60.0)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    panel, launches = simulate(a.apps, a.treated, effect=a.effect, mean_reviews=a.mean_reviews, seed=a.seed)
    panel.to_csv(a.out / "panel_app_lang_month.csv", index=False)
    launches.to_csv(a.out / "launch_dates.csv", index=False)
    print(f"{a.out}/panel_app_lang_month.csv: {len(panel):,} rows, {panel.package.nunique()} apps, "
          f"{(launches.ai_launch_month != '').sum()} treated, true effect {a.effect:+.0%}")


if __name__ == "__main__":
    main()
