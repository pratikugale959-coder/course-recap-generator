# Course Recap Generator

A single controlled pipeline that turns a course PDF into a
reviewed study recap — built as a college assignment on
OpenCode's extension points: a real MCP server, a reusable
custom skill, and a harness-defined sub-agent.

```
input/course.pdf
  → pdf_extractor MCP server (real MCP, no mocks)
  → work/course-content.json + work/extraction-report.txt
  → course-recap skill
  → output/draft/{course-summary.md, key-concepts.md, concept-diagram.mmd}
  → course-reviewer sub-agent (launched exactly once)
  → output/review.md (findings + VERDICT)
  → one correction pass
  → output/final/* + output/run-report.md
  → STOP (never a loop)
```

## Project layout

| Path | What it is |
| --- | --- |
| `opencode.jsonc` | OpenCode config: declares the MCP server, grants `skill:course-recap` and `subagent:course-reviewer` |
| `AGENTS.md` | The fixed 7-stage pipeline rules (extract → persist → draft → review → revise → report → stop) |
| `mcp-servers/pdf-extractor/` | The MCP server (Python, official `mcp` SDK + `pypdf`): tools `extract_pdf_text`, `get_pdf_outline`; project-directory safety boundary |
| `.opencode/skills/course-recap/` | The reusable course-recap skill (workflow + templates + output schema) |
| `.opencode/agents/course-reviewer.md` | The reviewer sub-agent: read-only 4-check protocol (fidelity, coverage, diagram, format) |
| `tests/test_pdf_extractor.py` | 17-check protocol test that boots the real server over MCP stdio |
| `input/course.pdf` | The course PDF to process |
| `work/` | Extraction outputs (source of truth: `course-content.json`) |
| `output/` | Drafts, final artifacts, review, run report |
| `output/evidence/` | Verification evidence pack (live captures) |

## Setup

```powershell
# Python environment with pinned dependencies
python -m venv .venv
.venv\Scripts\pip install -r mcp-servers/pdf-extractor/requirements.txt
#   mcp==1.30.0, pypdf==6.19.0

# OpenCode CLI v2 (npm)
npm install -g opencode

# Verify the MCP server connects
opencode mcp list     # → ✓ pdf_extractor connected
```

## Run

1. Place the course PDF at `input/course.pdf`.
2. Start OpenCode in this directory and ask for the pipeline
   (e.g. "run the course recap pipeline"). The main agent
   executes `AGENTS.md` exactly once:
   - calls the `pdf_extractor` MCP tools and persists the extraction,
   - loads the `course-recap` skill and writes the three drafts,
   - launches the `course-reviewer` sub-agent **exactly once**,
   - applies **one** correction pass to `output/final/`,
   - writes `output/review.md` and `output/run-report.md`, then stops.

No loops: if issues remain after the single revision pass, they
are documented honestly in the run report instead of re-running.

## Sample run

The bundled `input/course.pdf` (SPPU AI Unit 2 — Problem
Solving, 19 pages) has already been through the full pipeline.
See `output/evidence/pipeline-run/` for the archived run and
`output/evidence/` for live verification captures.

## Design constraints honored

- **Single controlled workflow** — fixed pipeline, no autonomous
  re-runs (enforced by `AGENTS.md`).
- **Real MCP server** — genuine protocol work, tested 17/17;
  nothing mocked.
- **Real sub-agent** — `course-reviewer` is a file-defined
  sub-agent launched by the harness; the successful child
  session is captured in `output/evidence/06-reviewer-session.txt`.
- **Reusable custom skill** — `course-recap` with templates.
- **Fidelity** — every module, concept, and claim in the recap
  cites source pages; nothing is invented.

## Known limitation (OpenCode free tier)

File-defined agents with `deny` permission rules fail on the
OpenCode Console free tier ("OpenCode's free tier can only be
used from within OpenCode"). `course-reviewer` therefore uses
allow rules only; its read-only behavior is enforced by its
system prompt. Details in `output/evidence/04-subagent-registration.txt`.
