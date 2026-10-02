@echo off
REM Full pipeline: scrape -> label languages -> build the panel.
REM Run from this folder after the one-time setup in README.md. Safe to stop with Ctrl+C and rerun.
cd /d "%~dp0"
if exist .venv\Scripts\activate.bat call .venv\Scripts\activate.bat
python scrape_reviews.py || goto :end
python detect_language.py label || goto :end
python build_panel.py
:end
pause
