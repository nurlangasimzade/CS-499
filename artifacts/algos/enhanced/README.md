# Course Planner (Topological Sort via Kahn's Algorithm)

**Category:** Algorithms & Data Structure  
**Student:** Nurlan Gasimzade

This artifact solves the course scheduling problem by building a directed graph from `(COURSE, PREREQ)` pairs and computing a valid order using **Kahn’s algorithm** in **O(V + E)** time. It includes clear error messaging for cycles, self-loops, and malformed inputs, plus unit tests.

## How to Run
```bash
# (Optional) create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python course_planner.py --input sample_inputs/courses_ok.csv
# Expect: a valid order such as: C101 -> C201 -> C301 -> C102 -> C202

# Cycle example
python course_planner.py --input sample_inputs/courses_cycle.csv
# Expect: non-zero exit and a clear “Cycle detected” message.
```

## Tests
```bash
pytest -q
```

## Design Notes
- **Graph**: adjacency list + indegree map
- **Algorithm**: Kahn’s algorithm (queue of indegree-0 nodes)
- **Complexity**: O(V + E)
- **Robustness**: cycle detection, self-loop detection, schema checks
- **Security**: no external inputs beyond the CSV file; safe parsing and explicit errors

## Files
- `course_planner.py` — Graph + algorithm + CLI
- `tests/test_course_planner.py` — unit tests (pytest)
- `sample_inputs/` — example CSVs
- `requirements.txt` — pinned minimal deps
- `CS499_Milestone3_Narrative_Algorithms_Data_Structure_Nurlan_Gasimzade.docx` — narrative
