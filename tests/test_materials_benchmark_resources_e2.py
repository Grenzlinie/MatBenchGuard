from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from tests.test_materials_benchmark_review_e1 import (
    SOURCE_PACKAGE,
    copy_source_package,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "run_review.py"
)
PSEUDO_BYTES = b"Si pseudopotential fixture\n"
CIF_BYTES = b"data_mp_123\n_cell_length_a 5.43\n"


class ResourceHandler(BaseHTTPRequestHandler):
    def do_HEAD(self) -> None:  # noqa: N802
        self._respond(include_body=False)

    def do_GET(self) -> None:  # noqa: N802
        self._respond(include_body=True)

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _respond(self, *, include_body: bool) -> None:
        routes = {
            "/": (200, b"materials resource homepage\n", "text/html"),
            "/pseudo/Si.psf": (
                200,
                PSEUDO_BYTES,
                "application/octet-stream",
            ),
            "/empty": (200, b"", "application/octet-stream"),
            "/structures/mp-123.json": (
                200,
                b'{"material_id":"mp-123","formula":"Si"}',
                "application/json",
            ),
            "/structures/mp-123.cif": (
                200,
                CIF_BYTES,
                "chemical/x-cif",
            ),
            "/package/ase": (
                200,
                b'{"name":"ase","version":"3.26.0"}',
                "application/json",
            ),
            "/private": (403, b"authentication required", "text/plain"),
            "/missing": (404, b"not found", "text/plain"),
            "/rate": (429, b"rate limited", "text/plain"),
        }
        status, body, content_type = routes.get(
            self.path,
            (404, b"not found", "text/plain"),
        )
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if include_body:
            self.wfile.write(body)


class LocalResourceServer:
    def __enter__(self) -> str:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), ResourceHandler)
        self.thread = threading.Thread(
            target=self.server.serve_forever,
            daemon=True,
        )
        self.thread.start()
        host, port = self.server.server_address
        return f"http://{host}:{port}"

    def __exit__(self, *args: object) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)


def resource_fixture(base_url: str) -> dict[str, object]:
    return {
        "version": 1,
        "resources": [
            {
                "id": "tool_homepage",
                "name": "SIESTA",
                "type": "tool",
                "role": "REPLACEABLE",
                "access": {"method": "url", "url": f"{base_url}/"},
            },
            {
                "id": "si_pseudopotential",
                "name": "Si pseudopotential",
                "type": "pseudopotential",
                "role": "CRITICAL",
                "required_level": "L5",
                "access": {
                    "method": "url",
                    "url": f"{base_url}/pseudo/Si.psf",
                    "checksum": "sha256:"
                    + hashlib.sha256(PSEUDO_BYTES).hexdigest(),
                    "version": "fixture-v1",
                    "compatibility": "test-only silicon calculation",
                },
            },
            {
                "id": "silicon_structure",
                "name": "Materials Project structure mp-123",
                "type": "structure",
                "role": "CRITICAL",
                "required_level": "L4",
                "access": {
                    "method": "accession",
                    "accession": "mp-123",
                    "metadata_url": f"{base_url}/structures/mp-123.json",
                    "artifact_url": f"{base_url}/structures/mp-123.cif",
                },
            },
            {
                "id": "ase",
                "name": "Atomic Simulation Environment",
                "type": "package",
                "role": "REPLACEABLE",
                "access": {
                    "method": "package",
                    "package": "ase",
                    "registry_url": f"{base_url}/package/ase",
                    "version": "",
                },
            },
            {
                "id": "commercial_solver",
                "name": "VASP",
                "type": "commercial_software",
                "role": "CRITICAL",
                "access": {
                    "method": "license",
                    "license": "commercial",
                    "authorization_provided": False,
                },
            },
            {
                "id": "missing_artifact",
                "name": "Missing potential",
                "type": "potential",
                "role": "CRITICAL",
                "access": {
                    "method": "url",
                    "url": f"{base_url}/missing",
                },
            },
            {
                "id": "private_basis",
                "name": "Private basis set",
                "type": "basis_set",
                "role": "CRITICAL",
                "access": {
                    "method": "url",
                    "url": f"{base_url}/private",
                },
            },
            {
                "id": "rate_limited_database",
                "name": "Rate-limited materials database",
                "type": "materials_database",
                "role": "REPLACEABLE",
                "access": {
                    "method": "url",
                    "url": f"{base_url}/rate",
                },
            },
            {
                "id": "transient_endpoint",
                "name": "Transient endpoint",
                "type": "file",
                "role": "REPLACEABLE",
                "access": {
                    "method": "url",
                    "url": "http://127.0.0.1:1/unreachable",
                },
            },
        ],
    }


def run_review(
    package: Path,
    execution_level: str,
    smoke_plan: Path | None = None,
    *,
    allow_private_network: bool = True,
) -> subprocess.CompletedProcess[str]:
    command = [
        sys.executable,
        str(RUNNER),
        str(package),
        "--paper-mode",
        "no_paper",
        "--execution-level",
        execution_level,
        "--resource-timeout",
        "1",
    ]
    if smoke_plan is not None:
        command.extend(["--e2-smoke-plan", str(smoke_plan)])
    if allow_private_network:
        command.append("--allow-private-network")
    return subprocess.run(
        command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBenchmarkResourcesE2Tests(unittest.TestCase):
    def test_e1_distinguishes_resource_levels_and_failure_classes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "resources.json").write_text(
                json.dumps(resource_fixture(base), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_review(package, "E1")

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
            resources = json.loads(
                (audit_dir / "resource_checks.json").read_text(encoding="utf-8")
            )
            by_id = {
                item["resource_id"]: item for item in resources["resources"]
            }
            self.assertEqual(
                by_id["tool_homepage"]["verified_level"], "L1"
            )
            self.assertEqual(
                by_id["si_pseudopotential"]["verified_level"], "L5"
            )
            self.assertTrue(
                by_id["si_pseudopotential"]["identity_match"]
            )
            self.assertEqual(
                by_id["silicon_structure"]["verified_level"], "L4"
            )
            self.assertEqual(by_id["ase"]["verified_level"], "L2")
            self.assertEqual(
                by_id["commercial_solver"]["status"],
                "REQUIRES_LICENSE",
            )
            self.assertEqual(
                by_id["missing_artifact"]["status"],
                "PERMANENT_UNAVAILABLE",
            )
            self.assertEqual(
                by_id["private_basis"]["status"], "REQUIRES_AUTH"
            )
            self.assertEqual(
                by_id["rate_limited_database"]["status"], "RATE_LIMITED"
            )
            self.assertEqual(
                by_id["transient_endpoint"]["status"], "TRANSIENT_FAILURE"
            )
            finding_codes = {
                item["code"] for item in resources["findings"]
            }
            self.assertTrue(
                {
                    "RESOURCE_HOMEPAGE_ONLY",
                    "UNPINNED_PACKAGE",
                    "COMMERCIAL_LICENSE_UNAVAILABLE",
                    "CRITICAL_RESOURCE_UNAVAILABLE",
                    "RESOURCE_REQUIRES_AUTH",
                }.issubset(finding_codes)
            )
            self.assertTrue(resources["summary"]["e2_recommended"])

    def test_checksum_mismatch_is_identity_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = resource_fixture(base)
            pseudo = data["resources"][1]
            pseudo["access"]["checksum"] = "sha256:" + "0" * 64
            (package / "resources.json").write_text(
                json.dumps(data, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_review(package, "E1")

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            by_id = {
                item["resource_id"]: item for item in resources["resources"]
            }
            self.assertEqual(
                by_id["si_pseudopotential"]["status"],
                "IDENTITY_MISMATCH",
            )
            self.assertFalse(
                by_id["si_pseudopotential"]["identity_match"]
            )
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")

    def test_e2_smoke_records_environment_evidence_without_reproduction_claim(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = resource_fixture(base)
            data["resources"] = [data["resources"][1]]
            data["resources"][0]["required_level"] = "L6"
            (package / "resources.json").write_text(
                json.dumps(data, ensure_ascii=False),
                encoding="utf-8",
            )
            smoke_script = workspace / "smoke.py"
            smoke_script.write_text(
                "import json\n"
                "from pathlib import Path\n"
                "assert Path('instruction.md').is_file()\n"
                "Path('e2_smoke_result.json').write_text("
                "json.dumps({'exercised_resources': ['si_pseudopotential']}), "
                "encoding='utf-8')\n"
                "print('materials-smoke-ok')\n",
                encoding="utf-8",
            )
            smoke_plan = workspace / "e2-smoke-plan.json"
            smoke_plan.write_text(
                json.dumps(
                    {
                        "schema_version": "0.1",
                        "script": smoke_script.name,
                        "verifies_resources": ["si_pseudopotential"],
                        "timeout_sec": 10,
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(package, "E2", smoke_plan)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["configuration"]["execution_level"], "E2")
            evidence = report["execution_evidence"]
            self.assertEqual(evidence["status"], "PASS")
            self.assertEqual(evidence["claim"], "SMOKE_RUN")
            self.assertFalse(evidence["scientific_reproduction"])
            self.assertIn("materials-smoke-ok", evidence["stdout"])
            resources = json.loads(
                (audit_dir / "resource_checks.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                resources["resources"][0]["verified_level"], "L5"
            )
            self.assertFalse(
                resources["resources"][0]["environment_verified"]
            )
            markdown = (audit_dir / "audit_report.md").read_text(
                encoding="utf-8"
            )
            execution_section = markdown.split(
                "## 12. Execution Feasibility", 1
            )[1].split("## 13.", 1)[0]
            self.assertIn("E2_SMOKE", execution_section)
            self.assertIn("does not establish scientific reproduction", execution_section)

    def test_critical_underverification_creates_a_resource_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = resource_fixture(base)
            pseudo = data["resources"][1]
            del pseudo["access"]["checksum"]
            data["resources"] = [pseudo]
            (package / "resources.json").write_text(
                json.dumps(data, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_review(package, "E1")

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(resources["resources"][0]["verified_level"], "L4")
            self.assertIn(
                "RESOURCE_VERIFICATION_INSUFFICIENT",
                {item["code"] for item in resources["findings"]},
            )
            self.assertEqual(resources["status"], "WARNING")

    def test_empty_artifact_is_discovered_but_not_downloadable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = {
                "resources": [
                    {
                        "id": "empty_potential",
                        "name": "Empty potential",
                        "type": "potential",
                        "role": "CRITICAL",
                        "required_level": "L4",
                        "access": {
                            "method": "url",
                            "url": f"{base}/empty",
                            "version": "fixture-v1",
                            "compatibility": "test-only",
                        },
                    }
                ]
            }
            (package / "resources.json").write_text(
                json.dumps(data), encoding="utf-8"
            )

            completed = run_review(package, "E1")

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(resources["resources"][0]["verified_level"], "L3")
            self.assertIn(
                "RESOURCE_VERIFICATION_INSUFFICIENT",
                {item["code"] for item in resources["findings"]},
            )

    def test_package_version_mismatch_is_identity_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = resource_fixture(base)
            package_resource = data["resources"][3]
            package_resource["access"]["version"] = "0.0.0"
            data["resources"] = [package_resource]
            (package / "resources.json").write_text(
                json.dumps(data), encoding="utf-8"
            )

            completed = run_review(package, "E1")

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                resources["resources"][0]["status"], "IDENTITY_MISMATCH"
            )

    def test_inline_declaration_without_public_evidence_stays_l0(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "resources.json").write_text(
                json.dumps(
                    {
                        "resources": [
                            {
                                "id": "inline_constants",
                                "name": "Inline constants",
                                "type": "file",
                                "role": "CRITICAL",
                                "access": {"method": "inline"},
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(package, "E1")

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(resources["resources"][0]["verified_level"], "L0")
            self.assertIn(
                "RESOURCE_VERIFICATION_INSUFFICIENT",
                {item["code"] for item in resources["findings"]},
            )

    def test_missing_resources_still_publishes_static_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "resources.json").unlink()

            completed = run_review(package, "E1")

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
            resources = json.loads(
                (audit_dir / "resource_checks.json").read_text(encoding="utf-8")
            )
            self.assertEqual(resources["status"], "NOT_ASSESSED")
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertIn(
                "MISSING_FILE",
                {item["title"] for item in report["findings"]},
            )

    def test_private_network_resource_is_blocked_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "resources.json").write_text(
                json.dumps(
                    {
                        "resources": [
                            {
                                "id": "private_artifact",
                                "name": "Private artifact",
                                "type": "file",
                                "role": "CRITICAL",
                                "access": {
                                    "method": "url",
                                    "url": f"{base}/pseudo/Si.psf",
                                },
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(
                package,
                "E1",
                allow_private_network=False,
            )

            self.assertEqual(completed.returncode, 0)
            resources = json.loads(
                (
                    package / "benchmark_audit/resource_checks.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                resources["resources"][0]["status"],
                "BLOCKED_PRIVATE_NETWORK",
            )

    def test_failed_e2_smoke_creates_hard_gate_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            data = resource_fixture(base)
            data["resources"] = [data["resources"][1]]
            (package / "resources.json").write_text(
                json.dumps(data), encoding="utf-8"
            )
            smoke_script = workspace / "smoke.py"
            smoke_script.write_text(
                "raise SystemExit(3)\n",
                encoding="utf-8",
            )
            smoke_plan = workspace / "e2-smoke-plan.json"
            smoke_plan.write_text(
                json.dumps(
                    {
                        "script": smoke_script.name,
                        "verifies_resources": ["si_pseudopotential"],
                        "timeout_sec": 10,
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(package, "E2", smoke_plan)

            self.assertEqual(completed.returncode, 0)
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["execution_evidence"]["status"], "FAIL")
            self.assertIn(
                "E2_SMOKE_FAILED",
                {item["title"] for item in report["findings"]},
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")

    def test_e2_smoke_cannot_read_original_solution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, LocalResourceServer() as base:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            secret_path = package / "solution/secret.txt"
            secret_path.write_text("hidden-answer", encoding="utf-8")
            data = resource_fixture(base)
            data["resources"] = [data["resources"][1]]
            (package / "resources.json").write_text(
                json.dumps(data), encoding="utf-8"
            )
            smoke_script = workspace / "smoke.py"
            smoke_script.write_text(
                "import json\n"
                "from pathlib import Path\n"
                f"print(Path({str(secret_path)!r}).read_text())\n"
                "Path('e2_smoke_result.json').write_text("
                "json.dumps({'exercised_resources': ['si_pseudopotential']}), "
                "encoding='utf-8')\n",
                encoding="utf-8",
            )
            smoke_plan = workspace / "e2-smoke-plan.json"
            smoke_plan.write_text(
                json.dumps(
                    {
                        "script": smoke_script.name,
                        "verifies_resources": ["si_pseudopotential"],
                        "timeout_sec": 10,
                    }
                ),
                encoding="utf-8",
            )

            completed = run_review(package, "E2", smoke_plan)

            self.assertEqual(completed.returncode, 0)
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            evidence = report["execution_evidence"]
            self.assertEqual(evidence["status"], "FAIL")
            self.assertNotIn("hidden-answer", evidence["stdout"])
            self.assertNotIn("hidden-answer", evidence["stderr"])


if __name__ == "__main__":
    unittest.main()
