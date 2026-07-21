from __future__ import annotations

import ast
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
    write_audit_attestation,
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


def nested_return_proof(checker: Path) -> dict[str, Any]:
    source = checker.read_text(encoding="utf-8")
    function = next(
        node
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.FunctionDef) and node.name == "score_0"
    )
    return {
        "proof_status": "PROVEN",
        "auto_fix_provable": True,
        "source_file": "tests/checker.py",
        "source_hash": sha256_file(checker),
        "function_name": "score_0",
        "function_span": {
            "lineno": function.lineno,
            "end_lineno": function.end_lineno,
            "col_offset": function.col_offset,
            "end_col_offset": function.end_col_offset,
        },
        "return_expression": "score(artifact, step, ctx)",
    }


class MaterialsIssue21RepairSecurityTests(unittest.TestCase):
    def test_batch_d3_proof_allows_mechanical_return_without_harbor_patch(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checker = root / "tests/checker.py"
            checker.parent.mkdir()
            source = (
                "def score_0(artifact, step, ctx):\n"
                "    def score(artifact, step, ctx):\n"
                "        return 0.5\n"
            )
            checker.write_text(source, encoding="utf-8")
            proof = nested_return_proof(checker)
            report_text = "SCORER_RETURN_NOT_TOTAL\n"
            (root / "benchmark_audit").mkdir()
            (root / "benchmark_audit/audit_report.json").write_text(
                report_text, encoding="utf-8"
            )
            operation = {
                "id": "append-score-return",
                "type": "replace_text",
                "file": "tests/checker.py",
                "old": source,
                "new": source + "    return score(artifact, step, ctx)\n",
                "evidence_ids": ["audit-finding"],
            }
            module = repair_module()
            fplan = {
                "finding_id": "F-D3",
                "repair_class": "AUTO_FIX",
                "deterministic_check": "D3",
                "finding_code": "SCORER_RETURN_NOT_TOTAL",
                "core_science_change": False,
                "deterministic_evidence": {"return_proof": {"score_0": proof}},
                "evidence": [
                    {
                        "id": "audit-finding",
                        "source": "benchmark_audit:F-D3",
                        "quote": report_text.strip(),
                        "source_hash": sha256_file(
                            root / "benchmark_audit/audit_report.json"
                        ),
                    }
                ],
                "operations": [operation],
                "regression_tests": [],
            }

            _, valid, blocked = module.classify_finding(
                root, {"findings": []}, {}, fplan
            )

        self.assertEqual(valid, [operation])
        self.assertEqual(blocked, [])

    def test_d3_proof_rejects_drift_and_unproven_semantic_change(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checker = root / "tests/checker.py"
            checker.parent.mkdir()
            source = (
                "def score_0(artifact, step, ctx):\n"
                "    def score(artifact, step, ctx):\n"
                "        return 0.5\n"
            )
            checker.write_text(source, encoding="utf-8")
            proof = nested_return_proof(checker)
            finding = {
                "deterministic_check": "D3",
                "title": "SCORER_RETURN_NOT_TOTAL",
                "evidence": {"return_proof": {"score_0": proof}},
            }
            module = repair_module()
            semantic_operation = {
                "id": "bad-return",
                "type": "replace_text",
                "file": "tests/checker.py",
                "old": source,
                "new": source + "    return 0\n",
            }
            self.assertIsNotNone(
                module.proof_bound_auto_fix_operation_error(
                    root, finding, semantic_operation
                )
            )

            checker.write_text(
                source.replace("return 0.5", "return 0.25"), encoding="utf-8"
            )
            drift_operation = {
                "id": "stale-return",
                "type": "replace_text",
                "file": "tests/checker.py",
                "old": checker.read_text(encoding="utf-8"),
                "new": checker.read_text(encoding="utf-8")
                + "    return score(artifact, step, ctx)\n",
            }
            error = module.proof_bound_auto_fix_operation_error(
                root, finding, drift_operation
            )

        self.assertIsNotNone(error)
        self.assertIn("source/function", error)

    def test_d4_normalization_rejects_source_value_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            grading = root / "tests/grading_spec.json"
            grading.parent.mkdir()
            grading.write_text(
                json.dumps(
                    {
                        "steps": [
                            {"id": "a", "weight": 2.0},
                            {"id": "b", "weight": 1.0},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            evidence_value = {
                "ratio_preserving_normalization": True,
                "weights": [
                    {"component_id": "a", "value": 2.0},
                    {"component_id": "b", "value": 1.0},
                ],
                "normalized_weights": [
                    {"component_id": "a", "value": 2 / 3},
                    {"component_id": "b", "value": 1 / 3},
                ],
            }
            operation = {
                "id": "normalize-a",
                "type": "json_set",
                "file": "tests/grading_spec.json",
                "path": ["steps", 0, "weight"],
                "value": 2 / 3,
            }
            module = repair_module()
            finding = {
                "deterministic_check": "D4",
                "title": "WEIGHTS_NOT_ONE",
                "evidence": evidence_value,
            }
            self.assertIsNone(
                module.proof_bound_auto_fix_operation_error(
                    root, finding, operation
                )
            )
            grading.write_text(
                json.dumps(
                    {
                        "steps": [
                            {"id": "a", "weight": 5.0},
                            {"id": "b", "weight": 1.0},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            error = module.proof_bound_auto_fix_operation_error(
                root, finding, operation
            )

        self.assertIsNotNone(error)
        self.assertIn("drifted", error)

    def test_co_tampered_report_and_manifest_are_blocked_by_attestation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            report["summary"]["co_tampered"] = True
            report_path = package / "benchmark_audit/audit_report.json"
            write_plan(report_path, report)
            manifest_path = package / "benchmark_audit/audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["output_hashes"]["audit_report.json"] = sha256_file(report_path)
            write_plan(manifest_path, manifest)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["evidence"][0]["source_hash"] = sha256_file(report_path)
            path = workspace / "co-tampered-audit.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_tampered_authoritative_audit_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            report["summary"]["tampered"] = True
            write_plan(package / "benchmark_audit/audit_report.json", report)
            plan["evidence"][0]["source_hash"] = sha256_file(
                package / "benchmark_audit/audit_report.json"
            )
            path = workspace / "tampered-audit.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_stale_current_review_implementation_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            manifest_path = package / "benchmark_audit/audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["review_implementation"]["aggregate_hash"] = (
                "sha256:" + "0" * 64
            )
            write_plan(manifest_path, manifest)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["source_audit"]["review_implementation"] = manifest[
                "review_implementation"
            ]
            path = workspace / "stale-review.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

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
                    "expected": "secret_field = 'private-protocol'",
                },
                {
                    "id": "solution",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["rewrite-solution"],
                    "type": "text_contains",
                    "file": "solution/solve.sh",
                    "expected": "secret_field=private-protocol\n",
                },
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

    def test_removed_fixture_fields_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            removed = repair_module().REMOVED_FIXTURE_FIELDS
            self.assertTrue(removed)
            for field in removed:
                with self.subTest(field=field):
                    plan = bind_plan(
                        package, safe_plan(report["audit_id"], finding_id)
                    )
                    plan[field] = {"removed": True}
                    path = workspace / f"{field}.json"
                    write_plan(path, plan)
                    completed = run_repair(package, path, runner)
                    self.assertEqual(completed.returncode, 3)
                    self.assertEqual(
                        json.loads(completed.stdout)["status"],
                        "BLOCKED_EVIDENCE",
                    )

    def test_unrelated_paper_quote_cannot_set_gold_value(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, paper_mode="paper_grounded"
            )
            paper = package / "paper/paper.md"
            paper.write_text(
                paper.read_text(encoding="utf-8")
                + "The required gold_target number is 1.0 eV from the "
                "published table.\n",
                encoding="utf-8",
            )
            manifest_path = package / "benchmark_audit/audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["input_hashes"]["paper/paper.md"] = sha256_file(paper)
            write_plan(manifest_path, manifest)
            write_audit_attestation(package)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["repair_class"] = "ASSISTED_FIX"
            plan["evidence"] = [
                evidence(
                    package,
                    "wrong-gold",
                    "paper/paper.md",
                    "The required gold_target number is 1.0 eV from the "
                    "published table.",
                    kind="gold",
                    precision={
                        "field": "gold_target",
                        "value": 2.0,
                        "type": "number",
                        "unit": "eV",
                        "required": True,
                        "source_or_derivation": "published table",
                    },
                )
            ]
            plan["operations"] = [
                {
                    "id": "set-gold",
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["gold_target"],
                    "value": 2.0,
                    "evidence_ids": ["wrong-gold"],
                }
            ]
            plan["regression_tests"] = [
                {
                    "id": "gold-value",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["set-gold"],
                    "type": "json_path_equals",
                    "file": "tests/grading_spec.json",
                    "path": ["gold_target"],
                    "expected": 2.0,
                }
            ]
            path = workspace / "unrelated-gold.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_same_file_extra_operation_needs_its_own_semantic_assertion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["operations"] = [
                {
                    "id": "write-intermediate",
                    "type": "write_file",
                    "file": "solution/solve.sh",
                    "content": "#!/bin/sh\nexit 7\n",
                    "evidence_ids": ["audit-finding"],
                },
                {
                    "id": "replace-final",
                    "type": "replace_text",
                    "file": "solution/solve.sh",
                    "old": "exit 7",
                    "new": "exit 0",
                    "evidence_ids": ["audit-finding"],
                },
            ]
            plan["regression_tests"] = [
                {
                    "id": "final-content",
                    "finding_id": finding_id,
                    "causal_operation_ids": [
                        "write-intermediate",
                        "replace-final",
                    ],
                    "type": "text_contains",
                    "file": "solution/solve.sh",
                    "expected": "exit 0",
                }
            ]
            path = workspace / "same-file-extra.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("semantic", completed.stderr)

    def test_paper_evidence_must_bind_source_audit_hash(self) -> None:
        # no_paper mode is gone: paper evidence is always admissible, but each
        # item must bind the exact paper/** file the source audit hashed.  Here
        # the paper file is dropped from the authoritative input hashes, so the
        # otherwise-valid paper-grounded edit is BLOCKED_EVIDENCE.
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            manifest_path = package / "benchmark_audit/audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["input_hashes"].pop("paper/paper.md", None)
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            write_audit_attestation(package)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["repair_class"] = "ASSISTED_FIX"
            plan["evidence"] = [
                evidence(
                    package,
                    "paper-method",
                    "paper/paper.md",
                    "The exact public replacement is paper-supported quantity.",
                    kind="scientific_method",
                    precision={
                        "claim": "paper-supported quantity",
                        "replacement": "paper-supported quantity",
                    },
                )
            ]
            plan["operations"] = [
                {
                    "id": "paper-edit",
                    "type": "replace_text",
                    "file": "instruction.md",
                    "old": "evidence-backed quantity",
                    "new": "paper-supported quantity",
                    "evidence_ids": ["paper-method"],
                }
            ]
            plan["regression_tests"] = [
                {
                    "id": "paper-edit",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["paper-edit"],
                    "type": "text_contains",
                    "file": "instruction.md",
                    "expected": "paper-supported quantity",
                }
            ]
            path = workspace / "unbound-paper-evidence.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_abandon_plan_cannot_carry_an_operation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["repair_class"] = "ABANDON"
            plan["regression_tests"] = []
            path = workspace / "abandon-operation.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("ABANDON", completed.stderr)

    def test_metadata_evidence_cannot_lower_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            (package / "resources.json").write_text(
                "required number unitless pass_threshold 0.5 absolute "
                "scoring threshold with "
                "mathematical proof",
                encoding="utf-8",
            )
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["repair_class"] = "ASSISTED_FIX"
            plan["evidence"] = [
                evidence(
                    package,
                    "metadata-threshold",
                    "resources.json",
                    "required number unitless pass_threshold 0.5 absolute "
                    "scoring threshold with "
                    "mathematical proof",
                    kind="scoring_contract",
                    precision={
                        "field": "pass_threshold",
                        "value": 0.5,
                        "type": "number",
                        "unit": "unitless",
                        "required": True,
                        "scoring_contract": "scoring threshold",
                        "mathematical_proof": "mathematical proof",
                    },
                )
            ]
            plan["operations"] = [
                {
                    "id": "lower-threshold",
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["pass_threshold"],
                    "value": 0.5,
                    "evidence_ids": ["metadata-threshold"],
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
            path = workspace / "metadata-threshold.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_json_replace_cannot_invent_field_with_harbor_path_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["repair_class"] = "ASSISTED_FIX"
            plan["evidence"] = [
                evidence(
                    package,
                    "path",
                    "instruction.md",
                    "Compute the evidence-backed quantity.",
                    kind="harbor_path",
                    precision={
                        "official_contract": "Compute",
                        "existing_path_code": "quantity",
                    },
                )
            ]
            plan["operations"] = [
                {
                    "id": "invent-field",
                    "type": "replace_text",
                    "file": "tests/grading_spec.json",
                    "old": '{"pass_threshold": 0.8}',
                    "new": '{"pass_threshold": 0.8, "secret_field": "private"}',
                    "evidence_ids": ["path"],
                }
            ]
            plan["regression_tests"] = [
                {
                    "id": "invented",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["invent-field"],
                    "type": "text_contains",
                    "file": "tests/grading_spec.json",
                    "expected": (
                        '{"pass_threshold": 0.8, '
                        '"secret_field": "private"}'
                    ),
                }
            ]
            path = workspace / "invent-field.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )

    def test_every_operation_requires_causal_regression_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["operations"].append(
                {
                    "id": "untested-extra",
                    "type": "write_file",
                    "file": "solution/extra.txt",
                    "content": "untested\n",
                    "evidence_ids": ["audit-finding"],
                }
            )
            plan["regression_tests"][0]["causal_operation_ids"].append(
                "untested-extra"
            )
            path = workspace / "extra-operation.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("causal", completed.stderr)

    def test_tests_shell_mutation_changes_frozen_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            before = plan["core_contract_digest"]
            (package / "tests/test.sh").write_text("#!/bin/sh\nexit 7\n")

            self.assertNotEqual(
                repair_module().core_contract_digest(package),
                before,
            )
            path = workspace / "mutated-test-shell.json"
            write_plan(path, plan)
            completed = run_repair(package, path, runner)
            self.assertEqual(completed.returncode, 2)
            self.assertIn("input changed since review", completed.stderr)

    def test_failed_history_bundle_is_complete_and_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(workspace)
            plan = bind_plan(package, safe_plan(report["audit_id"], finding_id))
            plan["regression_tests"] = [
                plan["regression_tests"][0],
                {
                    "id": "forced-failure",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["restore-solve"],
                    "type": "command",
                    "command": ["sh", "solution/solve.sh"],
                    "expected_returncode": 1,
                }
            ]
            path = workspace / "failed-bundle.json"
            write_plan(path, plan)

            completed = run_repair(package, path, runner)

            self.assertEqual(completed.returncode, 3)
            history = Path(json.loads(completed.stdout)["history_dir"])
            module = repair_module()
            module.validate_fixed_bundle(history)
            (history / "history.json").unlink()
            with self.assertRaises(ValueError):
                module.validate_fixed_bundle(history)

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
