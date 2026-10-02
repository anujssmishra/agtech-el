#!/usr/bin/env python3
"""
build_panel.py - turn labelled reviews into the app x language x month panel.

    python build_panel.py                       # data/reviews_lang.csv -> data/panel_app_lang_month.csv
    python build_panel.py --start 2017-01 --end 2026-08

Each app gets every month from its first review (or --start, if later) to the last full
month before the scrape (or --end), and every language, with 0 where there were no reviews.
Zeros are real observations in a Poisson regression, so keep them.

Months are Indian Standard Time (UTC+5:30), from the review's last-edit date.

Count columns in panel_app_lang_month.csv (one row per app x language x month):
    n_main        language from detect_language.py; mixed reviews (mostly English words) count as English
    n_mixed_ind   the same, but mixed reviews count as their Indian language
    n_script      Indian-script reviews by language; every review in Latin letters counts as English
    n_play        Google Play's own language tag (the language request that returned the review)
    indian        1 = Indian language, 0 = English, blank = Undetermined / No text (drop before estimating)

app_month.csv has one row per app x month with totals, Indian-language shares under each
measure and the mean star rating.
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
LANGS = ["English", "Hindi", "Marathi", "Gujarati", "Punjabi", "Bengali", "Tamil", "Telugu", "Kannada",
         "Malayalam", "Odia", "Assamese", "Urdu", "Other Indian", "Undetermined", "No text"]
INDIAN = set(LANGS[1:14])
CODE_NAME = {"eng": "English", "hin": "Hindi", "mar": "Marathi", "guj": "Gujarati", "pan": "Punjabi",
             "ben": "Bengali", "tam": "Tamil", "tel": "Telugu", "kan": "Kannada", "mal": "Malayalam",
             "ori": "Odia", "asm": "Assamese", "urd": "Urdu", "oth": "Other Indian", "und": "Undetermined",
             "none": "No text"}
PLAY_NAME = {"en": "English", "hi": "Hindi", "mr": "Marathi", "gu": "Gujarati", "pa": "Punjabi", "bn": "Bengali",
             "ta": "Tamil", "te": "Telugu", "kn": "Kannada", "ml": "Malayalam", "or": "Odia", "as": "Assamese",
             "ur": "Urdu"}
MEASURES = ["n_main", "n_mixed_ind", "n_script", "n_play"]


def play_language(tags):
    tags = [t for t in str(tags).split(";") if t and t != "nan"]
    other = [t for t in tags if t != "en"]
    if not tags:
        return "Undetermined"
    if not other:
        return "English"
    if len(set(other)) == 1:
        return PLAY_NAME.get(other[0], "Other Indian")
    return "Undetermined"


def script_language(row):
    if row["form"] in ("native", "native+latin"):
        return CODE_NAME.get(row["lang"], "Other Indian")
    if row["form"] == "none":
        return "No text"
    if row["script"] == "Latin":
        return "English"
    return "Undetermined"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inp", type=Path, default=HERE / "data" / "reviews_lang.csv")
    ap.add_argument("--packages", type=Path, default=HERE / "packages.csv")
    ap.add_argument("--out", type=Path, default=HERE / "data")
    ap.add_argument("--start", default="2016-01", help="first month to keep (YYYY-MM)")
    ap.add_argument("--end", default="", help="last month to keep (YYYY-MM); default: last full month before the scrape")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    df = pd.read_csv(a.inp, dtype={"reviewId": str, "play_langs": str}, encoding="utf-8-sig",
                     usecols=lambda c: c not in ("content", "replyContent"))
    df = df[df["at_utc"].notna()].copy()
    ist = pd.to_datetime(df["at_utc"], utc=True) + pd.Timedelta(hours=5, minutes=30)
    df["month"] = ist.dt.tz_localize(None).dt.to_period("M")
    if a.end:
        end = pd.Period(a.end, "M")
    else:
        fetched = pd.to_datetime(df["fetched_utc"], utc=True).max() + pd.Timedelta(hours=5, minutes=30)
        end = fetched.tz_localize(None).to_period("M") - 1
    start = pd.Period(a.start, "M")
    df = df[(df["month"] >= start) & (df["month"] <= end)]

    df["n_main"] = df["lang_main"].map(CODE_NAME).fillna("Undetermined")
    df["n_mixed_ind"] = df["lang"].map(CODE_NAME).fillna("Undetermined")
    df["n_script"] = df.apply(script_language, axis=1)
    df["n_play"] = df["play_langs"].map(play_language).where(df["form"] != "none", "No text")

    counts = []
    for m in MEASURES:
        c = df.groupby(["package", "month", m]).size().rename(m)
        c.index = c.index.set_names(["package", "month", "language"])
        counts.append(c)
    counts = pd.concat(counts, axis=1)

    grid = []
    first = df.groupby("package")["month"].min()
    for pkg, f in first.items():
        months = pd.period_range(max(f, start), end, freq="M")
        grid.append(pd.MultiIndex.from_product([[pkg], months, LANGS], names=["package", "month", "language"]))
    if not grid:
        sys.exit("No reviews in the chosen months.")
    idx = grid[0].append(grid[1:]) if len(grid) > 1 else grid[0]
    panel = counts.reindex(idx).fillna(0).astype(int).reset_index()
    panel["indian"] = panel["language"].map(lambda l: 1 if l in INDIAN else (0 if l == "English" else None)).astype("Int64")

    if a.packages.exists():
        pk = pd.read_csv(a.packages, encoding="utf-8-sig")[["package", "platform", "panel_role"]]
        panel = panel.merge(pk, on="package", how="left")
    else:
        panel["platform"], panel["panel_role"] = panel["package"], ""
    panel["platform"] = panel["platform"].fillna(panel["package"])
    panel["panel_role"] = panel["panel_role"].fillna("")
    panel["month"] = panel["month"].astype(str)
    panel["_order"] = panel["language"].map({l: i for i, l in enumerate(LANGS)})
    cols = ["package", "platform", "panel_role", "month", "language", "indian"] + MEASURES
    panel = panel.sort_values(["package", "month", "_order"])[cols]
    panel.to_csv(a.out / "panel_app_lang_month.csv", index=False, encoding="utf-8-sig")

    # app x month summary
    keys = ["package", "platform", "panel_role", "month"]
    am = panel.groupby(keys)["n_main"].sum().rename("n_reviews").to_frame()
    am["n_text"] = panel[panel["language"] != "No text"].groupby(keys)["n_main"].sum()
    is_ind, is_eng = panel["indian"].eq(1).fillna(False), panel["indian"].eq(0).fillna(False)
    for m in MEASURES:
        tag = m[2:]
        ind = panel[is_ind].groupby(keys)[m].sum()
        eng = panel[is_eng].groupby(keys)[m].sum()
        am[f"n_indian_{tag}"], am[f"n_english_{tag}"] = ind, eng
        am[f"share_indian_{tag}"] = (ind / (ind + eng)).round(4)
    am = am.reset_index()
    score = df.assign(month=df["month"].astype(str)).groupby(["package", "month"])["score"].mean().round(3)
    am = am.merge(score.rename("mean_score").reset_index(), on=["package", "month"], how="left")
    am.to_csv(a.out / "app_month.csv", index=False, encoding="utf-8-sig")

    n_apps = panel["package"].nunique()
    print(f"panel_app_lang_month.csv: {len(panel):,} rows = {n_apps} apps x months x {len(LANGS)} languages "
          f"(each app from its first review month, not before {start}, to {end})")
    print(f"app_month.csv: {len(am):,} app-months; reviews in window: {len(df):,}")
    for m in MEASURES:
        ind, eng = int(panel.loc[is_ind, m].sum()), int(panel.loc[is_eng, m].sum())
        print(f"  Indian-language share, {m:12}: {ind / max(1, ind + eng):.3f}  (Indian {ind:,}, English {eng:,})")
    missing = set(pd.read_csv(a.packages, encoding="utf-8-sig")["package"]) - set(first.index) if a.packages.exists() else set()
    if missing:
        print(f"No reviews in the window for {len(missing)} apps: {', '.join(sorted(missing))}")


if __name__ == "__main__":
    main()
