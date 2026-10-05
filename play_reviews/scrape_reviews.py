#!/usr/bin/env python3
"""
scrape_reviews.py - download Google Play reviews for the apps listed in packages.csv.

Run this on your own computer: Google Play cannot be reached from Claude's workspace.

Typical use (from this folder):
    python scrape_reviews.py --only com.ulink.agrostar --max-per-bucket 300   # 2-minute test
    python scrape_reviews.py                                                 # full run, resumable
    python scrape_reviews.py --combine-only                                  # rebuild reviews_raw.csv

Why one request per language: Google Play returns only the reviews tagged with the
requested language (hl=...). To get all reviews of an app, the script asks for each
language in --langs and merges the results by review ID.

What is saved (in --out, default ./data):
    raw/<package>/<lang>.jsonl        reviews as downloaded, one per line
    raw/<package>/<lang>.state.json   progress, so an interrupted run carries on where it stopped
    apps_metadata.csv                 installs, rating, release date etc. at scrape time
    apps_metadata_<date>.csv          the same, kept per run (snapshots)
    reviews_raw.csv                   one row per review, with the language buckets it came from
    scrape_summary.csv                reviews, date range and status for each app x language

Reviewer names and profile pictures are never stored. Review dates are the date of the
review's last edit, which is the only date Google Play shows.
"""
import argparse
import csv
import datetime as dt
import inspect
import json
import logging
import random
import ssl
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
UTC = dt.timezone.utc
# English first: later buckets are compared against it to spot languages Google does not filter
DEFAULT_LANGS = ["en", "hi", "mr", "gu", "pa", "bn", "ta", "te", "kn", "ml", "or", "as", "ur"]
DONE = {"complete", "since_reached", "not_filtered"}

log = logging.getLogger("scrape")


class BucketError(Exception):
    """Raised when a request keeps failing after all retries."""


class NoReviewList(Exception):
    """Google answered with no review list at all. It does this for a language with no reviews (and, rarely,
    as a one-off glitch); google-play-scraper 1.2.7 then fails with a TypeError about NoneType."""


# --------------------------------------------------------------------------- library
def import_library(insecure_tls):
    try:
        import google_play_scraper as gps
        from google_play_scraper import Sort
        from google_play_scraper.features import reviews as gps_reviews
        from google_play_scraper.constants.request import Formats
        from google_play_scraper.constants.element import ElementSpecs
        from google_play_scraper.exceptions import NotFoundError
    except ImportError:
        sys.exit("google-play-scraper is not installed. Run:  pip install -r requirements.txt")
    if not hasattr(gps_reviews, "_fetch_review_items"):
        sys.exit("This google-play-scraper version is not supported. Run:  pip install google-play-scraper==1.2.7")
    if not insecure_tls:
        # google-play-scraper switches off HTTPS certificate checks for the whole process when
        # it is imported; switch them back on. Use --insecure-tls only if your network breaks this.
        ssl._create_default_https_context = ssl.create_default_context
    return gps, Sort, gps_reviews, Formats, ElementSpecs, NotFoundError


# --------------------------------------------------------------------------- helpers
def now_utc():
    return dt.datetime.now(UTC)


def iso_from_ts(ts):
    if ts is None:
        return None
    try:
        return dt.datetime.fromtimestamp(int(ts), UTC).isoformat()
    except (TypeError, ValueError, OverflowError, OSError):
        return None


def parse_iso(s):
    return dt.datetime.fromisoformat(s) if s else None


def nested(item, path):
    try:
        for p in path:
            item = item[p]
        return item
    except (IndexError, KeyError, TypeError):
        return None


def polite_sleep(seconds):
    time.sleep(max(0.0, seconds * random.uniform(0.6, 1.4)))


def with_retries(fn, *args, attempts=6, base_wait=15, what="request", not_found=None, **kwargs):
    for k in range(attempts):
        try:
            return fn(*args, **kwargs)
        except (KeyboardInterrupt, TypeError, AttributeError, NameError):
            raise  # Ctrl+C, or a bug / library change: retrying will not help
        except Exception as e:  # network errors, rate limits, unexpected responses
            if not_found is not None and isinstance(e, not_found):
                raise
            if k == attempts - 1:
                raise BucketError(f"{what} failed after {attempts} attempts: {e!r}")
            wait = min(base_wait * 2 ** k, 600) * random.uniform(0.8, 1.2)
            log.warning("%s failed (%s). Waiting %.0f s, then retrying (%d/%d).",
                        what, type(e).__name__, wait, k + 1, attempts - 1)
            time.sleep(wait)


def read_packages(path, only):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    apps = []
    for r in rows:
        pkg = (r.get("package") or "").strip()
        if not pkg:
            continue
        if only:
            if pkg in only:
                apps.append(r)
        elif str(r.get("scrape", "1")).strip() not in ("0", "no", "No", "FALSE", "false"):
            apps.append(r)
    if only:
        missing = set(only) - {a["package"].strip() for a in apps}
        for m in sorted(missing):  # allow packages that are not in the CSV
            apps.append({"package": m, "platform": m})
    return apps


# --------------------------------------------------------------------------- state
def state_path(out, pkg, lang):
    return out / "raw" / pkg / f"{lang}.state.json"


def jsonl_path(out, pkg, lang):
    return out / "raw" / pkg / f"{lang}.jsonl"


def load_state(p):
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def save_state(p, state):
    state["updated_utc"] = now_utc().isoformat()
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1), encoding="utf-8")
    tmp.replace(p)


def load_ids(p):
    ids = set()
    if p.exists():
        with open(p, encoding="utf-8") as f:
            for line in f:
                try:
                    ids.add(json.loads(line)["reviewId"])
                except (json.JSONDecodeError, KeyError):
                    continue  # a half-written last line after a crash
    return ids


# --------------------------------------------------------------------------- scraping
class Scraper:
    def __init__(self, args):
        self.args = args
        (self.gps, self.Sort, self.rev, self.Formats,
         self.Specs, self.NotFoundError) = import_library(args.insecure_tls)
        # 1.2.x takes 7 arguments (with a device filter); older releases take 6
        self.n_args = len(inspect.signature(self.rev._fetch_review_items).parameters)
        spec = self.Specs.Review
        self.paths = {k: spec[k].data_map for k in
                      ("reviewId", "content", "score", "thumbsUpCount", "appVersion", "replyContent")}
        self.path_at = spec["at"].data_map
        self.path_replied = spec["repliedAt"].data_map

    # one request = one page of up to --page-size reviews, newest first
    def fetch_page(self, pkg, lang, token):
        url = self.Formats.Reviews.build(lang=lang, country=self.args.country)
        sort = self.Sort.NEWEST.value
        try:
            if self.n_args >= 7:
                items, nxt = self.rev._fetch_review_items(url, pkg, sort, self.args.page_size, None, None, token)
            else:
                items, nxt = self.rev._fetch_review_items(url, pkg, sort, self.args.page_size, None, token)
        except TypeError as e:
            if "NoneType" not in str(e):
                raise  # any other TypeError is a library change: stop
            raise NoReviewList(str(e)) from e
        if isinstance(nxt, list):
            nxt = None
        return items or [], nxt

    def parse(self, item, lang, fetched):
        r = {k: nested(item, p) for k, p in self.paths.items()}
        r["at_utc"] = iso_from_ts(nested(item, self.path_at))
        r["repliedAt_utc"] = iso_from_ts(nested(item, self.path_replied))
        r["bucket"] = lang
        r["fetched_utc"] = fetched
        return r

    def bucket(self, pkg, lang, saved, other_ids):
        """Download one app x language. `saved` = IDs already in this language's file (updated in place);
        `other_ids` = IDs already downloaded for this app in other languages."""
        a = self.args
        sp, jp = state_path(a.out, pkg, lang), jsonl_path(a.out, pkg, lang)
        jp.parent.mkdir(parents=True, exist_ok=True)
        state = load_state(sp)
        if state.get("status") in DONE and not a.refresh:
            return state
        token = state.get("token") if state.get("status") in ("running", "error", "capped") else None
        if a.refresh:
            token = None
        state.update({"package": pkg, "lang": lang, "status": "running",
                      "since": a.since.date().isoformat(), "page_size": a.page_size})
        state.setdefault("pages", 0)
        n_saved, empty_pages, first_page, no_list = len(saved), 0, token is None, 0
        log.info("  %-3s start (%d already saved%s)", lang, n_saved, ", resuming" if token else "")
        while True:
            if a.max_per_bucket and n_saved >= a.max_per_bucket:
                state["status"], state["note"] = "capped", f"stopped at --max-per-bucket {a.max_per_bucket}"
                break
            try:
                items, nxt = with_retries(self.fetch_page, pkg, lang, token, what=f"{pkg} [{lang}] page",
                                          not_found=NoReviewList)
            except NoReviewList:
                no_list += 1
                if no_list < 3:  # usually means no reviews in this language; try twice more in case of a glitch
                    polite_sleep(a.delay * 3)
                    continue
                if first_page and token is None:
                    state["status"], state["note"] = "complete", "no reviews in this language (no review list, 3 tries)"
                else:
                    state["status"], state["note"] = "error", "no review list part-way through; rerun to resume"
                break
            except BucketError as e:
                if token is not None and first_page is False and state.get("retried_from_start") is not True:
                    # an old continuation token may have expired: start the bucket again from the newest review
                    log.warning("  %s: restarting this language from the newest review", lang)
                    state["retried_from_start"] = True
                    token, first_page = None, True
                    continue
                state["status"], state["note"] = "error", str(e)[:300]
                break
            no_list = 0
            fetched = now_utc().isoformat()
            rows = [self.parse(i, lang, fetched) for i in items]
            rows = [r for r in rows if r.get("reviewId")]
            if not rows:
                if nxt is None:
                    state["status"] = "complete"
                    break
                empty_pages += 1
                if empty_pages >= 3:
                    state["status"], state["note"] = "complete", "3 empty pages in a row"
                    break
                polite_sleep(a.delay * 3)
                continue
            empty_pages = 0
            ids = [r["reviewId"] for r in rows]
            if lang != "en" and first_page and not saved and len(rows) >= 20:
                # Google answers some language codes with its default (unfiltered) list. If the first
                # page is almost all reviews we already have from other languages, skip this language.
                dup = sum(i in other_ids for i in ids) / len(ids)
                if dup >= 0.9:
                    state["status"] = "not_filtered"
                    state["note"] = f"{dup:.0%} of the first page already came from other languages; skipped"
                    break
            first_page = False
            dates = [parse_iso(r["at_utc"]) for r in rows if r["at_utc"]]
            keep = [r for r in rows if r["reviewId"] not in saved
                    and (r["at_utc"] is None or parse_iso(r["at_utc"]) >= a.since)]
            if keep:
                with open(jp, "a", encoding="utf-8") as f:
                    for r in keep:
                        f.write(json.dumps(r, ensure_ascii=False) + "\n")
                saved.update(r["reviewId"] for r in keep)
                n_saved += len(keep)
            elif a.refresh and all(i in saved for i in ids):
                state["status"], state["note"] = "complete", "up to date (refresh)"
                break
            state["pages"] += 1
            state["n_saved"] = n_saved
            if dates:
                old, new = min(dates).isoformat(), max(dates).isoformat()
                state["oldest_utc"] = min(filter(None, [state.get("oldest_utc"), old]))
                state["newest_utc"] = max(filter(None, [state.get("newest_utc"), new]))
            state["token"] = nxt
            save_state(sp, state)
            if dates and min(dates) < a.since:
                state["status"] = "since_reached"
                break
            if nxt is None:
                state["status"] = "complete"
                break
            token = nxt
            polite_sleep(a.delay)
        if state["status"] in DONE:
            state["token"] = None
        state["n_saved"] = n_saved
        save_state(sp, state)
        log.info("  %-3s %-13s %6d reviews  %s", lang, state["status"], n_saved, state.get("note", ""))
        return state

    def app(self, pkg):
        langs = self.args.langs
        ids = {l: load_ids(jsonl_path(self.args.out, pkg, l)) for l in langs}
        for k, lang in enumerate(langs):
            other = set().union(*(ids[l] for l in langs if l != lang))
            before = load_state(state_path(self.args.out, pkg, lang)).get("status")
            if k and (before not in DONE or self.args.refresh):
                polite_sleep(self.args.delay)
            self.bucket(pkg, lang, ids[lang], other)

    def metadata(self, apps):
        fields = ["title", "developer", "genre", "installs", "minInstalls", "realInstalls", "score",
                  "ratings", "reviews", "released", "lastUpdatedOn", "updated", "version",
                  "contentRating", "free", "containsAds", "offersIAP", "url"]
        stamp = now_utc()
        rows = []
        for a in apps:
            pkg = a["package"]
            row = {"package": pkg, "platform": a.get("platform", ""), "scraped_utc": stamp.isoformat()}
            try:
                d = with_retries(self.gps.app, pkg, lang="en", country=self.args.country,
                                 attempts=4, what=f"{pkg} details", not_found=self.NotFoundError)
                row["status"] = "ok"
                for k in fields:
                    v = d.get(k)
                    row[k] = json.dumps(v) if isinstance(v, (list, dict)) else v
                row["updated_utc"] = iso_from_ts(d.get("updated"))
                row["histogram"] = json.dumps(d.get("histogram"))
            except self.NotFoundError:
                row["status"] = "not_found"
            except BucketError as e:
                row["status"] = "error: " + str(e)[:120]
            log.info("details %-45s %s", pkg, row["status"])
            rows.append(row)
            polite_sleep(self.args.delay)
        cols = ["package", "platform", "status", "scraped_utc"] + fields + ["updated_utc", "histogram"]
        for name in ("apps_metadata.csv", f"apps_metadata_{stamp:%Y%m%d}.csv"):
            with open(self.args.out / name, "w", newline="", encoding="utf-8-sig") as f:
                w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                w.writeheader()
                w.writerows(rows)
        return {r["package"]: r["status"] for r in rows}


# --------------------------------------------------------------------------- combine
def combine(out, langs):
    try:
        import pandas as pd
    except ImportError:
        sys.exit("pandas is not installed. Run:  pip install -r requirements.txt")
    order = {l: i for i, l in enumerate(langs)}
    recs = []
    for jp in sorted((out / "raw").glob("*/*.jsonl")):
        pkg = jp.parent.name
        with open(jp, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                r["package"] = pkg
                recs.append(r)
    if not recs:
        log.warning("No reviews found under %s", out / "raw")
        return
    df = pd.DataFrame(recs)
    df["_o"] = df["bucket"].map(order).fillna(99)
    buckets = (df.sort_values("_o").groupby(["package", "reviewId"])["bucket"]
                 .agg(lambda s: ";".join(dict.fromkeys(s))).rename("play_langs"))
    latest = (df.sort_values(["fetched_utc"]).groupby(["package", "reviewId"]).tail(1)
                .set_index(["package", "reviewId"]))
    res = latest.join(buckets).reset_index()
    res["n_buckets"] = res["play_langs"].str.count(";") + 1
    cols = ["package", "reviewId", "at_utc", "score", "thumbsUpCount", "appVersion", "content",
            "replyContent", "repliedAt_utc", "play_langs", "n_buckets", "fetched_utc"]
    res = res[cols].sort_values(["package", "at_utc"])
    res.to_csv(out / "reviews_raw.csv", index=False, encoding="utf-8-sig")
    log.info("reviews_raw.csv: %d reviews from %d apps", len(res), res["package"].nunique())

    states = [load_state(p) for p in sorted((out / "raw").glob("*/*.state.json"))]
    keys = ["package", "lang", "status", "n_saved", "pages", "oldest_utc", "newest_utc", "note", "updated_utc"]
    with open(out / "scrape_summary.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(states)
    log.info("scrape_summary.csv: %d app x language rows", len(states))


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packages", type=Path, default=HERE / "packages.csv")
    ap.add_argument("--out", type=Path, default=HERE / "data")
    ap.add_argument("--langs", default=",".join(DEFAULT_LANGS),
                    help="Play language codes to request, comma-separated (default: %(default)s)")
    ap.add_argument("--country", default="in")
    ap.add_argument("--since", default="2016-01-01", help="ignore reviews older than this date (YYYY-MM-DD)")
    ap.add_argument("--page-size", type=int, default=1000, help="reviews per request (max 4500)")
    ap.add_argument("--delay", type=float, default=2.0, help="average seconds between requests")
    ap.add_argument("--only", default="", help="comma-separated package IDs to scrape (default: all with scrape=1)")
    ap.add_argument("--max-per-bucket", type=int, default=0, help="stop each app x language after this many reviews (testing)")
    ap.add_argument("--refresh", action="store_true", help="re-download finished languages (new reviews since last run)")
    ap.add_argument("--skip-metadata", action="store_true")
    ap.add_argument("--metadata-only", action="store_true")
    ap.add_argument("--combine-only", action="store_true")
    ap.add_argument("--insecure-tls", action="store_true", help="skip HTTPS certificate checks (only if your network requires it)")
    a = ap.parse_args()

    a.out.mkdir(parents=True, exist_ok=True)
    a.langs = [l.strip() for l in a.langs.split(",") if l.strip()]
    if "en" in a.langs:
        a.langs.remove("en")
        a.langs.insert(0, "en")
    a.since = dt.datetime.fromisoformat(a.since).replace(tzinfo=UTC)
    a.page_size = max(20, min(a.page_size, 4500))
    if a.max_per_bucket:  # a test run should not download a full page beyond its cap
        a.page_size = max(20, min(a.page_size, a.max_per_bucket))
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S",
                        handlers=[logging.StreamHandler(sys.stdout),
                                  logging.FileHandler(a.out / "scrape.log", encoding="utf-8")])

    if a.combine_only:
        combine(a.out, a.langs)
        return
    only = {p.strip() for p in a.only.split(",") if p.strip()}
    apps = read_packages(a.packages, only)
    log.info("%d apps, languages: %s, since %s", len(apps), ",".join(a.langs), a.since.date())
    s = Scraper(a)
    try:
        status = {} if a.skip_metadata else s.metadata(apps)
        if not a.metadata_only:
            for i, app in enumerate(apps, 1):
                pkg = app["package"].strip()
                if status.get(pkg) == "not_found":
                    log.info("[%d/%d] %s: not on Google Play, skipped", i, len(apps), pkg)
                    continue
                log.info("[%d/%d] %s (%s)", i, len(apps), pkg, app.get("platform", ""))
                s.app(pkg)
    except KeyboardInterrupt:
        log.warning("Stopped. Progress is saved; run the same command again to carry on.")
    finally:
        combine(a.out, a.langs)


if __name__ == "__main__":
    main()
