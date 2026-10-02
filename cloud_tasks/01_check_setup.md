# 01 Check the setup

1. Read CLAUDE.md.
2. The session-start hook runs `scripts/cloud_setup.sh`. If there was no "Cloud setup: …" line, run
   `CLAUDE_CODE_REMOTE=true bash scripts/cloud_setup.sh`. Confirm every item says ok; if not, read /tmp/agtech_setup.log and fix the environment (packages, model download). Do not
   change the project code to work around a missing package.
3. Run `python -m pytest -q` and `python play_reviews/detect_language.py demo`.
4. Report: Python version, what passed, anything missing and how you fixed it. If the IndicLID model could
   not be downloaded, say which host was blocked: it can be added to the environment's Custom network list.
5. Tick task 01 in TODO.md with today's date and commit.
