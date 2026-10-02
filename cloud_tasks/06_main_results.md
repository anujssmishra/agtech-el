# 06 Main results on the real data

Needs: `play_reviews/data/panel_app_lang_month.csv`, and `data/launch_dates.csv` with launch months and
include = 1 for the apps in the estimation sample.

1. Read CLAUDE.md and `results/dry_run_notes.md` if present.
2. Describe the sample first (`results/descriptives.md`): apps, months, reviews, Indian-language share
   by app type and over time, and which apps have launch dates.
3. Main estimates, all four language measures, with placebos (repeat until 1,000 draws):
   `python analysis/estimate.py --placebo 100`
4. Robustness, each into its own results subfolder:
   - `--exclude-overlap 3` (no funding round or acquisition within 3 months of launch);
   - input and advisory apps only (filter by the category in the sampling frame; add an option to
     estimate.py if needed);
   - drop each treated app in turn (leave-one-out) and report the range of estimates.
5. Make the paper table (LaTeX) and figures with the code from task 03.
6. Write `results/results_summary.md`: the main effect in %, its uncertainty, pre-trends, robustness, and
   threats (concurrent events, label error, survivorship). Plain language, no overstatement.
7. Commit and tick task 06 in TODO.md.
