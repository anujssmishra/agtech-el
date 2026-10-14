# Do Indian-language users take up AI features? Findings (6 October 2026)

This note covers the analysis registered in `docs/analysis_plan_ai_takeup.md` (commit 87621fa), run once on
6 October 2026. The full tables are in `summary.md` and `estimates.csv`. Departures from the plan are listed at
the end of the plan.

## In one paragraph

AI features almost never come up in what farmers write about these apps. Explicit AI terms appear in 90 of
181,071 reviews (0.05%). They appear in 26 of about 34,900 English and Indian-language reviews of treated apps
after their AI launch (0.07%). Because this is below the pre-set threshold of 200, the broader measure M2
(AI, photo, scan or voice terms) became the primary outcome.
- **H1.** M2 mentions did not rise detectably after AI launches: −0.17 percentage points, randomization p = 0.45.
- **H2.** The change did not differ between Indian-language and English reviews: −0.35 pp, p = 0.46.
- **H3.** Indian-language reviews give 0.245 fewer stars than English reviews of the same app in the same
  month (p < 0.001), as registered. In an exploratory check, this gap disappears once review length is held
  fixed (+0.002 stars). It reflects short English reviews such as "good" or "nice", not lower satisfaction among
  Indian-language users.

Together with the composition result from task 06, the data show no detectable effect of AI launches on who
reviews these apps or on what reviewers write about.

## Data

- **H1 and H2:** 89,447 English and Indian-language reviews of the 17 apps in the sample, 10 of them with a
  dated AI launch, from January 2016 to September 2026.
- **H3:** 172,170 reviews of all 46 apps.

## Results

| | Estimate | 95% CI (clustered by app) | p, clustered | p, randomization (1,000 draws) |
|---|---|---|---|---|
| H1: change in the share of reviews with M2 terms after launch | −0.17 pp | −0.48 to +0.14 | 0.26 | 0.45 |
| H2: Indian minus English, same change | −0.35 pp | −0.98 to +0.28 | 0.26 | 0.46 |
| H3: Indian minus English stars, same app and month (46 apps) | −0.245 stars | −0.283 to −0.207 | <0.001 | |
| H3 in the 17-app sample | −0.233 stars | −0.298 to −0.168 | <0.001 | |

- **Base rates.** Before launch, 0.15% of English and 0.38% of Indian-language reviews in treated apps
  contained M2 terms. After launch the rates were 0.29% and 0.31%. These raw before-and-after figures do not
  remove common time trends; the fixed-effect estimates above do.
- **Event studies** (`event_study_h1.pdf`, `event_study_h2.pdf`). No quarter differs detectably from the
  quarter before launch, before or after it.
- **Robustness: 14 registered variants** (7 checks × H1 and H2).
  - None changes the conclusions.
  - One variant has a clustered p-value below 0.05: H1 excluding PMKISAN, −0.32 pp, p = 0.036. It points to
    a fall in mentions, not a rise. One such p-value in 14 tests is about what chance alone produces, and the
    power simulation (task 02) showed that clustered standard errors reject too often in this design.
  - With M1 in place of M2, the estimates are +0.06 pp (H1) and +0.01 pp (H2).

## Exploratory: is the star gap a review-length effect?

A review needs a few words before its language can be identified. One- and two-word reviews are mostly
labelled English and are mostly 5 stars.

| Review length | Share of English reviews | Share of Indian-language reviews | Mean stars, English | Mean stars, Indian-language |
|---|---|---|---|---|
| 1 word | 31.7% | 13.5% | 4.57 | 4.31 |
| 2 words | 25.3% | 15.6% | 4.46 | 4.36 |
| 3–5 words | 21.0% | 28.0% | 4.07 | 4.23 |
| 6–10 words | 10.5% | 18.8% | 3.58 | 3.80 |
| 11–20 words | 6.9% | 13.1% | 3.21 | 3.62 |
| 21+ words | 4.7% | 11.0% | 2.99 | 3.31 |

Mean stars in this table are raw averages, not within the same app and month.

| H3 version | Estimate | 95% CI | p |
|---|---|---|---|
| As registered | −0.245 stars | −0.283 to −0.207 | <0.001 |
| (a) Plus review-length fixed effects | +0.002 stars | −0.141 to +0.145 | 0.97 |
| (b) Reviews of 5 or more words (53,403 reviews) | +0.051 stars | −0.100 to +0.202 | 0.50 |

Among reviews of the same length, Indian-language reviewers rate apps the same as English reviewers, or
slightly higher. The registered H3 result is a fact about which reviews can be labelled by language. It should
not be reported as evidence that Indian-language users are less satisfied.

## Validation (still to be done by the author)

- `play_reviews/data/ai_mention_validation.csv` holds 283 reviews. It contains review text, so it stays local.
  - Matches: 75 English and all 58 Indian-language M2 matches in the sample.
  - Non-matches: 75 English and 75 Indian-language post-launch reviews from treated apps, for missed mentions.
- Code `human_mentions_ai` as 1 if the review refers to an AI feature (chatbot, AI advisor, photo or voice
  diagnosis), else 0. Hide the `lang_main`, `group`, `m1` and `m2` columns while coding.
- If precision is below 70% in either language, H2 must be read with caution. Words such as "photo" and
  "image" may often refer to product pictures in the marketplace apps.

## What this means for the paper

- **No significant finding.** The data contain no significant, interpretable result supporting the idea that
  AI features draw in or serve Indian-language users. This holds for both reviewer composition (task 06) and
  take-up (this analysis).
- **What can be said:**
  - AI launches are almost invisible in farmers' reviews (0.07% of post-launch reviews mention AI);
  - there is no detectable shift in who reviews;
  - star-rating comparisons by language are confounded by review length.
- **What should not be said:**
  - that Indian-language users are less satisfied;
  - that AI features failed to reach them. Reviews are not usage data, and a feature can be used without
    being mentioned.
