from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / ".cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py"
)
SPEC = importlib.util.spec_from_file_location("validate_agent_decision", SCRIPT)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def evidence(result: str = "verified") -> list[dict[str, str]]:
    return [
        {
            "source_kind": "TEST",
            "path": "fixture",
            "locator": "line 1",
            "quote_or_result": result,
        }
    ]


def parameter_item(
    parameter_id: str,
    *,
    source_status: str = "PAPER_EXPLICIT",
    resolution: str = "FIXED_TO_SOURCE",
    depends_on: list[str] | None = None,
    scoring_sensitive: bool = False,
    execution_required: bool = True,
    paper_reference_required: bool = True,
) -> dict:
    return {
        "parameter_id": parameter_id,
        "category": "simulation protocol",
        "introduced_at": ["instruction.md:Step 1"],
        "source_status": source_status,
        "value_or_rule": "Source-backed value or explicit unresolved marker.",
        "depends_on": depends_on or [],
        "downstream_consumers": ["instruction.md:Step 2"],
        "affects_scored_outputs": ["result.json"] if scoring_sensitive else [],
        "scoring_sensitive": scoring_sensitive,
        "execution_required": execution_required,
        "paper_reference_required": paper_reference_required,
        "resolution": resolution,
        "evidence": evidence(parameter_id),
    }


def decision() -> dict:
    criteria = {
        key: {
            "name": name,
            "status": "PASS",
            "rationale": "Verified from primary evidence.",
            "evidence": evidence(),
        }
        for key, name in module.CRITERIA.items()
    }
    dimensions = [
        {"dimension": dim, "weight": weight, "normalized": 100, "evidence": evidence()}
        for dim, weight in module.DIMENSIONS.items()
    ]
    gates = [
        {
            "code": code,
            "status": "PASS",
            "disposition": "NONE",
            "failure_modes": [],
            "rationale": "No gate defect.",
            "evidence": evidence(),
        }
        for code in sorted(module.HARD_GATES)
    ]
    probes = {
        name: {
            "status": "PASS",
            "rationale": "Probe behaved as required.",
            "evidence": evidence(name),
        }
        for name in module.PROBES
    }
    resource = {
        "resource_id": "embedded",
        "role": "required input",
        "identity_version": "v1",
        "locator": "data/input.json",
        "access_result": "readable",
        "sufficiency": "complete",
        "allowed_alternative": "none required",
    }
    readiness = {
        name: {
            "status": "READY",
            "rationale": "Required resources are ready.",
            "evidence": evidence(name),
            "resources": [resource],
        }
        for name in module.READINESS
    }
    parameters = {
        name: {
            "status": "PASS",
            "rationale": "Policy boundary verified.",
            "evidence": evidence(name),
            "items": [],
        }
        for name in module.PARAMETER_BUCKETS
    }
    patterns = {
        pattern_id: {
            "criterion": criterion,
            "dimension": dimension,
            "status": "PASS",
            "rationale": "Pattern checked against package and paper.",
            "evidence": evidence(pattern_id),
        }
        for pattern_id, (criterion, dimension) in module.SCIENTIFIC_PATTERNS.items()
    }
    return {
        "schema_version": module.SCHEMA,
        "package_id": "cluster/theme/paper-1",
        "mode": "REVIEW",
        "reproduction_intent": "METHOD_REIMPLEMENTATION",
        "reviewed_scope": ["instruction.md", "resources.json", "paper/**", "tests/**"],
        "verdict": "PASS",
        "weighted_score": 100.0,
        "criteria": criteria,
        "dimensions": dimensions,
        "hard_gates": gates,
        "checker_probes": probes,
        "readiness": readiness,
        "parameter_assessment": parameters,
        "scientific_risk_patterns": patterns,
        "diagnostic_adjudications": [],
        "open_confirmed_findings": [],
        "limitations": [],
    }


def reasoning_absent_decision(*modes: str) -> dict:
    value = decision()
    value["criteria"]["2.3"]["status"] = "FAIL"
    gate = next(
        item
        for item in value["hard_gates"]
        if item["code"] == "SCIENTIFIC_REASONING_ABSENT"
    )
    gate.update(
        {"status": "FAIL", "disposition": "ABANDON", "failure_modes": list(modes)}
    )
    value["open_confirmed_findings"] = [
        {
            "finding_id": "F-SCI-REASONING-ABSENT",
            "title": "Final task lacks substantive scientific reasoning.",
            "severity": "FATAL",
            "dimension": "C03",
            "repairable": False,
            "hard_gate": True,
            "hard_gate_code": "SCIENTIFIC_REASONING_ABSENT",
            "disposition": "ABANDON",
            "failure_modes": list(modes),
            "evidence": evidence("instruction leaves only mechanical work"),
        }
    ]
    value["verdict"] = "REJECT"
    return value


class AgentFinalDecisionTests(unittest.TestCase):
    def test_full_quality_contract_passes(self) -> None:
        self.assertEqual(module.validate(decision())["verdict"], "PASS")

    def test_each_2_1_to_2_8_is_mandatory_for_pass(self) -> None:
        for key in module.CRITERIA:
            with self.subTest(key=key):
                value = decision()
                value["criteria"][key]["status"] = "FAIL"
                value["verdict"] = "CONDITIONAL"
                self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")
                value["verdict"] = "PASS"
                with self.assertRaisesRegex(ValueError, "expected CONDITIONAL"):
                    module.validate(value)

    def test_data_and_model_must_be_ready(self) -> None:
        for category in ("data", "model"):
            with self.subTest(category=category):
                value = decision()
                value["readiness"][category]["status"] = "NOT_READY"
                value["verdict"] = "CONDITIONAL"
                self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_solver_generated_model_can_be_not_required(self) -> None:
        value = decision()
        value["readiness"]["model"] = {
            "status": "NOT_REQUIRED",
            "rationale": "The task trains the model as its output.",
            "evidence": evidence("instruction requires model training"),
            "resources": [],
        }
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_parameter_policy_failure_blocks_pass(self) -> None:
        value = decision()
        value["parameter_assessment"]["fixed_or_source_required"]["status"] = "FAIL"
        value["verdict"] = "CONDITIONAL"
        self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_parameter_assessment_requires_all_2_3_buckets(self) -> None:
        value = decision()
        del value["parameter_assessment"]["derived_or_coupled"]
        with self.assertRaisesRegex(ValueError, "derived_or_coupled"):
            module.validate(value)

    def test_representation_equivalent_parameter_can_pass(self) -> None:
        value = decision()
        value["parameter_assessment"]["representation_equivalent"]["items"] = [
            parameter_item(
                "orientation_mapping",
                source_status="REPRESENTATION_EQUIVALENT",
                resolution="EQUIVALENCE_TRANSFORM",
                scoring_sensitive=True,
                execution_required=True,
                paper_reference_required=False,
            )
        ]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_solver_selectable_convergence_parameter_can_pass(self) -> None:
        value = decision()
        value["parameter_assessment"]["solver_selectable"]["items"] = [
            parameter_item(
                "scf_convergence",
                source_status="SOLVER_SELECTABLE",
                resolution="SOLVER_CHOICE_JUSTIFIED",
                scoring_sensitive=False,
                execution_required=True,
                paper_reference_required=False,
            )
        ]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_self_contained_extension_parameter_can_pass(self) -> None:
        value = decision()
        value["reproduction_intent"] = "SCIENTIFIC_EXTENSION"
        value["parameter_assessment"]["fixed_or_source_required"]["items"] = [
            parameter_item(
                "extension_temperature",
                source_status="PACKAGE_DEFINED",
                resolution="PACKAGE_SELF_CONTAINED",
                scoring_sensitive=True,
                execution_required=True,
                paper_reference_required=False,
            )
        ]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_parameter_dependency_cycle_is_rejected(self) -> None:
        value = decision()
        value["parameter_assessment"]["derived_or_coupled"]["items"] = [
            parameter_item(
                "strain_axis",
                source_status="PAPER_DERIVED",
                resolution="UNIQUE_DERIVATION",
                depends_on=["cell_orientation"],
            ),
            parameter_item(
                "cell_orientation",
                source_status="PAPER_DERIVED",
                resolution="UNIQUE_DERIVATION",
                depends_on=["strain_axis"],
            ),
        ]
        with self.assertRaisesRegex(ValueError, "contains a cycle"):
            module.validate(value)

    def test_essential_missing_paper_parameter_requires_abandon_gate(self) -> None:
        value = decision()
        value["parameter_assessment"]["fixed_or_source_required"].update(
            {
                "status": "FAIL",
                "items": [
                    parameter_item(
                        "loading_rate",
                        source_status="MISSING",
                        resolution="UNRESOLVED",
                        scoring_sensitive=True,
                    )
                ],
            }
        )
        with self.assertRaisesRegex(
            ValueError,
            "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE Gate must agree",
        ):
            module.validate(value)

        value["criteria"]["2.3"]["status"] = "FAIL"
        value["scientific_risk_patterns"]["SIMULATION_CONTRACT_UNDERDETERMINED"][
            "status"
        ] = "FAIL"
        gate = next(
            item
            for item in value["hard_gates"]
            if item["code"] == "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE"
        )
        gate.update({"status": "FAIL", "disposition": "ABANDON"})
        value["open_confirmed_findings"] = [
            {
                "finding_id": "F-ESSENTIAL-PARAMETER",
                "title": "Paper omits an essential loading rate.",
                "pattern_id": "SIMULATION_CONTRACT_UNDERDETERMINED",
                "severity": "FATAL",
                "dimension": "C03",
                "repairable": False,
                "hard_gate": True,
                "hard_gate_code": "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE",
                "disposition": "ABANDON",
                "failure_modes": [],
                "evidence": evidence("paper and supplement omit loading rate"),
            }
        ]
        value["verdict"] = "REJECT"
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_all_scientific_risk_patterns_are_required(self) -> None:
        value = decision()
        del value["scientific_risk_patterns"]["UNSUPPORTED_SYNTHETIC_GOLD"]
        with self.assertRaisesRegex(ValueError, "every canonical pattern"):
            module.validate(value)

    def test_failed_pattern_requires_failed_criterion_and_matching_finding(self) -> None:
        value = decision()
        pattern_id = "UNSUPPORTED_SYNTHETIC_GOLD"
        value["scientific_risk_patterns"][pattern_id]["status"] = "FAIL"
        with self.assertRaisesRegex(ValueError, "criteria.2.6 FAIL"):
            module.validate(value)

        value["criteria"]["2.6"]["status"] = "FAIL"
        value["verdict"] = "CONDITIONAL"
        with self.assertRaisesRegex(ValueError, "matching confirmed findings"):
            module.validate(value)

        value["open_confirmed_findings"] = [
            {
                "finding_id": "F-SYNTHETIC-GOLD",
                "title": "Gold was generated by random interpolation.",
                "pattern_id": pattern_id,
                "severity": "HIGH",
                "dimension": "C04",
                "repairable": True,
                "hard_gate": False,
                "hard_gate_code": None,
                "disposition": "REPAIR",
                "failure_modes": [],
                "evidence": evidence("tests/make_gold.py uses random interpolation"),
            }
        ]
        self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_not_applicable_pattern_does_not_block_pass(self) -> None:
        value = decision()
        value["scientific_risk_patterns"]["UNSPECIFIED_MD_CONDITIONS"][
            "status"
        ] = "NOT_APPLICABLE"
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_solution_is_forbidden_from_review_scope_and_evidence(self) -> None:
        value = decision()
        value["reviewed_scope"].append("solution/**")
        with self.assertRaisesRegex(ValueError, "must not include solution"):
            module.validate(value)

        value = decision()
        value["criteria"]["2.3"]["evidence"][0]["path"] = "solution/solve.sh"
        with self.assertRaisesRegex(ValueError, "must not reference solution"):
            module.validate(value)

    def test_applicable_checker_probe_must_not_be_unassessed(self) -> None:
        value = decision()
        value["checker_probes"]["quality_gradient"]["status"] = "NOT_ASSESSABLE"
        value["verdict"] = "NOT_ASSESSABLE"
        self.assertEqual(module.validate(value)["verdict"], "NOT_ASSESSABLE")

    def test_probe_claims_are_cross_checked_against_raw_observations(self) -> None:
        value = decision()
        observations = []
        for name in module.PROBES:
            case_id = name
            observations.append(
                {
                    "case_id": case_id,
                    "probe_class": name,
                    "status": "OBSERVED",
                    "reward": 0.0,
                    "breakdown": {},
                }
            )
            value["checker_probes"][name]["evidence"] = [
                {
                    "source_kind": "PROBE",
                    "path": "checker_observations.json",
                    "locator": case_id,
                    "quote_or_result": "executed",
                }
            ]

        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "checker_observations.json"
            path.write_text(
                json.dumps({"observations": observations}), encoding="utf-8"
            )
            module.validate_probe_observations(value, [path])

            observations_by_id = {item["case_id"]: item for item in observations}
            observations_by_id["quality_gradient"]["status"] = "NOT_ASSESSED"
            path.write_text(
                json.dumps({"observations": observations}), encoding="utf-8"
            )
            with self.assertRaisesRegex(
                ValueError,
                "quality_gradient PASS requires an executed OBSERVED case",
            ):
                module.validate_probe_observations(value, [path])

    def test_false_positive_schema_diagnostic_does_not_block(self) -> None:
        value = decision()
        value["diagnostic_adjudications"] = [
            {
                "diagnostic": "INVALID_GRADING_SPEC_SCHEMA",
                "disposition": "DISMISSED_FALSE_POSITIVE",
                "reason": "Equivalent valid contract verified directly.",
                "evidence": evidence("source and runtime agree"),
            }
        ]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_source_backed_smoke_trend_candidate_can_be_dismissed(self) -> None:
        value = decision()
        value["reproduction_intent"] = "METHOD_REIMPLEMENTATION"
        value["scientific_risk_patterns"]["METHOD_REFERENCE_MISMATCH"][
            "rationale"
        ] = (
            "The reduced system is scored only on a source-backed ordering, "
            "not on equality with paper values."
        )
        value["scientific_risk_patterns"]["UNSUPPORTED_SYNTHETIC_GOLD"][
            "rationale"
        ] = (
            "The checker evaluates the documented ordering directly and stores "
            "no fitted pseudo-Gold magnitudes."
        )
        value["diagnostic_adjudications"] = [
            {
                "diagnostic": "SMOKE_OR_SYNTHETIC_REFERENCE",
                "disposition": "DISMISSED_FALSE_POSITIVE",
                "reason": (
                    "The keyword belongs to the reduced runner; acceptance is "
                    "the authoritative source-backed trend."
                ),
                "evidence": evidence("checker tests A > B and reversed ordering"),
            }
        ]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_score_below_80_is_conditional_even_when_criteria_pass(self) -> None:
        value = decision()
        value["dimensions"][0]["normalized"] = 0
        value["weighted_score"] = 90.0
        self.assertEqual(module.validate(value)["verdict"], "PASS")
        value["dimensions"][1]["normalized"] = 0
        value["weighted_score"] = 70.0
        value["verdict"] = "CONDITIONAL"
        self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_hard_gate_forces_reject(self) -> None:
        value = decision()
        value["hard_gates"][0]["status"] = "FAIL"
        value["hard_gates"][0]["disposition"] = "REPAIR"
        value["verdict"] = "REJECT"
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_pure_information_extraction_is_rejected_and_abandoned(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_pure_algebraic_computation_is_rejected_and_abandoned(self) -> None:
        value = reasoning_absent_decision("PURE_ALGEBRAIC_COMPUTATION")
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_extraction_plus_algebra_records_both_modes_on_one_gate(self) -> None:
        value = reasoning_absent_decision(
            "PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION"
        )
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_model_and_evidence_reasoning_examples_do_not_trigger_gate(self) -> None:
        for rationale in (
            "Task requires validating model applicability before computing a value.",
            "Task requires comparing conflicting evidence before producing a table.",
        ):
            with self.subTest(rationale=rationale):
                value = decision()
                gate = next(
                    item
                    for item in value["hard_gates"]
                    if item["code"] == "SCIENTIFIC_REASONING_ABSENT"
                )
                gate["rationale"] = rationale
                self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_reasoning_absence_rejects_inconsistent_dispositions(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        gate = next(
            item
            for item in value["hard_gates"]
            if item["code"] == "SCIENTIFIC_REASONING_ABSENT"
        )
        gate["disposition"] = "REPAIR"
        with self.assertRaisesRegex(ValueError, "requires disposition ABANDON"):
            module.validate(value)

        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["open_confirmed_findings"][0]["repairable"] = True
        value["open_confirmed_findings"][0]["disposition"] = "REPAIR"
        with self.assertRaisesRegex(ValueError, "must be non-repairable ABANDON"):
            module.validate(value)

    def test_reasoning_absence_requires_reject_and_matching_c03_failure(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["criteria"]["2.3"]["status"] = "PASS"
        with self.assertRaisesRegex(ValueError, "criteria.2.3 FAIL"):
            module.validate(value)

        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["verdict"] = "CONDITIONAL"
        with self.assertRaisesRegex(ValueError, "expected REJECT"):
            module.validate(value)

    def test_version_2_2_is_rejected(self) -> None:
        value = decision()
        value["schema_version"] = "materials-agent-final-decision/2.2"
        with self.assertRaisesRegex(ValueError, "2.3"):
            module.validate(value)


if __name__ == "__main__":
    unittest.main()
