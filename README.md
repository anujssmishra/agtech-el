# AgTech AI and vernacular users: Economics Letters project

Code, small data files and task instructions for the paper. The main question (since 7 October 2026) is whether
Indian agtech apps answer farmers who write in an Indian language less often, more slowly or not in their language
(`docs/analysis_plan_replies.md`); the original question on AI and reviewer composition is now secondary. The to-do list is `TODO.md`. The rules
Claude follows in this repository are in `CLAUDE.md`. Review text never goes to GitHub.

| Folder | Contents |
|---|---|
| `play_reviews/` | Google Play scraper, language labeller, panel builder (see its README) |
| `analysis/` | Reply gaps (`replies.py`, main question); AI and reviewer composition (`estimate.py`); AI mentions (`ai_takeup.py`); simulated data and power analysis |
| `data/` | Launch dates (edit by hand), funding and acquisition events, the sampling frame workbook |
| `docs/project_guide/` | Start here if you are new: the idea, what you need, setup, data, method, status and rules |
| `cloud_tasks/` | One instruction file per Claude Code cloud task |
| `tests/` | Checks for all of the above: `python -m pytest -q` |
| `scripts/cloud_setup.sh` + `.claude/settings.json` | Install packages and the language model in each cloud session (`scripts/claude_settings.json` is a visible copy of the settings file) |

## 1. Put the project on GitHub (once)

You need a GitHub account and a Claude Pro, Max, Team or Enterprise plan.

**With git (recommended: it keeps the hidden `.claude` folder and `.gitignore`)**
1. On github.com, create a new repository named `agtech-el`. Set it to **Private** and add no files.
2. In a terminal inside this folder (replace YOUR-USERNAME):
   ```
   git init -b main
   git add .
   git commit -m "Project setup"
   git remote add origin https://github.com/YOUR-USERNAME/agtech-el.git
   git push -u origin main
   ```

**Without git**
1. Create the repository as above.
2. Click "uploading an existing file" and drag in everything in this folder.
3. Check that `.claude/settings.json` and `.gitignore` arrived. They are hidden files. To show them, press
   Cmd+Shift+. in Finder on a Mac, or tick View → Hidden items on Windows. If `.claude/settings.json` is
   missing, use Add file → Create new file, name it `.claude/settings.json` and paste in the contents of
   `scripts/claude_settings.json`. Even without it, Claude runs the setup itself; CLAUDE.md tells it to.

## 2. Connect Claude Code on the web (once)
1. Go to claude.ai/code and sign in. Choose **Sign in with GitHub** and install the Claude GitHub app with
   access to `agtech-el`.
2. Open the environment selector (the cloud icon above the message box) and edit the Default environment:
   - **Network access:** Trusted (the default) is enough for every task except scraping.
   - **Environment variables:** add `BASH_DEFAULT_TIMEOUT_MS=600000`, so commands may run for up to 10 minutes.
3. Optional, for scraping in the cloud: add a second environment, **agtech-scrape**, with network access
   **Custom**. Keep the default list and add `play.google.com`. Google may still refuse cloud traffic. Your
   PC is the dependable route.

Every session installs the Python packages and the IndicLID model by itself; this takes 1–2 minutes the
first time. If the model download is blocked, add `objects.githubusercontent.com` and
`release-assets.githubusercontent.com` to a Custom network list. The language labels fall back to script
rules without the model.

## 3. Run a task
1. On claude.ai/code, pick the `agtech-el` repository and the environment.
2. Choose **Accept edits** as the permission mode.
3. Type, for example, `Do cloud_tasks/02_power_simulation.md`.
4. When it finishes, review the changes and choose **Create PR**, then merge the pull request on GitHub.

Tasks 02, 03 and 04 are independent and can run at the same time in separate sessions. Order and
prerequisites are in `cloud_tasks/README.md` and `TODO.md`.

## What stays off the cloud
- **Google Play scraping** on the default network. Run it on your PC (`play_reviews/README.md`), or use the
  Custom network above.
- **EMIS, ProQuest, Tracxn and Dataful.** These need campus access. All IIM Lucknow databases may be cited and used as inputs under the author's written permission to publish (CLAUDE.md rule 2).
- **Hand-checking 600 review labels.**

## Getting your data in
After scraping on your PC, upload these four files from your `play_reviews/data/` folder to the same
folder on GitHub (Add file → Upload files):
- `panel_app_lang_month.csv`
- `app_month.csv`
- `apps_metadata.csv`
- `scrape_summary.csv`

They hold counts only, no review text. Edit `data/launch_dates.csv` directly on GitHub (the pencil icon)
as you date launches.
