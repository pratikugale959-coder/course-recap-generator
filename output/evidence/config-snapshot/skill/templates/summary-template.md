# Course Summary Template

Use this template for `output/draft/course-summary.md`. Replace every
`{placeholder}` with content traced to `work/course-content.json`.

```markdown
# {Course title} — Course Recap

- **Source:** {file name from the `file` field}
- **Pages:** {page_count}
- **Generated:** {date}

## 1. Course overview

{3–5 sentences summarizing what the course covers. Base this on the
document title/subject metadata and the outline.}

## 2. Learning objectives

- {objective 1}
- {objective 2}
- {objective 3}

{Only include objectives stated or clearly implied by the source.}

## 3. Module-by-module recap

### {Module title} (pages {start}–{end})

**Topics:**

- {topic}

**Key takeaways:**

- {takeaway}

{Repeat per module, using the outline entries as the module list.}

## 4. Glossary

| Term | Definition | Source page(s) |
| --- | --- | --- |
| {term} | {definition} | {page(s)} |

## 5. Self-check questions

1. {question 1}
2. {question 2}
3. {question 3}

---

*Fidelity note: every section above cites the source pages it was
derived from. Anything not present in the extraction is marked
"not covered in source".*
```

## Rules

- One module section per top-level outline entry; merge nested outline
  entries into their parent module as sub-sections.
- If the outline is empty, derive modules from the per-page text instead
  and state that in the summary.
- Keep the summary proportional to the source: roughly one paragraph per
  2–3 source pages.
- Preserve the source's terminology; do not rename concepts.
