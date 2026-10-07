# Evidence Pack — Course Recap Generator

Captured 2026-10-07. Each artifact proves one claim about the
implementation. All captures are from the live system (real OpenCode
server, real MCP server, real sub-agent) — nothing is mocked.

## Environment & component wiring

| File | Proves |
| --- | --- |
| `01-opencode-environment.txt` | OpenCode v2.0.24 running; `pdf_extractor` MCP server connected (CLI `mcp list` + `/api/mcp`) |
| `02-mcp-live-tool-call.txt` | Live `extract_pdf_text` / `get_pdf_outline` calls on the real input PDF (19 pages, 8,386 chars, scanned-page warning, 19 bookmarks) |
| `03-mcp-test-suite.txt` | 17/17 protocol tests against the real server subprocess over MCP stdio (exit code 0) |
| `04-subagent-registration.txt` | `course-reviewer` registered as a launchable sub-agent (mode subagent, steps 15, full review protocol, permissions) |
| `05-skill-registration.txt` | `course-recap` custom skill discovered and served by the running server |
| `06-reviewer-session.txt` | The real reviewer child session (`outcome: succeeded`) spawned from the main pipeline session, plus the free-tier/deny-rule development record |

## Configuration snapshot (as used by the run)

- `config-snapshot/opencode.jsonc` — MCP server declaration + permissions (`skill:course-recap`, `subagent:course-reviewer`)
- `config-snapshot/AGENTS.md` — the fixed 7-stage pipeline rules (single controlled workflow, no loops)
- `config-snapshot/agents/course-reviewer.md` — reviewer sub-agent definition
- `config-snapshot/skill/` — the course-recap skill (SKILL.md, templates, output schema)

## Pipeline run (Phase 6, end-to-end on the sample course PDF)

- `pipeline-run/course-content.json` — MCP extraction result (source of truth)
- `pipeline-run/extraction-report.txt` — human-readable extraction map
- `pipeline-run/manifest.json` — stage tracker: extract → draft → review → revise → report, all done
- `pipeline-run/draft/` — skill-generated drafts (pre-review)
- `pipeline-run/review.md` — reviewer findings (2 major, 1 minor) + `VERDICT: REVISE`
- `pipeline-run/final/` — artifacts after the single correction pass
- `pipeline-run/run-report.md` — stages run, corrections C1–C3 applied, remaining issues: none

## Reproduction

```powershell
# MCP server protocol tests (17/17)
.venv\Scripts\python tests/test_pdf_extractor.py

# MCP connectivity
opencode mcp list

# Component registration (location-scoped)
opencode api get "/api/agent?location[directory]=C:\Users\Sarthak\course-recap-generator"
opencode api get "/api/skill?location[directory]=C:\Users\Sarthak\course-recap-generator"

# Sessions (shows the reviewer child session)
opencode api get "/api/session?location[directory]=C:\Users\Sarthak\course-recap-generator"

# Full pipeline: place a course PDF at input/course.pdf, then run the
# AGENTS.md pipeline in OpenCode from this directory
```
