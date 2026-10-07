# 04 Fill gaps in the funding and acquisition list

`data/firm_events.csv` lists dated funding rounds and acquisitions, each with a public source. Coverage
gaps:
- BharatAgri: the date of the Arkam-led $4.3M Series A (Inc42 says 2023) and whether it is the same money as
  the Feb 2023 INR 14 crore extension led by Capria; when Kisanwala Technologies took over the app.
- KisanKraft: any outside funding (probably none).
- Gramophone: rounds before Oct 2021 (Siana Capital, Info Edge, Asha Impact), and when Info Edge's stake
  passed 50%.
- Animall: any acquisitions.

1. Read CLAUDE.md (rule 2: public news or press releases; Tracxn and DATAFUL allowed under the author's written permission since 7 Oct 2026; never Crunchbase, PitchBook or CB Insights).
2. If this session has no web search or fetch, stop and say so.
3. For each gap, find the first public report. Add rows with the same columns as the existing file:
   package, app, company, event, first_reported (YYYY-MM-DD), event_month (YYYY-MM), event_month_basis,
   round, amount, unit (as reported, no conversion), counterparty_or_investors, source_title, source_url,
   note. Leave the spot_check column blank.
4. Never guess a date or amount. Where sources disagree, add a note.
5. Commit, list the rows added in the summary, and tick task 04 in TODO.md.
