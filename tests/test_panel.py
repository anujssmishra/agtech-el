"""Label a small synthetic review file and build the panel."""
import csv
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest

pytest.importorskip("wordfreq")
PR = Path(__file__).resolve().parents[1] / "play_reviews"


def test_label_and_panel(tmp_path):
    texts = ["Very good app", "bahut accha app hai", "खूप छान", "👍"]
    rows = []
    for i in range(80):
        rows.append({"package": "app.a" if i % 2 else "app.b", "reviewId": f"r{i}",
                     "at_utc": f"2026-0{1 + i % 6}-15T10:00:00+00:00", "score": 4, "thumbsUpCount": 0,
                     "appVersion": "1", "content": texts[i % 4], "replyContent": "", "repliedAt_utc": "",
                     "play_langs": "mr" if i % 4 == 2 else "en", "n_buckets": 1,
                     "fetched_utc": "2026-08-02T00:00:00+00:00"})
    raw = tmp_path / "reviews_raw.csv"
    with open(raw, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    lab = tmp_path / "reviews_lang.csv"
    subprocess.run([sys.executable, PR / "detect_language.py", "label", "--in", raw, "--out", lab,
                    "--models", tmp_path / "none"], check=True)
    subprocess.run([sys.executable, PR / "build_panel.py", "--in", lab, "--packages", PR / "packages.csv",
                    "--out", tmp_path], check=True)
    p = pd.read_csv(tmp_path / "panel_app_lang_month.csv")
    assert p["n_main"].sum() == 80
    assert set(p["month"]) == {f"2026-0{m}" for m in range(1, 8)}       # last full month = July
    assert (p.groupby(["package", "month"]).size() == 16).all()          # every language, zeros included
    by = p.groupby("language")["n_main"].sum()
    assert by["English"] == 20 and by["Hindi"] == 20 and by["Marathi"] == 20 and by["No text"] == 20
