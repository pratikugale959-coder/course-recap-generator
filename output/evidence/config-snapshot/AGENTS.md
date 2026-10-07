# Course Recap Generator — Project Instructions

This project is a **single controlled workflow**, not an autonomous agent loop.
The main agent orchestrates a fixed pipeline exactly once, in order.

## Pipeline (fixed order — never skip, reorder, or repeat stages autonomously)

1. **Extract** — Call the `pdf_extractor` MCP tools (`extract_pdf_text`, then
   `get_pdf_outline`) on `input/course.pdf`.
2. **Persist** — Save structured output to `work/course-content.json` and
   `work/extraction-report.txt`; update `work/manifest.json`.
3. **Draft** — Load the `course-recap` skill, then write
   `output/draft/course-summary.md`, `output/draft/key-concepts.md`, and
   `output/draft/concept-diagram.mmd` following the skill templates.
4. **Review** — Launch the `course-reviewer` sub-agent **exactly once**
   (foreground) with the extraction JSON and the three draft files.
5. **Revise** — Apply the reviewer's blocker/major corrections in **one**
   revision pass; write final artifacts to `output/final/`.
6. **Report** — Save reviewer findings to `output/review.md` and write
   `output/run-report.md` (stages run, verdict, corrections applied,
   remaining issues).
7. **Stop** — The pipeline ends when the run report is written.

## Rules

- **No loops.** Never re-run the reviewer or the revision pass autonomously.
  If issues remain after the single revision pass, document them honestly in
  `output/run-report.md` and stop.
- **Fidelity.** Never invent topics, concepts, definitions, or claims that are
  not present in the MCP extraction. Cite source page ranges for every module.
- **Abort rule.** If the PDF yields little or no extractable text (scanned /
  image-only), stop with a clear message — OCR is out of scope.
- **Scope.** Only read and write files inside this project directory.
- **Sub-agent use.** Only the `course-reviewer` sub-agent may be launched, and
  only once per run.
- **Diagram.** Mermaid only (`flowchart TD`), max ~15 nodes, kebab-case node
  IDs, labeled edges reflecting relationships stated in the source.
