# Do agtech apps answer Indian-language farmers less often? Findings (7 October 2026)

This note covers the analysis registered in `docs/analysis_plan_replies.md` (commit 517bc83), run once on
7 October 2026. The full tables are in `summary.md` and `estimates.csv`. Departures from the plan, including a
design error in R3, are listed at the end of the plan.

## In one paragraph

Indian agtech apps answer reviews written in Indian languages almost exactly as often as English reviews.
- **R1 (reply rate).** −0.57 percentage points, 95% CI −1.41 to +0.27, p = 0.18. English reviews are answered
  54.6% of the time, so the interval rules out a gap larger than about 1.4 pp, or 2.6% of the base rate. The
  comparison holds fixed the app and month, the star rating and the review length.
- **R2 (speed).** Replies come at about the same speed: +2% later for Indian-language reviews, p = 0.06.
- **Reply language.** Apps often do not answer in the farmer's language:
  - one in three replies to an Indian-language review (32.7%) is written in English;
  - in an exploratory measure, an Indian-language review is 27 percentage points more likely than an English
    review of the same app to get an Indian-language reply. Apps partly switch language, not fully.
- **R4 (AI).** AI launches did not change the reply gap: +0.8 pp, randomization p = 0.86.

The average hides a few apps with large gaps: Krish-e (−25 pp), AgriApp (−10 pp) and Uzhavan (−10 pp).

## Data

- 170,450 English and Indian-language reviews of 46 apps, January 2016 to August 2026, of which 94,036 got a
  developer reply.
- The last reviews had 35 days to receive a reply before the scrape.

## Main results

| Question | Estimate | 95% CI (clustered by app) | p |
|---|---|---|---|
| R1: reply rate, Indian minus English | −0.57 pp | −1.41 to +0.27 | 0.18 |
| R1 without star and length controls | −0.01 pp | −1.21 to +1.20 | 0.99 |
| R2: time to reply, Indian minus English (replied reviews) | +0.02 log points | −0.00 to +0.05 | 0.06 |
| R3 as registered: reply in the review's language group | +3.0 pp | −64 to +70 | 0.93 (not interpretable; see below) |
| R3b, exploratory: reply in an Indian language | +27.5 pp | +7.3 to +47.7 | 0.009 |
| R4: change in the R1 gap after an AI launch (17 apps) | +0.78 pp | −4.6 to +6.2 | 0.76; randomization 0.86 (1,000 draws) |

**Raw figures (no adjustment).**

| | English reviews | Indian-language reviews |
|---|---|---|
| Replied | 54.6% | 57.9% |
| Median time to reply | 1.8 days | 1.4 days |
| Replies written in an Indian language | 26.9% | 67.3% |
| Replies written in the review's own language | 73.1% | 63.2% |

- **Reply rates.** Before controls, Indian-language reviews are answered slightly *more* often. Holding star
  rating and length fixed turns this into a small negative gap: Indian-language reviews are longer, and
  longer reviews are answered more often.
- **English reviews answered in Hindi.** 26.9% of replies to English reviews are in an Indian language. This
  comes mostly from Animall, which replies in Hindi to almost every review.

## How robust is the reply-rate result?

- **Flexible controls.** With more flexible controls, the gap is about −0.9 pp, and it reaches p < 0.05 in some
  checks:

  | Check | Gap | p |
  |---|---|---|
  | Star and length effects allowed to differ by app | −0.88 pp | 0.057 |
  | Excluding PMKISAN | −0.94 pp | 0.022 |
  | Apps that reply to at least 10% of reviews | −0.97 pp | 0.029 |
  | Poisson model | −1.5% | 0.026 |
  | Each app weighted equally | −1.82 pp | 0.089 |

  The checks not listed give −0.28 to −0.57 pp, none with p < 0.05.
- **Size of the gap.** The fairest summary is a small gap of about 1 pp, or 2% of the base rate. Whether it
  differs from zero depends on the specification. The registered main test does not reject zero.
- **Leaving out one app at a time:** −0.94 to −0.35 pp. PMKISAN, which answers both groups alike, moves the
  estimate most.
- **App by app** (23 apps with at least 100 reviews in each language group):
  - 19 gaps are negative and 4 positive;
  - 7 are significantly negative and none significantly positive;
  - three are large: Krish-e −25 pp, AgriApp −10 pp, Uzhavan −10 pp (`app_gaps.pdf`).

  Most apps answer both groups alike, and a few answer Indian-language reviews much less often.
- **Subgroups.** None of the registered splits differs significantly for R1:
  - government vs other apps: −0.85 vs −0.91 pp;
  - marketplace vs other apps: −0.39 vs −0.62 pp;
  - negative, neutral and positive reviews: −0.87, −1.18 and −0.93 pp;
  - Hindi vs other Indian languages: −0.22 vs −1.43 pp, p for equality 0.13;
  - Indian script vs romanized: −0.64 vs −0.45 pp.

  For R2, two subgroups have p < 0.05:
  - reviews in Indian languages other than Hindi wait about 7% longer (p = 0.017; Hindi reviews do not, p for
    equality 0.014);
  - romanized reviews wait about 2% longer (p = 0.020).

  These are 2 of 33 subgroup estimates, so they should not be stressed.

## Reply language

**R3 as registered cannot be read.** Its outcome, whether the reply's language group matches the review's,
mostly measures an app's default reply language, not whether it switches to the farmer's language. The plan's
Deviations section explains this.

**The registered descriptive shares are informative:**
- 67.3% of replies to Indian-language reviews are in an Indian language, and 63.2% are in the review's own
  language;
- so 32.7% are in English.

**Exploratory (R3b).** This was defined after R3 was seen, so it should be reported as exploratory.
- Within the same app and month, an Indian-language review is 27.5 pp (95% CI 7 to 48) more likely than an
  English review to get an Indian-language reply.
- Apps differ widely, from full switching to none, as shares of replies written in an Indian language:

  | App | To English reviews | To Indian-language reviews |
  |---|---|---|
  | ITC MAARS | 0% | 83% |
  | Kisaan Diary | 2% | 88% |
  | AgroStar | 3% | 70% |
  | BigHaat | 0% | 3% |
  | Amul Farmers App | 0% | 0% |

## Still to do (author)

- **Hand-check 100 reply languages:** `play_reviews/data/reply_language_validation.csv`, kept local because it
  contains text.
  - Write the reply's language code in `human_reply_lang`.
  - Hide the columns after `human_note` while coding.
  - If accuracy is below 90%, the reply-language results must carry that caution.
- **The 600-review language check** is still pending as well.

## What this means for the paper

- **What can be claimed:**
  - Indian agtech apps answer farmers who write in Indian languages almost as often, and as fast, as farmers
    who write in English. The gap is at most about 1–2 pp on a 55% base, and the estimate is precise.
  - One in three of those replies is in English.
  - A few apps show large gaps.
  - AI launches did not change any of this.
- **What should not be claimed:**
  - a large or general neglect of Indian-language users;
  - discrimination. Reviews differ in ways that stars and length do not capture.
- **Labelling.**
  - The language-switching estimate (R3b) is exploratory and depends on the reply-language hand check.
  - The app-level gaps are descriptive.
