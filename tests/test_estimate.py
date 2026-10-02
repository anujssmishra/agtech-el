"""The estimator recovers a known effect on simulated data; placebo and event study run."""
import pytest

pytest.importorskip("pyfixest")
from estimate import fit_event, fit_main, placebo, prepare  # noqa: E402
from simulate_panel import simulate  # noqa: E402


def test_recovers_effect():
    panel, lau = simulate(n_apps=40, n_treated=15, effect=0.5, seed=3)
    launch = {r.package: r.ai_launch_month for r in lau.itertuples() if r.ai_launch_month}
    d = prepare(panel, launch)
    res = fit_main(d, "n_main")
    assert 0.25 < res["beta"] < 0.6 and res["p"] < 0.01
    es = fit_event(d, "n_main")
    pre, post = es[es["quarter"] < -1], es[es["quarter"] >= 0]
    assert abs(pre["beta"].mean()) < 0.3 and post["beta"].mean() > 0.2   # single quarters are noisy
    pl = placebo(d, launch, "n_main", reps=2, seed=1)
    assert len(pl) == 2


def test_no_effect_is_small():
    panel, lau = simulate(n_apps=40, n_treated=15, effect=0.0, seed=4)
    launch = {r.package: r.ai_launch_month for r in lau.itertuples() if r.ai_launch_month}
    res = fit_main(prepare(panel, launch), "n_main")
    assert abs(res["beta"]) < 0.2
