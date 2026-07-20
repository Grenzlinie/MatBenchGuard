from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_e1 import (  # noqa: E402
    bind_public_fixture,
)
from tests.test_materials_issue27_deterministic_gate import (  # noqa: E402
    prepare_passing_review,
    run_review,
)
from tests.test_materials_safe_repair import (  # noqa: E402
    initial_repair_context,
    repair_module,
    run_repair,
    sha256_file,
    write_audit_attestation,
    write_json,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import audit_package  # noqa: E402
from d1_d2_contract import (  # noqa: E402
    compare_instruction_sections,
    compare_scored_outputs,
    is_structural_auto_fix_operation,
    output_repair_proof,
    structural_auto_fix_operation_error,
)
from deterministic_contract import (  # noqa: E402
    evaluate_deterministic_contract,
    validate_deterministic_contract,
)


class MaterialsIssue30D1D2Tests(unittest.TestCase):
    def test_d1_normalizes_sentence_punctuation_across_all_sources(self) -> None:
        instruction = """
### Step 1: Compute the result
- Role: scored
- Output file: /app/outputs/result.csv.
"""
        instruction_contract = audit_package.instruction_contract_map(instruction)
        result = compare_scored_outputs(
            instruction_contract,
            {
                "output_contract": {
                    "outputs": [{"file": "/app/outputs/result.csv"}]
                },
                "steps": [{"output_file": "result.csv", "weight": 1.0}],
            },
        )

        self.assertTrue(result["consistent"])
        self.assertEqual(
            result["declared_outputs"],
            {
                "instruction": ["result.csv"],
                "output_contract": ["result.csv"],
                "grading_steps": ["result.csv"],
            },
        )

    def test_literal_filename_punctuation_is_preserved(self) -> None:
        for literal_name in ("strange!.csv", "result."):
            with self.subTest(literal_name=literal_name):
                instruction = (
                    "### Step 1: Compute the result\n"
                    "- Role: scored\n"
                    f'- Output file: "/app/outputs/{literal_name}"\n'
                )
                contract = audit_package.instruction_contract_map(instruction)
                result = compare_scored_outputs(
                    contract,
                    {
                        "output_contract": {
                            "outputs": [{"file": literal_name}]
                        },
                        "steps": [
                            {
                                "output_file": literal_name,
                                "weight": 1.0,
                            }
                        ],
                    },
                )
                self.assertTrue(result["consistent"])
                self.assertEqual(
                    result["declared_outputs"]["instruction"],
                    [literal_name],
                )

    def test_prose_period_and_literal_period_remain_distinct(self) -> None:
        prose = audit_package.instruction_contract_map(
            "### Step 1\n"
            "- Role: scored\n"
            "- Output file: /app/outputs/result.csv.\n"
        )
        literal = audit_package.instruction_contract_map(
            "### Step 1\n"
            "- Role: scored\n"
            '- Output file: "/app/outputs/result.csv."\n'
        )
        self.assertEqual(prose["scored_outputs"], ["result.csv"])
        self.assertEqual(literal["scored_outputs"], ["result.csv."])

    def test_review_static_audit_detects_grading_output_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "tests").mkdir()
            (root / "instruction.md").write_text(
                "### Step 1\n"
                "- Role: scored\n"
                "- Output file: /app/outputs/result.csv\n",
                encoding="utf-8",
            )
            (root / "tests/grading_spec.json").write_text(
                json.dumps(
                    {
                        "output_contract": {"outputs": [{"file": "result.csv"}]},
                        "steps": [
                            {
                                "id": "result",
                                "output_file": "result.csv",
                                "weight": 0.5,
                            },
                            {
                                "id": "extra",
                                "output_file": "extra.csv.",
                                "weight": 0.5,
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "tests/checker.py").write_text("", encoding="utf-8")
            (root / "tests/test.sh").write_text("#!/bin/sh\n", encoding="utf-8")
            result = audit_package.static_audit(root, root / "static.json")

        findings = {item["code"] for item in result["issues"]}
        self.assertIn("OUTPUT_NOT_CONTRACTED", findings)
        self.assertNotIn("OUTPUT_DECLARATION_MISMATCH", findings)

    def test_review_cli_routes_d1_drift_to_deterministic_queue(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, assessment, fixture = prepare_passing_review(
                Path(temporary)
            )
            grading_path = package / "tests/grading_spec.json"
            grading = json.loads(grading_path.read_text(encoding="utf-8"))
            grading["steps"].append(
                {
                    "id": "stale_extra",
                    "output_file": "stale_extra.csv.",
                    "weight": 0.0,
                }
            )
            grading_path.write_text(
                json.dumps(grading, ensure_ascii=False), encoding="utf-8"
            )
            bind_public_fixture(package, fixture)
            completed = run_review(package, assessment, fixture)

            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            d1 = next(
                item
                for item in report["deterministic_contract"]["checks"]
                if item["check_id"] == "D1"
            )
            self.assertEqual(d1["status"], "FAIL")
            self.assertTrue(
                any(
                    item["title"] == "OUTPUT_NOT_CONTRACTED"
                    for item in report["findings"]
                )
            )

    def test_d2_compares_four_sections_and_surfaces_semantic_drift(self) -> None:
        result = compare_instruction_sections(
            """
## Workflow steps
### Step 1
- Output file: /app/outputs/result.csv.

## Output files
- /app/outputs/result.csv

## Output contract
```json
{"outputs": [{"file": "result.csv", "schema": {
  "required_columns": ["x"], "units": {"x": "eV"}
}}]}
```

## Self-check before finishing
```json
{"outputs": [{"file": "result.csv", "schema": {
  "required_columns": ["y"], "units": {"x": "kJ/mol"}
}}]}
```
"""
        )

        self.assertFalse(result["consistent"])
        self.assertFalse(result["mismatches"])
        self.assertEqual(
            {item["code"] for item in result["semantic_mismatches"]},
            {"OUTPUT_FIELD_MISMATCH", "OUTPUT_UNIT_MISMATCH"},
        )

    def test_d1_d2_repair_classes_separate_structure_from_semantics(self) -> None:
        findings = [
            {
                "finding_id": "structural",
                "title": "INSTRUCTION_INTERNAL_INCONSISTENCY",
                "status": "OPEN",
                "repairable": True,
                "evidence": {},
            },
            {
                "finding_id": "semantic",
                "title": "OUTPUT_UNIT_MISMATCH",
                "status": "OPEN",
                "repairable": True,
                "evidence": {},
            },
        ]
        contract = evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={},
            package_roles={},
            findings=findings,
        )
        validate_deterministic_contract(contract)
        classes = {
            item["finding_id"]: item["repair_class"]
            for item in contract["repair_summary"]["required_findings"]
        }

        self.assertEqual(classes, {"semantic": "ASSISTED_FIX", "structural": "AUTO_FIX"})

    def test_structural_auto_fix_only_allows_output_token_sync(self) -> None:
        self.assertTrue(
            is_structural_auto_fix_operation(
                {
                    "type": "replace_text",
                    "file": "instruction.md",
                    "old": "/app/outputs/stale.csv.",
                    "new": "/app/outputs/result.csv",
                }
            )
        )
        self.assertTrue(
            is_structural_auto_fix_operation(
                {
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["steps", 0, "output_file"],
                    "value": "result.csv",
                }
            )
        )
        self.assertFalse(
            is_structural_auto_fix_operation(
                {
                    "type": "replace_text",
                    "file": "instruction.md",
                    "old": "frequency in eV",
                    "new": "frequency in kJ/mol",
                }
            )
        )

    def test_structural_auto_fix_value_must_match_unique_contract_proof(
        self,
    ) -> None:
        proof = output_repair_proof(
            {
                "instruction_outputs": ["result.csv"],
                "cross_file_sets": {
                    "contract_outputs": ["result.csv"],
                    "grading_outputs": ["result.csv"],
                },
            }
        )
        self.assertIsNone(
            structural_auto_fix_operation_error(
                {
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["steps", 0, "output_file"],
                    "value": "result.csv",
                },
                proof,
            )
        )
        self.assertRegex(
            structural_auto_fix_operation_error(
                {
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["steps", 0, "output_file"],
                    "value": "invented.csv",
                },
                proof,
            )
            or "",
            "source-bound",
        )

    def test_repair_cli_applies_structural_d2_autofix_and_reaudits(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, _, finding_id, runner = initial_repair_context(workspace)
            report_path = package / "benchmark_audit/audit_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["findings"][0].update(
                {
                    "title": "INSTRUCTION_INTERNAL_INCONSISTENCY",
                    "affected_files": ["instruction.md"],
                }
            )
            report["contract_map"] = {
                "instruction_outputs": [],
                "cross_file_sets": {
                    "contract_outputs": ["result.csv"],
                    "grading_outputs": ["result.csv"],
                },
                "checker_analysis": {
                    "outputs": [{"file": "result.csv"}]
                },
            }
            write_json(report_path, report)
            manifest_path = package / "benchmark_audit/audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["output_hashes"]["audit_report.json"] = sha256_file(
                report_path
            )
            write_json(manifest_path, manifest)
            write_audit_attestation(package)
            core_digest = repair_module().core_contract_digest(package)

            old = "Compute the evidence-backed quantity.\n"
            new = old + "- Output file: /app/outputs/result.csv\n"
            plan = {
                "schema_version": "0.1",
                "audit_id": report["audit_id"],
                "core_contract_digest": core_digest,
                "source_audit": {
                    "audit_id": report["audit_id"],
                    "input_hashes": manifest["input_hashes"],
                    "paper_mode": "no_paper",
                    "execution_level": "E1",
                    "core_contract_digest": core_digest,
                },
                "findings": [
                    {
                        "finding_id": finding_id,
                        "deterministic_check": "D2",
                        "repair_class": "AUTO_FIX",
                        "justification": "Synchronize the missing output declaration.",
                        "core_science_change": False,
                        "evidence": [
                            {
                                "id": "audit-finding",
                                "source": f"benchmark_audit:{finding_id}",
                                "quote": "INSTRUCTION_INTERNAL_INCONSISTENCY",
                                "source_hash": sha256_file(report_path),
                            }
                        ],
                        "operations": [
                            {
                                "id": "add-output-declaration",
                                "type": "replace_text",
                                "file": "instruction.md",
                                "old": old,
                                "new": new,
                                "evidence_ids": ["audit-finding"],
                            }
                        ],
                        "regression_tests": [
                            {
                                "id": "output-declaration",
                                "finding_id": finding_id,
                                "causal_operation_ids": [
                                    "add-output-declaration"
                                ],
                                "type": "text_contains",
                                "file": "instruction.md",
                                "expected": new,
                            }
                        ],
                    }
                ],
            }
            plan_path = workspace / "d2-repair-plan.json"
            write_json(plan_path, plan)
            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 0, completed.stdout)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertTrue(result["publishable"])
            self.assertIn(
                "/app/outputs/result.csv",
                (package / "instruction.md").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
