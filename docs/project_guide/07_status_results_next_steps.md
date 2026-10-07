# Status, results and next steps (as of 6 October 2026)

## Timeline

| Date | What happened |
|---|---|
| 1 Oct 2026 | Sampling frame finished (47 apps; 100 dated funding and M&A events for 20 startups). Scraper, language labeller and panel builder written and tested. |
| 2 Oct 2026 | Estimation code, power simulation and tests prepared. Repository set up on GitHub; the web upload had dropped the hidden `.gitignore` and start-up hook, which were restored. Power simulation and dry run on simulated data done; paper table and figures added. |
| 5 Oct 2026 | Firm-event gaps filled (7 rows) and checked against the articles. Scraper fixed (it crashed on languages with no reviews). AI-launch leads collected for 41 apps (`data/launch_leads.csv`). Launch dates revised (see below). |
| 5–6 Oct 2026 | Full Google Play scrape in the cloud: 181,276 reviews from 46 apps. Languages labelled; panel built; aggregates committed. Raw data saved to the owner's computer (not GitHub). |
| 6 Oct 2026 | Main results (cloud task 06): no detectable effect. Pull request #4 opened. |

## Decisions taken (5 Oct 2026)

| App | Decision | Reason |
|---|---|---|
| Krishify | Launch moved from 2021-12 to 2023-01 | Its "Bhoomi" GPT-3 chatbot launched 12 Jan 2023; the old date was a feature article |
| Dr.Grow (Aquaconnect) | Moved to "AI from launch" (excluded) | The FarmMOJO app used AI from its 2017 launch |
| Cropwise Grower (Syngenta) | Added as treated, 2022-11 | "AI-powered" Crop Doctor announced 21 Nov 2022 |
| PMKISAN | Added as treated, 2023-09 | Kisan e-Mitra AI chatbot launched 21 Sep 2023; **still to confirm it is inside the app** |
| Uzhavan | Comparison → treated, 2020-02 | AI pest identification in the app "rolling out" by 5 Feb 2020 |
| Kisan Sarathi | Kept as a comparison app | May have an AI chatbot from about Aug 2025; unconfirmed |

## Main results (`results/results_summary.md`)

Sample: 17 apps (10 with a dated AI launch, 7 comparison apps), 94,222 reviews, Feb 2016 to Sep 2026.
16.3% of labelled reviews in the sample are in an Indian language (main measure).

| Language measure | Effect | 95% interval (clustered) | p (clustered) | p (randomization, 1,000 draws) |
|---|---|---|---|---|
| Main (mixed reviews count as English) | −12.3% | −27.1% to +5.5% | 0.165 | **0.602** |
| Mixed reviews count as Indian | −11.8% | −27.4% to +7.1% | 0.205 | |
| Indian script only | −11.6% | −25.4% to +4.7% | 0.154 | |
| Google Play language tag | +6.9% | −5.7% to +21.2% | 0.300 | |

- The placebo estimates spread 2.5 times as widely as the clustered standard error, so the realistic 95%
  interval for the main measure is about **−45% to +39%**.
- Event study: no quarter before or after launch is significant; no rise after launch.
- Robustness: no funding event within 3 months of launch −5.8% (randomization p 0.78); input and advisory apps
  only −6.3% (p 0.94); dropping each treated app in turn −20.0% to −5.8%.
- Dvara Surabhi has no reviews before its launch, so it adds nothing to the estimate. Kisan Sarathi's
  reviews start only in Aug 2025.

**Reading:** no detectable effect; the data cannot rule out moderate effects in either direction.

## Open decisions for the author

1. **Framing:** write the paper as a well-measured null with a bound, or strengthen the design first.
2. **Dvara Surabhi:** drop it from the treated count (it carries no information)?
3. **Staggered launches:** add an estimator robust to staggered timing as a robustness check (changes the
   estimating equation, so it needs approval).
4. **PMKISAN:** confirm the chatbot is inside the app; otherwise set `include = 0` or remove the date.

## To-do list

| Who | Task |
|---|---|
| Author | Review and merge pull request #4 |
| Author | Hand-code the 600-review sample and run `detect_language.py evaluate` |
| Author (library) | Confirm launch leads in EMIS/ProQuest; two sources per launch; 20% double-coded; aim for 15–20 dated launches |
| Author | Clear the remaining "check first" apps and open checks in the sampling frame; update `include` |
| Author (by hand) | Check the 33 Tracxn event leads; events may now cite Tracxn (written permission, 7 Oct 2026) |
| Author | Second sources still needed: BigHaat (2023-03), Cropwise Grower (2022-11) |
| Cloud (optional) | Placebo launches using non-AI product launches; heterogeneity by app type |
| Cloud | Task 07: draft the manuscript (at most 2,000 words; abstract, highlights, keywords, JEL codes, data statement) |
| Cloud | Task 08: replication package (README, data statement, reproduction check from shared files) |
| Author | Final read, cover letter, submission to *Economics Letters* (USD 125) |

## How to strengthen the design (if the author chooses to)

- More dated launches: Bayer FarmRise (chatbot dated only to 2025), JioKrishi, DeHaat and AgriCentral need a
  launch month; app release notes or archived Play Store pages may give it.
- More comparison apps: resolve the "check first" apps; each clean comparison app helps.
- Better labels: the hand check may show systematic errors to fix in `lexicons.py` (recorded as a method
  change).
