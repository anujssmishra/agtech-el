# AgTech AI and vernacular users: Economics Letters paper

## The study
**Main question (since 7 Oct 2026):** do Indian agtech apps answer farmers who write in an Indian language less often, more slowly, or not in their language? Registered plan: `docs/analysis_plan_replies.md`; code: `analysis/replies.py`.

- **Data.** Google Play reviews of about 47 Indian agtech farmer apps (`play_reviews/packages.csv`; full sampling frame in `data/sampling_frame/`), with each review's language and the developer's reply.
- **Outcome.** Whether a review gets a developer reply (also: days to reply, language of the reply).
- **Model.** Linear probability model with app×month, star-rating and review-length fixed effects; the coefficient of interest is on Indian-language. Standard errors clustered by app.

**Secondary question (the original one):** do AI features change who reviews these apps, moving the mix toward Indian-language users?
- **Outcome.** Review counts by app × language × month. **Treatment.** Each app's AI launch month (`data/launch_dates.csv`, coded from news coverage).
- **Model.** Poisson regression (PPML) with app×month, language×month and app×language fixed effects. The coefficient of interest is on AI × Indian-language. Standard errors are clustered by app, with randomization-inference placebos. Result: no detectable effect (`results/results_summary.md`; take-up follow-up in `results/ai_takeup/`).

The author is Anuj (IIM Lucknow). Write for an economist reader: plain language, numbers with units, no overstatement.

## Map
- `play_reviews/`: `scrape_reviews.py`, then `detect_language.py`, then `build_panel.py`. Its own README.md explains each step and the language-labelling choices.
- `analysis/`: `replies.py` (main question: reply gaps), `ai_takeup.py` (AI mentions), `estimate.py` (AI and reviewer composition, event study, placebos), `simulate_panel.py` (fake data with a known effect) and `power_simulation.py`.
- `data/launch_dates.csv`: edited by hand. It holds launch months, which apps are included, and per-app panel end dates.
- `data/firm_events.csv`: funding rounds and acquisitions from public news, used for the overlap robustness check.
- `results/`: estimation outputs. Commit them.
- `TODO.md`: the shared to-do list. `cloud_tasks/` holds one instruction file per task.

## Rules
1. **The repository stays private.** Never commit review text, reviewer names or raw or labelled review files; `.gitignore` keeps them out. The only data files that go to git are aggregates: `panel_app_lang_month.csv`, `app_month.csv`, `apps_metadata.csv`, `scrape_summary.csv`, `validation_report.txt`, `ai_mentions_app_lang_month.csv` (counts of reviews mentioning AI; added with the take-up plan, 6 Oct 2026) and `replies_app_lang_month.csv` (counts of reviews and developer replies; added with the reply plan, 7 Oct 2026).
2. **Sources.** Every database IIM Lucknow subscribes to (list in `docs/institute_resources.md`, including Tracxn, DATAFUL, CMIE, Venture Intelligence and PrivateCircle) may be used and cited as a source and input: the author holds written permission to publish from all of them (recorded 7 Oct 2026; the author keeps the permissions on file). Use each through the subscription and only as its permission allows (by hand or with the provider's own export tools; no scraping unless the permission covers it). Name the database and the access date as the source. Commit raw extracts to git, or put them in the replication package, only if that database's permission covers redistribution; otherwise commit only derived variables. Crunchbase, PitchBook and CB Insights are not subscribed and stay excluded: their terms bar reuse or automated access. Other sources are public news articles, press releases and official statistics.
3. **Method changes.** Do not change the estimating equation, the language-labelling rules or `lexicons.py` without stating the change in the task summary. Run `python -m pytest -q` after any code change.
4. **Network.** The default network (Trusted) cannot reach Google Play. Scraping needs the environment set to Custom with `play.google.com` allowed (or Full). Keep the scraper's default `--delay 2`.
5. **Long commands.** Commands stop after 10 minutes, and background jobs stop when the session goes idle. Split long work:
   - scraper: `--only <package>` per app or batch;
   - power simulation: one `--treated` value per run;
   - placebos: repeat `--placebo 100`.

   All three resume or append.
6. **Tracking.** When a task in TODO.md is done, tick it and add the date and a one-line outcome.

## Commands
If the session started without a "Cloud setup: …" line, run `CLAUDE_CODE_REMOTE=true bash scripts/cloud_setup.sh` first.
```
python -m pytest -q                                   # tests (about 1 min)
python analysis/replies.py aggregate                  # reply counts from the review file (local only)
python analysis/replies.py estimate --placebo 100     # reply gaps; repeat to 1,000 placebo draws for R4
python play_reviews/detect_language.py demo           # language labels on sample sentences
python analysis/simulate_panel.py --out data/sim      # fake panel with a known +15% effect
python analysis/estimate.py --panel data/sim/panel_app_lang_month.csv --launch data/sim/launch_dates.csv --out results/sim --placebo 100
python analysis/power_simulation.py --treated 8 --reps 50          # repeat for 12, 16, 20
python analysis/estimate.py --placebo 100                          # real data (needs the panel and launch dates)
python analysis/estimate.py --exclude-overlap 3 --out results/no_overlap
```

## Economics Letters requirements
- At most 2,000 words, excluding references.
- Abstract of at most 100 words.
- 3–5 highlights of at most 85 characters each.
- 1–7 keywords and at most 6 JEL codes.
- A data availability statement.
