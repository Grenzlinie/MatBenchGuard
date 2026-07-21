from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from tests.test_materials_benchmark_review_core import (
    SOURCE_PACKAGE,
    copy_source_package,
)


REPO_ROOT = Path(__file__).resolve().parents[1]

def external_audit_dir(package: Path) -> Path:
    paper_id = (
        package.name[len("paper-"):]
        if package.name.startswith("paper-")
        else package.name
    )
    path = package.parent / "review_outputs" / paper_id / "benchmark_audit"
    path.mkdir(parents=True, exist_ok=True)
    return path


RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "run_review.py"
)


class ResourceHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        body = b"not found" if self.path == "/missing" else b"direct input"
        self.send_response(404 if self.path == "/missing" else 200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        return


class LocalResourceServer:
    def __enter__(self) -> str:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), ResourceHandler)
        self.thread = threading.Thread(
            target=self.server.serve_forever, daemon=True
        )
        self.thread.start()
        host, port = self.server.server_address
        return f"http://{host}:{port}"

    def __exit__(self, *args: object) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)


def run_review(package: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--allow-private-network",
            "--resource-timeout",
            "1",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBenchmarkResourcesTests(unittest.TestCase):
    def test_only_indispensable_direct_instruction_input_is_verified(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\nThe indispensable direct input has no equivalent source and "
                + f"must be downloaded from {base}/missing.\n",
                encoding="utf-8",
            )

            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            audit_dir = external_audit_dir(package)
            checks = json.loads(
                (audit_dir / "resource_checks.json").read_text(encoding="utf-8")
            )
            self.assertEqual(len(checks["resources"]), 1)
            direct = checks["resources"][0]
            self.assertEqual(direct["declaration_source"], "instruction.md")
            self.assertTrue(direct["indispensable"])
            self.assertEqual(direct["status"], "PERMANENT_UNAVAILABLE")
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            gates = {
                item["gate_id"]: item["status"] for item in report["gate_results"]
            }
            self.assertEqual(gates["DIRECT_INPUT_AVAILABILITY"], "FAIL")

    def test_resources_metadata_is_not_reviewed_or_scored(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "resources.json").write_text(
                json.dumps(
                    {
                        "resources": [
                            {
                                "id": "obsolete",
                                "role": "CRITICAL",
                                "access": {
                                    "method": "url",
                                    "url": "http://127.0.0.1:1/unreachable",
                                },
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            checks = json.loads(
                (
                    external_audit_dir(package) / "resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(checks["resources"], [])
            report = json.loads(
                (
                    external_audit_dir(package) / "audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertNotIn(
                "resource_availability",
                json.dumps(report["dimensions_v11"]),
            )

    def test_equivalent_software_and_solver_parameters_are_not_direct_inputs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\nUse VASP, QE, or a scientifically equivalent solver. Choose "
                "converged cutoff and k-mesh parameters for the requested endpoint.\n",
                encoding="utf-8",
            )

            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            checks = json.loads(
                (
                    external_audit_dir(package) / "resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(checks["resources"], [])
            self.assertEqual(checks["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
