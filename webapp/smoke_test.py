r"""Smoke test for the Course Recap web app.

Requires the web app to be running on localhost:8000:
    .venv\Scripts\python webapp\server.py

Usage:
    .venv\Scripts\python webapp\smoke_test.py [pdf_path]
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

BASE = "http://localhost:8000"
DEFAULT_PDF = Path(__file__).resolve().parent.parent / "input" / "course.pdf"


def main() -> int:
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PDF
    if not pdf.is_file():
        print(f"PDF not found: {pdf}")
        return 1

    # liveness
    with urllib.request.urlopen(BASE + "/health", timeout=10) as r:
        health = json.load(r)
    print("health:", health)

    # generation
    with pdf.open("rb") as f:
        request = urllib.request.Request(
            BASE + "/generate",
            data=f.read(),
            headers={"X-File-Name": pdf.name},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=120) as r:
            recap = json.load(r)

    print("ok:", recap["ok"])
    print("title:", recap["title"])
    print(
        f"pages: {recap['page_count']} | chars: {recap['total_chars']} | "
        f"warnings: {len(recap['warnings'])}"
    )
    print(
        f"modules: {len(recap['modules'])} | "
        f"concepts: {len(recap['concepts'])} | "
        f"glossary: {len(recap['glossary'])}"
    )

    first = recap["modules"][0]
    print(f"first module: {first['title']} -> {len(first['takeaways'])} takeaways")
    if first["takeaways"]:
        print("  takeaway[0]:", first["takeaways"][0][:100])
    print("first concept:", recap["concepts"][0]["concept"])

    lines = recap["diagram"].splitlines()
    nodes = [ln for ln in lines if "[" in ln and "-->" not in ln]
    edges = [ln for ln in lines if "-->" in ln]
    print(
        f"diagram: {len(recap['diagram'])} chars | "
        f"nodes: {len(nodes)} | edges: {len(edges)}"
    )
    if edges:
        print("first edge:", edges[0].strip())

    assert recap["ok"] is True
    assert recap["modules"], "no modules generated"
    assert recap["concepts"], "no concepts generated"
    assert recap["diagram"].startswith("flowchart TD")
    assert nodes and edges, "diagram has no nodes/edges"
    print("\nSMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
