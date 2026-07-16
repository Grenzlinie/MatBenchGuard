from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tests.test_materials_safe_repair import (
    initial_repair_context,
    run_repair,
    safe_plan,
    sha256_file,
    write_plan,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)


def repair_module() -> Any:
    spec = importlib.util.spec_from_file_location("issue21_repair", REPAIR_RUNNER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bind_plan(package: Path, plan: dict[str, Any]) -> dict[str, Any]:
    module = repair_module()
    manifest = json.loads(
        (package / "benchmark_audit/audit_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    digest = module.core_contract_digest(package)
    plan["core_contract_digest"] = digest
    plan["source_audit"] = {
        "audit_id": plan["audit_id"],
        "finding_id": plan["finding_id"],
        "finding_status": "OPEN",
        "input_hashes": manifest["input_hashes"],
        "review_implementation": manifest.get("review_implementation", {}),
        "paper_mode": "no_paper",
        "execution_level": "E1",
        "core_contract_digest": digest,
        "fixture_hashes": {},
        "assessment_hashes": {},
    }
    for item in plan["evidence"]:
        if item["source"].startswith("benchmark_audit:"):
            item["source_hash"] = sha256_file(
                package / "benchmark_audit/audit_report.json"
            )
        else:
            source_path = package / item["source"]
            if source_path.is_file():
                item["source_hash"] = sha256_file(source_path)
    return plan


def evidence(
    package: Path,
    evidence_id: str,
    source: str,
    quote: str,
    *,
    kind: str = "harbor_path",
    precision: dict[str, Any] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "id": evidence_id,
        "source": source,
        "quote": quote,
        "source_hash": (
            sha256_file(package / "benchmark_audit/audit_report.json")
            if source.startswith("benchmark_audit:")
            else sha256_file(package / source)
        ),
        "kind": kind,
    }
    if precision is not None:
        item["precision"] = precision
    return item


class MaterialsIssue21RepairSecurityTests(unittest.TestCase):
    def test_fabricated_source_is_abandoned_before_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            plan = safe_plan(report["audit_id"], finding_id)
            plan["evidence"][0]["source"] = "not-a-real-source.md"
            plan = bind_plan(package, plan)
            before = sha256_file(package / "instruction.md")
            path = Path(temporary) / "plan.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["decision"], "ABANDON")
            self.assertEqual(result["status"], "BLOCKED_EVIDENCE")
            self.assertEqual(sha256_file(package / "instruction.md"), before)
            self.assertFalse((package / "benchmark_repair").exists())

    def test_absolute_traversal_url_and_symlink_sources_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            outside = workspace / "outside.md"
            outside.write_text("SOLUTION_ENTRYPOINT_MISSING\n", encoding="utf-8")
            (package / "link.md").symlink_to(outside)

            for source in (
                str(outside),
                "../outside.md",
                "https://example.invalid/evidence",
                "link.md",
            ):
                with self.subTest(source=source):
                    plan = safe_plan(report["audit_id"], finding_id)
                    plan["evidence"][0]["source"] = source
                    plan = bind_plan(package, plan)
                    path = workspace / f"plan-{abs(hash(source))}.json"
                    write_plan(path, plan)
                    completed = run_repair(package, path, runner)
                    self.assertEqual(completed.returncode, 3)
                    self.assertEqual(
                        json.loads(completed.stdout)["status"],
                        "BLOCKED_EVIDENCE",
                    )

    def test_wrong_quote_or_hash_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            for field, value in (
                ("quote", "not present in the report"),
                ("source_hash", "sha256:" + "0" * 64),
            ):
                with self.subTest(field=field):
                    plan = bind_plan(
                        package, safe_plan(report["audit_id"], finding_id)
                    )
                    plan["evidence"][0][field] = value
                    path = Path(temporary) / f"{field}.json"
                    write_plan(path, plan)
                    completed = run_repair(package, path, runner)
                    self.assertEqual(completed.returncode, 3)
                    self.assertEqual(
                        json.loads(completed.stdout)["status"],
                        "BLOCKED_EVIDENCE",
                    )

    def test_resolved_finding_cannot_be_repaired(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            report["findings"][0]["status"] = "RESOLVED"
            (package / "benchmark_audit/audit_report.json").write_text(
                json.dumps(report), encoding="utf-8"
            )
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            path = Path(temporary) / "resolved.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["decision"], "ABANDON"
            )

    def test_method_quote_cannot_lower_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            plan = safe_plan(report["audit_id"], finding_id)
            plan["repair_class"] = "ASSISTED_FIX"
            plan["evidence"] = [
                evidence(
                    package,
                    "method",
                    "paper/paper.md",
                    "The published method computes the evidence-backed quantity.",
                    kind="scientific_method",
                    precision={"claim": "the published method"},
                )
            ]
            plan["operations"] = [
                {
                    "id": "lower-threshold",
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["pass_threshold"],
                    "value": 0.5,
                    "evidence_ids": ["method"],
                }
            ]
            plan["regression_tests"] = [
                {
                    "id": "threshold",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["lower-threshold"],
                    "type": "json_path_equals",
                    "file": "tests/grading_spec.json",
                    "path": ["pass_threshold"],
                    "expected": 0.5,
                }
            ]
            plan = bind_plan(package, plan)
            path = Path(temporary) / "method.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )
            self.assertEqual(
                json.loads(
                    (package / "tests/grading_spec.json").read_text()
                )["pass_threshold"],
                0.8,
            )

    def test_auto_fix_cannot_rewrite_private_checker_solution_protocol(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            plan = safe_plan(report["audit_id"], finding_id)
            plan["operations"] = [
                {
                    "id": "rewrite-checker",
                    "type": "replace_text",
                    "file": "tests/checker.py",
                    "old": "raise SystemExit(0)",
                    "new": "secret_field = 'private-protocol'",
                    "evidence_ids": ["audit-finding"],
                },
                {
                    "id": "rewrite-solution",
                    "type": "write_file",
                    "file": "solution/solve.sh",
                    "content": "secret_field=private-protocol\n",
                    "evidence_ids": ["audit-finding"],
                },
            ]
            plan["regression_tests"] = [
                {
                    "id": "checker",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["rewrite-checker"],
                    "type": "text_contains",
                    "file": "tests/checker.py",
                    "expected": "secret_field",
                }
            ]
            plan = bind_plan(package, plan)
            path = Path(temporary) / "private.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "POLICY_VIOLATION")
            self.assertNotIn(
                "secret_field",
                (package / "tests/checker.py").read_text(encoding="utf-8"),
            )

    def test_missing_causal_binding_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, report, finding_id, runner = initial_repair_context(
                Path(temporary)
            )
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            del plan["regression_tests"][0]["causal_operation_ids"]
            path = Path(temporary) / "causal.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("causal", completed.stderr)

    def test_fixture_hash_must_match_source_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            fixture = workspace / "known-valid-output"
            fixture.write_text("independent fixture\n", encoding="utf-8")
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["known_valid_output"] = str(fixture)
            plan["source_audit"]["fixture_hashes"] = {
                "known_valid_output": "sha256:" + "0" * 64
            }
            path = workspace / "fixture.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_stale_core_contract_digest_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["core_contract_digest"] = "sha256:" + "0" * 64
            path = workspace / "digest.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )


if __name__ == "__main__":
    unittest.main()
