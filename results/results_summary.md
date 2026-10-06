# Main results: AI launches and Indian-language reviews

Task 06, run 6 Oct 2026 on the real panel (Google Play reviews scraped 5–6 Oct 2026). Commands:

```
python analysis/descriptives.py
python analysis/estimate.py --placebo 100 --leave-one-out          # run 10 times: 1,000 placebo draws
python analysis/estimate.py --exclude-overlap 3 --out results/no_overlap --placebo 100                 # x3
python analysis/estimate.py --categories "Input marketplace + advisory;Advisory / crop health" \
    --out results/input_advisory --placebo 100 --leave-one-out                                          # x3
```

The paper table is `results/main_table.tex` (and `.csv`); the figures are `results/event_study.pdf` and
`results/placebo.pdf`. The sample is described in `results/descriptives.md`.

## In one paragraph

We find no evidence that AI launches changed how many of an app's reviews are written in Indian
languages. On the main language measure the estimate is **−12.3%**, but it is far from statistically
significant: the randomization-inference p-value is **0.60** (1,000 placebo draws). Three of the four
language measures give similar negative estimates (−11.6% to −12.3%), while Google Play's own language tag gives
+6.9%; none is significant. The data are also too noisy to rule out sizeable effects in either direction:
judged by the spread of the placebo estimates, the 95% interval runs from about **−45% to +39%**. The result
should be read as "no detectable effect", not as evidence of no effect.

## Sample

- 17 apps with `include = 1`: 10 with a dated AI launch and 7 comparison apps; 94,222 reviews from
  February 2016 to September 2026. After cells with no information are dropped, the main estimate uses 8,663
  app × language × month cells and 89,447 reviews.
- 16.3% of reviews in the sample are in an Indian language on the main measure (18.7% if reviews mixing
  English with a few Indian words count as Indian; 10.2% counting only Indian scripts; 13.1% by Google
  Play's tag). 5.1% of reviews have no language label (undetermined or no text).
- The comparison apps are a small group: 8,966 reviews, 9.5% of the sample. Most of the identifying
  variation therefore comes from treated apps before their own launch. One app, PMKISAN, supplies 32% of all
  reviews.

## Main estimate (`results/main_table.tex`)

| Language measure | Effect (%) | 95% interval, clustered SE (%) | p, clustered | p, randomization |
|---|---|---|---|---|
| Main: mixed reviews count as English | −12.3 | −27.1 to +5.5 | 0.165 | 0.602 |
| Mixed reviews count as Indian | −11.8 | −27.4 to +7.1 | 0.205 | |
| Indian script only | −11.6 | −25.4 to +4.7 | 0.154 | |
| Google Play language tag | +6.9 | −5.7 to +21.2 | 0.300 | |

The effect is the percentage change in an app's Indian-language reviews after its AI launch, relative to
its English reviews in the same month (Poisson regression with app × month, language × month and
app × language fixed effects).

**Use the randomization-inference p-value, not the clustered one.** Across 1,000 placebo draws (random apps
and launch months), the placebo estimates spread with a standard deviation of 0.234 log points, 2.5 times
the clustered standard error of 0.094. The clustered intervals in the table are therefore much too narrow,
as the power simulation warned (`results/power_summary.md`). Using the placebo spread instead, the 95%
interval for the main estimate is −0.589 to +0.327 log points, or **−44.5% to +38.7%**. At that spread, the
smallest effect the design could detect with 80% power is about **+92%**.

## Timing (event study, `results/event_study.pdf`)

Estimates by quarter relative to the launch quarter, with the quarter before launch as the reference
(log points; standard errors in brackets):

- Before launch: −0.068 [0.140] (4 or more quarters before), +0.173 [0.117], +0.184 [0.196].
- After launch: −0.105 [0.101], −0.017 [0.158], +0.180 [0.165], −0.145 [0.160], −0.272 [0.168] (4 or more
  quarters after).

No single quarter is significant. The two positive pre-launch quarters mean the quarter just before launch
was, if anything, a low point, so the comparison is noisy rather than clearly trending. There is no sign of a
rise after launch.

## Robustness

| Check | Apps (treated) | Effect (%) | p, clustered | p, randomization |
|---|---|---|---|---|
| Main | 17 (10) | −12.3 | 0.165 | 0.602 (1,000 draws) |
| No funding round or acquisition within 3 months of launch (drops BharatAgri) | 16 (9) | −5.8 | 0.580 | 0.783 (300 draws) |
| Input-marketplace and advisory apps only | 8 (5) | −6.3 | 0.676 | 0.940 (300 draws) |
| Leave one treated app out | 16 (9) | −20.0 to −5.8 | | |

- **Leave one out** (`results/leave_one_out.csv`): the estimate stays negative whichever treated app is
  dropped. It is most negative without PMKISAN (−20.0%, the only case with a clustered p below 0.05, 0.012)
  and least negative without BharatAgri (−5.8%). In the input-and-advisory subsample it ranges from −24.6%
  (without AgroStar) to +7.6% (without BharatAgri).
- **Dvara Surabhi** has no reviews before its launch month (its first review is from July 2021, after the
  June 2021 launch), so the fixed effects absorb it: dropping it moves the estimate only from −12.3% to
  −12.4%. It is counted as a treated app but contributes no identifying variation.
- In the no-overlap sample, Google Play's language tag gives +12.7% with a clustered p of 0.019. Given how
  much the clustered p-values over-reject here, and that no randomization p-value was computed for that
  measure, this is not evidence of an effect.

## Threats and limitations

- **Too little power.** With 10 dated launches, one of which carries no information, and a small comparison
  group, only very large effects could be detected. The honest summary is an interval, not a test.
- **Launch dating.** Several launch months rest on one or two reports: PMKISAN's chatbot is not yet confirmed
  to be inside the app; Uzhavan's date is when the feature was "rolling out" (by Feb 2020); BharatAgri's
  August 2023 is when its chatbot was already in use, so the real launch is earlier; Amul's launch
  (Feb 2026) leaves only 8 months of data after it. Misdated launches bias the estimate toward zero.
- **Concurrent events.** App × month fixed effects absorb anything that moves all of an app's reviews
  (marketing, funding, outages), but not changes aimed at Indian-language users at the same time as the AI
  launch, such as a new Hindi interface or a regional campaign. Only BharatAgri has a funding round within 3
  months of launch (October 2023, 2 months after); dropping it moves the estimate to −5.8%.
- **Language labels.** About 5% of reviews cannot be labelled, and the measures disagree in sign: the three
  measures built from the review text are negative, Google Play's tag is positive. The 600-review hand check
  (pending) will show how accurate the labels are.
- **Staggered launches.** Launches fall between 2019 and 2026, so apps that launched earlier serve as
  controls for later ones. If the effect differs across apps or grows over time, this kind of regression can
  be biased (Goodman-Bacon 2021; Sun and Abraham 2021). An estimator robust to this would change the
  estimating equation, so it is left as a decision for the author.
- **What Google Play shows.** Reviews carry their last-edit date, not the original date; only reviews with
  text are returned; apps already removed from the store could not be scraped (survivorship); BharatAgri's
  panel ends in October 2025, when the company shut down.
