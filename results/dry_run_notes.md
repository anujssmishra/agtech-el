# Estimation dry run on simulated data

Task 03, run 2 Oct 2026. Simulated data only. `data/sim/` and `results/sim/` are git-ignored, so the commands
below rebuild them (the panel is deterministic: seed 0).

```
python analysis/simulate_panel.py --out data/sim --effect 0.15
python analysis/estimate.py --panel data/sim/panel_app_lang_month.csv --launch data/sim/launch_dates.csv --out results/sim --placebo 100   # x5
```

The simulated panel has 40 apps, 15 with an AI launch, January 2017 to August 2026 and 35,347 app × language
× month rows. The true effect is +15% (β = log 1.15 = 0.140). Each run of 100 placebo draws took about a
minute on the 4-core cloud machine, so the 1,000 draws for task 06 need ten runs.

## What came out

| Check | Result | Verdict |
|---|---|---|
| Main estimate | β = 0.218 (SE 0.062), +24.4%; 95% CI 0.097 to 0.339 | Covers the true 0.140 |
| Pre-launch quarters | −0.113, +0.048, −0.033 (SE 0.10–0.15); average −0.033 | Near zero |
| Post-launch quarters | +0.195, +0.533, −0.029, +0.167, +0.101; average +0.193 | Positive; single quarters are noisy |
| Randomization inference | p = 0.012 with 500 draws (0.020, 0.015, 0.010, 0.013 after 100–400) | Small and stable |
| Clustered p-value | < 0.001 | Smaller than the RI p-value (see below) |

## Things that look odd, and why

- **The estimate is 0.08 above the truth.** That is 1.3 clustered SEs. Task 02 found that the clustered
  SE understates the true spread of the estimate by a factor of about 1.3–1.5. Measured against the true
  spread, the gap is under one standard deviation: one draw's luck, not bias. Task 02's 1,200 draws had an
  average error of −0.002.
- **All four language measures give identical results.** `simulate_panel.py` copies one count into all
  four columns. They will differ on the real panel.
- **Quarter 1 after launch is 0.533.** That is 0.39 above the truth and 3.2 of its clustered SEs. The
  neighbouring quarters are −0.029 and +0.167. Single quarters rest on a few months of 15 apps, so one
  extreme quarter among eight is not surprising. It also pulls the pooled estimate up a little.
- **The placebo estimates are centred on +0.025, not zero, and spread more than the clustered SE.** Their SD
  is 0.091, against a clustered SE of 0.062 (ratio 1.47). This is the task-02 finding again, and it is why
  the RI p-value (0.012) is larger than the clustered one (< 0.001).

  The off-zero centre is the noise of this one panel. All placebo draws reuse the same data, so they share
  its quirks. In eight panels simulated with no effect at all, the placebo mean ranged from −0.06 to +0.02
  (SD 0.025 across panels). Placing placebo launches only on never-treated apps gave 0.019 (SE 0.014), so
  the shift is not caused by the real launches leaking into the placebos.
- **Observations are 34,233, not 35,347.** `estimate.py` drops 1,114 rows in app × language, app × month
  or language × month groups with no reviews at all. They carry no information in a Poisson model.

## Outputs for the paper (no change to the model)

`estimate.py` now writes these in its `--out` folder on every run:

- **`main_table.csv` and `main_table.tex`**, from the new `analysis/tables.py`:
  - one column per language measure;
  - effect in % with its delta-method SE in brackets;
  - 95% CI in %;
  - clustered and randomization-inference p-values;
  - apps, treated apps, observations and reviews;
  - notes describing all of this.

  The `.tex` file is a booktabs table that also needs `\usepackage{threeparttable}`. It compiles cleanly
  with pdflatex. To rebuild a table without re-estimating: `python analysis/tables.py results`.
- **`event_study.png/.pdf` and `placebo.png/.pdf`**, redrawn for one journal column (90 mm wide, 7–8 pt
  text) in black and grey only.
  - **Event study:** binned end quarters are labelled ≤−4 and ≥4, and the reference quarter has a hollow
    marker.
  - **Placebo:** the histogram's x-axis is symmetric about zero, the estimate is marked and labelled, and
    the RI p-value and number of draws are printed on the figure.
  - Use the PDFs in the manuscript. The PNGs are 600 dpi.

Other code changes:
- `ri_pvalue()` in `estimate.py` now holds the randomization-inference formula, unchanged, so the summary
  and the table share it.
- `plot_event()` no longer takes a title argument; the caption should say which measure is shown.
- New tests are in `tests/test_tables.py`. All 11 tests pass.

## For task 06

Run `estimate.py` as before; the table and figures appear in each results folder, including the robustness
folders.
- The caption is `AI launches and Indian-language reviews` (change it in `tables.to_latex` if needed).
- The randomization-inference row is filled for column (1) only, because the placebos are run for the main
  measure only.
- Report the RI p-value as the main test (see `results/power_summary.md`).
