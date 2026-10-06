# Getting started, step by step

Two ways to work: **on your own computer** (needed for anything that keeps raw review text) and **with
Claude Code on the web** (cloud tasks that read and write the GitHub repository). Most people use both.

## A. On your own computer (Mac shown; Windows notes in brackets)

### A1. Get the code

```
git clone https://github.com/anujssmishra/agtech-el.git
cd agtech-el
```

You need to be a collaborator on the private repository. Prefer `git` over GitHub's web upload: the web
upload silently drops hidden files such as `.gitignore`, which is what keeps review text out of git.

### A2. Install Python packages

Use Python 3.11 or 3.12.

```
python3 -m venv .venv
source .venv/bin/activate                 # [Windows: .venv\Scripts\activate]
pip install -r play_reviews/requirements.txt -r analysis/requirements.txt
cd play_reviews && python detect_language.py download-models && cd ..     # IndicLID model, ~260 MB
```

If `fasttext-wheel` will not install, remove it from `play_reviews/requirements.txt` and skip the model
download: Indian-script reviews are then labelled by script rules (less precise only for Hindi versus Marathi).

### A3. Check that everything works (about 1 minute)

```
python -m pytest -q                              # all tests should pass (13 as of 6 Oct 2026)
python play_reviews/detect_language.py demo      # language labels for sample sentences
```

### A4. Get the review data

Either **restore** the copy saved on 6 Oct 2026 (the owner has it as two zip files:
`agtech_reviews_part1_raw_2026-10-06.zip` and `agtech_reviews_part2_labelled_2026-10-06.zip`; unzip both
inside the `agtech-el` folder, which recreates `play_reviews/data/`), then bring it up to date:

```
cd play_reviews
python scrape_reviews.py --refresh         # adds only reviews posted since the last run
python scrape_reviews.py --combine-only    # rebuilds reviews_raw.csv if it is missing
```

or **collect from scratch** (about 2 hours; stop with Ctrl+C at any time and rerun the same command to resume):

```
cd play_reviews
python scrape_reviews.py --only com.ulink.agrostar --max-per-bucket 200 --out test_data   # 2-minute test
python scrape_reviews.py                                                                  # full scrape
```

Keep the default `--delay 2`. If you see many "failed … retrying" lines, Google is limiting requests: wait an
hour and rerun with `--delay 5`.

### A5. Label languages and build the panel

```
python detect_language.py label        # data/reviews_raw.csv -> data/reviews_lang.csv (under a minute)
python build_panel.py                  # -> data/panel_app_lang_month.csv and data/app_month.csv
cd ..
```

Only aggregate files may go to GitHub: `panel_app_lang_month.csv`, `app_month.csv`,
`apps_metadata.csv`, `scrape_summary.csv`, `ai_mentions_app_lang_month.csv` (from
`analysis/ai_takeup.py aggregate`) and `validation_report.txt` after the hand check. `.gitignore`
blocks everything else in `play_reviews/data/`.

### A6. Hand-check 600 language labels

```
cd play_reviews
python detect_language.py sample --n 600          # -> data/validation_sample.csv
```

Open it in Excel, hide the `form`, `lang` and `lang_main` columns, fill `human_lang` with one code per review
(eng hin mar guj pan ben tam tel kan mal ori asm urd oth, or und if you cannot tell), save as CSV UTF-8, then:

```
python detect_language.py evaluate data/validation_sample.csv     # writes data/validation_report.txt
```

### A7. Run the analysis

```
python analysis/descriptives.py                                         # results/descriptives.md
python analysis/estimate.py --placebo 100 --leave-one-out               # repeat until 1,000 placebo draws
python analysis/estimate.py --exclude-overlap 3 --out results/no_overlap --placebo 100
python analysis/estimate.py --categories "Input marketplace + advisory;Advisory / crop health" \
       --out results/input_advisory --placebo 100 --leave-one-out
```

Results land in `results/`; `results/results_summary.md` explains them. To check the code on fake data with a
known +15% effect first:

```
python analysis/simulate_panel.py --out data/sim
python analysis/estimate.py --panel data/sim/panel_app_lang_month.csv --launch data/sim/launch_dates.csv --out results/sim --placebo 100
```

### A8. Update launch dates

Edit `data/launch_dates.csv` (by hand or with the pencil icon on GitHub): set `ai_launch_month` (YYYY-MM),
`include` (1 or 0) and, if needed, `panel_end`. Record the source in the `source` and `note` columns. Then
rerun step A7.

## B. With Claude Code on the web (cloud tasks)

1. Go to **claude.ai/code**, sign in with GitHub and install the Claude GitHub app with access to
   `agtech-el`.
2. Edit the environment (cloud icon above the message box):
   - **Network access:** Trusted (default) is enough for code and analysis. For **scraping**, use Custom
     with `play.google.com` added (or Full). For **web research** on launches and firm events, use Full or
     Custom with the news sites (entrackr.com, inc42.com, yourstory.com, business-standard.com and so on).
   - **Environment variable:** `BASH_DEFAULT_TIMEOUT_MS=600000` so commands may run for 10 minutes.
3. Pick the repository and the environment, choose **Accept edits** as the permission mode, and type a task,
   for example `Do cloud_tasks/07_draft_manuscript.md`.
4. Each session installs packages and the language model by itself (1–2 minutes, via the start-up hook in
   `.claude/settings.json` that runs `scripts/cloud_setup.sh`).
5. Claude works on a branch and pushes it; review the changes and merge the pull request on GitHub.

**Important:** a cloud session's files are deleted when the session ends. Anything not committed (raw reviews
included) is lost. Raw review text must never be committed, so save it to your own computer first.

### The cloud tasks (`cloud_tasks/`)

| Task | What it does | Status (6 Oct 2026) |
|---|---|---|
| 01_check_setup | Check the environment and tests | Done |
| 02_power_simulation | How many launches are needed | Done |
| 03_estimation_dry_run | Full analysis on simulated data; paper table and figures | Done |
| 04_firm_event_gaps | Fill gaps in funding and acquisition events (web research) | Done |
| 05_scrape_in_cloud | Scrape Google Play in the cloud | Done |
| 06_main_results | Main results on the real data | Done (pull request #4) |
| 07_draft_manuscript | Economics Letters draft in LaTeX | To do |
| 08_replication_package | Replication README, data statement, reproduction check | To do |
