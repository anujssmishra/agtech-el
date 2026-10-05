# To-do: Economics Letters paper

Who or where does each task:
- **You**: something only you can do.
- **PC**: your computer.
- **Cloud**: Claude Code on the web. Start a session and say "Do cloud_tasks/NN…".
- **Cowork**: the Claude chat linked to your computer.

Tick items as they are done.

## 1. Set up (once)
- [ ] **You.** Create a private GitHub repository, upload this folder and connect it to claude.ai/code (steps in README.md).
- [x] **Cloud.** `cloud_tasks/01_check_setup.md`: confirm the environment works and the tests pass. (2 Oct 2026: Python 3.11.15; every setup item ok and IndicLID downloaded on Trusted; 7 of 7 tests pass and the demo labels are correct. Restored the `.gitignore` and `.claude/settings.json` that the upload dropped.)

## 2. Can start now (no real data needed)
- [x] **Cloud.** `02_power_simulation.md`: how many dated AI launches are needed to detect a 10–20% effect. (2 Oct 2026: in a 40-app panel the effect detectable with 80% power is about 44% with 8 launches and 31% with 20, so 10–20% effects are underpowered; clustered SEs reject 8–24% of the time at a zero effect, so randomization inference should be the main test. See `results/power_summary.md`.)
- [x] **Cloud.** `03_estimation_dry_run.md`: full estimation on simulated data, with tables, event-study figure and placebos. (2 Oct 2026: true +15% estimated at +24% (95% CI 10–40%), pre-launch quarters near zero, randomization-inference p = 0.012 with 500 draws; `estimate.py` now also writes the LaTeX/CSV table (`analysis/tables.py`) and single-column black-and-white figures. See `results/dry_run_notes.md`.)
- [x] **Cloud or Cowork.** `04_firm_event_gaps.md`: BharatAgri's 2023 round and Kisanwala handover, KisanKraft, Gramophone's early rounds, Animall acquisitions. (5 Oct 2026: 7 rows added. BharatAgri's $4.3M extension dated Oct 2023; whether it includes Feb's INR 14 crore is unresolved. 6 Gramophone rounds from 2018 to 2024 added; Info Edge reached 50% only at the Jan 2026 exit. No public report found of the Kisanwala handover, KisanKraft funding or Animall acquisitions. Rows checked against the articles on 5 Oct: the Oct 2023 money is the second tranche of the extended Series A, separate from Feb's INR 14 crore; the Apr 2019 row is partly checked (Business Standard returns 403).)
- [ ] **You (Tracxn, by hand).** Check the 33 items on the "Event leads" sheet of the sampling frame. Start with BharatAgri's 2023 round and Krishify's closing date.
- [ ] **You.** Clear the 20 "Check first" apps and the 7 open checks in the sampling frame. Update `include` in `data/launch_dates.csv`.

## 3. Collect the data
- [ ] **PC.** Do the setup and the 2-minute test scrape (AgroStar), as in `play_reviews/README.md`. Or, in the cloud, use `05_scrape_in_cloud.md` with the network set to Custom plus `play.google.com`.
- [ ] **PC.** Run the full scrape: a few hours, and it can be stopped and restarted.
- [ ] **PC or Cowork.** Label languages and build the panel (`detect_language.py label`, then `build_panel.py`). Upload only the four aggregate files to `play_reviews/data/` (see `data/README.md`).
- [ ] **You (library).** Re-extract AI-launch news from EMIS and ProQuest for every app. Search the app or company name plus AI terms.
- [ ] **You + Cowork.** Code the Launch log in the sampling frame. Each launch needs two sources, and 20% are double-coded. Copy the months into `data/launch_dates.csv`. Target at least 10 dated launches, ideally 15–20.
- [ ] **You.** Hand-code 600 reviews (`detect_language.py sample`, then `evaluate`). This gives the accuracy figure for the paper's appendix.

## 4. Analysis
- [ ] **Cloud.** `06_main_results.md`: the main model under all four language measures, event study, placebos, and the funding-overlap robustness check.
- [ ] **Cloud (optional).** Placebo launches using non-AI product launches from the Launch log, and heterogeneity by app type.

## 5. Write and submit
- [ ] **Cloud.** `07_draft_manuscript.md`: Economics Letters draft, at most 2,000 words, with abstract, highlights, JEL codes and keywords.
- [ ] **Cloud.** `08_replication_package.md`: code, aggregate data and the data statement. No review text.
- [ ] **You.** Final read, cover letter and submission (USD 125 fee).

## Done
- [x] Sampling frame: 47 apps, your directory reconciled, 100 dated funding and M&A events for 20 startups (1 Oct 2026).
- [x] Scraper, language labeller and panel builder written and tested (1 Oct 2026).
- [x] Estimation code, power simulation, tests and this repository prepared (2 Oct 2026).
