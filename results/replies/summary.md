# Developer replies by review language: results

Implements `docs/analysis_plan_replies.md` (registered 7 Oct 2026). R1 and R3 are in percentage points,
R2 in log points (0.10 is about 10% longer). All models hold fixed the app and month, the star rating and the
review length, unless stated; 95% intervals and p-values are clustered by app.

## Raw figures (no adjustment)

| | English | Indian-language |
|---|---|---|
| Reviews | 140,004 | 30,446 |
| Replied (%) | 54.6 | 57.9 |
| Median days to reply | 1.8 | 1.4 |
| Replied reviews edited after the reply (%) | 2.0 | 3.0 |
| Replies of undetermined language (%) | 0.0 | 0.0 |
| Replies in an Indian language (% of determined) | 26.9 | 67.3 |
| Replies in the review's own language (% of determined) | 73.1 | 63.2 |

## Main estimates

| Question | Specification | Estimate | 95% CI | p | p (randomization) | Reviews | Apps |
|---|---|---|---|---|---|---|---|
| R1 | main | -0.57 pp | [-1.41, +0.27] | 0.177 |  | 170,450 | 46 |
| R1 | app x month fixed effects only | -0.01 pp | [-1.21, +1.20] | 0.992 |  | 170,450 | 46 |
| R2 | main | +0.02 log points | [-0.00, +0.05] | 0.058 |  | 92,032 | 40 |
| R2 | app x month fixed effects only | +0.02 log points | [-0.00, +0.05] | 0.074 |  | 92,032 | 40 |
| R3 | main | +2.98 pp | [-64.27, +70.23] | 0.929 |  | 94,036 | 40 |
| R3 | app x month fixed effects only | +4.64 pp | [-64.26, +73.53] | 0.892 |  | 94,036 | 40 |
| R4 | AI launch x Indian (17 apps) | +0.78 pp | [-4.63, +6.19] | 0.764 | 0.863 (1,000 draws) | 89,087 | 17 |

## Exploratory (not in the plan): does the reply switch to an Indian language?

R3b: how much more likely a reply is to be in an Indian language when the review is in one, within the same
app and month. Defined after R3 was seen; see the plan's Deviations.

| Specification | Estimate | 95% CI | p | Replies | Apps |
|---|---|---|---|---|---|
| main | +27.46 pp | [+7.27, +47.66] | 0.009 | 94,036 | 40 |
| app x month fixed effects only | +27.15 pp | [+5.66, +48.64] | 0.015 | 94,036 | 40 |

## Heterogeneity

| Question | Split | Estimate | 95% CI | p | p (groups equal) |
|---|---|---|---|---|---|
| R1 | Government apps vs others: government | -0.85 pp | [-2.44, +0.74] | 0.285 | 0.947 |
| R1 | Government apps vs others: other | -0.91 pp | [-1.72, -0.10] | 0.029 | 0.947 |
| R1 | Input-marketplace apps vs others: marketplace | -0.39 pp | [-2.16, +1.37] | 0.657 | 0.814 |
| R1 | Input-marketplace apps vs others: other | -0.62 pp | [-1.55, +0.30] | 0.180 | 0.814 |
| R1 | By star rating: negative | -0.87 pp | [-1.94, +0.20] | 0.108 | 0.921 |
| R1 | By star rating: neutral | -1.18 pp | [-2.86, +0.51] | 0.167 | 0.921 |
| R1 | By star rating: positive | -0.93 pp | [-1.68, -0.18] | 0.016 | 0.921 |
| R1 | Hindi vs other Indian languages (each vs English): hindi | -0.22 pp | [-0.81, +0.37] | 0.452 | 0.131 |
| R1 | Hindi vs other Indian languages (each vs English): other | -1.43 pp | [-3.24, +0.37] | 0.117 | 0.131 |
| R1 | Indian script vs romanized (each vs English): script | -0.64 pp | [-1.71, +0.42] | 0.229 | 0.724 |
| R1 | Indian script vs romanized (each vs English): romanized | -0.45 pp | [-1.30, +0.40] | 0.295 | 0.724 |
| R2 | Government apps vs others: government | +0.06 log points | [-0.01, +0.12] | 0.087 | 0.340 |
| R2 | Government apps vs others: other | +0.02 log points | [-0.00, +0.05] | 0.066 | 0.340 |
| R2 | Input-marketplace apps vs others: marketplace | +0.04 log points | [-0.01, +0.10] | 0.109 | 0.364 |
| R2 | Input-marketplace apps vs others: other | +0.02 log points | [-0.01, +0.04] | 0.139 | 0.364 |
| R2 | By star rating: negative | +0.03 log points | [-0.02, +0.08] | 0.287 | 0.983 |
| R2 | By star rating: neutral | +0.02 log points | [-0.02, +0.06] | 0.234 | 0.983 |
| R2 | By star rating: positive | +0.03 log points | [-0.01, +0.06] | 0.140 | 0.983 |
| R2 | Hindi vs other Indian languages (each vs English): hindi | +0.01 log points | [-0.01, +0.02] | 0.376 | 0.014 |
| R2 | Hindi vs other Indian languages (each vs English): other | +0.07 log points | [+0.01, +0.13] | 0.017 | 0.014 |
| R2 | Indian script vs romanized (each vs English): script | +0.03 log points | [-0.00, +0.06] | 0.093 | 0.673 |
| R2 | Indian script vs romanized (each vs English): romanized | +0.02 log points | [+0.00, +0.04] | 0.020 | 0.673 |
| R3 | Government apps vs others: government | -69.00 pp | [-100.70, -37.30] | <0.001 | 0.048 |
| R3 | Government apps vs others: other | +4.26 pp | [-63.61, +72.13] | 0.900 | 0.048 |
| R3 | Input-marketplace apps vs others: marketplace | -45.54 pp | [-69.01, -22.08] | <0.001 | 0.107 |
| R3 | Input-marketplace apps vs others: other | +20.65 pp | [-59.17, +100.47] | 0.603 | 0.107 |
| R3 | By star rating: negative | -18.12 pp | [-66.74, +30.50] | 0.455 | 0.163 |
| R3 | By star rating: neutral | -33.09 pp | [-74.51, +8.33] | 0.114 | 0.163 |
| R3 | By star rating: positive | +9.85 pp | [-61.13, +80.82] | 0.780 | 0.163 |
| R3 | Hindi vs other Indian languages (each vs English): hindi | +19.18 pp | [-50.63, +88.99] | 0.581 | 0.011 |
| R3 | Hindi vs other Indian languages (each vs English): other | -36.09 pp | [-67.52, -4.67] | 0.026 | 0.011 |
| R3 | Indian script vs romanized (each vs English): script | -2.58 pp | [-64.61, +59.46] | 0.933 | 0.027 |
| R3 | Indian script vs romanized (each vs English): romanized | +12.82 pp | [-60.29, +85.93] | 0.724 | 0.027 |

## Robustness of R1

| Check | Estimate | 95% CI | p |
|---|---|---|---|
| 1. Stars and length fixed effects by app | -0.88 pp | [-1.78, +0.03] | 0.057 |
| 2. Mixed reviews count as Indian | -0.57 pp | [-1.47, +0.32] | 0.204 |
| 3. Excluding PMKISAN | -0.94 pp | [-1.74, -0.14] | 0.022 |
| 4. Each app weighted equally | -1.82 pp | [-3.93, +0.29] | 0.089 |
| 5. Apps replying to at least 10% of reviews | -0.97 pp | [-1.83, -0.11] | 0.029 |
| 6. Excluding reviews edited after the reply | -0.57 pp | [-1.44, +0.30] | 0.195 |
| 7. Reviews from January 2020 on | -0.28 pp | [-1.09, +0.53] | 0.483 |
| 8. Poisson, reply counts (log points) | -0.01 log points | [-0.03, -0.00] | 0.026 |
| 9. Leaving out one app at a time | -0.94 to -0.35 pp | largest change: without `com.nic.project.pmkisan` (-0.94) | |
| 10. App by app (23 apps with at least 100 reviews in each language) | 19 negative, 4 positive; 7 significantly negative, 0 significantly positive | `app_gaps.pdf` | |

