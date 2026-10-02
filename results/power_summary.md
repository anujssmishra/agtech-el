# Power: how many dated AI launches are needed?

Task 02, run 2 Oct 2026 on simulated data only (`analysis/simulate_panel.py`); no real reviews are used.

## Bottom line

- In a 40-app panel, with a test that wrongly rejects 5% of the time when there is no effect, the smallest
  rise in Indian-language reviews detectable with 80% power is about **44% with 8 dated launches, 36% with
  12, 33% with 16 and 31% with 20**.
- Effects of 10–20% are hard to detect. Even with 20 launches, a correctly sized test catches a 10% effect
  in about 17% of samples, a 15% effect in 31% and a 20% effect in 48%.
- **App-clustered standard errors are too small in this design.** When the true effect is zero, the
  clustered p-value is below 0.05 in 8–24% of samples rather than 5% (17% pooled over the main case). The
  estimates are centred on the true effect, so the problem is the standard errors, not bias. The
  randomization-inference p-value (`estimate.py --placebo`) should be the main test.
- Review volume hardly matters: 20 or 60 written reviews per app-month give nearly the same numbers. What
  matters is the number of launches, the number of apps and how noisy monthly language counts are.

## Setup

```
python analysis/power_simulation.py --treated 8 --reps 50          # then 12, 16, 20
python analysis/power_simulation.py --treated 8 --reps 50 --mean-reviews 20 --tag low   # then 12, 16, 20
python analysis/power_simulation.py --apps 16 --treated 8 --reps 50 --tag apps16        # extra, section 4
```

Each cell has 50 simulated panels. Each panel is estimated with the main model in `estimate.py` (PPML with
app×month, language×month and app×language fixed effects, the `n_main` count, standard errors clustered by
app), and a draw counts as a rejection if the two-sided clustered p-value is below 0.05. The panels have
40 apps, 2017-01 to 2026-08, and a true effect of 0, 5, 10, 15, 20 or 30% on Indian-language reviews from
the launch month on.

- **Main case:** about 60 written reviews per app-month (the default).
- **Low case:** about 20 (`--mean-reviews 20`).

Files: `power_draws*.csv` (every draw), `power*.csv` (nominal power by cell), `power*.png` (nominal power
curves), with no suffix for the main case and `_low` and `_apps16` for the others. No draw failed to
estimate: there are 1,200 draws in each of the main and low cases and 300 in the extra case.

## 1. False positives at a true effect of zero

| Treated apps | Main case: rejected at 5% | Low case: rejected at 5% | Spread of estimates ÷ mean clustered SE, all effects (main / low) |
|---|---|---|---|
| 8 | 24% (12 of 50; 95% CI 14–37%) | 10% (5 of 50; 4–21%) | 1.53 / 1.33 |
| 12 | 20% (10 of 50; 11–33%) | 8% (4 of 50; 3–19%) | 1.33 / 1.30 |
| 16 | 16% (8 of 50; 8–29%) | 14% (7 of 50; 7–26%) | 1.35 / 1.41 |
| 20 | 8% (4 of 50; 3–19%) | 8% (4 of 50; 3–19%) | 1.31 / 1.26 |
| All | 17% (34 of 200; 12–23%) | 10% (20 of 200; 7–15%) | |

The false-positive rate is **well above 5%**. The last column shows why. Across simulated samples, the
estimates vary about 1.3–1.5 times as much as the average clustered standard error says they should. So the
clustered t-statistic is too large, and more so with few treated apps. This is the familiar problem of
cluster-robust inference when only a few clusters are treated (MacKinnon and Webb, 2018, *Econometrics
Journal*). PPML probably makes it worse here, because it gives large apps more weight, so a handful of apps carry
most of the identifying variation.

Randomization inference does not depend on these standard errors, so its p-value should be the one
reported. With at least 1,000 placebo draws (`--placebo 100` repeated ten times), a p-value near 0.05 has a
simulation error of about ±0.007.

The spread is computed over all 300 draws for each number of treated apps, as the standard deviation of
the estimate minus the true log effect. Separate standard deviations for each effect size range from 0.08
to 0.15 with no trend, so pooling them is reasonable. Averaged over all draws, the estimate minus the true
effect is −0.002 log points (SE 0.003) in the main case and 0.000 (SE 0.003) in the low case.

## 2. Power by number of treated apps and size of effect

Each entry is the share of samples in which the effect is detected at 5%. With 50 draws, a power near 0.5
has a sampling error of about ±0.07, so small reversals in a row (for example, 16 treated apps at 15% in
the main case) are noise.

### Nominal power: clustered p-value below 0.05 (as in `power.csv`, `power_low.csv` and the plots)

These figures **overstate** power, because they include the false positives in section 1.

Main case (about 60 reviews per app-month)

| Treated apps | 0% | 5% | 10% | 15% | 20% | 30% |
|---|---|---|---|---|---|---|
| 8 | 0.24 | 0.22 | 0.32 | 0.46 | 0.58 | 0.72 |
| 12 | 0.20 | 0.22 | 0.36 | 0.54 | 0.56 | 0.86 |
| 16 | 0.16 | 0.18 | 0.26 | 0.34 | 0.56 | 0.88 |
| 20 | 0.08 | 0.24 | 0.32 | 0.58 | 0.72 | 0.94 |

Low case (about 20 reviews per app-month)

| Treated apps | 0% | 5% | 10% | 15% | 20% | 30% |
|---|---|---|---|---|---|---|
| 8 | 0.10 | 0.24 | 0.24 | 0.40 | 0.52 | 0.68 |
| 12 | 0.08 | 0.14 | 0.44 | 0.42 | 0.66 | 0.84 |
| 16 | 0.14 | 0.16 | 0.24 | 0.46 | 0.68 | 0.88 |
| 20 | 0.08 | 0.16 | 0.30 | 0.54 | 0.64 | 0.84 |

### Size-corrected power: a test that rejects 5% of the time when there is no effect

These figures approximate the power of randomization inference. Let *s* be the spread of the estimates
from section 1. Then power at effect *e* is Φ(ln(1+*e*)/*s* − 1.96) + Φ(−ln(1+*e*)/*s* − 1.96). Each *s*
rests on 300 draws and is accurate to about ±4%.

Main case

| Treated apps | *s* | 0% | 5% | 10% | 15% | 20% | 30% |
|---|---|---|---|---|---|---|---|
| 8 | 0.130 | 0.05 | 0.07 | 0.11 | 0.19 | 0.29 | 0.53 |
| 12 | 0.110 | 0.05 | 0.07 | 0.14 | 0.24 | 0.38 | 0.66 |
| 16 | 0.103 | 0.05 | 0.08 | 0.15 | 0.27 | 0.42 | 0.72 |
| 20 | 0.096 | 0.05 | 0.08 | 0.17 | 0.31 | 0.48 | 0.78 |

Low case

| Treated apps | *s* | 0% | 5% | 10% | 15% | 20% | 30% |
|---|---|---|---|---|---|---|---|
| 8 | 0.127 | 0.05 | 0.07 | 0.12 | 0.20 | 0.30 | 0.54 |
| 12 | 0.117 | 0.05 | 0.07 | 0.13 | 0.22 | 0.34 | 0.61 |
| 16 | 0.112 | 0.05 | 0.07 | 0.14 | 0.24 | 0.37 | 0.65 |
| 20 | 0.096 | 0.05 | 0.08 | 0.17 | 0.31 | 0.48 | 0.78 |

## 3. Smallest effect detectable with 80% power

| Treated apps | Main, nominal | Main, size-corrected | Low, nominal | Low, size-corrected |
|---|---|---|---|---|
| 8 | above 30% | **44%** | above 30% | **43%** |
| 12 | 28% | **36%** | 28% | **39%** |
| 16 | 28% | **33%** | 26% | **37%** |
| 20 | 24% | **31%** | 28% | **31%** |

How each column is computed:
- **Nominal:** linear interpolation of the nominal power curve where it crosses 0.80. This understates the
  detectable effect, because of the false positives.
- **Size-corrected:** exp(2.80 × *s*) − 1, accurate to about ±2 percentage points.

Use the size-corrected column.

## 4. Extra run: the sample as it stands now (16 apps, 8 launches)

`data/launch_dates.csv` now has include = 1 for 16 apps, 8 of them with a dated launch. This is not 40.
One extra run used 16 simulated apps with 8 treated and otherwise the main case (`power*_apps16.*`).

- The spread is *s* = 0.146, against 0.130 with 40 apps.
- The smallest effect detectable with 80% power is about **50%**.
- Size-corrected power is 0.10 at a 10% effect, 0.16 at 15%, 0.24 at 20% and 0.44 at 30%.
- The clustered test rejected 10% of the time at a zero effect (5 of 50; 95% CI 4–21%).

## 5. What this means

**For the news coding.** More dated launches help, but each extra launch helps less than the one before.
On these assumptions, even 20 launches do not give a well-powered test of a 10–20% effect.

- Going from 8 to 20 launches lowers the detectable effect from about 44% to 31%.
- The spread *s* falls roughly with the cube root of the number of launches. Extending that trend, 80%
  power at a 20% effect would take about 60 or more launches. That is more apps than the 47-app sampling
  frame contains, so this is a rough extrapolation.
- Comparison apps count too. With the 16 apps marked include = 1 today, 8 launches can detect about 50%,
  against 44% in a 40-app panel. Clearing the "check first" apps therefore adds power, as well as adding
  launches.

The realistic plan:
- code as many launches as the sources support (15–20 is worth the effort);
- make randomization inference the main test;
- frame the result around its confidence interval, that is, which effect sizes the data rule out, rather
  than around significance alone.

**Assumptions in `simulate_panel.py` that drive these numbers.**

- **Noisy monthly counts.** Each app × language × month count has negative-binomial noise with dispersion
  2. In other words, it varies by about ±70% around its expected value, independently from month to month.
  This is the main source of noise, which is why 20 versus 60 reviews per app-month barely matters. If the
  real counts are less noisy, power will be higher. Once the real panel exists, its dispersion can be
  estimated and the simulation re-run to match (`dispersion` is an argument of `simulate`, not yet an
  option of `power_simulation.py`).
- **No persistent shocks and no app-specific language trends.** Real panels probably have both, for
  example a regional marketing push or a Hindi interface update. Both would lower power and raise the
  false-positive rate further, so on this count the numbers above are optimistic.
- **Very unequal app sizes.** Sizes are log-normal with SD 1, so the largest of 40 apps is typically about
  9 times the median app. PPML weights large apps more, so a few apps dominate.
- **Long panels.** Apps enter between January 2017 and February 2024 and run to August 2026, about six years
  on average. Each launch has at least 12 months of data before it and 6 after. In the real data, panels
  that end early (BharatAgri, AgriCentral, Gramophone) and late launches (Amul, February 2026) give less to
  work with.
- **A simple effect.** The effect is the same for every treated app and every Indian language, starts in
  the launch month and persists. An effect that builds up slowly or differs by app would lower the power of
  the single post-launch coefficient.
- **Language mix.** Indian languages make up about 40% of reviews on average (the English share is drawn
  around 60%), and Hindi is the largest Indian language.
