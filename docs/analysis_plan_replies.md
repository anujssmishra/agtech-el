# Analysis plan: do agtech apps answer Indian-language farmers less often?

**Registered 7 October 2026, approved by the author, before any outcome below was computed.** The commit
whose message begins "Register analysis plan: replies" is the registration record; the analysis code is
written and run after it. Any change after registration goes in the "Deviations" section at the end, with
the reason.

## Why this question

Firms and governments are moving farm advice and services onto phone apps. Most Indian farmers read and
write an Indian language, not English. Google Play shows each developer reply to a review, so we can measure
directly whether apps answer farmers who write in an Indian language as often, as fast, and in the same
language as farmers who write in English.

With about 170,000 reviews from 46 apps, the answer will be precise whichever way it comes out. The question
of AI and reviewer composition (task 06 and the take-up analysis) becomes a secondary section.

## What had been seen before this plan

- All results of task 06 and of the take-up analysis (`results/results_summary.md`,
  `results/ai_takeup/findings.md`). This includes one fact that shaped this design: Indian-language reviews
  are longer than English ones, and short reviews are more positive. That is why every comparison below holds
  review length fixed.
- Pooled reply coverage, not split by language or anything else:
  - 99,508 of 181,276 reviews (54.9%) have a developer reply;
  - 40 of the 46 apps reply to at least one review;
  - 31 apps reply to at least 10% of their reviews.
- **Not seen:** any reply statistic by language, app type or star rating; any reply delay; the language of
  any reply.

## Questions (all tests two-sided, 5% level)

- **R1, primary: reply rate.** Within the same app and month, and for reviews with the same star rating and
  length, is an Indian-language review more or less likely to receive a developer reply than an English
  review?
- **R2, secondary: reply speed.** Among reviews that received a reply, does the time to reply differ?
- **R3, secondary: reply language.** Are Indian-language reviews answered in an Indian language?
  - Reported as a share: the share of replies to Indian-language reviews that are written in an Indian
    language, and the share written in the review's own language.
  - Tested as a gap: within the same app and month, how much less (or more) likely is the reply's language
    to match the review's language (Indian vs English) for Indian-language reviews than for English reviews.
- **R4, secondary, low power: AI.** Does the R1 gap change after an app's AI launch? Only 10 apps have a dated
  launch, so this test can detect only large changes. That will be stated when it is reported.

## Data and sample

- Review-level file `play_reviews/data/reviews_lang.csv`, scraped 5–6 October 2026. It is local only and never
  committed.
- **Language** (`lang_main`, the main measure): `indian` = 1 for an Indian language, 0 for English. Mixed
  reviews count as English. Reviews of undetermined language or with no text are dropped.
- **Month:** review date (`at_utc`) in Indian time.
  - The window runs from January 2016 to August 2026.
  - September 2026 is left out so that every review had at least 35 days to receive a reply before the
    scrape.
- **Apps:**
  - R1–R3 use all 46 apps with reviews. Apps that never reply add no information within an app and month,
    so including them does not change the estimates.
  - R4 uses the 17-app sample of `data/launch_dates.csv` (`include` = 1, up to `panel_end`) with the same
    launch months as before.
- **Reply:** Google Play shows only the developer's latest reply to a review. A review counts as replied if
  that reply has text.

## Outcomes

- `replied` = 1 if the review has a developer reply (R1, R4).
- **Reply delay**, `log(1 + days)`, where `days` = reply date (`repliedAt_utc`) minus review date (R2).
  - Google Play dates a review by its *last edit*. A review edited after the reply therefore shows a reply
    dated before the review. Such replies are left out of R2, and the share left out is reported by
    language.
- **Reply language** (R3): the reply text is labelled with the same labeller and rules as the reviews
  (`detect_language.py`; mixed counts as English).
  - `reply_indian` = 1 if the reply is in an Indian language.
  - `matched` = 1 if the reply's language group equals the review's (Indian vs English).
  - `same_language` = 1 if the reply is in exactly the review's language.

## Specifications

All are linear probability models (or linear models for R2) at the review level. Coefficients are in
percentage points (R1, R3, R4) or log points (R2). Standard errors are clustered by app.

- **R1 (main):** `replied_i = β · Indian_i + app × month FE + star-rating FE + review-length FE + ε`.
  - Star-rating fixed effects: 1–5 stars.
  - Review-length fixed effects, by word count: 1, 2, 3–5, 6–10, 11–20, 21+.
  - β is the difference in the probability of a reply between an Indian-language and an English review of
    the same app, in the same month, with the same stars and length.
- **R2:** the same equation with `log(1 + days)` as the outcome, among replied reviews with a valid delay.
- **R3:** the same equation with `matched` as the outcome, among replied reviews.
- **R4:** `replied_i = δ · Post_at × Indian_i + app × month FE + app × language FE + language × month FE + star FE + length FE + ε`.
  - This is the structure of the main composition model.
  - Inference: randomization inference with 1,000 placebo launches, exactly as in `estimate.py`, plus an event
    study by quarter (binned at ±4, reference = the quarter before launch).

**Estimation.** Each model is estimated by weighted least squares on cell means. A cell is an
app × month × language × stars × length-bin combination, and the weight is the number of reviews in it. This
gives the same point estimates as the review-level regression.

**Unadjusted figures.** These are reported alongside the regressions:
- reply rates, median reply delays and reply-language shares, by language;
- the R1 gap with app × month fixed effects only (no star or length controls).

## Heterogeneity, specified now and all reported (R1, with R2 and R3 where samples allow)

1. Government apps vs all others (`owner_type` in `play_reviews/packages.csv`).
2. Input-marketplace apps (category containing "Input marketplace") vs all others.
3. Negative (1–2 stars), neutral (3) and positive (4–5) reviews.
4. Hindi vs other Indian languages, each against English.
5. Indian-script vs romanized Indian-language reviews, each against English.

## Robustness for R1, specified now and all reported

1. Star and length fixed effects interacted with app (app × stars, app × length bin).
2. Mixed reviews counted as Indian.
3. Excluding PMKISAN, which supplies about a third of reviews.
4. Each app weighted equally rather than by its number of reviews.
5. Only apps that reply to at least 10% of all their reviews. This share does not depend on language.
6. Excluding reviews edited after the reply.
7. Reviews from January 2020 on.
8. A Poisson model of reply counts per cell, with the number of reviews as exposure.
9. Leaving out one app at a time: the range of estimates, and which app moves it most.
10. App-by-app gaps for apps with at least 100 reviews in each language group, shown as a figure.

## Validation

- Whether a review has a reply comes straight from Google Play; it needs no validation.
- Review language: the pending 600-review hand check.
- Reply language: after estimation, and whatever the results, the author hand-codes 100 replies to
  Indian-language reviews (50 labelled Indian-language, 50 labelled English). Accuracy is reported. If it is
  below 90%, R3 is reported with that caution.

## How the results will be read

- β measures how apps treat reviews in different languages. It is not by itself evidence of discrimination.
  A gap could come from:
  - staff who cannot read some scripts;
  - reply tools that handle only English;
  - differences in content that stars and length do not capture.
- The paper will describe the gap and its pattern across app types, not claim a single cause.
- All four questions, the heterogeneity splits and the robustness checks are reported whatever the results,
  together with the task-06 and take-up results. Analyses not listed here are labelled exploratory.

## Outputs and data files

- Code: `analysis/replies.py`, with tests in `tests/test_replies.py`.
- Results: `results/replies/` (estimates, figures, summary).
- Aggregate counts with no text: `play_reviews/data/replies_app_lang_month.csv`.
  - One row per app × month × language label × stars × length bin.
  - Columns: number of reviews; number replied; number with a valid delay and the sum of `log(1 + days)`;
    replies in an Indian language; replies in the matching group and in the same language; reviews edited
    after the reply; Indian-script flag.
  - This file is needed for replication. On approval it is added to the `.gitignore` allow-list and to
    CLAUDE.md rule 1.
- On approval, CLAUDE.md "The study", the README and TODO.md are updated to make reply gaps the main
  question.

## Deviations

None so far.
