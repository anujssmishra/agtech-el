# Cloud tasks

Each file is a complete instruction for one Claude Code session on the web. Start a session on this
repository and type, for example:

    Do cloud_tasks/02_power_simulation.md

Claude reads CLAUDE.md first (it holds the project rules). It works on a new branch, and you review the
changes and merge them on GitHub.

| Task | Needs | Network |
|---|---|---|
| 01_check_setup | nothing | Trusted (default) |
| 02_power_simulation | nothing | Trusted |
| 03_estimation_dry_run | nothing | Trusted |
| 04_firm_event_gaps | web search in the session | Trusted; Full if pages won't load |
| 05_scrape_in_cloud (optional) | nothing | Custom + play.google.com |
| 06_main_results | panel files + launch dates | Trusted |
| 07_draft_manuscript | results from 06 | Trusted |
| 08_replication_package | 06 and 07 done | Trusted |
