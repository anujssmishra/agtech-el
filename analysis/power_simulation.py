#!/usr/bin/env python3
"""
power_simulation.py - how many dated AI launches does the design need?

For each number of treated apps and each true effect, simulate panels (simulate_panel.py),
estimate the main PPML model (estimate.py) and record how often the effect is significant at 5%.
Effect 0 shows the false-positive rate (should be about 5%).

    python analysis/power_simulation.py --reps 50                      # default grid, ~15-25 min
    python analysis/power_simulation.py --treated 10 --reps 50         # one row of the grid (fits in 10 min)
    python analysis/power_simulation.py --mean-reviews 20 --tag low    # fewer reviews per app-month

Draws are appended to results/power_draws[_tag].csv, so the grid can be built in several runs.
results/power[_tag].csv and power[_tag].png summarise all draws so far.
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estimate import fit_main, prepare  # noqa: E402
from simulate_panel import simulate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def one_draw(n_apps, n_treated, effect, seed, mean_reviews):
    panel, lau = simulate(n_apps=n_apps, n_treated=n_treated, effect=effect, seed=seed, mean_reviews=mean_reviews)
    launch = {r.package: r.ai_launch_month for r in lau.itertuples() if r.ai_launch_month}
    res = fit_main(prepare(panel, launch), "n_main")
    return res


def summarise(draws, out_csv, out_png, title):
    s = (draws.groupby(["n_treated", "effect"])
         .agg(draws=("beta", "size"), power=("reject", "mean"), mean_beta=("beta", "mean"), mean_se=("se", "mean"))
         .reset_index())
    s["true_beta"] = np.log1p(s["effect"])
    s.to_csv(out_csv, index=False)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(5.5, 3.6), dpi=200)
    styles = ["-o", "--s", "-.^", ":D", "-v", "--x"]
    for i, (k, g) in enumerate(s.groupby("n_treated")):
        ax.plot(100 * g["effect"], g["power"], styles[i % len(styles)], color=str(0.15 + 0.15 * i), label=f"{k} treated apps")
    ax.axhline(0.8, color="0.6", lw=0.8, ls="--")
    ax.axhline(0.05, color="0.8", lw=0.8, ls=":")
    ax.set_xlabel("True rise in Indian-language reviews after AI launch (%)")
    ax.set_ylabel("Share of draws significant at 5%")
    ax.set_ylim(0, 1)
    ax.set_title(title, fontsize=9)
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    fig.savefig(out_png)
    plt.close(fig)
    return s


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apps", type=int, default=40)
    ap.add_argument("--treated", default="8,12,16,20")
    ap.add_argument("--effects", default="0,0.05,0.10,0.15,0.20,0.30")
    ap.add_argument("--reps", type=int, default=50)
    ap.add_argument("--mean-reviews", type=float, default=60.0, help="average written reviews per app-month")
    ap.add_argument("--tag", default="")
    ap.add_argument("--out", type=Path, default=ROOT / "results")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    tag = f"_{a.tag}" if a.tag else ""
    draws_path = a.out / f"power_draws{tag}.csv"
    old = pd.read_csv(draws_path) if draws_path.exists() else pd.DataFrame()
    rows, t0 = [], time.time()
    for k in [int(x) for x in a.treated.split(",")]:
        for e in [float(x) for x in a.effects.split(",")]:
            done = 0 if old.empty else int(((old["n_treated"] == k) & (old["effect"] == e)).sum())
            for r in range(done, done + a.reps):
                seed = 10_000 * k + 1_000 * int(round(100 * e)) + r
                res = one_draw(a.apps, k, e, seed, a.mean_reviews)
                if res:
                    rows.append({"n_treated": k, "effect": e, "seed": seed, "beta": res["beta"], "se": res["se"],
                                 "p": res["p"], "reject": int(res["p"] < 0.05)})
            print(f"treated={k:>2} effect={e:.2f}: {a.reps} draws done ({time.time() - t0:.0f}s)", flush=True)
            pd.concat([old, pd.DataFrame(rows)], ignore_index=True).to_csv(draws_path, index=False)
    draws = pd.concat([old, pd.DataFrame(rows)], ignore_index=True)
    s = summarise(draws, a.out / f"power{tag}.csv", a.out / f"power{tag}.png",
                  f"{a.apps} apps, about {a.mean_reviews:.0f} reviews per app-month")
    print(s.to_string(index=False))


if __name__ == "__main__":
    main()
