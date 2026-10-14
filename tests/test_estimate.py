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


def test_leave_one_out_and_categories(tmp_path):
    from estimate import keep_categories, leave_one_out
    panel, lau = simulate(n_apps=12, n_treated=4, effect=0.3, seed=5)
    launch = {r.package: r.ai_launch_month for r in lau.itertuples() if r.ai_launch_month}
    d = prepare(panel, launch)
    loo = leave_one_out(d, "n_main")
    assert sorted(loo["dropped"]) == sorted(launch) and (loo["n_treated"] == len(launch) - 1).all()
    pk = tmp_path / "packages.csv"
    pk.write_text("package,category\nsim.app00,Input marketplace + advisory\nsim.app05,Advisory / crop health (GenAI)\n"
                  "sim.app06,Weather / agromet advisory\n")
    p2, l2 = keep_categories(panel, launch, pk, ["Input marketplace", "Advisory / crop health"])
    assert set(p2["package"]) == {"sim.app00", "sim.app05"} and set(l2) == {"sim.app00"} & set(launch)
