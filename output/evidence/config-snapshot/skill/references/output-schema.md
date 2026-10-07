# Output Schema Reference

## Input contract: `work/course-content.json`

Assembled by the main agent from the two `pdf_extractor` MCP tools:

- `extract_pdf_text` → everything except `outline`
- `get_pdf_outline` → the `outline` list

```json
{
  "file": "C:\\...\\input\\course.pdf",
  "page_count": 19,
  "metadata": { "title": "...", "author": "...", "subject": "..." },
  "total_chars": 8386,
  "warnings": [
    "page 2: little or no extractable text (likely image-only/scanned)"
  ],
  "pages": [ { "page": 1, "char_count": 400, "text": "..." } ],
  "outline": [ { "title": "Module 1", "page": 1, "depth": 0 } ]
}
```

## Artifact 1: `output/draft/course-summary.md`

Markdown following `templates/summary-template.md`. Required sections,
in order:

1. Course overview
2. Learning objectives
3. Module-by-module recap (with page ranges per module)
4. Glossary
5. Self-check questions

## Artifact 2: `output/draft/key-concepts.md`

Markdown table — one row per key concept:

```markdown
| Concept | Definition | Source page(s) | Why it matters |
| --- | --- | --- | --- |
| problem-solving agent | An agent that searches for a sequence of actions to reach a goal | 3–5 | Core abstraction of the unit |
```

Rules:

- 5–15 concepts for a typical course unit.
- Definitions must paraphrase the source, not copy long passages.
- `Source page(s)` is required for every row — no exceptions.
- `Why it matters` must come from the source's emphasis (headings,
  summaries, repeated topics), not from general knowledge.

## Artifact 3: `output/draft/concept-diagram.mmd`

Mermaid `flowchart TD` per `templates/diagram-guide.md`: max ~15 nodes,
kebab-case IDs, labeled edges, node set equal to the key-concepts table.
