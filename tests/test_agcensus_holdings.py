"""Agriculture Census holdings: size groups, social groups, shares and coverage flags."""
import csv

import pytest

from agcensus_holdings import CLASS_TO_CATEGORY, build

HEAD = ["year", "state_name", "state_code", "district_name", "district_code", "social_group", "farm_size_class",
        "farm_size_category", "hol_no", "hol_ar"]


def write(path, rows, district=True):
    cols = HEAD if district else [c for c in HEAD if not c.startswith("district")]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])


def row(year, state, social, cls, n, a, district="D1"):
    return {"year": year, "state_name": state, "state_code": "9", "district_name": district, "district_code": "1",
            "social_group": social, "farm_size_class": cls, "farm_size_category": CLASS_TO_CATEGORY[cls],
            "hol_no": n, "hol_ar": a}


def test_build(tmp_path):
    st = [row("2015-16", "A", "Others", "< 0.5", 60, 15), row("2015-16", "A", "Scheduled Tribes", "0.5-1.0", 10, 7),
          row("2015-16", "A", "Others", "1.0-2.0", 20, 28), row("2015-16", "A", "Institutional", "> 20.0", 10, 400),
          row("2015-16", "B", "Others", "2.0-3.0", 5, 12), row("2010-11", "A", "Scheduled Tribe", "< 0.5", 50, 12)]
    di = [row("2015-16", "A", "Others", "< 0.5", 60, 15), row("2015-16", "A", "Others", "1.0-2.0", 20, 28)]
    write(tmp_path / "s.csv", st, district=False)
    write(tmp_path / "d.csv", di)
    states, districts = build(tmp_path / "s.csv", tmp_path / "d.csv", tmp_path / "out")
    a = next(r for r in states if r["year"] == "2015-16" and r["state_name"] == "A")
    assert (a["holdings_total"], a["marginal"], a["small"], a["large"], a["small_and_marginal"]) == (100, 70, 20, 10, 90)
    assert a["pct_small_and_marginal"] == 90.0 and a["institutional_holdings"] == 10
    assert a["avg_holding_ha"] == pytest.approx(4.5) and a["pct_area_small_and_marginal"] == pytest.approx(11.11)
    assert a["year_complete"] == 1
    assert next(r for r in states if r["year"] == "2010-11")["year_complete"] == 0      # only 1 of 2 states
    assert districts[0]["state_coverage_pct"] == 80.0                                   # 80 of A's 100 holdings
    long = list(csv.DictReader(open(tmp_path / "out" / "agcensus_holdings_long.csv")))
    assert {r["social_group"] for r in long} == {"Others", "Scheduled Tribes", "Institutional"}


def test_rejects_mislabelled_size_class(tmp_path):
    bad = row("2015-16", "A", "Others", "1.0-2.0", 1, 1)
    bad["farm_size_category"] = "Marginal"
    write(tmp_path / "s.csv", [bad], district=False)
    write(tmp_path / "d.csv", [bad])
    with pytest.raises(ValueError):
        build(tmp_path / "s.csv", tmp_path / "d.csv", tmp_path / "out")
