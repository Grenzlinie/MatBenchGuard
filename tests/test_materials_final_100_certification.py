from __future__ import annotations

import json
import sys
import unittest


from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(SCRIPTS))

import artifact_schema  # noqa: E402
import agent_contract_wiring  # noqa: E402
import certify_final_100  # noqa: E402
import deterministic_contract  # noqa: E402


def dimensions() -> list[dict[str, object]]:
    return [
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


def hard_gates() -> list[dict[str, object]]:
    return [
        {
            "code": code,
            "status": "PASS",
            "evidence": [{"fact": "gate assessed"}],
            "affected_locations": [
                {"file": "instruction.md", "line": 1, "quote": "task"}
            ],
        }
        for code in (
            "NON_MATERIALS_TASK",
            "SCIENTIFIC_TARGET_INVALID",
            "CHECKER_CORE_TASK_UNASSESSED",
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
        )
    ]


def probe_coverage() -> dict[str, object]:
    unavailable = {
        "status": "NOT_ASSESSABLE",
        "reason": "Agent-quality evidence was not supplied.",
        "provenance": {
            "source_kind": "NONE",
            "oracle_used": False,
            "external_result_directory_accepted": False,
        },
    }
    return {
        "positive": {
            "status": "ASSESSED",
            "provenance": {
                "source_kinds": ["ORACLE_POSITIVE_MOCK"],
                "oracle_used": True,
                "oracle_scientific_evidence": False,
            },
        },
        "negative": {
            "status": "ASSESSED",
            "provenance": {
                "source_kind": "SCHEMA_SHAPED_SYNTHETIC_ATTACKS",
                "oracle_used": False,
            },
        },
        "discrimination": unavailable,
        "equivalence": unavailable,
        "component_isolation": unavailable,
    }


def effective_contract_bundle() -> tuple[
    dict[str, object], dict[str, object], dict[str, object]
]:
    machine = deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={"d6_core_output_scoring": {"status": "UNKNOWN"}},
        package_roles={},
        findings=[],
    )
    assessment = agent_contract_wiring.make_agent_contract_assessment(
        machine,
        {
            check_id: {
                "status": "PASS" if check_id == "D6" else "NOT_PROVEN",
                "rationale": f"{check_id} contract wiring is established",
                "evidence": (
                    [
                        {
                            "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
                            "path": "deterministic_core/probe_results.json",
                            "scope": "CONTRACT_WIRING",
                            "claim": claim,
                            "quote": f'"{claim}": "PROVEN"',
                            "artifact_digest": "sha256:" + "1" * 64,
                        }
                        for claim in agent_contract_wiring.D6_CHAIN_STATES
                    ]
                    if check_id == "D6"
                    else []
                ),
                **(
                    {
                        "chain_states": {
                            name: "PROVEN"
                            for name in agent_contract_wiring.D6_CHAIN_STATES
                        }
                    }
                    if check_id == "D6"
                    else {}
                ),
            }
            for check_id in deterministic_contract.CHECK_IDS
        },
    )
    effective = agent_contract_wiring.derive_effective_contract(
        machine, assessment
    )
    return machine, assessment, effective


class MaterialsFinal100CertificationTests(unittest.TestCase):
    def test_canonical_pass_separates_verdict_from_publication_route(self) -> None:
        report = {
            "summary": {
                "final_verdict": "PASS",
                "disposition": "PASS",
                "publication_route": "PUBLISH_CANDIDATE",
                "publishability": "PUBLISH_CANDIDATE",
            },
            "publishability": "PUBLISH_CANDIDATE",
        }
        fields = {
            "review_verdict": "PASS",
            "publishability": "PUBLISH_CANDIDATE",
        }

        certify_final_100.validate_report_canonical_fields(report, fields)

        route_mismatch = json.loads(json.dumps(report))
        route_mismatch["summary"]["publication_route"] = "PASS"
        with self.assertRaisesRegex(
            certify_final_100.CertificationError,
            "publication route",
        ):
            certify_final_100.validate_report_canonical_fields(
                route_mismatch, fields
            )

        verdict_mismatch = json.loads(json.dumps(report))
        verdict_mismatch["summary"]["disposition"] = "PUBLISH_CANDIDATE"
        with self.assertRaisesRegex(
            certify_final_100.CertificationError,
            "verdict",
        ):
            certify_final_100.validate_report_canonical_fields(
                verdict_mismatch, fields
            )

    def test_v2_dimensions_and_score_snapshot_are_self_consistent(self) -> None:
        dims = dimensions()
        report = {
            "summary": {
                "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
                "total_score": 100,
            },
            "dimensions_v11": dims,
            "hard_gates": hard_gates(),
        }
        snapshot = {
            "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
            "total_score": 100,
            "final_verdict": "PASS",
            "dimensions_v11": dims,
            "hard_gates": report["hard_gates"],
        }
        snapshot["snapshot_hash"] = certify_final_100.canonical_json_hash(
            snapshot
        )

        certify_final_100.validate_dimensions(report)
        certify_final_100.validate_score(report, snapshot)
        certify_final_100.validate_hard_gates(report)


    def test_legacy_scoring_schema_is_rejected(self) -> None:
        with self.assertRaisesRegex(
            ValueError, artifact_schema.AUDIT_REPORT_SCHEMA_VERSION
        ):
            artifact_schema.require_schema(
                {"schema_version": "materials-review-scoring/1.0"},
                artifact_schema.AUDIT_REPORT_SCHEMA_VERSION,
                "legacy artifact",
            )

    def test_persisted_pass_certifies_effective_clean_not_machine_state(self) -> None:
        machine, assessment, effective = effective_contract_bundle()
        report = {
            "review_verdict": "PASS",
            "publishability": "PUBLISH_CANDIDATE",
            "repair_decision": "NOT_REQUIRED",
            "repair_status": "NOT_APPLICABLE",
            "summary": {
                "final_verdict": "PASS",
                "disposition": "PASS",
                "publication_route": "PUBLISH_CANDIDATE",
                "publishability": "PUBLISH_CANDIDATE",
                "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
                "total_score": 90,
                "hard_gate_triggered": False,
            },
            "dimensions_v11": dimensions(),
            "hard_gates": hard_gates(),
            "deterministic_contract": machine,
            "effective_deterministic_contract": effective,
            "agent_contract_assessment": assessment,
            "findings": [],
        }

        certify_final_100.validate_persisted_reaudit_pass(report)


if __name__ == "__main__":
    unittest.main()
