"""Language labels for typical review texts (script rules + word lists; no model needed)."""
from pathlib import Path

import pytest

wf = pytest.importorskip("wordfreq")
import detect_language as D  # noqa: E402

D.zipf_frequency = wf.zipf_frequency

CASES = {
    "Very good app for farmers": ("english", "eng"), "good": ("english", "eng"), "Nice app": ("english", "eng"),
    "osm app 👍": ("english", "eng"), "👍👍👍": ("none", "none"),
    "bahut accha app hai kisan bhaiyon ke liye": ("roman", "hin"), "app kaam nahi kar raha": ("roman", "hin"),
    "khup chan app aahe": ("roman", "mar"), "saras app che": ("roman", "guj"), "romba nalla app": ("roman", "tam"),
    "chala bagundi app": ("roman", "tel"), "app is good but delivery late hoti hai": ("mixed", "eng"),
    "यह ऐप बहुत अच्छा है किसानों के लिए": ("native", "hin"), "हे ॲप खूप छान आहे": ("native", "mar"),
    "खूप छान": ("native", "mar"), "ખૂબ સરસ એપ છે": ("native", "guj"), "ৰাইজৰ বাবে ভাল এপ": ("native", "asm"),
    "மிகவும் நல்ல செயலி": ("native", "tam"), "بہت اچھی ایپ ہے": ("native", "urd"),
    "Very good app बहुत अच्छा": ("native+latin", "hin"),
}


@pytest.mark.parametrize("models", ["rules", "model"])
def test_labels(models):
    root = Path(D.__file__).resolve().parent / "models"
    if models == "model" and not (root / D.FTN_FILE).exists():
        pytest.skip("IndicLID model not downloaded")
    lab = D.Labeller(root if models == "model" else Path("/nonexistent"), quiet=True)
    res = lab.label_unique([D.clean(t) for t in CASES])
    for text, (form, main) in CASES.items():
        r = res[D.clean(text)]
        assert (r["form"], r["lang_main"]) == (form, main), (text, r)
