from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = (
    REPO_ROOT / ".cursor" / "skills" / "materials-benchmark-review" / "scripts"
)
if str(REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REVIEW_SCRIPTS))

import audit_package  # noqa: E402
from d5_package_completeness import (  # noqa: E402
    d5_role_failures,
    validate_auto_fix_operation,
)
from deterministic_contract import (  # noqa: E402
    DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
    evaluate_deterministic_contract,
    validate_deterministic_contract,
    validate_deterministic_plan_binding,
)


def write_fixture(root: Path) -> None:
    (root / "tests").mkdir(parents=True)
    (root / "solution").mkdir()
    (root / "instruction.md").write_text(
        "### Step 1\n- Return `/app/outputs/result.csv`.\n",
        encoding="utf-8",
    )
    (root / "tests/grading_spec.json").write_text(
        json.dumps(
            {
                "output_contract": {"outputs": [{"file": "result.csv"}]},
                "steps": [{"id": "result", "output_file": "result.csv", "weight": 1}],
                "pass_threshold": 0.8,
            }
        ),
        encoding="utf-8",
    )
    (root / "tests/checker.py").write_text(
        "def check():\n    return 1\n",
        encoding="utf-8",
    )
    (root / "tests/test.sh").write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")


class MaterialsIssue29D5Tests(unittest.TestCase):
    def test_metadata_roles_are_not_d5_quality_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_fixture(root)
            static = audit_package.static_audit(root, root / "static.json")
            metadata = {"task.toml", "manifest.json", "steps.json", "resources.json"}
            self.assertFalse(
                any(
                    set(item.get("affected_files", [])) & metadata
                    for item in static["issues"]
                )
            )
            self.assertEqual(
                static["package_roles"]["metadata_roles_excluded"],
                [
                    "task.toml",
                    "manifest.json",
                    "steps.json",
                    "resources.json",
                    "environment",
                ],
            )
            self.assertEqual(
                d5_role_failures(static["package_roles"]), ["solution/solve.sh"]
            )

    def test_missing_oracle_contract_is_d5_and_validates_special_class(self) -> None:
        contract = evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={},
            package_roles={
                "quality_roles": {
                    "instruction.md": "ok",
                    "tests/grading_spec.json": "ok",
                    "tests/checker.py": "ok",
                    "tests/test.sh": "ok",
                },
                "oracle_entrypoint": "missing",
            },
            findings=[
                {
                    "finding_id": "F-D5",
                    "title": "SOLUTION_ORACLE_MISSING",
                    "status": "OPEN",
                    "repairable": True,
                    "affected_files": ["solution/solve.sh"],
                    "evidence": {},
                }
            ],
        )
        d5 = next(item for item in contract["checks"] if item["check_id"] == "D5")
        self.assertEqual(d5["status"], "FAIL")
        self.assertEqual(d5["recommended_repair_class"], "AUTO_FIX")
        self.assertEqual(
            contract["repair_summary"]["required_findings"][0]["repair_class"],
            "AUTO_FIX",
        )
        validate_deterministic_contract(contract)
        binding = {
            "schema_version": contract["schema_version"],
            "registry_version": contract["registry_version"],
            "contract_digest": contract["contract_digest"],
            "audit_id": "A1",
            "required_finding_ids": contract["repair_summary"][
                "required_finding_ids"
            ],
        }
        validate_deterministic_plan_binding(
            {"audit_id": "A1", "deterministic_contract": contract},
            {
                "schema_version": DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
                "audit_id": "A1",
                "deterministic_contract": binding,
                "source_audit": {
                    "audit_id": "A1",
                    "deterministic_contract": binding,
                },
                "findings": [
                    {
                        "finding_id": "F-D5",
                        "deterministic_check": "D5",
                        "finding_code": "SOLUTION_ORACLE_MISSING",
                        "repair_class": "ASSISTED_FIX",
                    }
                ],
            },
        )

    def test_unique_wrapper_and_structural_syntax_are_auto_fixable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "solution").mkdir()
            (root / "tests").mkdir()
            (root / "solution/producer.py").write_text(
                "print('existing implementation')\n", encoding="utf-8"
            )
            validate_auto_fix_operation(
                root,
                {
                    "type": "write_file",
                    "file": "solution/solve.sh",
                    "content": (
                        '#!/bin/sh\nexec python3 "$(dirname "$0")/producer.py"\n'
                    ),
                    "executable": True,
                },
                None,
            )
            validate_auto_fix_operation(
                root,
                {
                    "type": "replace_text",
                    "file": "tests/grading_spec.json",
                    "old": '{"steps": [1,], "x": 2',
                    "new": '{"steps": [1], "x": 2}',
                },
                "PARSE_ERROR",
            )

    def test_auto_fix_cannot_fabricate_scientific_producer(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "solution").mkdir()
            with self.assertRaisesRegex(ValueError, "exactly one existing"):
                validate_auto_fix_operation(
                    root,
                    {
                        "type": "write_file",
                        "file": "solution/solve.sh",
                        "content": "#!/bin/sh\necho fabricated\n",
                        "executable": True,
                    },
                    None,
                )


if __name__ == "__main__":
    unittest.main()
