"""pdf_extractor — MCP server for the Course Recap Generator.

A real Model Context Protocol server (stdio transport, official `mcp` SDK)
that performs the genuine PDF extraction work this project exists for.

Tools:
  * extract_pdf_text(path)  — per-page text, document metadata, char counts,
                                scanned-page warnings
  * get_pdf_outline(path)   — normalized bookmark/outline (table of contents)

Security boundary: the server only reads PDF files located inside the
course-recap-generator project directory.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCANNED_PAGE_CHAR_THRESHOLD = 20

mcp = FastMCP(
    "pdf_extractor",
    instructions=(
        "Extracts text, metadata, and the outline/bookmarks from course PDF "
        "files located inside the course-recap-generator project directory."
    ),
)


def _resolve_safe_path(path: str) -> Path:
    """Validate that *path* is a PDF file inside the project directory."""
    if not path or not path.strip():
        raise ValueError("path is required")
    candidate = Path(path.strip()).expanduser()
    if not candidate.is_absolute():
        candidate = PROJECT_ROOT / candidate
    candidate = candidate.resolve()
    if not candidate.exists():
        raise ValueError(f"file not found: {candidate}")
    if not candidate.is_file():
        raise ValueError(f"not a file: {candidate}")
    try:
        candidate.relative_to(PROJECT_ROOT)
    except ValueError:
        raise ValueError(
            f"access denied: {candidate} is outside the project directory "
            f"({PROJECT_ROOT})"
        )
    if candidate.suffix.lower() != ".pdf":
        raise ValueError(f"not a PDF file: {candidate}")
    return candidate


def _read_pdf(path: Path) -> PdfReader:
    try:
        reader = PdfReader(str(path))
    except Exception as exc:  # malformed / corrupted PDF
        raise ValueError(f"could not parse PDF: {exc}") from exc
    if getattr(reader, "is_encrypted", False):
        # Many PDFs carry an empty user password (owner-password-only
        # restrictions). Those open normally — try the empty password
        # and reject only when the content stays locked.
        try:
            reader.decrypt("")
        except Exception:
            pass
        try:
            len(reader.pages)  # readability probe
        except Exception as exc:
            raise ValueError(
                f"PDF is encrypted and cannot be read: {path}"
            ) from exc
    return reader


def _normalize_metadata(metadata: Any) -> dict:
    """Flatten pypdf document information into a plain {key: string} dict."""
    if not metadata:
        return {}
    normalized: dict[str, str] = {}
    for raw_key, value in dict(metadata).items():
        key = str(raw_key).lstrip("/").lower()
        normalized[key] = str(value)
    return normalized


def _walk_outline(items: Any, reader: PdfReader, depth: int = 0) -> list[dict]:
    """Recursively flatten pypdf's nested outline into a flat entry list."""
    entries: list[dict] = []
    for item in items or []:
        if isinstance(item, list):
            entries.extend(_walk_outline(item, reader, depth + 1))
            continue
        title = getattr(item, "title", None)
        if not title:
            continue
        page_number: int | None = None
        try:
            page_number = reader.get_destination_page_number(item) + 1  # 1-based
        except Exception:
            page_number = None
        entries.append({"title": str(title), "page": page_number, "depth": depth})
    return entries


@mcp.tool()
def extract_pdf_text(path: str) -> dict:
    """Extract per-page text and document metadata from a course PDF.

    Args:
        path: Absolute or project-relative path to a PDF inside the project.

    Returns:
        JSON object with page_count, metadata, total_chars, warnings, and a
        per-page list of {page, char_count, text}. Pages with little or no
        extractable text are flagged as likely image-only/scanned.
    """
    pdf_path = _resolve_safe_path(path)
    reader = _read_pdf(pdf_path)

    pages: list[dict] = []
    warnings: list[str] = []
    total_chars = 0

    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        char_count = len(text.strip())
        total_chars += char_count
        entry = {"page": index, "char_count": char_count, "text": text}
        if char_count < SCANNED_PAGE_CHAR_THRESHOLD:
            warning = (
                f"page {index}: little or no extractable text "
                "(likely image-only/scanned)"
            )
            entry["warning"] = warning
            warnings.append(warning)
        pages.append(entry)

    return {
        "ok": True,
        "file": str(pdf_path),
        "page_count": len(reader.pages),
        "metadata": _normalize_metadata(reader.metadata),
        "total_chars": total_chars,
        "warnings": warnings,
        "pages": pages,
    }


@mcp.tool()
def get_pdf_outline(path: str) -> dict:
    """Extract the PDF bookmark/outline (table of contents) of a course PDF.

    Args:
        path: Absolute or project-relative path to a PDF inside the project.

    Returns:
        JSON object with a flat outline list of {title, page, depth} entries.
        The page field is 1-based (null when it cannot be determined).
    """
    pdf_path = _resolve_safe_path(path)
    reader = _read_pdf(pdf_path)

    try:
        outline = _walk_outline(reader.outline, reader)
        outline_warning = None
    except Exception as exc:
        outline = []
        outline_warning = f"outline could not be read: {exc}"

    return {
        "ok": True,
        "file": str(pdf_path),
        "page_count": len(reader.pages),
        "entry_count": len(outline),
        "warning": outline_warning,
        "outline": outline,
    }


if __name__ == "__main__":
    mcp.run()  # stdio transport (default)
