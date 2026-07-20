from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_e1 import (
    bind_public_fixture,
    write_public_valid_dispersion,
)
from tests.test_materials_benchmark_review_paper_grounded import (
    assessment,
    copy_source_package,
    no_paper_assessment,
)
from tests.test_materials_disposition import (
    clear_external_resources,
    install_passing_oracle,
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


def run_review(package: Path, assessment_path: Path, fixture: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--paper-mode",
            "paper_grounded",
            "--execution-level",
            "E1",
            "--agent-assessment",
            str(assessment_path),
            "--known-valid-output",
            str(fixture),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


def write_assessment(path: Path) -> None:
    value = assessment()
    value["materials_qualification"] = no_paper_assessment()[
        "materials_qualification"
    ]
    value["dimensions"]["checker_fidelity"]["evidence"][0][
        "package_quote"
    ] = "scientific_contract"
    value["dimensions"]["gold_provenance"]["evidence"][0][
        "package_quote"
    ] = "reward = 1.0"
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


def prepare_passing_review(workspace: Path) -> tuple[Path, Path, Path]:
    package = workspace / "paper-fixture"
    copy_source_package(package)
    clear_external_resources(package)
    install_passing_oracle(package)
    fixture = workspace / "known-valid-output"
    write_public_valid_dispersion(fixture)
    bind_public_fixture(package, fixture)
    assessment_path = workspace / "assessment.json"
    write_assessment(assessment_path)
    return package, assessment_path, fixture


class MaterialsIssue27DeterministicGateTests(unittest.TestCase):
    def test_deterministic_gate_preserves_rejection_precedence(self) -> None:
        scripts = (
            REPO_ROOT
            / ".cursor"
            / "skills"
            / "materials-benchmark-review"
            / "scripts"
        )
        sys.path.insert(0, str(scripts))
        from deterministic_contract import (  # pylint: disable=import-outside-toplevel
            apply_deterministic_gate,
        )

        required_contract = {
            "repair_summary": {"state": "REQUIRED"},
        }
        for verdict, score, hard_gate, evidence_gaps in (
            ("REJECT", 40, False, []),
            ("NOT_ASSESSABLE", None, False, ["C04"]),
            ("PASS", 90, True, []),
        ):
            actual, reason = apply_deterministic_gate(
                verdict=verdict,
                score=score,
                hard_gate=hard_gate,
                evidence_gaps=evidence_gaps,
                contract=required_contract,
            )
            self.assertEqual(actual, verdict)
            self.assertIsNone(reason)

    def test_proven_medium_blocker_routes_high_score_to_repair_queue(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package, assessment_path, fixture = prepare_passing_review(
                Path(temporary)
            )
            grading_path = package / "tests/grading_spec.json"
            grading = json.loads(grading_path.read_text(encoding="utf-8"))
            grading["steps"].append(
                {
                    "id": "optional_zero_weight",
                    "output_file": "dispersion_curves.csv",
                    "weight": 0.0,
                }
            )
            grading_path.write_text(
                json.dumps(grading, ensure_ascii=False), encoding="utf-8"
            )
            bind_public_fixture(package, fixture)

            completed = run_review(package, assessment_path, fixture)
            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            summary = report["summary"]
            deterministic = report["deterministic_contract"]
            self.assertGreaterEqual(summary["total_score"], 80)
            self.assertEqual(summary["final_verdict"], "CONDITIONAL")
            self.assertEqual(summary["publication_route"], "REPAIR_QUEUE")
            self.assertEqual(
                summary["repair_state"], "DETERMINISTIC_REPAIR_REQUIRED"
            )
            self.assertEqual(
                deterministic["repair_summary"]["state"], "REQUIRED"
            )
            d4 = next(
                item
                for item in deterministic["checks"]
                if item["check_id"] == "D4"
            )
            self.assertEqual(d4["status"], "FAIL")
            self.assertTrue(d4["blocking_finding_ids"])
            self.assertEqual(
                {
                    item["title"]
                    for item in report["findings"]
                    if item["finding_id"] in d4["blocking_finding_ids"]
                },
                {"ZERO_WEIGHT_SCORING_COMPONENT"},
            )
            disposition = json.loads(
                (
                    package / "benchmark_audit/disposition.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(disposition["route"], "REPAIR_QUEUE")
            self.assertFalse(disposition["publishable"])

    def test_advisory_threshold_reachability_does_not_block(self) -> None:
        scripts = (
            REPO_ROOT
            / ".cursor"
            / "skills"
            / "materials-benchmark-review"
            / "scripts"
        )
        sys.path.insert(0, str(scripts))
        from deterministic_contract import (  # pylint: disable=import-outside-toplevel
            evaluate_deterministic_contract,
        )

        result = evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={},
            package_roles={},
            findings=[
                {
                    "finding_id": "FINDING-001",
                    "title": "SINGLE_COMPONENT_THRESHOLD_REACHABLE",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"bypass_proven": False},
                }
            ],
        )
        d4 = next(
            item for item in result["checks"] if item["check_id"] == "D4"
        )
        self.assertEqual(d4["status"], "PASS")
        self.assertEqual(d4["advisory_finding_ids"], ["FINDING-001"])
        self.assertEqual(
            result["repair_summary"]["state"], "CLEAN"
        )

    def test_deterministic_repair_binding_requires_complete_queue(self) -> None:
        scripts = (
            REPO_ROOT
            / ".cursor"
            / "skills"
            / "materials-benchmark-review"
            / "scripts"
        )
        sys.path.insert(0, str(scripts))
        from deterministic_contract import (  # pylint: disable=import-outside-toplevel
            evaluate_deterministic_contract,
            validate_deterministic_plan_binding,
        )

        contract = evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={},
            package_roles={},
            findings=[
                {
                    "finding_id": "FINDING-001",
                    "title": "ZERO_WEIGHT_SCORING_COMPONENT",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {},
                }
            ],
        )
        binding = {
            "schema_version": contract["schema_version"],
            "registry_version": contract["registry_version"],
            "contract_digest": contract["contract_digest"],
        }
        with self.assertRaisesRegex(ValueError, "complete source queue"):
            validate_deterministic_plan_binding(
                {"deterministic_contract": contract},
                {"deterministic_contract": binding, "findings": []},
            )


if __name__ == "__main__":
    unittest.main()
