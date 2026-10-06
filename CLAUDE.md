# AgTech AI and vernacular users: Economics Letters paper

## The study
Do AI features in Indian farmer apps change who reviews them, moving the mix toward Indian-language users?

- **Data.** Google Play reviews of about 47 Indian agtech farmer apps (`play_reviews/packages.csv`; full sampling frame in `data/sampling_frame/`).
- **Outcome.** Review counts by app × language × month.
- **Treatment.** Each app's AI launch month (`data/launch_dates.csv`, coded from news coverage).
- **Model.** Poisson regression (PPML) with app×month, language×month and app×language fixed effects. The coefficient of interest is on AI × Indian-language. Standard errors are clustered by app, with randomization-inference placebos.

The author is Anuj (IIM Lucknow). Write for an economist reader: plain language, numbers with units, no overstatement.

## Map
- `play_reviews/`: `scrape_reviews.py`, then `detect_language.py`, then `build_panel.py`. Its own README.md explains each step and the language-labelling choices.
- `analysis/`: `estimate.py` (main model, event study, placebos), `simulate_panel.py` (fake data with a known effect) and `power_simulation.py`.
- `data/launch_dates.csv`: edited by hand. It holds launch months, which apps are included, and per-app panel end dates.
- `data/firm_events.csv`: funding rounds and acquisitions from public news, used for the overlap robustness check.
- `results/`: estimation outputs. Commit them.
- `TODO.md`: the shared to-do list. `cloud_tasks/` holds one instruction file per task.

## Rules
1. **The repository stays private.** Never commit review text, reviewer names or raw or labelled review files; `.gitignore` keeps them out. The only data files that go to git are aggregates: `panel_app_lang_month.csv`, `app_month.csv`, `apps_metadata.csv`, `scrape_summary.csv`, `validation_report.txt` and `ai_mentions_app_lang_month.csv` (counts of reviews mentioning AI; added with the take-up plan, 6 Oct 2026).
2. **Sources.** Do not use Tracxn, Crunchbase, PitchBook, CB Insights or Dataful pages or exports as sources or inputs: their terms bar reuse or automated access. Firm events must cite public news articles or press releases.
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
python -m pytest -q                                   # tests (about 30 s)
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
