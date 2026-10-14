#!/usr/bin/env python3
"""
agcensus_holdings.py - marginal and small farmers by state and district, from the Agriculture Census.

    python analysis/agcensus_holdings.py --state STATE.csv --district DISTRICT.csv --out data/external

Inputs are the India Data Portal files "State level AgCensus Non Crop" and "District level AgCensus Non Crop"
(<https://ckandev.indiadataportal.com/dataset/agricultural-census-non-crop>, Open Data Commons Attribution
Licence; original source: Agriculture Census, Ministry of Agriculture and Farmers Welfare). Only the standard
library is used, so it runs under `python -I`.

Size groups (operational holding): marginal < 1 ha, small 1-2 ha, semi-medium 2-4 ha, medium 4-10 ha,
large >= 10 ha. The number of operational holdings is the usual count of farmers; institutional holdings are
counted separately so they can be left out.

Outputs:
    agcensus_holdings_state.csv      one row per state and census year
    agcensus_holdings_district.csv   one row per district and census year, with the share of the state's
                                     holdings that the portal's district file covers
    agcensus_holdings_long.csv       state and district counts by social group and size group
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

CATEGORIES = ["Marginal", "Small", "Semi-Medium", "Medium", "Large"]
CLASS_TO_CATEGORY = {"< 0.5": "Marginal", "0.5-1.0": "Marginal", "1.0-2.0": "Small", "2.0-3.0": "Semi-Medium",
                     "3.0-4.0": "Semi-Medium", "4.0-5.0": "Medium", "5.0-7.5": "Medium", "7.5-10.0": "Medium",
                     "10.0-20.0": "Large", "> 20.0": "Large"}
SOCIAL = {"Scheduled Tribe": "Scheduled Tribes", "Scheduled Tribes": "Scheduled Tribes",
          "Scheduled Caste": "Scheduled Castes", "Others": "Others", "Institutional": "Institutional"}
COLS = {"Marginal": "marginal", "Small": "small", "Semi-Medium": "semi_medium", "Medium": "medium", "Large": "large"}


def num(x):
    return float(x) if x not in ("", None) else 0.0


def read(path, level):
    """Counts by (year, state, district, social group, size group): holdings and area (ha)."""
    out = defaultdict(lambda: [0.0, 0.0])
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            cat = CLASS_TO_CATEGORY[r["farm_size_class"].strip()]
            if r["farm_size_category"].strip() != cat:
                raise ValueError(f"size class {r['farm_size_class']} labelled {r['farm_size_category']}")
            key = (r["year"].strip(), r["state_name"].strip(), r["state_code"].strip(),
                   r["district_name"].strip() if level == "district" else "",
                   r["district_code"].strip() if level == "district" else "",
                   SOCIAL[r["social_group"].strip()], cat)
            out[key][0] += num(r["hol_no"])
            out[key][1] += num(r["hol_ar"])
    return out


def summarise(counts):
    """One row per (year, state, district): counts, shares and area by size group."""
    rows = defaultdict(lambda: defaultdict(float))
    for (year, st, stc, d, dc, social, cat), (n, a) in counts.items():
        r = rows[(year, st, stc, d, dc)]
        r[COLS[cat]] += n
        r[f"area_{COLS[cat]}_ha"] += a
        r["holdings_total"] += n
        r["area_total_ha"] += a
        if social == "Institutional":
            r["institutional_holdings"] += n
    out = []
    for (year, st, stc, d, dc), r in sorted(rows.items()):
        sm, sma = r["marginal"] + r["small"], r["area_marginal_ha"] + r["area_small_ha"]
        tot, area = r["holdings_total"], r["area_total_ha"]
        out.append({"year": year, "state_name": st, "state_code": stc, "district_name": d, "district_code": dc,
                    "holdings_total": round(tot), **{c: round(r[c]) for c in COLS.values()},
                    "small_and_marginal": round(sm),
                    "pct_marginal": round(100 * r["marginal"] / tot, 2) if tot else "",
                    "pct_small": round(100 * r["small"] / tot, 2) if tot else "",
                    "pct_small_and_marginal": round(100 * sm / tot, 2) if tot else "",
                    "area_total_ha": round(area, 2),
                    "area_marginal_ha": round(r["area_marginal_ha"], 2), "area_small_ha": round(r["area_small_ha"], 2),
                    "pct_area_small_and_marginal": round(100 * sma / area, 2) if area else "",
                    "avg_holding_ha": round(area / tot, 3) if tot else "",
                    "institutional_holdings": round(r["institutional_holdings"])})
    return out


def write(rows, path, drop=()):
    cols = [c for c in rows[0] if c not in drop]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def build(state_csv, district_csv, out):
    out.mkdir(parents=True, exist_ok=True)
    sc, dc = read(state_csv, "state"), read(district_csv, "district")
    states, districts = summarise(sc), summarise(dc)

    # how complete is each census year in the state file, and each state in the district file
    n_states = defaultdict(set)
    for r in states:
        n_states[r["year"]].add(r["state_name"].lower())
    full = max(len(s) for s in n_states.values())
    for r in states:
        r["year_complete"] = int(len(n_states[r["year"]]) == full)
    state_total = {(r["year"], r["state_name"].lower()): r["holdings_total"] for r in states}
    dist_sum = defaultdict(float)
    for r in districts:
        dist_sum[(r["year"], r["state_name"].lower())] += r["holdings_total"]
    for r in districts:
        k = (r["year"], r["state_name"].lower())
        r["state_coverage_pct"] = round(100 * dist_sum[k] / state_total[k], 1) if state_total.get(k) else ""

    write(states, out / "agcensus_holdings_state.csv", drop=("district_name", "district_code"))
    write(districts, out / "agcensus_holdings_district.csv")
    long_rows = [{"level": lvl, "year": y, "state_name": st, "state_code": stc, "district_name": d,
                  "district_code": dcode, "social_group": soc, "size_group": cat, "holdings": round(n),
                  "area_ha": round(a, 2)}
                 for lvl, counts in (("state", sc), ("district", dc))
                 for (y, st, stc, d, dcode, soc, cat), (n, a) in sorted(counts.items())]
    write(long_rows, out / "agcensus_holdings_long.csv")
    return states, districts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--district", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "data" / "external")
    a = ap.parse_args()
    states, districts = build(a.state, a.district, a.out)
    for y in sorted({r["year"] for r in states}):
        s = [r for r in states if r["year"] == y]
        tot = sum(r["holdings_total"] for r in s)
        print(f"{y}: {len(s)} states, {tot / 1e6:.2f} M holdings; marginal "
              f"{sum(r['marginal'] for r in s) / 1e6:.2f} M, small {sum(r['small'] for r in s) / 1e6:.2f} M; "
              f"{len([r for r in districts if r['year'] == y])} districts in the district file")


if __name__ == "__main__":
    main()
