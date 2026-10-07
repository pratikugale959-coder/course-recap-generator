r"""Course Recap Generator — local web app (stdlib-only HTTP server).

Endpoints:
  GET  /           → upload UI (index.html)
  POST /generate   → raw PDF bytes → JSON recap (deterministic)
  GET  /health     → liveness check

Run with the project virtualenv:
    .venv\Scripts\python webapp\server.py [port]

Default port: 8000. Binds to 127.0.0.1 (localhost) only.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from recap_core import extract_pdf, generate_recap

WEBAPP_ROOT = Path(__file__).resolve().parent
INDEX_HTML = (WEBAPP_ROOT / "index.html").read_text(encoding="utf-8")
MAX_UPLOAD_BYTES = 25 * 1024 * 1024


class Handler(BaseHTTPRequestHandler):
    # ------------------------------------------------------------- GET
    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self._send(200, "text/html; charset=utf-8", INDEX_HTML.encode("utf-8"))
        elif self.path == "/health":
            self._send_json(200, {"ok": True, "service": "course-recap-webapp"})
        else:
            self.send_error(404)

    # ------------------------------------------------------------ POST
    def do_POST(self) -> None:
        if self.path != "/generate":
            self.send_error(404)
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            length = 0
        if length == 0 or length > MAX_UPLOAD_BYTES:
            self._send_json(413, {
                "ok": False,
                "error": "empty upload or file too large (max 25 MB)",
            })
            return

        data = self.rfile.read(length)
        if not data.startswith(b"%PDF"):
            self._send_json(400, {
                "ok": False,
                "error": "uploaded file does not look like a PDF "
                         "(missing %PDF header)",
            })
            return

        filename = self.headers.get("X-File-Name", "uploaded.pdf")
        fd, tmp_name = tempfile.mkstemp(suffix=".pdf")
        tmp_path = Path(tmp_name)
        try:
            os.write(fd, data)
            os.close(fd)
            extraction = extract_pdf(tmp_path)
            recap = generate_recap(extraction, filename=filename)
            self._send_json(200, recap)
        except ValueError as exc:
            self._send_json(400, {"ok": False, "error": str(exc)})
        except Exception as exc:  # unexpected — report, don't crash
            self._send_json(500, {"ok": False, "error": f"generation failed: {exc}"})
        finally:
            tmp_path.unlink(missing_ok=True)

    # ----------------------------------------------------------- helpers
    def _send(self, status: int, content_type: str, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: int, payload: dict) -> None:
        self._send(
            status,
            "application/json; charset=utf-8",
            json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        )

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("[webapp] " + (fmt % args) + "\n")


def main(port: int = 8000) -> None:
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Course Recap web app → http://localhost:{port}/  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
