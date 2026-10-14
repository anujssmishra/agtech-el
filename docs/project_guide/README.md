# AgTech AI and vernacular users: project guide

**Start here.** This folder (`docs/project_guide/` in the repository) explains the whole project to someone who has never seen it: the research idea,
what you need to get going, how to set everything up, where the data come from, how the analysis works,
what has been done so far and what remains. It was written on **6 October 2026**; check the repository for
anything newer.

## The project in one paragraph

Indian agtech companies (AgroStar, BigHaat, Krishify, ITC's ITCMAARS, government apps such as PM-KISAN and
others) have been adding AI features to their farmer apps: crop-disease photo diagnosis, chatbots,
voice assistants. Many of these features work in Indian languages. **Do they change who uses the apps,
shifting the user base toward farmers who write in Indian languages rather than English?** The project
answers this with Google Play reviews: it counts each app's reviews by language and month, dates each app's
AI launch from news coverage, and asks whether Indian-language reviews rose relative to English ones after
the launch (a Poisson regression with fixed effects, inference by randomization). The target is a short paper
in *Economics Letters* (at most 2,000 words). Author: Anuj (IIM Lucknow).

## Where things stand (6 Oct 2026)

- Data collected: 181,276 Google Play reviews from 46 apps (Jan 2016 to Sep 2026), labelled by language and
  turned into an app × language × month panel.
- Main result: **no detectable effect.** The main estimate is −12.3% with a randomization-inference p-value of
  0.60; the data cannot rule out effects between about −45% and +39%.
- Next: decide the paper's framing, finish the hand check of 600 language labels, then draft the manuscript.

## Files in this guide (read in this order)

| File | What it covers |
|---|---|
| `01_what_you_need.md` | Checklist: accounts, software, access, people, time and money needed to start |
| `02_research_idea.md` | The question, why it matters, the mechanism, what the paper can claim |
| `03_data.md` | Every data source: the app list, Google Play reviews, language labels, launch dates, firm events |
| `04_method.md` | The estimating equation, inference, event study, placebos, robustness, power |
| `05_getting_started.md` | Step-by-step setup on a Mac or PC and in Claude Code on the web, with every command |
| `06_repository_map.md` | What each folder and file in the GitHub repository does |
| `07_status_results_next_steps.md` | What has been done, the results, the decisions taken, and the to-do list |
| `08_rules_and_lessons.md` | Project rules (privacy, sources) and lessons learned the hard way |
| `09_glossary.md` | Terms and abbreviations |
| The repository itself | The files this guide refers to: `CLAUDE.md`, `TODO.md`, `results/`, `data/`, `cloud_tasks/` |

## Where the project lives

- **Code and aggregate data:** private GitHub repository `anujssmishra/agtech-el`
  (https://github.com/anujssmishra/agtech-el). Ask the owner for access.
- **Raw review text:** never on GitHub (privacy and Google's terms). The owner keeps a copy on his own
  computer; anyone else re-collects it with the scraper (see `05_getting_started.md`).
- **Sampling frame workbook:** `data/sampling_frame/Indian_AgTech_Sampling_Frame.xlsx` in the repository.
