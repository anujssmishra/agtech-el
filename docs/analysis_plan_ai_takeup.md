# Analysis plan: do Indian-language users take up AI features?

**Registered 6 October 2026, before any of the outcomes below were computed or looked at.** This file is
committed to the repository before the analysis code is run; its git timestamp is the registration record.
Any change after registration is listed in a "Deviations" section at the end, with the reason.

## What had been seen before registration

- The main composition results (task 06): the share of Indian-language reviews did not change detectably
  after AI launches (main measure −12.3%, randomization p = 0.60).
- Language shares by app, owner type and year (`results/descriptives.md`).
- **Not seen:** any count of AI-related words in reviews, any star ratings by language, any split of review
  text by period. No keyword has been matched against the review data.

## Questions and hypotheses (all tests two-sided, 5% level)

- **H1 (take-up).** After an app's AI launch, the share of its reviews that mention AI features rises.
- **H2 (main question).** The post-launch rise in AI mentions differs between Indian-language and English
  reviews of the same app. (The motivating conjecture is that it is smaller among Indian-language reviews,
  but the test is two-sided.)
- **H3 (supporting).** Within the same app and month, Indian-language reviewers give different star ratings
  from English reviewers.

## Data and sample

- Review-level file `play_reviews/data/reviews_lang.csv` (local only; never committed), scraped 5–6 Oct 2026.
- Language: `indian` = 1 for an Indian language, 0 for English (main measure: mixed reviews count as
  English). Reviews with undetermined language or no text are dropped.
- Month: review date (`at_utc`) converted to Indian time, as in `build_panel.py`; Jan 2016 to Sep 2026.
- **H1 and H2 sample:** the 17 apps with `include = 1` in `data/launch_dates.csv` as of this date (10 with a
  dated launch, 7 comparison apps), months up to each app's `panel_end`. Launch months as in that file.
- **H3 sample:** all 46 scraped apps with reviews (main), and the 17-app sample (secondary).

## Outcome for H1 and H2: does a review mention AI?

Text is Unicode-normalised (NFC). Latin-script terms are matched case-insensitively at word boundaries,
except `AI`, which must be written in capitals as a separate word. Indian-script terms are matched as
substrings.

**M1, primary: explicit AI terms.** A review counts if it contains any of the following.

- Generic terms, counted in every app:
  - Latin script: `AI` (capitals, separate word); `A.I.`; `artificial intelligence` (also
    `artificial inteligence`); `chatbot`, `chat bot`, `chat-bot`; `bot` (separate word); `gpt`, `chatgpt`,
    `chat gpt`; `virtual assistant`, `voice assistant`, `digital assistant`; `machine learning`.
  - Devanagari (Hindi, Marathi): `एआई`, `ए आई`, `ए.आई`, `आर्टिफिशियल`, `कृत्रिम बुद्धिमत्ता`, `चैटबॉट`,
    `चैट बॉट`, `चॅटबॉट`, `बॉट`.
  - Other scripts ("AI"): Gujarati `એઆઈ`, Bengali `এআই`, Tamil `ஏஐ`, Telugu `ఏఐ`, Kannada `ಎಐ`, Malayalam
    `എഐ`, Punjabi `ਏਆਈ`, Odia `ଏଆଇ`, Urdu `اے آئی`.
- Feature names, counted only in reviews of the app that launched them:
  - BigHaat and Cropwise Grower: `crop doctor`.
  - ITCMAARS: `krishi mitra`, `कृषि मित्र`.
  - Amul Farmers App: `sarlaben`, `sarla ben`, `सरलाबेन`, `સરલાબેન`.
  - PMKISAN: `kisan e-mitra`, `kisan e mitra`, `kisan emitra`, `किसान ई-मित्र`, `किसान ई मित्र`. A plain
    "e-Mitra" is not counted, because it also names Rajasthan's government service kiosks.
  - Dvara Surabhi: `e-tag`, `etag`, `muzzle`.
  - Uzhavan: `pest identification`, `identify pest`.
  - Krishify's "Bhoomi" is not counted, because *bhoomi* also means land.

**M2, secondary: M1 plus photo, scan and voice terms**, which have higher recall and lower precision.
- Latin script: `photo`, `pic`, `picture`, `image`, `scan`, `camera`, `voice`, `bol kar`, `bolkar`,
  `bol ke`.
- Devanagari: `फोटो`, `फ़ोटो`, `तस्वीर`, `स्कैन`, `कैमरा`, `आवाज`, `आवाज़`, `बोलकर`, `बोल कर`.

**Decision rule fixed in advance.** If M1 matches fewer than 200 reviews in total in treated apps after their
launch, M1 is too rare to test. M2 then becomes the primary outcome, and the report says so.

## Specifications

All are linear probability models at the review level, with coefficients in percentage points. Each is
re-estimated as a Poisson model on app × language × month counts of mentions, with total reviews as
exposure, as a robustness check.

- **H1:** `mention_i = β1 · Post_at + app FE + month FE + Indian_i + ε`.
  - `Post_at` = 1 from app *a*'s launch month on.
  - β1 is the change in the share of reviews mentioning AI after launch.
- **H2 (main):** `mention_i = β2 · Post_at × Indian_i + app × month FE + app × language FE + language × month FE + ε`.
  - This is the same structure as the main composition model.
  - β2 is how much more, or less, the post-launch AI-mention share rose among Indian-language reviews than
    among English reviews of the same app in the same month.
- **H3:** `stars_i = θ · Indian_i + app × month FE + ε`.
  - θ is the difference in star rating (1–5) between Indian-language and English reviews of the same app in
    the same month.

**Inference.**
- H1 and H2: the randomization-inference p-value is the primary test, with 1,000 placebo draws that reassign
  launch months to random apps exactly as in `estimate.py`. Standard errors clustered by app are reported as
  secondary.
- H3: standard errors clustered by app (46 clusters).

**Event study (H1 and H2).** Quarters relative to launch, binned at −4 and +4, with the quarter before launch
as the reference. This shows whether mentions jump at the launch rather than drift.

## Robustness, all specified now and all reported

1. The Poisson count version (above).
2. Mixed reviews counted as Indian (`n_mixed_ind` definition).
3. Hindi and Marathi reviews only, against English, because the keyword lists are most complete in these
   languages.
4. Excluding PMKISAN, which supplies 32% of reviews.
5. Excluding Dvara Surabhi, which has no pre-launch reviews.
6. A window of ±12 months around each launch.
7. M2 in place of M1.

## Validation of the outcome

After estimation, and whatever the results, the author hand-codes:
- 150 random M1 matches (75 English, 75 Indian-language) for precision;
- 150 random post-launch reviews from treated apps without a match (75 and 75) for missed mentions.

Precision and recall are reported by language. If precision is below 70% in either language, the report says
so and treats H2 with caution.

## Reporting

- All three hypotheses, the robustness checks and the validation are reported, whatever the results,
  together with the null result on reviewer composition from task 06.
- Exploratory analyses not listed here are labelled exploratory.

## Outputs and data files

- Code: `analysis/ai_takeup.py`.
- Results: `results/ai_takeup/` (estimates, event-study figure, placebo distribution, summary).
- Aggregate counts with no text: `play_reviews/data/ai_mentions_app_lang_month.csv` (app × language × month
  counts of M1 and M2 mentions and of all reviews). These counts are needed for replication. This file is
  added to the `.gitignore` allow-list and to CLAUDE.md rule 1 (approved with this plan). Review text stays
  off GitHub.

## Deviations

None so far.
