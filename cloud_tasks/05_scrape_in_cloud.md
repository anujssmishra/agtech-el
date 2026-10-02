# 05 (Optional) Scrape Google Play in the cloud

Only if the environment's network access is Custom with `play.google.com` added (or Full). The default
route is to run the scraper on Anuj's PC.

1. Read CLAUDE.md and play_reviews/README.md.
2. Test: `cd play_reviews && python scrape_reviews.py --only com.ulink.agrostar --max-per-bucket 200 --out test_data`.
   If requests fail repeatedly (Google refusing cloud traffic), stop and report.
3. Full run, in steps that each finish within 10 minutes: metadata first
   (`python scrape_reviews.py --metadata-only`), then apps a few at a time with
   `python scrape_reviews.py --skip-metadata --only <pkg1>,<pkg2>`, rerunning the same command until every
   language of those apps is finished (`data/scrape_summary.csv`). Keep the session active; background jobs
   stop when it is idle.
4. When all apps are done: `python detect_language.py label` then `python build_panel.py`.
5. Commit only the four aggregate files that `.gitignore` allows in `play_reviews/data/`. Raw and labelled
   reviews must not be committed. They stay on this cloud machine only, and the cloud machine can be
   wiped. Report how many reviews each app has and the language shares.
6. Tick the scraping tasks in TODO.md.
