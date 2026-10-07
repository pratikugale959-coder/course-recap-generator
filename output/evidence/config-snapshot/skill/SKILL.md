---
name: Course Recap
description: Generate a course recap — summary, key concepts, and a Mermaid concept diagram — from structured PDF course content extracted by the pdf_extractor MCP server
---

## When to use

The extraction stage of the Course Recap Generator pipeline has already
run: `work/course-content.json` (from the `pdf_extractor` MCP tools
`extract_pdf_text` and `get_pdf_outline`) exists and is up to date.

## Workflow

1. Read `work/course-content.json`. Note `page_count`, `metadata`, and
   `warnings` (scanned pages). If the extraction is missing or empty,
   stop and report — never generate content from nothing.
2. Write `output/draft/course-summary.md` following the template at
   `templates/summary-template.md` (relative to this skill's directory).
3. Write `output/draft/key-concepts.md` following the concept-table
   contract in `references/output-schema.md` (relative to this skill's
   directory).
4. Write `output/draft/concept-diagram.mmd` following
   `templates/diagram-guide.md` (relative to this skill's directory).
5. Update `work/manifest.json`: mark stage `draft` done and record the
   three artifact paths.
6. Hand off to the main agent: request the `course-reviewer` sub-agent
   (launched exactly once by the main agent, not by this skill).

## Rules

- **Fidelity first.** Every module, concept, definition, and claim must
  trace to `work/course-content.json`. Cite source page ranges (from the
  outline or the per-page text) for every module and concept.
- **Never invent** topics, examples, objectives, or relationships that
  are not present in the extraction. If the source is silent on
  something, mark it "not covered in source".
- **Scanned pages.** Pages flagged in `warnings` have little or no
  extractable text — do not fabricate content for them.
- **Diagram discipline.** Mermaid `flowchart TD` only, max ~15 nodes,
  kebab-case node IDs, edges labeled with relationships stated in the
  source (see `templates/diagram-guide.md`).
- **Paths.** Artifact paths (`work/`, `output/`) are relative to the
  project root (the directory containing `opencode.jsonc`); template and
  reference paths are relative to this skill's directory.
