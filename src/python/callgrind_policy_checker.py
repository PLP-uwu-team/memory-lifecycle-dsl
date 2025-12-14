import os
import subprocess
import tempfile


def generate_callgraph_svg(binary_path):
    """
    Runs callgrind + gprof2dot + dot.
    Returns path to generated SVG.
    """
    with tempfile.TemporaryDirectory() as tmp:
        cg_out = os.path.join(tmp, "callgrind.out")
        svg_out = os.path.join(tmp, "callgraph.svg")

        # 1. Run callgrind
        subprocess.run(
            [
                "valgrind",
                "--tool=callgrind",
                f"--callgrind-out-file={cg_out}",
                binary_path,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )

        # 2. gprof2dot → dot → svg
        gprof = subprocess.Popen(
            [
                "gprof2dot",
                "-f",
                "callgrind",
                "-n0",
                "-e0",
                cg_out,
            ],
            stdout=subprocess.PIPE,
        )

        subprocess.run(
            ["dot", "-Tsvg", "-o", svg_out],
            stdin=gprof.stdout,
            check=True,
        )

        # Read SVG content (tmp dir will be deleted)
        with open(svg_out, "r", encoding="utf-8") as f:
            svg_data = f.read()

    return svg_data


import xml.etree.ElementTree as ET
from collections import defaultdict


def parse_svg_callgraph(svg_text):
    root = ET.fromstring(svg_text)

    nodes = set()
    edges = []

    for g in root.iter():
        if g.tag.endswith("g"):
            cls = g.attrib.get("class")
            title = g.find("./{*}title")
            if title is None:
                continue

            title_text = title.text.strip()

            if cls == "node":
                nodes.add(title_text)

            elif cls == "edge" and "->" in title_text:
                caller, callee = title_text.split("->", 1)

                calls = 0
                for t in g.findall(".//{*}text"):
                    if t.text and "×" in t.text:
                        calls = int(t.text.replace("×", ""))
                        break

                edges.append(
                    {
                        "caller": caller,
                        "callee": callee,
                        "calls": calls,
                    }
                )

    graph = defaultdict(list)
    for e in edges:
        graph[e["caller"]].append(e)

    return nodes, graph


def reaches(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)

        for e in graph.get(cur, []):
            if e["calls"] <= 0:
                continue

            if e["callee"] == target:
                return True

            stack.append(e["callee"])

    return False


def build_reverse_graph(graph):
    rev = defaultdict(list)
    for caller, edges in graph.items():
        for e in edges:
            rev[e["callee"]].append(
                {
                    "caller": caller,
                    "calls": e["calls"],
                }
            )
    return rev


def reaches_down(graph, start, targets):
    visited = set()
    stack = [start]

    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)

        if cur in targets:
            return True

        for e in graph.get(cur, []):
            if e["calls"] > 0:
                stack.append(e["callee"])

    return False


def ownership_freed(graph, rev_graph, alloc_fn, free_fns):
    """
    Walk UP to callers.
    For each caller, check if it (or below it) calls free.
    """
    visited = set()
    stack = [alloc_fn]

    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)

        # Does THIS owner free it (directly or indirectly)?
        if reaches_down(graph, cur, free_fns):
            return True

        # Otherwise, ownership propagates upward
        for e in rev_graph.get(cur, []):
            if e["calls"] > 0:
                stack.append(e["caller"])

    return False


def check_policy_with_callgrind(binary_path, policy):
    svg = generate_callgraph_svg(binary_path)
    nodes, graph = parse_svg_callgraph(svg)
    rev_graph = build_reverse_graph(graph)

    allocs = policy.allocate
    frees = set(policy.deallocate)

    results = []

    for alloc in allocs:
        if alloc not in nodes:
            results.append(
                {
                    "function": alloc,
                    "severity": "ERROR",
                    "status": "NOT CALLED",
                }
            )
            continue

        freed = ownership_freed(graph, rev_graph, alloc, frees)

        if freed:
            results.append(
                {
                    "function": alloc,
                    "severity": "OK",
                    "status": "OWNERSHIP FREED",
                }
            )
        else:
            results.append(
                {
                    "function": alloc,
                    "severity": "WARNING",
                    "status": "LEAKED OWNERSHIP",
                }
            )

    return results
