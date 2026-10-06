r"""Phase 3 verification for the pdf_extractor MCP server.

Boots the REAL server as a subprocess over the MCP stdio transport using the
official MCP client SDK, then exercises both tools — including failure paths.
Nothing is mocked: the process under test is mcp-servers/pdf-extractor/server.py.

Run with the project virtualenv:
    .venv\Scripts\python tests/test_pdf_extractor.py
"""

import asyncio
import json
import shutil
import sys
import tempfile
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVER = PROJECT_ROOT / "mcp-servers" / "pdf-extractor" / "server.py"
FIXTURE = PROJECT_ROOT / "tests" / "fixtures" / "sample.pdf"

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition, detail: str = "") -> None:
    CHECKS.append((name, bool(condition), detail))
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))


async def call_tool(session: ClientSession, name: str, arguments: dict):
    """Call a tool; return (parsed_json, None) or (None, error_text)."""
    try:
        result = await session.call_tool(name, arguments)
    except Exception as exc:  # some SDK versions raise ToolError directly
        return None, f"{type(exc).__name__}: {exc}"
    text = "".join(
        getattr(chunk, "text", "") for chunk in (result.content or [])
    )
    if getattr(result, "isError", False):
        return None, text
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, f"non-JSON tool output: {text[:200]}"


async def main() -> int:
    check("server script exists", SERVER.is_file(), str(SERVER))
    check("fixture PDF exists", FIXTURE.is_file(), str(FIXTURE))
    if not (SERVER.is_file() and FIXTURE.is_file()):
        print("\n0/2 preconditions passed — aborting")
        return 1

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Tool discovery over the MCP protocol
            listed = await session.list_tools()
            tool_names = {tool.name for tool in listed.tools}
            check(
                "tool advertised: extract_pdf_text",
                "extract_pdf_text" in tool_names,
                ", ".join(sorted(tool_names)),
            )
            check(
                "tool advertised: get_pdf_outline",
                "get_pdf_outline" in tool_names,
            )

            # 2. Genuine extraction work
            data, err = await call_tool(
                session, "extract_pdf_text", {"path": str(FIXTURE)}
            )
            check("extract_pdf_text succeeds on fixture", data is not None, str(err))
            if data:
                check("result ok=true", data.get("ok") is True)
                check(
                    "page_count > 0",
                    data.get("page_count", 0) > 0,
                    f"page_count={data.get('page_count')}",
                )
                check("pages list non-empty", len(data.get("pages", [])) > 0)
                check(
                    "total_chars > 0",
                    data.get("total_chars", 0) > 0,
                    f"total_chars={data.get('total_chars')}",
                )
                check("metadata is a dict", isinstance(data.get("metadata"), dict))
                check(
                    "every page has text",
                    all("text" in page for page in data.get("pages", [])),
                )

            # 3. Outline extraction
            outline, err = await call_tool(
                session, "get_pdf_outline", {"path": str(FIXTURE)}
            )
            check("get_pdf_outline succeeds on fixture", outline is not None, str(err))
            if outline:
                check("result ok=true", outline.get("ok") is True)
                check("outline is a list", isinstance(outline.get("outline"), list))

            # 4. Failure path: missing file
            data, err = await call_tool(
                session,
                "extract_pdf_text",
                {"path": str(PROJECT_ROOT / "does-not-exist.pdf")},
            )
            check("missing file rejected", data is None and bool(err), str(err)[:120])

            # 5. Failure path: non-PDF file
            data, err = await call_tool(
                session,
                "extract_pdf_text",
                {"path": str(PROJECT_ROOT / "opencode.jsonc")},
            )
            check("non-PDF rejected", data is None and bool(err), str(err)[:120])

            # 6. Failure path: path outside the project directory
            with tempfile.TemporaryDirectory() as tmp:
                outside = Path(tmp) / "outside.pdf"
                shutil.copy(FIXTURE, outside)
                data, err = await call_tool(
                    session, "extract_pdf_text", {"path": str(outside)}
                )
                check(
                    "outside-project path rejected",
                    data is None and bool(err),
                    str(err)[:120],
                )

    failed = [name for name, ok, _ in CHECKS if not ok]
    print(f"\n{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
