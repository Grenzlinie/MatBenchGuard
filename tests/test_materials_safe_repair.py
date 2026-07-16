from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
AUDIT_ID = "audit-source-001"
FINDING_ID = "finding-missing-solve"


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def install_repair_harness(workspace: Path) -> Path:
    harness_runner = (
        workspace
        / "harness/materials-benchmark-repair/scripts/run_repair.py"
    )
    harness_runner.parent.mkdir(parents=True)
    shutil.copy2(REPAIR_RUNNER, harness_runner)
    review_runner = (
        workspace
        / "harness/materials-benchmark-review/scripts/run_review.py"
    )
    review_runner.parent.mkdir(parents=True)
    review_runner.write_text(
        textwrap.dedent(
            """\
            import argparse
            import hashlib
            import json
            from pathlib import Path

            parser = argparse.ArgumentParser()
            parser.add_argument("root")
            parser.add_argument("--paper-mode", required=True)
            parser.add_argument("--execution-level", required=True)
            parser.add_argument("--known-valid-output")
            parser.add_argument("--agent-assessment")
            parser.add_argument("--e2-smoke-plan")
            args = parser.parse_args()
            root = Path(args.root)
            audit = root / "benchmark_audit"
            if audit.exists():
                import shutil
                shutil.rmtree(audit)
            audit.mkdir()
            report = {
                "audit_id": "audit-reaudit-001",
                "configuration": {
                    "paper_mode": args.paper_mode,
                    "execution_level": args.execution_level,
                },
                "findings": [],
                "summary": {
                    "final_verdict": "PASS",
                    "disposition": "PUBLISH_CANDIDATE",
                },
            }
            (audit / "audit_report.json").write_text(json.dumps(report))
            (audit / "disposition.json").write_text(json.dumps({
                "route": "PUBLISH_CANDIDATE",
                "verdict": "PASS",
            }))
            hashes = {}
            for relative in (
                "instruction.md",
                "tests/checker.py",
                "tests/grading_spec.json",
                "solution/solve.sh",
                "paper/paper.md",
            ):
                path = root / relative
                if path.is_file():
                    hashes[relative] = "sha256:" + hashlib.sha256(
                        path.read_bytes()
                    ).hexdigest()
            (audit / "audit_manifest.json").write_text(json.dumps({
                "audit_id": report["audit_id"],
                "benchmark_root": str(root),
                "input_hashes": hashes,
                "output_hashes": {},
            }))
            print(json.dumps(report))
            """
        ),
        encoding="utf-8",
    )
    return harness_runner


def initial_repair_context(
    workspace: Path,
) -> tuple[Path, dict[str, Any], str, Path]:
    runner = install_repair_harness(workspace)
    package = workspace / "paper-fixture"
    (package / "tests").mkdir(parents=True)
    (package / "solution").mkdir()
    (package / "paper").mkdir()
    (package / "instruction.md").write_text(
        "Compute the evidence-backed quantity.\n", encoding="utf-8"
    )
    (package / "tests/checker.py").write_text(
        "raise SystemExit(0)\n", encoding="utf-8"
    )
    write_json(package / "tests/grading_spec.json", {"pass_threshold": 0.8})
    (package / "paper/paper.md").write_text(
        "The published method computes the evidence-backed quantity.\n",
        encoding="utf-8",
    )
    write_json(package / "manifest.json", {"id": "paper-fixture"})
    report = {
        "audit_id": AUDIT_ID,
        "configuration": {"paper_mode": "no_paper", "execution_level": "E1"},
        "findings": [
            {
                "finding_id": FINDING_ID,
                "title": "SOLUTION_ENTRYPOINT_MISSING",
                "severity": "HIGH",
            }
        ],
        "summary": {
            "final_verdict": "CONDITIONAL",
            "disposition": "REPAIR_QUEUE",
        },
    }
    write_json(package / "benchmark_audit/audit_report.json", report)
    write_json(
        package / "benchmark_audit/disposition.json",
        {"route": "REPAIR_QUEUE", "verdict": "CONDITIONAL"},
    )
    input_hashes = {
        relative: sha256_file(package / relative)
        for relative in (
            "instruction.md",
            "tests/checker.py",
            "tests/grading_spec.json",
            "paper/paper.md",
            "manifest.json",
        )
    }
    write_json(
        package / "benchmark_audit/audit_manifest.json",
        {
            "audit_id": AUDIT_ID,
            "benchmark_root": str(package),
            "input_hashes": input_hashes,
            "output_hashes": {},
        },
    )
    return package, report, FINDING_ID, runner


def safe_plan(audit_id: str, finding_id: str) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "audit_id": audit_id,
        "finding_id": finding_id,
        "repair_class": "SAFE_AUTO_FIX",
        "justification": "Restore the missing deterministic solution entrypoint.",
        "core_science_change": False,
        "evidence": [
            {
                "id": "audit-finding",
                "source": f"benchmark_audit:{finding_id}",
                "quote": "SOLUTION_ENTRYPOINT_MISSING",
            }
        ],
        "operations": [
            {
                "id": "restore-solve",
                "type": "write_file",
                "file": "solution/solve.sh",
                "content": "#!/bin/sh\nexit 0\n",
                "executable": True,
                "evidence_ids": ["audit-finding"],
            }
        ],
        "regression_tests": [
            {"type": "file_exists", "file": "solution/solve.sh"},
            {
                "type": "command",
                "command": ["sh", "solution/solve.sh"],
                "expected_returncode": 0,
            },
        ],
    }


def write_plan(path: Path, value: dict[str, Any]) -> None:
    write_json(path, value)


def run_repair(
    package: Path, plan: Path, runner: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(runner), str(package), "--plan", str(plan)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


class MaterialsSafeRepairTests(unittest.TestCase):
    def test_missing_solution_entrypoint_is_repaired_and_atomically_published(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))
            manifest_before = sha256_file(package / "manifest.json")
            paper_before = sha256_file(package / "paper/paper.md")

            completed = run_repair(package, plan, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            repair_manifest = json.loads(
                (package / "benchmark_repair/repair_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(repair_manifest["status"], "PUBLISHED")
            self.assertEqual(repair_manifest["finding_id"], finding_id)
            self.assertEqual(
                [item["before_passed"] for item in repair_manifest["regression_tests"]],
                [False, False],
            )
            self.assertTrue(
                all(
                    item["after_passed"]
                    for item in repair_manifest["regression_tests"]
                )
            )
            self.assertEqual(
                repair_manifest["reaudit"]["execution_level"], "E1"
            )
            self.assertEqual(
                repair_manifest["reaudit"]["paper_mode"], "no_paper"
            )
            self.assertTrue((package / "solution/solve.sh").is_file())
            self.assertEqual(sha256_file(package / "manifest.json"), manifest_before)
            self.assertEqual(sha256_file(package / "paper/paper.md"), paper_before)
            self.assertEqual(package.name, "paper-fixture")
            history = Path(result["history_dir"])
            self.assertTrue((history / "snapshot").is_dir())
            self.assertTrue((history / "original").is_dir())
            self.assertTrue((history / "repair_plan.json").is_file())
            self.assertTrue((history / "attempt_manifest.json").is_file())

    def test_repair_rejects_targets_outside_instruction_tests_and_solution(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            value = safe_plan(report["audit_id"], finding_id)
            value["operations"][0]["file"] = "paper/paper.md"
            plan = workspace / "repair-plan.json"
            write_plan(plan, value)
            before = sha256_file(package / "paper/paper.md")

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("unsupported repair target", completed.stderr)
            self.assertEqual(sha256_file(package / "paper/paper.md"), before)

    def test_stale_audit_is_rejected_before_repair_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8") + "changed\n",
                encoding="utf-8",
            )

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("stale audit", completed.stderr)
            self.assertFalse((package / "benchmark_repair").exists())

    def test_repair_reaudit_rejects_non_e1_source_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            report["configuration"]["execution_level"] = "E2"
            write_json(package / "benchmark_audit/audit_report.json", report)
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("fixed E1", completed.stderr)
            self.assertFalse((package / "benchmark_repair").exists())


if __name__ == "__main__":
    unittest.main()
