import pytest
from pathlib import Path
from course_planner import build_graph_from_csv, topo_sort_kahn

DATA = Path(__file__).resolve().parents[1] / "sample_inputs"

def test_valid_plan():
    g = build_graph_from_csv(str(DATA / "courses_ok.csv"))
    order = topo_sort_kahn(g)
    assert order.index("C101") < order.index("C201") < order.index("C301")

def test_cycle_detection():
    g = build_graph_from_csv(str(DATA / "courses_cycle.csv"))
    with pytest.raises(ValueError):
        topo_sort_kahn(g)

def test_self_loop_detection(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("CX,CX\n", encoding="utf-8")
    with pytest.raises(ValueError):
        _ = build_graph_from_csv(str(p))
