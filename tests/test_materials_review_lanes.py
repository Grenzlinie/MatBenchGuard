from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
sys.path.insert(0, str(SCRIPTS))
REPAIR_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
)
sys.path.insert(0, str(REPAIR_SCRIPTS))

import deterministic_contract  # noqa: E402
import dynamic_checker_probe  # noqa: E402
import artifact_schema  # noqa: E402
import certify_final_100  # noqa: E402
import prepare_audit_output  # noqa: E402


class MaterialsReviewLaneTests(unittest.TestCase):
    def test_new_artifact_versions_and_attestation_binding(self) -> None:
        self.assertEqual(
            artifact_schema.DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
            "materials-deterministic-core/2.0",
        )
        self.assertEqual(
            artifact_schema.AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
            "materials-agent-quality/2.0",
        )
        with tempfile.TemporaryDirectory() as temporary:
            audit = Path(temporary)
            files = {
                "audit_manifest.json": {
                    "schema_version": artifact_schema.AUDIT_MANIFEST_SCHEMA_VERSION,
                    "audit_id": "audit-1",
                    "bundle_schema_version": artifact_schema.AUDIT_BUNDLE_SCHEMA_VERSION,
                    "assessment_hashes": {},
                    "output_hashes": {},
                },
                "audit_report.json": {
                    "schema_version": artifact_schema.AUDIT_REPORT_SCHEMA_VERSION,
                    "deterministic_core": {
                        "schema_version": artifact_schema.DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION
                    },
                    "agent_quality": {
                        "schema_version": artifact_schema.AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION
                    },
                    "summary": {
                        "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION
                    },
                },
                "disposition.json": {},
                "deterministic_core/report.json": {
                    "schema_version": artifact_schema.DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION
                },
                "deterministic_core/probe_results.json": {
                    "schema_version": artifact_schema.DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION
                },
                "agent_quality/assessment.json": {
                    "schema_version": artifact_schema.AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION
                },
            }
            for relative, value in files.items():
                path = audit / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value), encoding="utf-8")

            payload = prepare_audit_output.audit_attestation_payload(audit)

        self.assertEqual(
            payload["artifact_schema_versions"]["deterministic_core"],
            artifact_schema.DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
        )
        self.assertEqual(
            payload["artifact_schema_versions"]["agent_quality"],
            artifact_schema.AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
        )
        self.assertEqual(
            set(payload["artifact_hashes"]),
            {
                "audit_report.json",
                "deterministic_core/report.json",
                "deterministic_core/probe_results.json",
                "agent_quality/assessment.json",
            },
        )

    def test_certifier_accepts_v2_scoring_snapshot(self) -> None:
        dimensions = [
            {
                "dimension": name,
                "weight": weight,
                "max_points": weight,
                "points_earned": weight,
                "normalized": 100,
                "status": "PASS",
            }
            for name, weight in (
                ("C01", 10),
                ("C02", 20),
                ("C03", 20),
                ("C04", 20),
                ("C05", 10),
                ("C06", 10),
                ("C07", 10),
            )
        ]
        report = {
            "summary": {
                "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
                "total_score": 100,
            },
            "dimensions_v11": dimensions,
            "hard_gates": [],
        }
        snapshot = {
            "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
            "total_score": 100,
            "final_verdict": "PASS",
            "dimensions_v11": dimensions,
            "hard_gates": [],
        }
        snapshot["snapshot_hash"] = certify_final_100.canonical_json_hash(
            snapshot
        )

        certify_final_100.validate_dimensions(report)
        certify_final_100.validate_score(report, snapshot)

    def test_quality_probe_findings_never_enter_deterministic_contract(self) -> None:
        findings = deterministic_contract.annotate_findings(
            [
                {
                    "finding_id": "quality-1",
                    "title": "ADVERSARIAL_OUTPUT_PASSES",
                    "severity": "HIGH",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"fixture_source_kind": "INDEPENDENT_PUBLIC_FIXTURE"},
                },
                {
                    "finding_id": "quality-2",
                    "title": "KNOWN_VALID_OUTPUT_REJECTED",
                    "severity": "HIGH",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"fixture_source_kind": "INDEPENDENT_PUBLIC_FIXTURE"},
                },
                {
                    "finding_id": "core-1",
                    "title": "CORE_RUNTIME_ORDERING_VIOLATION",
                    "severity": "HIGH",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"deterministic_core": True},
                },
            ]
        )

        by_id = {item["finding_id"]: item for item in findings}
        self.assertEqual(by_id["quality-1"]["lane"], "quality_results")
        self.assertIsNone(by_id["quality-1"]["deterministic_check"])
        self.assertFalse(by_id["quality-1"]["blocking"])
        self.assertEqual(by_id["quality-2"]["lane"], "quality_results")
        self.assertIsNone(by_id["quality-2"]["deterministic_check"])
        self.assertEqual(by_id["core-1"]["deterministic_check"], "D6")
        self.assertTrue(by_id["core-1"]["blocking"])

        registry_codes = {
            code
            for check in deterministic_contract.check_registry()
            for code in check["finding_codes"]
        }
        self.assertNotIn("ADVERSARIAL_OUTPUT_PASSES", registry_codes)
        self.assertNotIn("KNOWN_VALID_OUTPUT_REJECTED", registry_codes)
        self.assertNotIn("SINGLE_COMPONENT_CAN_PASS", registry_codes)

    def test_schema_derived_plan_requires_isolated_oracle_only(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [
                    {"file": "result.json", "format": "json"},
                    {"file": "support.csv", "format": "csv"},
                ]
            },
            "steps": [
                {"id": "result", "output_file": "result.json", "weight": 0.6},
                {"id": "support", "output_file": "support.csv", "weight": 0.4},
            ],
        }
        plan, reason = dynamic_checker_probe.schema_derived_probe_plan(
            specification, None
        )
        self.assertEqual(plan, [])
        self.assertIn("isolated Oracle", reason or "")

    def test_schema_derived_plan_has_partial_and_all_wrong_cases(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [
                    {"file": "result.json", "format": "json"},
                    {"file": "support.csv", "format": "csv"},
                ]
            },
            "steps": [
                {"id": "result", "output_file": "result.json", "weight": 0.6},
                {"id": "support", "output_file": "support.csv", "weight": 0.4},
            ],
        }
        plan, reason = dynamic_checker_probe.schema_derived_probe_plan(
            specification, Path("/tmp/oracle-output")
        )
        self.assertIsNone(reason)
        self.assertEqual(plan[0]["case"], "all_wrong")
        self.assertEqual(
            [item["case"] for item in plan[1:]],
            ["partial__result", "partial__support"],
        )
        self.assertTrue(
            all(
                item["probe_origin"] == "SCHEMA_DERIVED_DETERMINISTIC"
                for item in plan
            )
        )

    def test_partial_probe_copies_and_mutates_isolated_oracle_outputs(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [{"file": "result.json", "format": "json"}]
            },
            "steps": [
                {"id": "result", "output_file": "result.json", "weight": 1.0}
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            oracle = root / "oracle"
            probe = root / "probe"
            oracle.mkdir()
            json_output = oracle / "result.json"
            json_output.write_text('{"prediction": 1}\n', encoding="utf-8")

            created = dynamic_checker_probe.copy_oracle_outputs(
                oracle, probe, specification
            )
            component = dynamic_checker_probe.declared_scoring_components(
                specification
            )[0]
            detail = dynamic_checker_probe.mutate_declared_component(
                probe, component
            )

            self.assertEqual(created, ["result.json"])
            self.assertEqual(detail["operation"], "schema_derived_wrong_component")
            self.assertNotEqual(
                json.loads(json_output.read_text(encoding="utf-8")),
                json.loads((probe / "result.json").read_text(encoding="utf-8")),
            )

if __name__ == "__main__":
    unittest.main()
