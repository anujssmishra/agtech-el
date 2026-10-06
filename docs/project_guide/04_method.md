# The method

All estimation code is in `analysis/estimate.py`. Do not change the estimating equation, the language rules
or `lexicons.py` without recording the change (project rule 3).

## Estimating equation

One observation per app *a*, language *l* (English or one of the Indian languages) and month *t*.
Undetermined and no-text reviews are dropped.

    E[ n_alt ] = exp( β · AI_at × Indian_l  +  α_at  +  γ_lt  +  δ_al )

- `n_alt`: number of reviews of app *a* in language *l* in month *t*.
- `AI_at`: 1 from app *a*'s AI launch month onward, 0 before (and always 0 for comparison apps).
- `Indian_l`: 1 for an Indian language, 0 for English.
- `α_at` (app × month fixed effects): absorb everything that moves an app's total reviews in a month:
  marketing, funding, outages, seasons, rating prompts.
- `γ_lt` (language × month fixed effects): absorb India-wide shifts in who writes reviews in each language
  (smartphone spread, Google Play changes).
- `δ_al` (app × language fixed effects): absorb each app's usual language mix.
- **β** is the change in Indian-language reviews relative to English ones after the launch; the effect in
  percent is 100 × (exp(β) − 1).

Estimated by Poisson pseudo-maximum likelihood (PPML; Santos Silva and Tenreyro 2006) with `pyfixest`'s
`fepois`. PPML handles the many zero counts. Groups whose counts are all zero carry no information and are
dropped before fitting.

## Inference

- **Clustered standard errors** by app (about 17 clusters). These are reported but are **too small** in this
  design: few treated apps and very unequal app sizes. In simulations the clustered test rejected 8–24% of
  the time when the true effect was zero; on the real data the placebo estimates spread 2.5 times as widely
  as the clustered standard error.
- **Randomization inference (the main test):** reassign "launches" to randomly chosen apps and months many
  times (`--placebo 100`, repeated to 1,000 draws), re-estimate each time, and report the share of placebo
  estimates at least as large in absolute value as the real one. Valid with few treated apps.

## Event study

Replaces the single post-launch dummy with quarters relative to launch (quarters −4 or earlier to +4 or
later, the quarter before launch as reference) interacted with `Indian_l`. Pre-launch quarters should be
near zero; post-launch quarters show how the effect builds up. Figure: `results/event_study.pdf`.

## Robustness checks (each in its own results folder)

| Check | Command | Folder |
|---|---|---|
| All four language measures | default | `results/` |
| No funding round or acquisition within 3 months of launch | `--exclude-overlap 3` | `results/no_overlap/` |
| Input-marketplace and advisory apps only | `--categories "Input marketplace + advisory;Advisory / crop health"` | `results/input_advisory/` |
| Drop each treated app in turn | `--leave-one-out` | `results/leave_one_out.csv` |
| Placebo (randomization) distribution | `--placebo 100` (repeat) | `results/placebo.csv`, `placebo.pdf` |

Optional extensions in the to-do list: placebo launches using non-AI product launches from the Launch log,
heterogeneity by app type, and (needs the author's approval because it changes the equation) an estimator
robust to staggered launch timing (Sun and Abraham 2021; Goodman-Bacon 2021).

## Power (before the real data; `results/power_summary.md`)

Simulated panels with a known effect (`analysis/simulate_panel.py`, `analysis/power_simulation.py`) showed:
- with 40 apps, the smallest effect detectable with 80% power by a correctly sized test is about 44% with
  8 dated launches and 31% with 20;
- review volume hardly matters; the number of launches, the number of apps and the noise in monthly counts
  do;
- on the real data the placebo spread (0.234 log points) implies a detectable effect of about 92%.

**Practical consequence:** the project needs more dated launches and more comparison apps to detect
moderate effects, and the paper should report intervals, not only significance.

## Outputs written by every estimation run (in `--out`)

`main_estimates.csv`, `main_table.csv` and `main_table.tex` (booktabs; effect in %, delta-method SE in
brackets, 95% CI, clustered and randomization p-values, counts), `event_study.csv/.png/.pdf`,
`placebo.csv/.png/.pdf`, `summary.md`, and `leave_one_out.csv` with `--leave-one-out`. Figures are black and
white, 90 mm wide (one journal column).
