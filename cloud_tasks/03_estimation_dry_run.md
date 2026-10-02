# 03 Estimation dry run on simulated data

Goal: make sure the whole analysis works and produces paper-ready output before the real panel arrives.

1. Read CLAUDE.md and `analysis/estimate.py`.
2. `python analysis/simulate_panel.py --out data/sim --effect 0.15`
3. `python analysis/estimate.py --panel data/sim/panel_app_lang_month.csv --launch data/sim/launch_dates.csv --out results/sim --placebo 100`
   (run `--placebo 100` again until there are 500 draws).
4. Check: the estimate is close to log(1.15) = 0.14; pre-launch event-study quarters average near zero;
   the randomization-inference p-value is small. Explain anything odd.
5. Improve the outputs for the paper without changing the model:
   - a regression table as CSV and as LaTeX (`results/sim/main_table.tex`, booktabs style; effect in %,
     standard errors in brackets, apps, treated apps, observations);
   - the event-study and placebo figures, readable in black and white at single-column width.
   Put any new table code in `analysis/` so task 06 can reuse it on the real data.
6. Run the tests, commit (data/sim and results/sim are git-ignored; commit only code and a short
   `results/dry_run_notes.md`). Tick task 03 in TODO.md.
