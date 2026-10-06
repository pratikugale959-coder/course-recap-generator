# pdf_extractor — MCP server

A real Model Context Protocol server used by the Course Recap Generator.
OpenCode launches it as a **local stdio server** (see `opencode.jsonc` →
`mcp.servers.pdf_extractor`). It performs the project's genuine core work:
parsing course PDFs and extracting structured content.

## Tools

### `extract_pdf_text(path)`
Extracts per-page text and document metadata from a course PDF.

- **Input:** `path` — absolute or project-relative path to a PDF inside the
  project directory.
- **Output (JSON):**
  ```json
  {
    "ok": true,
    "file": "C:\\...\\input\\course.pdf",
    "page_count": 12,
    "metadata": { "title": "...", "author": "..." },
    "total_chars": 45231,
    "warnings": ["page 7: little or no extractable text (likely image-only/scanned)"],
    "pages": [ { "page": 1, "char_count": 3200, "text": "..." }, "..." ]
  }
  ```
  Pages with fewer than 20 extractable characters are flagged as likely
  image-only/scanned.

### `get_pdf_outline(path)`
Extracts the PDF bookmark/outline (table of contents).

- **Input:** `path` — same rules as above.
- **Output (JSON):**
  ```json
  {
    "ok": true,
    "file": "C:\\...\\input\\course.pdf",
    "page_count": 12,
    "entry_count": 8,
    "warning": null,
    "outline": [ { "title": "Module 1: ...", "page": 1, "depth": 0 }, "..." ]
  }
  ```
  `page` is 1-based (null when it cannot be determined).

## Setup

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

The venv path matters: `opencode.jsonc` launches the server with
`.venv\Scripts\python.exe`.

## Verify

```powershell
# Protocol-level integration test (boots the real server over stdio)
.venv\Scripts\python tests/test_pdf_extractor.py

# OpenCode connection check — expect: ✓ pdf_extractor connected
cmd /c "C:\Users\Sarthak\AppData\Roaming\npm\node_modules\@opencode\cli-windows-x64\bin\opencode.exe mcp list"
```

## Security boundary

The server only reads PDF files inside the course-recap-generator project
directory. It rejects missing files, non-file paths, non-PDF files, corrupted
PDFs, PDFs locked with a non-empty password, and any path outside the project
root. PDFs with owner-password-only restrictions (empty user password) are
readable.

## Dependencies

- `mcp` — official Model Context Protocol Python SDK (FastMCP, stdio transport)
- `pypdf` — pure-Python PDF parsing
