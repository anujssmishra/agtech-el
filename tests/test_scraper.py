"""Scraper logic against a fake Google Play backend (no network needed)."""
import datetime as dt
import json
import sys

import pytest

pytest.importorskip("google_play_scraper")
import google_play_scraper  # noqa: E402
from google_play_scraper.features import reviews as R  # noqa: E402

import scrape_reviews as S  # noqa: E402

BASE = dt.datetime(2026, 9, 30, tzinfo=dt.timezone.utc)


def items(n, prefix, step_days=1.5):
    out = []
    for i in range(n):
        ts = int((BASE - dt.timedelta(days=i * step_days)).timestamp())
        out.append([f"{prefix}{i}", ["user", None], 5, None, f"text {i}", [ts, 0], 0, None, None, None, "1.0"])
    return out


@pytest.fixture
def fake_play(monkeypatch):
    data = {("app.a", "en"): items(900, "E"), ("app.a", "hi"): items(120, "H", 10)}
    data[("app.a", "mr")] = data[("app.a", "en")]          # a language Google does not filter
    state = {"calls": 0, "interrupt_at": None}

    def fetch(url, app_id, sort, count, f1, f2, token):
        state["calls"] += 1
        if state["interrupt_at"] == state["calls"]:
            raise KeyboardInterrupt
        lang = url.split("hl=")[1].split("&")[0]
        if lang == "or":  # Google sends no review list for a language with no reviews; the library then fails
            raise TypeError("object of type 'NoneType' has no len()")
        it = data.get((app_id, lang), [])
        s = int(token or 0)
        return it[s:s + count], (str(s + count) if s + count < len(it) else None)

    monkeypatch.setattr(R, "_fetch_review_items", fetch)
    monkeypatch.setattr(google_play_scraper, "app", lambda pkg, lang="en", country="us": {"title": pkg})
    monkeypatch.setattr(S.time, "sleep", lambda s: None)
    return data, state


def run(tmp_path, *extra):
    pk = tmp_path / "pk.csv"
    pk.write_text("package,platform,scrape\napp.a,App A,1\n")
    sys.argv = ["x", "--packages", str(pk), "--out", str(tmp_path / "out"), "--langs", "en,hi,mr",
                "--page-size", "200", "--delay", "0", *extra]
    S.main()
    return tmp_path / "out"


def test_resume_filter_and_refresh(tmp_path, fake_play):
    data, state = fake_play
    state["interrupt_at"] = 3                       # stop part-way through English
    out = run(tmp_path)
    st = json.loads((out / "raw/app.a/en.state.json").read_text())
    assert st["status"] == "running" and st["token"]
    state["interrupt_at"] = None
    out = run(tmp_path)                             # resume
    summary = {r.split(",")[1]: r for r in (out / "scrape_summary.csv").read_text(encoding="utf-8-sig").splitlines()[1:]}
    assert "complete" in summary["en"] and ",900," in summary["en"]
    assert "not_filtered" in summary["mr"]
    raw = (out / "reviews_raw.csv").read_text(encoding="utf-8-sig").splitlines()
    assert len(raw) == 1 + 900 + 120                 # no duplicates across languages
    data[("app.a", "en")] = items(3, "N", -1) + data[("app.a", "en")]
    calls = state["calls"]
    run(tmp_path, "--refresh", "--skip-metadata", "--langs", "en")
    assert state["calls"] - calls <= 2               # refresh only reads the newest pages


def test_since_cutoff(tmp_path, fake_play):
    out = run(tmp_path, "--since", "2025-01-01", "--skip-metadata")
    st = json.loads((out / "raw/app.a/en.state.json").read_text())
    assert st["status"] == "since_reached"
    assert st["n_saved"] < 900


def test_language_without_reviews_and_cap(tmp_path, fake_play):
    out = run(tmp_path, "--langs", "en,or", "--max-per-bucket", "50", "--skip-metadata")
    st = json.loads((out / "raw/app.a/or.state.json").read_text())
    assert st["status"] == "complete" and st["n_saved"] == 0 and "no reviews" in st["note"]
    en = json.loads((out / "raw/app.a/en.state.json").read_text())
    assert en["status"] == "capped" and en["n_saved"] == 50          # the cap also limits the page size
