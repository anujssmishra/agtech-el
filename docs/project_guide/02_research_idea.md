# The research idea

## Question

Do AI features in Indian farmer apps change **who** uses and reviews them, moving the mix of users toward
people who write in Indian languages rather than English?

## Why it matters

- Most Indian farmers are more comfortable in Hindi, Marathi, Gujarati, Tamil or another Indian language than
  in English. Digital agricultural services have mostly reached better-off, English-literate users.
- New AI features (photo-based crop-disease diagnosis, chatbots, voice assistants) lower the cost of using an
  app without typing or reading English. If they work, they should widen access to farmers who were left out.
- Companies and governments (PM-KISAN's Kisan e-Mitra chatbot, Amul's Sarlaben, ITC's Krishi Mitra) market
  these features as inclusive. There is little causal evidence on whether they change who participates.
- An *Economics Letters* paper can give a clean, credible first estimate, or a credible bound if the effect is
  small.

## Mechanism and prediction

If an AI feature makes an app easier to use in Indian languages, then after the launch:
1. more Indian-language speakers start using the app, and some of them write reviews in their language;
2. so the number of Indian-language reviews rises **relative to English reviews of the same app in the same
   month**.

The relative comparison matters: an app's total reviews move with marketing, funding, outages and seasons. By
comparing languages within the same app and month, all of that drops out.

## What is measured

- **Outcome:** the number of Google Play reviews per app × language × month.
- **Treatment:** the month each app launched a farmer-facing AI feature, dated from news coverage.
- **Effect:** the percentage change in Indian-language reviews after the launch, relative to English
  reviews, net of India-wide shifts in who writes reviews.

Reviews are a proxy for users: not every user writes a review, and reviewers differ from users. The paper
interprets results as changes in the composition of *reviewers*, which is informative about the user base
but not identical to it.

## Contribution (as planned)

1. A new, transparent dataset: the near-complete set of Indian agtech farmer apps (47 in the sampling frame),
   all their Google Play reviews since 2016, and hand-dated AI launches.
2. A language-composition outcome that is cheap to measure at scale (reviews labelled by language with
   IndicLID plus word lists).
3. A credible estimate (or bound) of how much AI features shift participation toward Indian-language users.

## What the current results allow the paper to say (6 Oct 2026)

The main estimate is −12.3% with a randomization-inference p-value of 0.60: **no detectable effect**. The
data are too noisy to rule out effects between roughly −45% and +39%. A paper written now would therefore be
a well-measured null with a bound ("AI launches did not produce a large, quick shift toward Indian-language
reviewers"), not a positive finding. Whether to frame it that way, or to strengthen the design first (more
dated launches, more comparison apps), is the author's decision. See `07_status_results_next_steps.md`.

## Target journal: *Economics Letters* requirements

- At most 2,000 words, excluding references.
- Abstract of at most 100 words.
- 3 to 5 highlights, each at most 85 characters.
- 1 to 7 keywords and at most 6 JEL codes (likely O33, Q16, L86, D83).
- A data availability statement: the aggregate panel and code are shared; review text is not.
- Writing style: plain language, numbers with units, no overstatement.
