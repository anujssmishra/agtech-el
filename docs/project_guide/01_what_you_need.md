# What you need to start this project

A checklist. Items marked **essential** are needed for the core pipeline; the rest help but are optional.

## Accounts and access

| Item | Why | Notes |
|---|---|---|
| **GitHub account** (essential) | The code and aggregate data live in the private repository `anujssmishra/agtech-el` | Free. The owner must add you as a collaborator. Keep the repository private. |
| **Claude Pro, Max, Team or Enterprise plan** | To run the "cloud tasks" with Claude Code on the web (claude.ai/code) | Optional if you run everything yourself. Sign in with GitHub and install the Claude GitHub app on the repository. |
| **University library access to EMIS and ProQuest** (essential for launch dating) | AI-launch dates are coded from news archives; each launch needs two sources | IIM Lucknow access was used. Searches must be done by hand under the databases' terms. |
| **Tracxn** (optional) | Leads on funding rounds and acquisitions | Only by hand, as leads. Tracxn, Crunchbase, PitchBook, CB Insights and Dataful may **never** be cited or used as inputs: their terms bar reuse. Every firm event must cite a public news article or press release. |
| **Journal account** (at the end) | Submission to *Economics Letters* (Elsevier) | Submission fee USD 125. |

## Computer and software

| Item | Version | Notes |
|---|---|---|
| **Computer** (essential) | Mac or Windows PC with about 2 GB free disk | The language model alone is about 260 MB; the scraped reviews about 200 MB uncompressed. |
| **Python** (essential) | 3.11 or 3.12 | Newer versions may not install `fasttext-wheel`. |
| **Python packages** (essential) | `google-play-scraper==1.2.7` (pinned), `pandas`, `wordfreq`, `fasttext-wheel`, `pyfixest`, `numpy`, `matplotlib`, `pytest` | Listed in `play_reviews/requirements.txt` and `analysis/requirements.txt`. |
| **IndicLID language model** | `indiclid-ftn` (AI4Bharat) | Downloaded by `python detect_language.py download-models` from GitHub. Without it, Indian-script reviews are labelled by script rules only. |
| **git** | any recent | Recommended for uploading: GitHub's web upload drops hidden files such as `.gitignore`. |
| **LaTeX** (for the paper) | TeX Live with `booktabs`, `threeparttable`, Elsevier's `elsarticle` | Needed only to compile the manuscript and the results table. |
| **Spreadsheet program** | Excel or similar | For the sampling frame workbook and for hand-coding the 600-review sample. |

## Network

- Google Play must be reachable from wherever you scrape (your own computer works; in Claude Code on the web
  the environment's network must be **Custom with `play.google.com` allowed**, or **Full**).
- Web research on launch dates and firm events in the cloud needs news sites reachable (network **Full**, or
  Custom with the news domains). The default "Trusted" network blocks them.

## People

| Role | Who | Time |
|---|---|---|
| Author: research design, launch dating, final decisions | Anuj | Throughout |
| Second coder for 20% of AI-launch dates | A colleague or research assistant | About half a day |
| Hand-coder for 600 reviews (language accuracy check) | Author or a research assistant who reads Hindi, Marathi and other Indian languages | About a day |

## Time (rough, measured on this project)

| Step | Time |
|---|---|
| Software setup | 30 minutes |
| Full Google Play scrape of 47 apps (default 2-second delay) | about 2 hours; can be stopped and resumed |
| Language labelling of 181,276 reviews | under 1 minute |
| Building the panel | seconds |
| Main estimate | about 15 seconds; 1,000 placebo draws about 5 minutes |
| Power simulation (one setting) | about 4 minutes |
| Dating AI launches from EMIS/ProQuest for 47 apps | several days of library work |

## Money

- Economics Letters submission fee: USD 125.
- Claude plan if you use the cloud tasks.
- Everything else (Python, packages, data) is free.
