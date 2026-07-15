from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_paper_grounded import (
    REPO_ROOT,
    copy_source_package,
)
from tests.test_materials_disposition import run_no_paper


REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
INLINE_QUOTE = "c11 = 1.68×10¹² dynes/cm²"
EVIDENCE = [{"file": "instruction.md", "quote": INLINE_QUOTE}]


def write_plan(path: Path, audit_id: str, finding_id: str) -> None:
    path.write_text(
        json.dumps(
            {
                "schema_version": "0.1",
                "audit_id": audit_id,
                "finding_id": finding_id,
                "repair_class": "SAFE_AUTO_FIX",
                "justification": (
                    "The resource is already fully embedded in the public "
                    "instruction; this records exact provenance only."
                ),
                "operations": [
                    {
                        "type": "json_set",
                        "file": "resources.json",
                        "path": ["resources", 0, "access", "evidence"],
                        "value": EVIDENCE,
                    }
                ],
                "regression_tests": [
                    {
                        "type": "json_path_equals",
                        "file": "resources.json",
                        "path": ["resources", 0, "access", "evidence"],
                        "expected": EVIDENCE,
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def run_repair(package: Path, plan: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPAIR_RUNNER), str(package), "--plan", str(plan)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )


def initial_repair_context(
    workspace: Path,
) -> tuple[Path, dict[str, object], str]:
    package = workspace / "paper-fixture"
    copy_source_package(package)
    completed = run_no_paper(package)
    if completed.returncode != 0:
        raise AssertionError(completed.stderr)
    report = json.loads(
        (package / "benchmark_audit/audit_report.json").read_text(
            encoding="utf-8"
        )
    )
    finding = next(
        item
        for item in report["findings"]
        if item["title"] == "RESOURCE_VERIFICATION_INSUFFICIENT"
    )
    return package, report, finding["finding_id"]


class MaterialsSafeRepairTests(unittest.TestCase):
    def test_safe_fix_reaudits_and_atomically_publishes_full_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id = initial_repair_context(workspace)
            self.assertEqual(
                report["summary"]["disposition"], "REPAIR_QUEUE"
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, report["audit_id"], finding_id)
            before_hash = hashlib.sha256(
                (package / "resources.json").read_bytes()
            ).hexdigest()

            completed = run_repair(package, plan)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            repaired_report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            repair_manifest = json.loads(
                (
                    package / "benchmark_repair/repair_manifest.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                repaired_report["summary"]["final_verdict"], "PASS"
            )
            self.assertEqual(
                repaired_report["summary"]["disposition"],
                "PUBLISH_CANDIDATE",
            )
            self.assertEqual(repair_manifest["status"], "PUBLISHED")
            self.assertEqual(repair_manifest["finding_id"], finding_id)
            self.assertNotEqual(
                repair_manifest["changes"][0]["before_hash"],
                repair_manifest["changes"][0]["after_hash"],
            )
            self.assertEqual(
                repair_manifest["changes"][0]["before_hash"],
                "sha256:" + before_hash,
            )
            regression = repair_manifest["regression_tests"][0]
            self.assertFalse(regression["before_passed"])
            self.assertTrue(regression["after_passed"])
            self.assertEqual(
                repair_manifest["reaudit"]["execution_level"], "E1"
            )
            self.assertEqual(
                repair_manifest["reaudit"]["paper_mode"], "no_paper"
            )
            history = Path(result["history_dir"])
            self.assertTrue((history / "snapshot").is_dir())
            self.assertTrue((history / "original").is_dir())
            self.assertTrue((package / "solution").is_dir())
            self.assertEqual(package.name, "paper-fixture")

    def test_stale_audit_is_rejected_before_repair_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id = initial_repair_context(workspace)
            plan = workspace / "repair-plan.json"
            write_plan(plan, report["audit_id"], finding_id)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8") + "\nchanged\n",
                encoding="utf-8",
            )
            resources_hash = hashlib.sha256(
                (package / "resources.json").read_bytes()
            ).hexdigest()

            completed = run_repair(package, plan)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("stale audit", completed.stderr)
            self.assertEqual(
                resources_hash,
                hashlib.sha256(
                    (package / "resources.json").read_bytes()
                ).hexdigest(),
            )
            self.assertFalse((package / "benchmark_repair").exists())


if __name__ == "__main__":
    unittest.main()
