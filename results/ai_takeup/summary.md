# AI take-up by language: results

Implements `docs/analysis_plan_ai_takeup.md` (registered 6 Oct 2026). Coefficients for H1 and H2 are in
percentage points of reviews mentioning AI; H3 is in stars (1–5).

Decision rule: 26 M1 mentions in treated apps after launch (fewer than 200), so the primary outcome is M2: the review
contains AI, photo, scan or voice terms (M2).

## Share of reviews with AI, photo, scan or voice terms (M2) in treated apps (%)

| Period | English | Indian-language |
|---|---|---|
| Before launch | 0.15 (58 of 38,256) | 0.38 (30 of 7,908) |
| After launch | 0.29 (85 of 29,342) | 0.31 (17 of 5,526) |

## Main estimates

| Hypothesis | Sample | Estimate | 95% CI (clustered) | p (clustered) | p (randomization) |
|---|---|---|---|---|---|
| H1 | main | -0.172 pp | [-0.484, +0.139] | 0.258 | 0.450 (1,000 draws) |
| H2 | main | -0.348 pp | [-0.977, +0.282] | 0.259 | 0.457 (1,000 draws) |
| H3 | all 46 apps | -0.245 stars | [-0.283, -0.207] | <0.001 |  |
| H3 | 17-app sample | -0.233 stars | [-0.298, -0.168] | <0.001 |  |

H3: English reviews average 4.16 stars (all 46 apps).

## Robustness (clustered p-values)

| Hypothesis | Variant | Outcome | Estimate | p |
|---|---|---|---|---|
| H1 | Poisson counts, exposure = reviews | M2 | -0.488 (log points) | 0.348 |
| H2 | Poisson counts, exposure = reviews | M2 | +1.803 (log points) | 0.500 |
| H1 | Mixed reviews count as Indian | M2 | -0.170 pp | 0.258 |
| H2 | Mixed reviews count as Indian | M2 | -0.346 pp | 0.315 |
| H1 | Hindi and Marathi vs English only | M2 | -0.190 pp | 0.234 |
| H2 | Hindi and Marathi vs English only | M2 | -0.557 pp | 0.123 |
| H1 | Excluding PMKISAN | M2 | -0.321 pp | 0.036 |
| H2 | Excluding PMKISAN | M2 | -0.538 pp | 0.179 |
| H1 | Excluding Dvara Surabhi | M2 | -0.189 pp | 0.217 |
| H2 | Excluding Dvara Surabhi | M2 | -0.352 pp | 0.256 |
| H1 | Window of 12 months around launch | M2 | -0.210 pp | 0.415 |
| H2 | Window of 12 months around launch | M2 | -0.595 pp | 0.261 |
| H1 | M1 instead of M2 | M1 | +0.058 pp | 0.362 |
| H2 | M1 instead of M2 | M1 | +0.008 pp | 0.932 |
