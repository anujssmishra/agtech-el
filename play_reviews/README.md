# Google Play reviews → language labels → app × language × month panel

| File | What it does |
|---|---|
| `packages.csv` | The 47 apps from the sampling frame. Set `scrape` to 0 to skip an app. |
| `scrape_reviews.py` | Downloads reviews and app details from Google Play. Resumable. |
| `detect_language.py` | Labels each review's language (English, Hindi, Marathi … native script or romanized). |
| `lexicons.py` | Word lists used for romanized text. Edit if hand-checking shows systematic errors. |
| `build_panel.py` | Counts reviews by app × language × month, with zeros, ready for Poisson regression. |
| `run_all.bat` / `run_all.sh` | Runs scrape → label → panel in one go (Windows / Mac). |

Run the scraper on your own computer: Google Play cannot be reached from Claude's workspace.

## One-time setup (Windows)

1. Install Python 3.12 from python.org (tick "Add python.exe to PATH").
2. Open this folder in File Explorer, type `cmd` in the address bar and press Enter.
3. In that window:

```
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python detect_language.py download-models
```

The last command downloads IndicLID's native-script model (170 MB) into `models\`. If `fasttext-wheel`
will not install, delete that line from `requirements.txt` and skip the download: Indian-script reviews are
then labelled by script, and only Hindi vs Marathi in Devanagari becomes less precise.

## On a Mac

Same steps, in Terminal from this folder:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python detect_language.py download-models
```

Then run the commands under **Run** with `/` instead of `\` in paths (for example
`test_data/scrape_summary.csv`). `./run_all.sh` runs the whole pipeline; make it executable once with
`chmod +x run_all.sh` if needed. If `fasttext-wheel` will not install, delete that line from
`requirements.txt` and skip `download-models`, as described above.

## Run

Each time, open `cmd` in this folder and run `.venv\Scripts\activate` first.

1. **Test (2–3 minutes)**
   `python scrape_reviews.py --only com.ulink.agrostar --max-per-bucket 200 --out test_data`
   Open `test_data\scrape_summary.csv`: languages should show reviews, and none should say `error`.
2. **Full scrape (a few hours)**
   `python scrape_reviews.py`
   Stop it any time with Ctrl+C and run the same command again: it carries on where it stopped.
   Later, `python scrape_reviews.py --refresh` adds only reviews posted since the last run.
3. **Label languages** `python detect_language.py label`
4. **Hand-check the labels** (for the paper's appendix)
   `python detect_language.py sample --n 600` writes `data\validation_sample.csv`. In Excel, hide the
   `form`, `lang` and `lang_main` columns, fill `human_lang` with a code (eng hin mar guj pan ben tam tel
   kan mal ori asm urd oth, or und if you cannot tell), save as CSV UTF-8, then run
   `python detect_language.py evaluate data\validation_sample.csv`.
5. **Build the panel** `python build_panel.py`

Steps 3–5 need no internet. Claude can also run them from its side on the `data` folder once the scrape is done.

## What you get (in `data\`)

| File | Contents |
|---|---|
| `reviews_raw.csv` | One row per review: package, review ID, date (UTC), stars, thumbs-up, app version, text, developer reply, and `play_langs` (the language requests that returned it). |
| `apps_metadata.csv` | Per app at scrape time: installs, rating, number of ratings, **release date**, last update. A dated copy is kept for each run. |
| `scrape_summary.csv` | Per app × language: status, reviews, oldest and newest review. |
| `reviews_lang.csv` | `reviews_raw.csv` plus the language columns (see the top of `detect_language.py`). |
| `panel_app_lang_month.csv` | App × language × month counts, zeros included (details below). |
| `app_month.csv` | App × month totals, Indian-language shares under each measure, mean stars. |
| `replies_app_lang_month.csv` | App × month × language label × stars × review-length bin: reviews, developer replies, reply delays (sum of log(1 + days)), reply languages. Written by `analysis/replies.py aggregate`; rules in `docs/analysis_plan_replies.md`. No text, so it is committed. |
| `ai_mentions_app_lang_month.csv` | App × month × language label: reviews, reviews mentioning AI (M1, M2) and star sums. Written by `analysis/ai_takeup.py aggregate`; keyword rules in `docs/analysis_plan_ai_takeup.md`. No text, so it is committed. |

Panel count columns:

- `n_main`: the language label, with *mixed* reviews (mostly English words plus a few Hindi ones) counted as English. Use this for the main estimate.
- `n_mixed_ind`: the same, but mixed reviews count as Indian-language.
- `n_script`: only reviews in an Indian script count as Indian, and all Latin-letter reviews count as English. This is the most conservative measure.
- `n_play`: Google Play's own language tag.

The `indian` column is 1 for Indian languages and 0 for English. It is blank for *Undetermined* and *No text* rows (emoji only, for example), which you should drop before estimating.

## How languages are labelled, and why

- **One request per language.** Google Play returns only reviews tagged with the requested language. The scraper asks for English plus 12 Indian languages and merges the results by review ID. If Google ignores a language code and returns its default list, that language is marked `not_filtered` and skipped. No reviews are lost, because they arrive through the other languages.
- **Indian scripts.** IndicLID (AI4Bharat) decides the language. On short Devanagari reviews it often names the wrong language: in tests it labelled "अच्छा" Sanskrit, "खूप छान" Kashmiri and "बेकार ऐप" Dogri. For those cases, Marathi and Hindi word lists make the final call.
- **Latin letters.** Each word is checked against English word frequencies (`wordfreq`) and the romanized-Indian word lists in `lexicons.py`:
  - "bahut accha app hai" is romanized Hindi.
  - "khup chan app aahe" is romanized Marathi.
  - "very good app" is English.

  IndicLID's romanized-text model is **not** used by default. In tests it labelled "good" Manipuri, "nice app" Odia and "super" Punjabi, all with confidence above 0.9, and those are among the most common reviews. `--ftr` lets it decide only reviews of four or more words that the lists cannot place.
- **Unplaced reviews.** Reviews the lists cannot place (names only, rare dialect words) are labelled *Undetermined*. Hand-checking (step 4) gives the accuracy figures to report.

## Notes for the paper

- **Dates.** Review dates are last-edit dates, the only dates Google Play shows. Months are in Indian time.
- **What Google Play returns.** It returns only reviews with text, not star ratings without text. Apps already removed from the store cannot be scraped (survivorship; see the sampling frame).
- **Privacy.** Reviewer names and photos are never stored. Don't publish review text. Share the panel and these scripts as the replication package.
- **Google's terms.** Scraping Google Play is common in published research, but Google's terms limit automated access. Keep the default delay and describe the collection method in the data statement.
- **Cite:**
  - Madhani, Khapra and Kunchukuttan (2023), "Bhasha-Abhijnaanam: Native-script and romanized language identification for 22 Indic languages", ACL 2023 (IndicLID).
  - Speer (2022), wordfreq v3.

## Settings worth knowing

| Option | Default | Use |
|---|---|---|
| `--since` | 2016-01-01 | Reviews older than this are not downloaded. |
| `--langs` | en,hi,mr,gu,pa,bn,ta,te,kn,ml,or,as,ur | Languages to request. |
| `--delay` | 2 | Average seconds between requests. Raise it if Google starts refusing. |
| `--out` | `data` | Output folder. This folder is synced by OneDrive; if that is slow, use `--out C:\play_data` (and give the same folder to the other scripts with `--in` / `--out`). |
| `--insecure-tls` | off | Only if your network breaks HTTPS certificate checks. |

## If something goes wrong

- **Many "failed … retrying" lines.** Google is limiting requests. Stop, wait an hour, then rerun with `--delay 5`.
- **A language shows `error` in `scrape_summary.csv`.** Rerun; that language resumes.
- **A language shows 0 reviews with the note "no reviews in this language".** Google sends no review list for a
  language with no reviews. If the app clearly has reviews in that language, it was a glitch: rerun that
  language with `--refresh --only <package> --langs <code>`.
- **The summary shows a language's oldest review much later than the app's release date.** That is all Google returned for that language.
