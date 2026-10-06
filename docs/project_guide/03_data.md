# The data

Five pieces, all built from public sources. Only aggregates and hand-coded tables are stored in the
repository; review text never is.

## 1. The app list (sampling frame)

- **File:** `data/sampling_frame/Indian_AgTech_Sampling_Frame.xlsx`, and `play_reviews/packages.csv` (the 47
  apps to scrape).
- **What it is:** 47 Indian farmer-facing Android apps: startups (AgroStar, BigHaat, DeHaat, Krishify,
  BharatAgri, Gramophone, Animall and others), corporates (ITCMAARS, Bayer FarmRise, Syngenta Cropwise Grower,
  UPL's nurture.farm), a cooperative (Amul), government apps (PM-KISAN, eNAM, Meghdoot, Kisan Sarathi, Uzhavan,
  Bihar Krishi, PMFBY) and AI-first apps (Plantix, KissanAI, Farmer.Chat, Bharat-VISTAAR, MahaVISTAAR-AI,
  CottonAce).
- **Workbook sheets:** Read me; Platforms (one row per app: operator, category, AI features, panel role,
  sources); Not eligible (apps left out and why); Still to verify; Directory check; Launch log (to be filled:
  one row per dated AI launch, two sources each); Firm events; Event overlap; Event leads.
- **Panel roles:** treated (dated AI launch), comparison (no AI found), AI from launch (excluded: no
  before-and-after), check first (unresolved).

## 2. Google Play reviews

- **Collected with:** `play_reviews/scrape_reviews.py` (uses `google-play-scraper` 1.2.7).
- **How:** for each app, one request stream per language (English plus 12 Indian languages: Hindi, Marathi,
  Gujarati, Punjabi, Bengali, Tamil, Telugu, Kannada, Malayalam, Odia, Assamese, Urdu), country = India,
  newest first, back to 1 January 2016. Results are merged by review ID. Average 2 seconds between requests.
- **What is kept:** review ID, date, star rating, thumbs-up, app version, text, developer reply, and which
  language requests returned it. **Reviewer names and photos are never stored.**
- **Collected:** 5–6 October 2026, in the cloud. 181,276 reviews from 46 apps (CottonAce has none). Every app
  × language request stream finished; scraped counts match Google Play's own review counts.
- **Limits:** Google Play shows only reviews with text; dates are last-edit dates; apps already removed from
  the store cannot be scraped (survivorship).

## 3. Language labels

- **Done by:** `play_reviews/detect_language.py label`, with word lists in `play_reviews/lexicons.py`.
- **Indian scripts:** IndicLID (AI4Bharat, Madhani, Khapra and Kunchukuttan, ACL 2023) decides the language;
  on short Devanagari reviews, Hindi and Marathi word lists make the final call because IndicLID mislabels
  them (it called "अच्छा" Sanskrit and "खूप छान" Kashmiri).
- **Latin letters:** each word is checked against English word frequencies (`wordfreq`, Speer 2022) and
  romanized-Indian word lists: "bahut accha app hai" is romanized Hindi, "khup chan app aahe" romanized
  Marathi, "very good app" English. IndicLID's romanized model is not used by default (it called "good"
  Manipuri).
- **Four language measures** (each a count column in the panel):
  - `n_main`: the label, with *mixed* reviews (mostly English with a few Indian words) counted as English.
    **Main measure.**
  - `n_mixed_ind`: mixed reviews counted as Indian.
  - `n_script`: only reviews in an Indian script count as Indian (most conservative).
  - `n_play`: Google Play's own language tag.
- **Accuracy:** a 600-review hand check (`detect_language.py sample`, then `evaluate`) gives the figure for
  the paper's appendix. The sample was drawn on 6 Oct 2026; coding is pending.
- **Result:** on the main measure, 17.9% of labelled reviews (Indian + English) are in an Indian language. As
  shares of all reviews: English 78.0%, Hindi 12.3%, Marathi 2.2%, Gujarati 0.8%, other Indian languages
  about 1.6% together, undetermined 3.5%, no text (emoji only) 1.4%.

## 4. The panel

- **Built by:** `play_reviews/build_panel.py`.
- **Files (in the repository):**
  - `play_reviews/data/panel_app_lang_month.csv`: one row per app × language × month, zeros included,
    57,536 rows. Columns: package, platform, panel_role, month, language, indian (1/0, blank for
    undetermined), n_main, n_mixed_ind, n_script, n_play.
  - `play_reviews/data/app_month.csv`: app × month totals and Indian-language shares under each measure.
  - `play_reviews/data/apps_metadata.csv`: installs, rating, release date and so on per app at scrape time.
  - `play_reviews/data/scrape_summary.csv`: status and counts per app × language.

## 5. AI launch dates

- **File:** `data/launch_dates.csv` (edited by hand). Columns: package, platform, panel_role,
  ai_launch_month (YYYY-MM or blank), include (1/0), panel_end (optional last month), source, note.
- **Rule:** each launch needs two sources (news articles, release notes or an archived Play Store page); 20%
  are double-coded.
- **Current sample (6 Oct 2026):** 17 apps with include = 1; 10 dated launches: AgroStar 2019-09, Uzhavan
  2020-02, Dvara Surabhi 2021-06, Cropwise Grower 2022-11, Krishify 2023-01, BigHaat 2023-03, BharatAgri
  2023-08, PMKISAN 2023-09 (unconfirmed that the chatbot is inside the app), ITCMAARS 2024-02, Amul 2026-02.
  7 comparison apps: Gramophone (to Jun 2023), KhetiGaadi, Kisan Sarathi, Meghdoot, TractorJunction, eNAM,
  nurture.farm.
- **Leads:** `data/launch_leads.csv` lists, for 41 apps, the earliest dated public report of an AI feature
  found by web search, a second source where found, and what it implies. Leads must be confirmed in EMIS or
  ProQuest before use.

## 6. Firm events (for the robustness check)

- **File:** `data/firm_events.csv` (107 rows): funding rounds, acquisitions, layoffs and shutdowns for about
  20 startups, each with the first public news report, the month, the amount as reported and the source URL.
- **Use:** `estimate.py --exclude-overlap 3` drops treated apps with an event within 3 months of the AI launch
  (only BharatAgri at present: a funding round two months after its launch).
- **Sources:** public news and press releases only (Entrackr, Inc42, YourStory, Business Standard,
  company releases). Never Tracxn, Crunchbase, PitchBook, CB Insights or Dataful.
