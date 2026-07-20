"""Shared D1-D6 deterministic review/repair contract.

The module intentionally owns the contract seam, not the individual D-check
implementations.  Review supplies normalized contract analysis and findings;
Repair consumes the resulting registry identities and complete blocking queue.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable


DETERMINISTIC_SCHEMA_VERSION = "materials-deterministic-contract/1.0"
DETERMINISTIC_REGISTRY_VERSION = "materials-deterministic-check-registry/1.0"
CHECK_STATUSES = frozenset({"PASS", "FAIL", "BLOCKED", "NOT_ASSESSABLE"})
REPAIR_SUMMARY_STATES = frozenset({"CLEAN", "REQUIRED", "NOT_APPLICABLE"})
CHECK_IDS = ("D1", "D2", "D3", "D4", "D5", "D6")


# Finding ownership is centralized here so Review and Repair never need to
# infer a D check from scattered C02/C04 attribution lists.
_CHECK_REGISTRY: tuple[dict[str, Any], ...] = (
    {
        "check_id": "D1",
        "name": "scored_output_declaration_consistency",
        "description": (
            "Instruction, structured output contract, and grading steps "
            "declare the same scored outputs."
        ),
        "finding_codes": (
            "OUTPUT_DECLARATION_MISMATCH",
            "OUTPUT_NOT_CONTRACTED",
            "OUTPUT_NOT_SCORED",
        ),
        "repair_class": "AUTO_FIX",
        "required_inputs": ("instruction_contract", "grading_contract"),
    },
    {
        "check_id": "D2",
        "name": "instruction_contract_internal_consistency",
        "description": (
            "Workflow, output files, output contract, and self-check "
            "declarations agree."
        ),
        "finding_codes": (
            "INSTRUCTION_INTERNAL_INCONSISTENCY",
            "EVIDENCE_NOT_ENFORCED",
            "CONTRADICTORY_OUTPUT_ROLE",
            "INSTRUCTION_ONLY_OUTPUT",
        ),
        "repair_class": "AUTO_FIX",
        "required_inputs": ("instruction_contract",),
    },
    {
        "check_id": "D3",
        "name": "checker_code_health",
        "description": (
            "Statically proven checker syntax, return-path, constant-scorer, "
            "and literal divide-by-zero defects are absent."
        ),
        "finding_codes": (
            "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
            "SCORER_MISSING_RETURN",
            "SCORER_RETURN_NOT_TOTAL",
            "ALWAYS_ZERO_SCORER",
            "ALWAYS_PASS_SCORER",
            "DIVISION_BY_ZERO_LITERAL",
            "CHECKER_CRASH",
        ),
        "repair_class": "ASSISTED_FIX",
        "required_inputs": ("checker_analysis",),
    },
    {
        "check_id": "D4",
        "name": "weight_validity_and_effective_weight",
        "description": (
            "Scoring weights are finite, normalized, and give core scoring "
            "items positive effective weight."
        ),
        "finding_codes": (
            "INVALID_WEIGHT",
            "WEIGHTS_NOT_ONE",
            "ZERO_WEIGHT_SCORING_COMPONENT",
            "INVALID_PASS_THRESHOLD",
            # This is a reachability warning until isolation proves a bypass.
            "SINGLE_COMPONENT_THRESHOLD_REACHABLE",
        ),
        "advisory_codes": ("SINGLE_COMPONENT_THRESHOLD_REACHABLE",),
        "repair_class": "ASSISTED_FIX",
        "required_inputs": ("grading_contract",),
    },
    {
        "check_id": "D5",
        "name": "package_role_and_entrypoint_completeness",
        "description": (
            "Required quality roles, parsers, and verifier/Oracle "
            "entrypoints are complete."
        ),
        "finding_codes": (
            "MISSING_FILE",
            "PARSE_ERROR",
            "SOLUTION_ROLE_MISSING",
            "SOLUTION_ORACLE_MISSING",
            "SOLUTION_ORACLE_BROKEN",
        ),
        "repair_class": "AUTO_FIX",
        "required_inputs": ("package_roles",),
    },
    {
        "check_id": "D6",
        "name": "core_output_scoring_trace",
        "description": (
            "Every core output is content-read, scorer-bound, positively "
            "weighted, finite-returning, and included in final reward."
        ),
        "finding_codes": (
            "CHECKER_CORE_TASK_UNASSESSED",
            "SCORING_COMPONENT_NOT_BOUND",
            "ZERO_WEIGHT_SCORING_COMPONENT",
            "SCORER_RETURN_NOT_TOTAL",
            "CHECKER_RESULT_UNUSABLE",
            "ADVERSARIAL_OUTPUT_PASSES",
        ),
        "repair_class": "ASSISTED_FIX",
        "required_inputs": (
            "instruction_contract",
            "grading_contract",
            "checker_analysis",
        ),
    },
)

_REGISTRY_BY_ID = {item["check_id"]: item for item in _CHECK_REGISTRY}
_OWNERSHIP: dict[str, str] = {}
for _entry in _CHECK_REGISTRY:
    for _code in _entry["finding_codes"]:
        # D4 owns the zero-weight finding as a weight fact; D6 consumes the
        # same fact as a trace failure only when a later implementation proves
        # that a core output is affected.
        _OWNERSHIP.setdefault(_code, _entry["check_id"])


def check_registry() -> list[dict[str, Any]]:
    """Return a defensive, machine-readable copy of the D1-D6 registry."""

    return json.loads(json.dumps(_CHECK_REGISTRY))


def check_for_finding_code(code: Any) -> str | None:
    """Return the authoritative D check owner for a finding code."""

    return _OWNERSHIP.get(code) if isinstance(code, str) else None


def repair_class_for_check(check_id: str) -> str:
    try:
        return str(_REGISTRY_BY_ID[check_id]["repair_class"])
    except KeyError as exc:
        raise ValueError(f"unknown deterministic check: {check_id!r}") from exc


def _is_advisory(code: Any, evidence: Any) -> bool:
    if code == "SINGLE_COMPONENT_THRESHOLD_REACHABLE":
        return True
    if isinstance(evidence, dict) and evidence.get("bypass_proven") is False:
        return True
    return False


def annotate_findings(
    findings: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Attach shared D ownership and blocking semantics to Review findings."""

    annotated: list[dict[str, Any]] = []
    for raw in findings:
        item = dict(raw)
        code = item.get("title", item.get("code"))
        check_id = check_for_finding_code(code)
        advisory = check_id is not None and _is_advisory(
            code, item.get("evidence")
        )
        proven = (
            check_id is not None
            and not advisory
            and item.get("proven_defect", True) is not False
        )
        open_finding = item.get("status", "OPEN") == "OPEN"
        repairable = item.get("repairable") is True
        blocking = bool(check_id and proven and open_finding and repairable)
        item.update(
            {
                "deterministic_check": check_id,
                "proven_defect": proven,
                "advisory": advisory,
                "blocking": blocking,
                "deterministic_repair_class": (
                    repair_class_for_check(check_id) if check_id else None
                ),
            }
        )
        annotated.append(item)
    return annotated


def _canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def deterministic_contract_digest(contract: dict[str, Any]) -> str:
    """Hash the source-bound deterministic result without its self-hash."""

    value = json.loads(json.dumps(contract))
    value.pop("contract_digest", None)
    return _canonical_hash(value)


def _input_available(inputs: dict[str, Any], required: Iterable[str]) -> bool:
    return all(isinstance(inputs.get(name), dict) for name in required)


def evaluate_deterministic_contract(
    *,
    normalized_instruction_contract: Any,
    grading_contract: Any,
    checker_analysis: Any,
    package_roles: Any,
    findings: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Build the authoritative D1-D6 result from normalized Review inputs.

    Individual D implementations can add richer evidence later without
    changing this interface.  For this foundation slice, existing proven
    finding codes are the evidence source and missing normalized inputs are
    explicitly non-assessable.
    """

    inputs = {
        "instruction_contract": normalized_instruction_contract,
        "grading_contract": grading_contract,
        "checker_analysis": checker_analysis,
        "package_roles": package_roles,
    }
    normalized_findings = annotate_findings(findings)
    by_check: dict[str, list[dict[str, Any]]] = {key: [] for key in CHECK_IDS}
    for item in normalized_findings:
        check_id = item.get("deterministic_check")
        if check_id in by_check:
            by_check[check_id].append(item)

    checks: list[dict[str, Any]] = []
    for definition in _CHECK_REGISTRY:
        check_id = definition["check_id"]
        matched = by_check[check_id]
        missing_inputs = [
            name
            for name in definition["required_inputs"]
            if not isinstance(inputs.get(name), dict)
        ]
        proven = [
            item
            for item in matched
            if item.get("proven_defect") is True
        ]
        advisory = [
            item for item in matched if item.get("advisory") is True
        ]
        blocking = [
            item
            for item in matched
            if item.get("blocking") is True
        ]
        blocked_by: list[str] = []
        if (
            check_id == "D6"
            and not proven
            and any(
                item.get("deterministic_check") == "D5"
                and item.get("proven_defect") is True
                and item.get("title")
                in {"MISSING_FILE", "PARSE_ERROR", "SOLUTION_ROLE_MISSING"}
                for item in normalized_findings
            )
        ):
            blocked_by.append("D5")
        if missing_inputs:
            status = "NOT_ASSESSABLE"
            reason = "Required normalized contract input is unavailable."
        elif proven:
            status = "FAIL"
            reason = "One or more proven deterministic findings are present."
        elif blocked_by:
            status = "BLOCKED"
            reason = "An earlier structural check prevents this check."
        else:
            status = "PASS"
            reason = (
                "No proven deterministic defect is present."
                if not advisory
                else "Only advisory deterministic risks are present."
            )
        checks.append(
            {
                "check_id": check_id,
                "name": definition["name"],
                "description": definition["description"],
                "status": status,
                "reason": reason,
                "required_inputs": list(definition["required_inputs"]),
                "missing_inputs": missing_inputs,
                "blocked_by": blocked_by,
                "finding_ids": [
                    item.get("finding_id") for item in matched
                ],
                "proven_finding_ids": [
                    item.get("finding_id") for item in proven
                ],
                "blocking_finding_ids": [
                    item.get("finding_id") for item in blocking
                ],
                "advisory_finding_ids": [
                    item.get("finding_id") for item in advisory
                ],
                "recommended_repair_class": definition["repair_class"],
                "blocking_policy": (
                    "proven_defect=true AND status=OPEN AND repairable=true"
                ),
            }
        )

    required_findings = [
        {
            "finding_id": item["finding_id"],
            "check_id": item["deterministic_check"],
            "title": item["title"],
            "status": item.get("status", "OPEN"),
            "repair_class": item["deterministic_repair_class"],
            "proven_defect": True,
            "blocking": True,
        }
        for item in normalized_findings
        if item.get("blocking") is True
    ]
    required_findings.sort(key=lambda item: item["finding_id"])
    not_assessable = any(
        item["status"] == "NOT_ASSESSABLE" for item in checks
    )
    if required_findings:
        repair_state = "REQUIRED"
        repair_reason = (
            "Every OPEN, proven, repairable D1-D6 blocker must be covered "
            "by the deterministic Repair queue."
        )
    elif not_assessable:
        repair_state = "NOT_APPLICABLE"
        repair_reason = (
            "Deterministic checks are incomplete because key normalized "
            "contract evidence is unavailable."
        )
    else:
        repair_state = "CLEAN"
        repair_reason = "All D1-D6 checks are clean or advisory-only."

    result: dict[str, Any] = {
        "schema_version": DETERMINISTIC_SCHEMA_VERSION,
        "registry_version": DETERMINISTIC_REGISTRY_VERSION,
        "check_registry": check_registry(),
        "checks": checks,
        "repair_summary": {
            "state": repair_state,
            "required_findings": required_findings,
            "required_finding_ids": [
                item["finding_id"] for item in required_findings
            ],
            "reason": repair_reason,
            "complete": repair_state == "CLEAN",
        },
        "blocking_policy": {
            "proven_defect_required": True,
            "open_status_required": True,
            "repairable_required": True,
            "advisory_risks_block": False,
        },
        "contract_digest": None,
    }
    result["contract_digest"] = deterministic_contract_digest(result)
    return result


def validate_deterministic_contract(value: Any) -> dict[str, Any]:
    """Validate the authoritative Review/Repair deterministic schema."""

    if not isinstance(value, dict):
        raise ValueError("deterministic_contract must be an object")
    if value.get("schema_version") != DETERMINISTIC_SCHEMA_VERSION:
        raise ValueError("deterministic_contract schema_version is invalid")
    if value.get("registry_version") != DETERMINISTIC_REGISTRY_VERSION:
        raise ValueError("deterministic_contract registry_version is invalid")
    if value.get("check_registry") != check_registry():
        raise ValueError("deterministic check registry is stale")
    checks = value.get("checks")
    if not isinstance(checks, list) or [
        item.get("check_id") for item in checks if isinstance(item, dict)
    ] != list(CHECK_IDS):
        raise ValueError("deterministic checks must contain D1-D6 in order")
    for item in checks:
        if (
            not isinstance(item, dict)
            or item.get("status") not in CHECK_STATUSES
            or not isinstance(item.get("finding_ids"), list)
            or not isinstance(item.get("blocking_finding_ids"), list)
            or not isinstance(item.get("advisory_finding_ids"), list)
            or not isinstance(item.get("blocked_by"), list)
        ):
            raise ValueError("deterministic check schema is invalid")
        if not all(
            isinstance(finding_id, str) and finding_id
            for finding_id in item["finding_ids"]
            + item["blocking_finding_ids"]
            + item["advisory_finding_ids"]
        ):
            raise ValueError("deterministic finding IDs are invalid")
    summary = value.get("repair_summary")
    if not isinstance(summary, dict) or summary.get("state") not in {
        "CLEAN",
        "REQUIRED",
        "NOT_APPLICABLE",
    }:
        raise ValueError("deterministic repair summary is invalid")
    required = summary.get("required_findings")
    required_ids = summary.get("required_finding_ids")
    if (
        not isinstance(required, list)
        or not isinstance(required_ids, list)
        or required_ids
        != [
            item.get("finding_id")
            for item in required
            if isinstance(item, dict)
        ]
    ):
        raise ValueError("deterministic required finding queue is invalid")
    if summary["state"] == "CLEAN" and required:
        raise ValueError("CLEAN deterministic contract has required findings")
    if summary["state"] == "REQUIRED" and not required:
        raise ValueError("REQUIRED deterministic contract has no findings")
    blocking_ids = sorted(
        {
            finding_id
            for item in checks
            for finding_id in item["blocking_finding_ids"]
        }
    )
    if sorted(required_ids) != blocking_ids:
        raise ValueError("deterministic blocking queue is incomplete")
    check_by_id = {item["check_id"]: item for item in checks}
    for item in required:
        if (
            not isinstance(item, dict)
            or item.get("finding_id") not in blocking_ids
            or item.get("check_id") not in check_by_id
            or item.get("repair_class")
            != repair_class_for_check(item["check_id"])
            or item.get("proven_defect") is not True
            or item.get("blocking") is not True
        ):
            raise ValueError("deterministic required finding is invalid")
    policy = value.get("blocking_policy")
    if not isinstance(policy, dict) or policy.get("advisory_risks_block") is not False:
        raise ValueError("deterministic blocking policy is invalid")
    expected_digest = deterministic_contract_digest(value)
    if value.get("contract_digest") != expected_digest:
        raise ValueError("deterministic contract digest is stale")
    return value


def deterministic_repair_summary(contract: dict[str, Any]) -> dict[str, Any]:
    """Return the compact source-bound repair summary for artifacts."""

    validated = validate_deterministic_contract(contract)
    return {
        "schema_version": validated["schema_version"],
        "registry_version": validated["registry_version"],
        "contract_digest": validated["contract_digest"],
        **validated["repair_summary"],
    }


def apply_deterministic_gate(
    *,
    verdict: str,
    score: float | int | None,
    hard_gate: bool,
    evidence_gaps: Iterable[str],
    contract: dict[str, Any],
) -> tuple[str, str | None]:
    """Apply the D1-D6 gate without changing rejection precedence."""

    if (
        contract["repair_summary"]["state"] != "REQUIRED"
        or verdict != "PASS"
        or hard_gate
        or list(evidence_gaps)
        or score is None
        or score < 60
    ):
        return verdict, None
    return (
        "CONDITIONAL",
        "The authoritative C01-C07 score is publishable, but one or more "
        "proven OPEN repairable D1-D6 blockers require deterministic Repair.",
    )


def validate_deterministic_plan_binding(
    report: dict[str, Any], plan: dict[str, Any]
) -> None:
    """Validate an explicitly deterministic repair plan against Review."""

    binding = plan.get("deterministic_contract")
    if binding is None:
        # Historical 0.1 plans remain readable.  New deterministic plans opt
        # into this binding by carrying the field.
        return
    contract = validate_deterministic_contract(report.get("deterministic_contract"))
    if not isinstance(binding, dict):
        raise ValueError("deterministic repair binding must be an object")
    if (
        binding.get("schema_version") != contract["schema_version"]
        or binding.get("registry_version") != contract["registry_version"]
        or binding.get("contract_digest") != contract["contract_digest"]
    ):
        raise ValueError("deterministic repair binding is stale")
    expected = contract["repair_summary"]["required_findings"]
    planned = plan.get("findings")
    if not isinstance(planned, list):
        raise ValueError("deterministic repair plan must be a batch")
    expected_ids = [item["finding_id"] for item in expected]
    planned_ids = [
        item.get("finding_id") for item in planned if isinstance(item, dict)
    ]
    if not all(isinstance(item, str) and item for item in planned_ids):
        raise ValueError("deterministic plan finding IDs are invalid")
    if planned_ids != sorted(expected_ids):
        raise ValueError(
            "deterministic repair plan must cover the complete source queue"
        )
    expected_by_id = {item["finding_id"]: item for item in expected}
    for item in planned:
        if not isinstance(item, dict):
            raise ValueError("deterministic plan finding must be an object")
        source = expected_by_id.get(item.get("finding_id"))
        if source is None:
            raise ValueError("deterministic plan finding is not in source queue")
        if item.get("deterministic_check") != source["check_id"]:
            raise ValueError("deterministic finding ownership is stale")
        if item.get("repair_class") != source["repair_class"]:
            raise ValueError("deterministic repair class is stale")
