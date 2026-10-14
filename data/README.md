# data/

| File | What it is | Who edits it |
|---|---|---|
| `launch_dates.csv` | One row per app (see below) | You, by hand or on GitHub |
| `firm_events.csv` | 100 dated funding rounds, acquisitions, layoffs and shutdowns for 20 startups, each with a public news or press-release source (from the sampling frame's "Firm events" sheet, 1 Oct 2026) | Task 04 adds rows |
| `launch_leads.csv` | Leads for the Launch log, one row per app checked (5 Oct 2026): the AI feature, the earliest dated public report found, a second source where found, whether the page was opened, and what it implies for `launch_dates.csv`. Leads only: confirm in EMIS/ProQuest before coding a launch | You (confirm and copy into the Launch log) |
| `external/agcensus_holdings_state.csv` | Marginal, small and larger farm holdings (number and area) by state, Agriculture Census 2015-16 (complete) and 2010-11 (25 states only); see below | Rebuilt by `analysis/agcensus_holdings.py` |
| `external/agcensus_holdings_district.csv` | The same by district (2015-16: 613 districts; some districts missing, see `state_coverage_pct`) | Rebuilt by `analysis/agcensus_holdings.py` |
| `external/agcensus_holdings_long.csv` | State and district holdings by social group (SC, ST, others, institutional) and size group | Rebuilt by `analysis/agcensus_holdings.py` |
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

## `external/`: farm holdings by size (Agriculture Census)

**What the files give**
- The number and area of operational holdings in each size group:
  - marginal, under 1 ha;
  - small, 1–2 ha;
  - semi-medium, 2–4 ha;
  - medium, 4–10 ha;
  - large, 10 ha and over.
- The number of operational holdings is the standard count of farmers.
- Institutional holdings (government farms, trusts and similar) are reported separately, so they can be left
  out.

**Source.** India Data Portal, "Agricultural Census Non Crop", state and district files
(<https://ckandev.indiadataportal.com/dataset/agricultural-census-non-crop>), downloaded 14 October 2026.
Open Data Commons Attribution Licence. The original source is the Agriculture Census of the Ministry of
Agriculture and Farmers Welfare; cite both.

**Checks**
- **2015-16, state level: complete.** The files reproduce the official national figures exactly: 146.45
  million holdings, of which 100.25 million are marginal (68.45%) and 25.81 million small (17.62%); 157.82
  million ha; average 1.08 ha.
- **2010-11, state level: 25 states only.** Uttar Pradesh, Madhya Pradesh, Rajasthan, Karnataka, Tamil Nadu,
  Andhra Pradesh and smaller states are missing. The states present match the published figures.
  - "Telangana" in 2010-11 is the Telangana part of undivided Andhra Pradesh; the rest of Andhra Pradesh is
    missing.
  - `year_complete` = 0 marks this year.
- **District level: incomplete.**
  - 2015-16 has 613 districts. Only 12 of 33 states are fully covered: Odisha 74%, Andhra Pradesh 81%,
    Telangana 82%, Bihar 83%, Gujarat 86% and others less than complete. Sikkim and Lakshadweep are absent.
  - `state_coverage_pct` gives, for each state, the share of the state's holdings that its listed districts
    cover.
  - The portal's sub-district file has more districts but misses many sub-districts (112 of 146 million
    holdings), so it is not used.
- **Where to get complete district tables:** the official Agriculture Census site (agcensus.da.gov.in). It
  refuses connections from the cloud machine, so open it from a computer in India. DATAFUL also has state-wise
  holdings tables.
- **Newer data:** the 11th Agriculture Census (2021-22) finished fieldwork, but its results were not
  published as of 14 October 2026.

**To rebuild:** download the two portal files and run:

```
python analysis/agcensus_holdings.py --state state-level-agcensus-non-crop.csv --district district-level-agcensus-non-crop.csv
```

