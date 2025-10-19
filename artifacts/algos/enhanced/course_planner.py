"""
Course Planner (Graph + Topological Sort via Kahn's Algorithm)
Author: Nurlan Gasimzade

Usage:
  python course_planner.py --input sample_inputs/courses_ok.csv
  python course_planner.py --input sample_inputs/courses_cycle.csv

Input format (CSV, no header):
  COURSE_CODE,PREREQ_CODE
  If a course has no prerequisites, provide a line with COURSE_CODE only, or leave PREREQ_CODE empty.

Output:
  A valid topological ordering of courses, or an explicit error when a cycle or invalid reference exists.
"""
from __future__ import annotations
import argparse, csv, sys
from collections import deque, defaultdict
from typing import Dict, List, Set, Tuple

class Graph:
    def __init__(self):
        self._adj: Dict[str, Set[str]] = defaultdict(set)   # u -> set of v
        self._in_deg: Dict[str, int] = defaultdict(int)     # v -> indegree

    def add_vertex(self, v: str) -> None:
        if v not in self._adj:
            self._adj[v] = set()
            self._in_deg.setdefault(v, 0)

    def add_edge(self, u: str, v: str) -> None:
        if v not in self._adj[u]:
            self._adj[u].add(v)
            self._in_deg[v] += 1
            self._in_deg.setdefault(u, 0)

    def vertices(self) -> List[str]:
        return list(self._adj.keys())

    def neighbors(self, u: str) -> Set[str]:
        return self._adj[u]

    def indegree(self, v: str) -> int:
        return self._in_deg[v]

def build_graph_from_csv(path: str) -> Graph:
    g = Graph()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader, start=1):
            if not row:  # skip empty lines
                continue
            if len(row) == 1:
                course = row[0].strip()
                if not course:
                    raise ValueError(f"Line {i}: empty course code.")
                g.add_vertex(course)
            else:
                course = row[0].strip()
                prereq = row[1].strip() if len(row) > 1 else ""
                if not course:
                    raise ValueError(f"Line {i}: empty course code.")
                g.add_vertex(course)
                if prereq:
                    g.add_vertex(prereq)
                    if course == prereq:
                        raise ValueError(f"Line {i}: self-loop detected for course '{course}'.")
                    g.add_edge(prereq, course)
    return g

def topo_sort_kahn(g: Graph) -> List[str]:
    """
    Kahn's algorithm: O(V + E).
    Returns an ordering or raises ValueError if a cycle exists.
    """
    indeg = {v: g.indegree(v) for v in g.vertices()}
    q = deque([v for v, d in indeg.items() if d == 0])
    order: List[str] = []

    while q:
        v = q.popleft()
        order.append(v)
        for w in list(g.neighbors(v)):
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)

    if len(order) != len(indeg):
        cyc_nodes = [v for v, d in indeg.items() if d > 0]
        raise ValueError(f"Cycle detected among courses: {', '.join(sorted(cyc_nodes))}")
    return order

def main():
    parser = argparse.ArgumentParser(description="Course Planner (Topological Sort)")
    parser.add_argument("--input", required=True, help="Path to CSV input (COURSE,PREREQ)")
    args = parser.parse_args()

    try:
        g = build_graph_from_csv(args.input)
        order = topo_sort_kahn(g)
        print("Valid course plan:")
        print(" -> ".join(order))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
