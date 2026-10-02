# 02 Power: how many dated AI launches are needed?

Goal: tell Anuj, before the real data exist, how large an effect the design can detect with 8, 12, 16 or
20 dated launches.

1. Read CLAUDE.md, `analysis/simulate_panel.py` and `analysis/power_simulation.py`.
2. Run the default grid one treated-count at a time so each command stays under 10 minutes:
   `python analysis/power_simulation.py --treated 8 --reps 50`, then 12, 16 and 20. Draws append.
3. Repeat with fewer reviews per app-month (a pessimistic case):
   `--mean-reviews 20 --tag low`, same four runs.
4. Write `results/power_summary.md`:
   - a table of power by number of treated apps and effect size, for both cases;
   - the false-positive rate at effect 0 (it should be near 5%; if it is well above, say so, because then
     the randomization-inference p-value matters more);
   - the smallest effect detectable with 80% power for each number of treated apps;
   - one paragraph on what this means for how many launches the news coding must find, and on the main
     assumptions in `simulate_panel.py` that drive the result.
5. Commit results/power*.csv, results/power*.png and the summary. Tick task 02 in TODO.md.
