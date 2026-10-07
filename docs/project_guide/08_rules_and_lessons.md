# Rules and lessons learned

## Project rules (from `CLAUDE.md`; they apply to people and to Claude)

1. **The repository stays private.** Never commit review text, reviewer names, or raw or labelled review
   files. The only data files that go to git are the aggregates: `panel_app_lang_month.csv`,
   `app_month.csv`, `apps_metadata.csv`, `scrape_summary.csv`, `validation_report.txt`,
   `ai_mentions_app_lang_month.csv` (counts of reviews mentioning AI) and `replies_app_lang_month.csv` (counts of
   reviews and developer replies); none holds text. `.gitignore`
   enforces this; do not weaken it.
2. **Sources.** Do not use Tracxn, Crunchbase, PitchBook, CB Insights or Dataful pages or exports as sources
   or inputs (their terms bar reuse or automated access). Firm events cite public news articles or press
   releases.
3. **Method changes.** Do not change the estimating equation, the language-labelling rules or `lexicons.py`
   without stating the change. Run `python -m pytest -q` after any code change.
4. **Network.** Scraping needs Google Play reachable; keep the scraper's default `--delay 2`.
5. **Long commands.** Cloud commands stop after 10 minutes. Split long work: the scraper per app or batch
   (`--only`), the power simulation one `--treated` value per run, placebos `--placebo 100` at a time. All
   resume or append.
6. **Tracking.** When a task in `TODO.md` is done, tick it with the date and a one-line outcome.

Writing style for the paper and notes: plain language, numbers with units, no overstatement.

## Lessons learned (October 2026)

### Setup
- **GitHub's web upload drops hidden files.** The first upload lost `.gitignore` and `.claude/settings.json`.
  Use `git`, or check that both arrived.
- **Cloud sessions are temporary.** Files not committed are deleted when the session ends. Review text must
  not be committed, so download it to your own computer before the session ends (it was sent as two zip
  files under the app's 30 MB limit).
- **Claude Code's safety checks** may block some actions, such as merging a pull request without human
  review or packaging scraped review data. These need the owner's explicit decision.

### Data collection
- **Google sends no review list for a language with no reviews,** and `google-play-scraper` 1.2.7 crashed on
  it. Fixed on 5 Oct 2026: such a language is now recorded as having 0 reviews.
- **Scraped counts match Google Play's own counts** (ratio about 1.00 per app), so coverage since 2016 is
  essentially complete for apps still on the store.
- **About 18% of reviews are in Indian languages,** much lower than the 40% assumed in the power simulation.
- `data/firm_events.csv` uses Windows (CRLF) line endings; keep them when editing so the diff stays small.

### Launch dating
- **A feature article is not a launch.** Krishify's and Aquaconnect's original dates came from articles
  describing AI already in use; BharatAgri's August 2023 is when its chatbot was already answering 30% of
  queries. Look for the announcement, release notes or an archived store page.
- **Check comparison apps for AI too.** Uzhavan, a comparison app, turned out to have AI pest identification
  from about February 2020.
- **Check the review window.** Dvara Surabhi's reviews start after its launch, so it carries no information.
- **Sister apps:** some companies put AI in a separate app (Animall's Pashu Robot, Mahindra's Krish-e Nidaan);
  decide case by case whether that counts.
- Several news sites block automated access (YourStory, Bayer, Agro Spectrum; Business Standard at times).
  Library databases and archived pages are the dependable route.

### Analysis
- **Clustered standard errors are too small here** (few treated apps, very unequal app sizes). In simulations
  they rejected 8–24% of the time at a true zero; on the real data placebo estimates spread 2.5 times as
  widely. Use randomization inference and report intervals.
- **One app can dominate:** PMKISAN supplies 32% of reviews; leave-one-out shows how much each app matters.
- **Power is the binding constraint.** With about 10 launches only very large effects are detectable;
  adding launches and comparison apps is the most valuable improvement.
