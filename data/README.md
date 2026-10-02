# data/

| File | What it is | Who edits it |
|---|---|---|
| `launch_dates.csv` | One row per app (see below) | You, by hand or on GitHub |
| `firm_events.csv` | 100 dated funding rounds, acquisitions, layoffs and shutdowns for 20 startups, each with a public news or press-release source (from the sampling frame's "Firm events" sheet, 1 Oct 2026) | Task 04 adds rows |
| `sampling_frame/Indian_AgTech_Sampling_Frame.xlsx` | The full sampling frame: platforms, exclusions, open checks, Launch log, firm events and overlap check | You |

`launch_dates.csv` columns:
- `ai_launch_month`: YYYY-MM; blank if the app has no dated AI launch.
- `include`: 1 or 0, whether the app is in the estimation sample.
- `panel_end`: optional; the last month to use for that app.

It is pre-filled from the sampling frame:
- **8 dated launches** (include = 1). Confirm each one against the Launch log.
- **8 comparison apps** (include = 1).
- **Everything else** has include = 0 until resolved: "date needed", "check first", and "AI from launch",
  which stays out of the main estimate.
- **Panel end months:**
  - BharatAgri ends Oct 2025, when the company shut.
  - AgriCentral ends Jan 2025, when it changed owner.
  - Gramophone ends Jun 2023, after which the app was no longer updated.

The review panel itself goes in `play_reviews/data/`. Only the four aggregate files listed in `.gitignore`
are committed.
