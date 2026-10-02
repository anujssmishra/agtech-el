"""The paper table and figures are written from estimate.py's output files."""
import numpy as np
import pandas as pd
import pytest

from estimate import plot_event, plot_placebo, ri_pvalue  # noqa: E402
from tables import write_main_table  # noqa: E402


def _estimates(folder, betas=(0.2, -0.1)):
    rows = [{"measure": m, "beta": b, "se": 0.05, "p": 0.0004 if b > 0 else 0.0456, "ci_low": b - 0.1,
             "ci_high": b + 0.1, "effect_pct": 100 * np.expm1(b), "n_obs": 34233, "n_apps": 40, "n_treated": 15,
             "n_reviews": 248142} for m, b in zip(["n_main", "n_script"], betas)]
    pd.DataFrame(rows).to_csv(folder / "main_estimates.csv", index=False)


def test_main_table(tmp_path):
    _estimates(tmp_path)
    pd.DataFrame({"draw_seed": 1000, "draw": range(4), "beta": [0.05, -0.25, 0.1, 0.3]}).to_csv(
        tmp_path / "placebo.csv", index=False)
    write_main_table(tmp_path)
    csv = pd.read_csv(tmp_path / "main_table.csv", dtype=str, keep_default_na=False)
    assert list(csv.columns[1:]) == ["(1) Main", "(2) Indian script only"]
    assert csv.iloc[0, 1:].tolist() == ["22.1", "−9.5"]                 # 100*(exp(b)-1)
    assert csv.iloc[1, 1] == f"[{100 * np.exp(0.2) * 0.05:.1f}]"              # delta-method SE
    assert csv.iloc[3, 1:].tolist() == ["<0.001", "0.046"]
    assert csv.iloc[4, 1:].tolist() == ["0.500", ""]                         # RI p for column (1) only
    tex = (tmp_path / "main_table.tex").read_text()
    for s in (r"\toprule", r"\midrule", r"\bottomrule", r"$-$9.5", "[6.1]", "[4.5]", "34,233", "share of 4 placebo"):
        assert s in tex
    rows = [line for line in tex.splitlines() if line.endswith(r"\\")]
    assert len(rows) == 12 and all(line.count("&") == 2 for line in rows)     # 3 header + 9 body rows, 3 cells each


def test_main_table_without_placebo(tmp_path):
    _estimates(tmp_path, betas=(0.2,))
    write_main_table(tmp_path)
    tex = (tmp_path / "main_table.tex").read_text()
    assert "placebo" not in tex and r"\bottomrule" in tex


def test_ri_pvalue():
    assert ri_pvalue([0.1, -0.3, 0.2, -0.05], 0.2) == pytest.approx(0.5)
    assert ri_pvalue([0.1, -0.3], -0.25) == pytest.approx(0.5)


def test_figures(tmp_path):
    pytest.importorskip("matplotlib")
    es = pd.DataFrame({"quarter": range(-4, 5), "beta": [0.0] * 9, "se": [0.1] * 9})
    es["ci_low"], es["ci_high"] = es["beta"] - 0.2, es["beta"] + 0.2
    plot_event(es, tmp_path / "event_study.png")
    plot_placebo(pd.DataFrame({"beta": np.linspace(-0.2, 0.2, 50)}), 0.15, tmp_path / "placebo.png", 0.04)
    for name in ("event_study", "placebo"):
        assert (tmp_path / f"{name}.png").stat().st_size > 0 and (tmp_path / f"{name}.pdf").stat().st_size > 0
