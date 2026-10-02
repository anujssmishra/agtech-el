#!/usr/bin/env python3
"""
detect_language.py - label the language of every review.

    python detect_language.py download-models        # IndicLID native-script model (170 MB) into ./models
    python detect_language.py demo                   # see how sample reviews are labelled
    python detect_language.py label                  # data/reviews_raw.csv  ->  data/reviews_lang.csv
    python detect_language.py sample --n 600         # reviews to check by hand -> data/validation_sample.csv
    python detect_language.py evaluate data/validation_sample.csv   # accuracy, once human_lang is filled in

How a review is labelled
1. Script. Letters are counted by writing system. A review written mostly in an Indian script
   (Devanagari, Bengali-Assamese, Gurmukhi, Gujarati, Odia, Tamil, Telugu, Kannada, Malayalam,
   Urdu) gets its language from IndicLID's native-script model (AI4Bharat). Without the model,
   the script decides, plus a Marathi/Hindi word check for Devanagari and the letters ৰ/ৱ for
   Assamese.
2. Latin letters. Each word is checked against English word frequencies (wordfreq) and the
   lists of romanized Indian words in lexicons.py:
       'very good app'                         -> English
       'bahut accha app hai'                   -> romanized Hindi
       'app is good but delivery late hoti hai'-> mixed (mostly English with Hindi words)
   IndicLID's romanized-text model is not used by default because on short reviews it calls
   'good' Manipuri and 'nice app' Odia. With --ftr it decides only reviews of 4+ words that
   the word lists cannot place.

Columns added to each review
    form        english | roman | native | mixed | native+latin | unknown | none
    lang        eng hin mar guj pan ben tam tel kan mal ori asm urd oth (other Indian) und (undetermined) none (no words)
    lang_main   lang, except that 'mixed' reviews (mostly English words) count as eng
    lang_name   readable name of lang_main
    indian      1 if lang_main is an Indian language, 0 if English, blank otherwise
    method      native-ftn | native-ftn+words | native-ftn+script | native-rule | latin-words | latin-ftr | none
    script, indic_share, n_eng, n_ind, n_unk, model_label, model_score
"""
import argparse
import collections
import csv
import functools
import re
import sys
import unicodedata
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lexicons as LX  # noqa: E402

FTN_FILE = Path("indiclid-ftn") / "model_baseline_roman.bin"   # IndicLID's file names, as released
FTR_FILE = Path("indiclid-ftr") / "model_baseline_roman.bin"
MODEL_URLS = {
    "ftn": "https://github.com/AI4Bharat/IndicLID/releases/download/v1.0/indiclid-ftn.zip",
    "ftr": "https://github.com/AI4Bharat/IndicLID/releases/download/v1.0/indiclid-ftr.zip",
}
EN_ZIPF = 3.0          # a word at least this frequent in English (wordfreq Zipf scale) counts as English
MIN_FTR_WORDS = 4

LANG_NAMES = {"eng": "English", "hin": "Hindi", "mar": "Marathi", "guj": "Gujarati", "pan": "Punjabi",
              "ben": "Bengali", "tam": "Tamil", "tel": "Telugu", "kan": "Kannada", "mal": "Malayalam",
              "ori": "Odia", "asm": "Assamese", "urd": "Urdu", "oth": "Other Indian",
              "und": "Undetermined", "none": "No text"}
INDIAN = {"hin", "mar", "guj", "pan", "ben", "tam", "tel", "kan", "mal", "ori", "asm", "urd", "oth"}

SCRIPT_RANGES = [
    (0x0900, 0x097F, "Devanagari"), (0xA8E0, 0xA8FF, "Devanagari"), (0x0980, 0x09FF, "Bengali"),
    (0x0A00, 0x0A7F, "Gurmukhi"), (0x0A80, 0x0AFF, "Gujarati"), (0x0B00, 0x0B7F, "Odia"),
    (0x0B80, 0x0BFF, "Tamil"), (0x0C00, 0x0C7F, "Telugu"), (0x0C80, 0x0CFF, "Kannada"),
    (0x0D00, 0x0D7F, "Malayalam"), (0x0600, 0x06FF, "Arabic"), (0x0750, 0x077F, "Arabic"),
    (0x08A0, 0x08FF, "Arabic"), (0xFB50, 0xFDFF, "Arabic"), (0xFE70, 0xFEFF, "Arabic"),
    (0x1C50, 0x1C7F, "OlChiki"), (0xABC0, 0xABFF, "MeeteiMayek"),
    (0x0041, 0x005A, "Latin"), (0x0061, 0x007A, "Latin"), (0x00C0, 0x024F, "Latin"), (0x1E00, 0x1EFF, "Latin"),
]
INDIC_SCRIPTS = {"Devanagari", "Bengali", "Gurmukhi", "Gujarati", "Odia", "Tamil", "Telugu", "Kannada",
                 "Malayalam", "Arabic", "OlChiki", "MeeteiMayek"}
SCRIPT_LANG = {"Gurmukhi": "pan", "Gujarati": "guj", "Odia": "ori", "Tamil": "tam", "Telugu": "tel",
               "Kannada": "kan", "Malayalam": "mal", "Arabic": "urd", "OlChiki": "oth", "MeeteiMayek": "oth"}
URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+", re.I)
WORD_RE = re.compile(r"[a-z]+")

MARKER_INDEX = collections.defaultdict(set)
for _lang, _words in LX.ROMAN_MARKERS.items():
    for _w in _words:
        MARKER_INDEX[_w].add(_lang)
PRIORITY = {l: i for i, l in enumerate(LX.LANG_PRIORITY)}
DEV_MARATHI = {unicodedata.normalize("NFC", w) for w in LX.DEVANAGARI_MARATHI}
DEV_HINDI = {unicodedata.normalize("NFC", w) for w in LX.DEVANAGARI_HINDI}


# --------------------------------------------------------------------------- basics
def clean(text):
    if text is None or (isinstance(text, float) and text != text):
        return ""
    t = unicodedata.normalize("NFC", str(text))
    t = URL_RE.sub(" ", t)
    return " ".join(t.split())


def script_of(ch):
    o = ord(ch)
    for lo, hi, name in SCRIPT_RANGES:
        if lo <= o <= hi:
            return name
    return "Other"


def script_profile(text):
    counts = collections.Counter()
    for ch in text:
        cat = unicodedata.category(ch)
        if cat[0] in "LM":
            counts[script_of(ch)] += 1
    total = sum(counts.values())
    if not total:
        return None, 0.0, 0, counts
    indic = sum(v for k, v in counts.items() if k in INDIC_SCRIPTS)
    top = counts.most_common(1)[0][0]
    return top, indic / total, total, counts


def code_from_label(label):
    """IndicLID label (hin_Deva, mar_Latn, other ...) -> our language code."""
    if not label or label == "other":
        return "und"
    code = label.split("_")[0]
    if code == "eng":
        return "eng"
    return code if code in INDIAN else "oth"


def _word_variants(tok):
    two = re.sub(r"(.)\1{2,}", r"\1\1", tok)       # goooood -> good
    one = re.sub(r"(.)\1+", r"\1", tok)            # niceee -> nice
    return list(dict.fromkeys([tok, two, one]))


@functools.lru_cache(maxsize=None)
def word_class(tok):
    """'eng', 'ind' (with languages), 'neutral' or 'unk' for one lower-case Latin word."""
    if len(tok) < 2:
        return "neutral", ()
    variants = _word_variants(tok)
    for t in variants:
        if t in LX.NEUTRAL:
            return "neutral", ()
        if t in MARKER_INDEX:
            return "ind", tuple(sorted(MARKER_INDEX[t]))
        if t in LX.ENGLISH_EXTRA:
            return "eng", ()
    if len(tok) == 2:
        return "neutral", ()   # me, to, ki, ka, se, ho ... are both English and Hindi
    for t in variants:
        if zipf_frequency(t, "en") >= EN_ZIPF:
            return "eng", ()
    return "unk", ()


def pick_language(votes):
    return max(votes, key=lambda l: (votes[l], -PRIORITY.get(l, 99)))


# --------------------------------------------------------------------------- models
def load_fasttext(path, quiet=False):
    try:
        import fasttext
        try:
            fasttext.FastText.eprint = lambda *a, **k: None   # silence a harmless load warning
        except AttributeError:
            pass
    except ImportError:
        if not quiet:
            print("fasttext is not installed (pip install fasttext-wheel); using the script rules instead.")
        return None
    return fasttext.load_model(str(path))


def ft_predict(model, texts):
    lines = [t.replace("\n", " ") + "\n" for t in texts]
    try:
        labels, probs = model.f.multilinePredict(lines, 1, 0.0, "replace")
    except (AttributeError, TypeError):
        labels, probs = [], []
        for t in texts:
            l, p = model.predict(t.replace("\n", " "))
            labels.append(l)
            probs.append(list(p))
    out = []
    for l, p in zip(labels, probs):
        lab = l[0].replace("__label__", "") if len(l) else "other"
        out.append((lab, min(1.0, float(p[0])) if len(p) else 0.0))
    return out


def download_models(models_dir, with_ftr):
    models_dir.mkdir(parents=True, exist_ok=True)
    for key in (["ftn", "ftr"] if with_ftr else ["ftn"]):
        target = models_dir / (FTN_FILE if key == "ftn" else FTR_FILE)
        if target.exists():
            print(f"{target} already there")
            continue
        url = MODEL_URLS[key]
        zpath = models_dir / Path(url).name
        print(f"Downloading {url} ...")

        def hook(blocks, bs, size):
            if size > 0 and blocks % 200 == 0:
                print(f"  {min(100, blocks * bs * 100 // size)}%", end="\r", flush=True)
        urllib.request.urlretrieve(url, zpath, hook)
        with zipfile.ZipFile(zpath) as zf:
            zf.extractall(models_dir)
        zpath.unlink()
        print(f"  saved {target}")


# --------------------------------------------------------------------------- labelling
class Labeller:
    def __init__(self, models_dir=None, use_ftn=True, use_ftr=False, quiet=False):
        self.ftn = self.ftr = None
        if use_ftn and models_dir and (models_dir / FTN_FILE).exists():
            self.ftn = load_fasttext(models_dir / FTN_FILE, quiet)
        elif use_ftn and not quiet:
            print(f"IndicLID native-script model not found in {models_dir}; using script rules "
                  f"(run: python detect_language.py download-models).")
        if use_ftr:
            if models_dir and (models_dir / FTR_FILE).exists():
                self.ftr = load_fasttext(models_dir / FTR_FILE, quiet)
            elif not quiet:
                print("--ftr given but the romanized model is missing (download-models --with-ftr).")

    # Latin-letter text -------------------------------------------------------
    @staticmethod
    def latin(text):
        n_eng = n_ind = n_unk = 0
        votes = collections.Counter()
        for tok in WORD_RE.findall(text.lower()):
            cls, langs = word_class(tok)
            if cls == "eng":
                n_eng += 1
            elif cls == "ind":
                n_ind += 1
                for l in langs:
                    votes[l] += 1 / len(langs)
            elif cls == "unk":
                n_unk += 1
        if n_ind == 0:
            if n_eng == 0 and n_unk == 0:
                form, lang = "none", "none"
            elif n_eng >= n_unk:
                form, lang = "english", "eng"
            else:
                form, lang = "unknown", "und"
        else:
            lang = pick_language(votes)
            form = "roman" if n_ind >= n_eng else "mixed"
        return form, lang, n_eng, n_ind, n_unk

    @staticmethod
    def devanagari_votes(text):
        words = set(re.findall(r"[ऀ-ॿ]+", text))
        return len(words & DEV_MARATHI), len(words & DEV_HINDI)

    @classmethod
    def native_rule(cls, text, script):
        if script == "Devanagari":
            mar, hin = cls.devanagari_votes(text)
            return "mar" if mar > hin else "hin"
        if script == "Bengali":
            return "asm" if ("ৰ" in text or "ৱ" in text) else "ben"
        return SCRIPT_LANG.get(script, "oth")

    @classmethod
    def settle_devanagari(cls, text, code):
        """IndicLID is unreliable on short Devanagari text (it calls short Marathi 'Maithili' and a
        single Hindi word 'Sanskrit'). Use Marathi/Hindi marker words to settle those cases."""
        mar, hin = cls.devanagari_votes(text)
        if code in ("hin", "mar"):
            if code == "hin" and mar >= 2 and hin == 0:
                return "mar", True
            if code == "mar" and hin >= 2 and mar == 0:
                return "hin", True
            return code, False
        if mar or hin:
            return ("mar" if mar > hin else "hin"), True
        if len(text.split()) < 4:
            return "hin", True
        return code, False

    def label_unique(self, texts):
        """texts: list of cleaned unique strings -> dict text -> result dict."""
        res, native, ftr_todo = {}, [], []
        for t in texts:
            script, share, n_letters, counts = script_profile(t)
            r = {"script": script or "", "indic_share": round(share, 3), "model_label": "", "model_score": None}
            if not n_letters:
                r.update(form="none", lang="none", method="none", n_eng=0, n_ind=0, n_unk=0)
            elif share >= 0.5 or (share >= 0.2 and sum(v for k, v in counts.items() if k in INDIC_SCRIPTS) >= 3):
                top_indic = max((k for k in counts if k in INDIC_SCRIPTS), key=lambda k: counts[k])
                r.update(form="native" if share >= 0.5 else "native+latin", script=top_indic,
                         n_eng=0, n_ind=0, n_unk=0)
                native.append(t)
            elif counts.get("Latin", 0) >= sum(counts.values()) / 2:
                form, lang, ne, ni, nu = self.latin(t)
                r.update(form=form, lang=lang, method="latin-words" if form != "none" else "none",
                         n_eng=ne, n_ind=ni, n_unk=nu)
                if form == "unknown" and self.ftr and len(WORD_RE.findall(t.lower())) >= MIN_FTR_WORDS:
                    ftr_todo.append(t)
            else:   # mostly another script (Chinese, Cyrillic ...)
                r.update(form="unknown", lang="und", method="none", n_eng=0, n_ind=0, n_unk=0)
            res[t] = r
        if native:
            # the model sees only the Indian-script words (English words in the same review confuse it)
            only_native = [" ".join(w for w in t.split() if script_profile(w)[1] >= 0.5) or t for t in native]
            preds = ft_predict(self.ftn, only_native) if self.ftn else [None] * len(native)
            for t, nt, p in zip(native, only_native, preds):
                r = res[t]
                if p is None:
                    r.update(lang=self.native_rule(nt, r["script"]), method="native-rule")
                    continue
                label, score = p
                code = code_from_label(label)
                r.update(model_label=label, model_score=round(score, 4), method="native-ftn")
                if r["script"] == "Devanagari":
                    code, changed = self.settle_devanagari(nt, code)
                    if changed:
                        r["method"] = "native-ftn+words"
                elif code in ("oth", "und", "eng"):
                    code = self.native_rule(nt, r["script"])
                    r["method"] = "native-ftn+script"
                r["lang"] = code
        if ftr_todo:
            for t, (label, score) in zip(ftr_todo, ft_predict(self.ftr, ftr_todo)):
                code = code_from_label(label)
                code = "hin" if code == "urd" else code    # romanized Urdu and Hindi are one language here
                r = res[t]
                r.update(model_label=label, model_score=round(score, 4), method="latin-ftr")
                if code == "eng":
                    r.update(form="english", lang="eng")
                elif code in INDIAN:
                    r.update(form="roman", lang=code)
        for r in res.values():
            r["lang_main"] = "eng" if r["form"] == "mixed" else r["lang"]
            r["lang_name"] = LANG_NAMES.get(r["lang_main"], r["lang_main"])
            r["indian"] = 1 if r["lang_main"] in INDIAN else (0 if r["lang_main"] == "eng" else "")
        return res


OUT_COLS = ["form", "lang", "lang_main", "lang_name", "indian", "method", "script", "indic_share",
            "n_eng", "n_ind", "n_unk", "model_label", "model_score"]


def cmd_label(a):
    import pandas as pd
    df = pd.read_csv(a.inp, dtype={"reviewId": str}, encoding="utf-8-sig")
    print(f"{len(df):,} reviews read from {a.inp}")
    lab = Labeller(a.models, use_ftn=not a.no_ftn, use_ftr=a.ftr)
    cleaned = df["content"].map(clean)
    uniq = list(dict.fromkeys(cleaned))
    print(f"{len(uniq):,} distinct texts to label")
    results = {}
    step = 50000
    for i in range(0, len(uniq), step):
        results.update(lab.label_unique(uniq[i:i + step]))
        print(f"  {min(i + step, len(uniq)):,} / {len(uniq):,}", flush=True)
    lab_df = pd.DataFrame([results[t] for t in cleaned], index=df.index)[OUT_COLS]
    out = pd.concat([df, lab_df], axis=1)
    out.to_csv(a.out, index=False, encoding="utf-8-sig")
    print(f"Saved {a.out}")
    print("\nShare of reviews by form:")
    print(out["form"].value_counts(normalize=True).round(3).to_string())
    print("\nShare by language (main measure):")
    print(out["lang_name"].value_counts(normalize=True).round(3).to_string())


DEMO = [
    "Very good app for farmers", "good", "Nice app", "Super", "osm app 👍", "👍👍👍", "5 star",
    "bahut accha app hai kisan bhaiyon ke liye", "Bekar app hai paisa wapas nahi mila",
    "app kaam nahi kar raha", "khup chan app aahe", "saras app che", "bahut vadiya app hai ji",
    "khub bhalo app", "romba nalla app", "chala bagundi app", "tumba chennagide", "Mast app",
    "app is good but delivery late hoti hai", "Rate list update karo", "Jai jawan jai kisan",
    "यह ऐप बहुत अच्छा है किसानों के लिए", "अच्छा", "बहुत बढ़िया", "बेकार ऐप", "हे ॲप खूप छान आहे", "खूप छान",
    "छान माहिती मिळते", "ખૂબ સરસ એપ છે", "ਬਹੁਤ ਵਧੀਆ ਐਪ ਹੈ",
    "খুব ভালো অ্যাপ", "ৰাইজৰ বাবে ভাল এপ", "மிகவும் நல்ல செயலி", "చాలా మంచి యాప్", "ತುಂಬಾ ಒಳ್ಳೆಯ ಆಪ್",
    "വളരെ നല്ല ആപ്പ്", "ବହୁତ ଭଲ ଆପ୍", "بہت اچھی ایپ ہے", "Very good app बहुत अच्छा", "Urea DAP rate",
]


def cmd_demo(a):
    lab = Labeller(a.models, use_ftn=not a.no_ftn, use_ftr=a.ftr)
    res = lab.label_unique([clean(t) for t in DEMO])
    print(f"{'review':45} {'form':13} {'lang':5} {'main':5} method")
    for t in DEMO:
        r = res[clean(t)]
        print(f"{t[:44]:45} {r['form']:13} {r['lang']:5} {r['lang_main']:5} {r['method']} {r['model_label']}")


def cmd_sample(a):
    import pandas as pd
    df = pd.read_csv(a.inp, dtype={"reviewId": str}, encoding="utf-8-sig")
    df = df[df["form"] != "none"]
    forms = sorted(df["form"].unique())
    per = max(1, a.n // len(forms))
    parts = []
    for f in forms:
        g = df[df["form"] == f]
        s = g.sample(n=min(per, len(g)), random_state=a.seed).copy()
        s["stratum_N"] = len(g)
        parts.append(s)
    out = pd.concat(parts).sample(frac=1, random_state=a.seed)   # shuffle so coders do not see the strata
    out.insert(0, "sample_id", range(1, len(out) + 1))
    out["human_lang"] = ""
    out["human_note"] = ""
    keep = ["sample_id", "package", "reviewId", "content", "human_lang", "human_note", "form", "lang", "lang_main", "stratum_N"]
    out[keep].to_csv(a.out, index=False, encoding="utf-8-sig")
    print(f"Saved {len(out)} reviews to {a.out}")
    print("Fill human_lang with one code per review: " + " ".join(k for k in LANG_NAMES if k != "none") +
          "  (und = cannot tell, e.g. names only). Code romanized Hindi as hin; code a review that is mostly "
          "English with a few Hindi words as eng. Hide the form/lang columns while coding.")


def cmd_evaluate(a):
    import pandas as pd
    df = pd.read_csv(a.coded, dtype=str, encoding="utf-8-sig").fillna("")
    df = df[df["human_lang"].str.strip() != ""].copy()
    df["human_lang"] = df["human_lang"].str.strip().str.lower()
    df["stratum_N"] = df["stratum_N"].astype(float)
    lines = [f"Coded reviews: {len(df)}"]
    known = df[~df["human_lang"].isin(["und", "none"])].copy()
    known["h_ind"] = known["human_lang"].isin(INDIAN)
    known["p_ind"] = known["lang_main"].isin(INDIAN)
    known["ok_bin"] = known["h_ind"] == known["p_ind"]
    known["ok_lang"] = known["human_lang"] == known["lang_main"]
    w = known.groupby("form")["stratum_N"].first() / known.groupby("form").size()
    known["w"] = known["form"].map(w)
    lines.append(f"Indian vs English agreement, unweighted: {known['ok_bin'].mean():.3f}")
    lines.append(f"Indian vs English agreement, weighted to the full data: "
                 f"{(known['ok_bin'] * known['w']).sum() / known['w'].sum():.3f}")
    lines.append(f"Exact language agreement, weighted: {(known['ok_lang'] * known['w']).sum() / known['w'].sum():.3f}")
    lines.append("\nBy predicted form (n coded, Indian-vs-English agreement, exact language agreement):")
    for f, g in known.groupby("form"):
        lines.append(f"  {f:13} n={len(g):4d}  {g['ok_bin'].mean():.3f}  {g['ok_lang'].mean():.3f}")
    lines.append("\nPredicted (rows) vs human (columns):")
    lines.append(pd.crosstab(df["lang_main"], df["human_lang"]).to_string())
    report = "\n".join(lines)
    print(report)
    rp = Path(a.coded).with_name("validation_report.txt")
    rp.write_text(report, encoding="utf-8")
    print(f"\nSaved {rp}")


def main():
    global zipf_frequency
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--models", type=Path, default=HERE / "models", help="folder with the IndicLID models")
    common.add_argument("--no-ftn", action="store_true", help="do not use the native-script model")
    common.add_argument("--ftr", action="store_true", help="let IndicLID's romanized model decide long unplaced reviews")
    p = sub.add_parser("label", parents=[common])
    p.add_argument("--in", dest="inp", type=Path, default=HERE / "data" / "reviews_raw.csv")
    p.add_argument("--out", type=Path, default=HERE / "data" / "reviews_lang.csv")
    sub.add_parser("demo", parents=[common])
    p = sub.add_parser("download-models")
    p.add_argument("--models", type=Path, default=HERE / "models")
    p.add_argument("--with-ftr", action="store_true", help="also fetch the romanized model (230 MB)")
    p = sub.add_parser("sample")
    p.add_argument("--in", dest="inp", type=Path, default=HERE / "data" / "reviews_lang.csv")
    p.add_argument("--out", type=Path, default=HERE / "data" / "validation_sample.csv")
    p.add_argument("--n", type=int, default=600)
    p.add_argument("--seed", type=int, default=2026)
    p = sub.add_parser("evaluate")
    p.add_argument("coded", type=Path)
    a = ap.parse_args()

    if a.cmd == "download-models":
        download_models(a.models, a.with_ftr)
        return
    if a.cmd in ("label", "demo"):
        try:
            from wordfreq import zipf_frequency as zf
        except ImportError:
            sys.exit("wordfreq is not installed. Run:  pip install -r requirements.txt")
        zipf_frequency = zf
    {"label": cmd_label, "demo": cmd_demo, "sample": cmd_sample, "evaluate": cmd_evaluate}[a.cmd](a)


zipf_frequency = None

if __name__ == "__main__":
    main()
