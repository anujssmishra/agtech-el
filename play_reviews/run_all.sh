#!/usr/bin/env bash
# Full pipeline: scrape -> label languages -> build the panel.
# Run from this folder after the one-time setup in README.md. Safe to stop with Ctrl+C and rerun.
set -e
cd "$(dirname "$0")"
if [ -f .venv/bin/activate ]; then source .venv/bin/activate; fi
python scrape_reviews.py
python detect_language.py label
python build_panel.py
