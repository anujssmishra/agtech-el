#!/usr/bin/env bash
# Runs at the start of every Claude Code cloud session (hooked in .claude/settings.json).
# Installs the Python packages and IndicLID's native-script model. Does nothing on your own computer.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0
LOG=/tmp/agtech_setup.log
pipi() { python3 -m pip install -q "$@" >>"$LOG" 2>&1 || python3 -m pip install -q --break-system-packages "$@" >>"$LOG" 2>&1; }
python3 -c "import google_play_scraper, pandas, wordfreq, pyfixest, matplotlib, pytest" 2>/dev/null \
  || pipi "google-play-scraper==1.2.7" pandas wordfreq pyfixest matplotlib pytest
python3 -c "import fasttext" 2>/dev/null || pipi fasttext-wheel || true
MODEL=play_reviews/models/indiclid-ftn/model_baseline_roman.bin
[ -f "$MODEL" ] || python3 play_reviews/detect_language.py download-models >>"$LOG" 2>&1 || true
has() { python3 -c "import $1" 2>/dev/null && echo ok || echo MISSING; }
echo "Cloud setup: pyfixest $(has pyfixest), wordfreq $(has wordfreq), google_play_scraper $(has google_play_scraper), fasttext $(has fasttext), IndicLID model $([ -f "$MODEL" ] && echo ok || echo MISSING). Log: $LOG"
exit 0
