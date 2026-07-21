"""Review-side Agent adjudication for unavailable D1-D6 checks.

The deterministic contract remains the machine authority.  This module only
validates an external, source-bound assessment and derives an additive
effective view for checks that the machine could not assess.  It deliberately
does not accept paper, solution, metadata, or scientific-quality evidence and
does not merge Agent-quality findings into the deterministic lane.
"""

from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from typing import Any, Iterable

from artifact_schema import (
    AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION,
    EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION,
)
from deterministic_contract import (
    CHECK_IDS,
    CHECK_STATUSES,
    UNAVAILABLE_CHECK_STATUSES,
    validate_deterministic_contract,
)


AGENT_CONTRACT_STATUSES = frozenset({"PASS", "NOT_PROVEN"})
AGENT_CONTRACT_LANE = "deterministic_core"
AGENT_PROVENANCE_SOURCE = "EXTERNAL_AGENT_ASSESSMENT"
CONTRACT_WIRING_SCOPE = "CONTRACT_WIRING"

ALLOWED_EVIDENCE_SOURCE_KINDS = frozenset(
    {"INSTRUCTION", "GRADING_SPEC", "DETERMINISTIC_PROBE_ARTIFACT"}
)
ALLOWED_EVIDENCE_SCOPES = frozenset(
    {"CONTRACT_WIRING", "DETERMINISTIC_CONTRACT"}
)
FORBIDDEN_EVIDENCE_TOKENS = frozenset(
    {
        "paper",
        "solution",
        "oracle",
        "manifest",
        "metadata",
        "gold",
        "golds",
        "target",
        "targets",
        "tolerance",
        "tolerances",
        "formula",
        "formulas",
        "unit",
        "units",
        "science",
        "scientific",
        "sciences",
        "quality",
    }
)

_GRADING_SPEC_PATH = re.compile(
    r"^tests/(?:[^/]+/)*grading_spec(?:\.[^/]*)?$"
)
_PROBE_PATH_PREFIXES = (
    "deterministic_core/",
    "deterministic_probe_artifacts/",
)
_PROBE_FILE_NAMES = frozenset(
    {"probe_results.json", "report.json", "probe_artifacts.json"}
)
_EVIDENCE_ALLOWED_KEYS = frozenset(
    {
        "id",
        "source_kind",
        "kind",
        "path",
        "source",
        "package_file",
        "quote",
        "excerpt",
        "locator",
        "claim_scope",
        "scope",
        "claim",
        "artifact_digest",
        "sha256",
    }
)
_ASSESSMENT_ALLOWED_KEYS = frozenset(
    {
        "schema_version",
        "lane",
        "machine_contract_digest",
        "machine_schema_version",
        "machine_registry_version",
        "checks",
        "provenance",
        "assessment_digest",
    }
)
_CHECK_ASSESSMENT_ALLOWED_KEYS = frozenset(
    {"check_id", "status", "rationale", "scope", "claim_scope", "evidence"}
)


def _canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _copy_without(value: dict[str, Any], key: str) -> dict[str, Any]:
    copied = deepcopy(value)
    copied.pop(key, None)
    return copied


def agent_contract_assessment_digest(assessment: dict[str, Any]) -> str:
    """Return the self-binding digest for an external assessment."""

    return _canonical_hash(_copy_without(assessment, "assessment_digest"))


def effective_contract_digest(contract: dict[str, Any]) -> str:
    """Return the self-binding digest for an effective contract."""

    return _canonical_hash(_copy_without(contract, "effective_contract_digest"))


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_relative_path(value: Any, context: str) -> str:
    if not _non_empty_string(value):
        raise ValueError(f"{context} evidence path is required")
    path = value.strip().replace("\\", "/")
    parts = path.split("/")
    if (
        path.startswith("/")
        or any(part in {"", ".", ".."} for part in parts)
        or ":" in parts[0]
    ):
        raise ValueError(f"{context} evidence path is not a safe relative path")
    return path


def _canonical_source_kind(value: Any, path: str) -> str:
    if isinstance(value, str):
        normalized = value.strip().upper().replace("-", "_")
        aliases = {
            "INSTRUCTION_MD": "INSTRUCTION",
            "PACKAGE_INSTRUCTION": "INSTRUCTION",
            "GRADING_SPEC_JSON": "GRADING_SPEC",
            "PACKAGE_GRADING_SPEC": "GRADING_SPEC",
            "DETERMINISTIC_PROBE": "DETERMINISTIC_PROBE_ARTIFACT",
            "PROBE_ARTIFACT": "DETERMINISTIC_PROBE_ARTIFACT",
        }
        normalized = aliases.get(normalized, normalized)
        if normalized in ALLOWED_EVIDENCE_SOURCE_KINDS:
            return normalized
    if path == "instruction.md":
        return "INSTRUCTION"
    if _GRADING_SPEC_PATH.fullmatch(path):
        return "GRADING_SPEC"
    if any(path.startswith(prefix) for prefix in _PROBE_PATH_PREFIXES):
        return "DETERMINISTIC_PROBE_ARTIFACT"
    raise ValueError("contract evidence source kind is not allowed")


def _validate_scope(value: Any, context: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{context} evidence claim scope is required")
    normalized = value.strip().upper().replace("-", "_")
    if normalized not in ALLOWED_EVIDENCE_SCOPES:
        raise ValueError(
            f"{context} evidence claim scope is outside contract wiring"
        )
    return normalized


def _contains_forbidden_scope(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    lowered = value.casefold()
    for token in FORBIDDEN_EVIDENCE_TOKENS:
        if re.search(rf"(?<![a-z]){re.escape(token)}(?![a-z])", lowered):
            return token
    return None


def validate_contract_evidence(value: Any, *, context: str = "evidence") -> dict[str, Any]:
    """Validate one source-bound contract-wiring evidence item.

    The accepted package surface is intentionally narrower than the general
    review evidence boundary.  In particular, ``tests/checker.py`` is not
    accepted here; deterministic probe artifacts are the only non-declaration
    input allowed.
    """

    if not isinstance(value, dict):
        raise ValueError(f"{context} must be an object")
    unknown = sorted(set(value) - _EVIDENCE_ALLOWED_KEYS)
    if unknown:
        raise ValueError(f"{context} has unsupported fields: {unknown}")
    for key in value:
        token = _contains_forbidden_scope(key)
        if token is not None:
            raise ValueError(f"{context} uses forbidden evidence field: {key}")

    raw_path = value.get("path", value.get("source", value.get("package_file")))
    path = _safe_relative_path(raw_path, context)
    source_kind = _canonical_source_kind(
        value.get("source_kind", value.get("kind")), path
    )
    scope = _validate_scope(
        value.get("claim_scope", value.get("scope")), context
    )

    path_token = _contains_forbidden_scope(path)
    if path_token is not None:
        raise ValueError(f"{context} uses forbidden evidence path: {path}")
    if source_kind == "INSTRUCTION" and path != "instruction.md":
        raise ValueError(f"{context} instruction evidence path is invalid")
    if source_kind == "GRADING_SPEC" and not _GRADING_SPEC_PATH.fullmatch(path):
        raise ValueError(f"{context} grading-spec evidence path is invalid")
    if source_kind == "DETERMINISTIC_PROBE_ARTIFACT" and not (
        any(path.startswith(prefix) for prefix in _PROBE_PATH_PREFIXES)
        and (
            path.rsplit("/", 1)[-1] in _PROBE_FILE_NAMES
            or "probe" in path.rsplit("/", 1)[-1].casefold()
        )
    ):
        raise ValueError(f"{context} deterministic probe artifact path is invalid")

    for key in ("claim_scope", "scope", "claim"):
        token = _contains_forbidden_scope(value.get(key))
        if token is not None:
            raise ValueError(f"{context} uses forbidden {key}: {token}")
    normalized = deepcopy(value)
    normalized["path"] = path
    normalized["source_kind"] = source_kind
    normalized["claim_scope"] = scope
    normalized.pop("source", None)
    normalized.pop("package_file", None)
    normalized.pop("kind", None)
    normalized.pop("scope", None)
    return normalized


def _validate_provenance(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("contract adjudication provenance must be an object")
    source_kind = value.get("source_kind")
    if source_kind != AGENT_PROVENANCE_SOURCE:
        raise ValueError("contract adjudication provenance source is invalid")
    if value.get("external") is False:
        raise ValueError("contract adjudication provenance must be external")
    return deepcopy(value)


def validate_agent_contract_assessment(
    assessment: Any, machine_contract: dict[str, Any]
) -> dict[str, Any]:
    """Validate an external per-check PASS/NOT_PROVEN assessment."""

    machine = validate_deterministic_contract(machine_contract)
    if not isinstance(assessment, dict):
        raise ValueError("agent contract assessment must be an object")
    unknown = sorted(set(assessment) - _ASSESSMENT_ALLOWED_KEYS)
    if unknown:
        raise ValueError(f"agent contract assessment has unsupported fields: {unknown}")
    if assessment.get("schema_version") != AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION:
        raise ValueError("agent contract assessment schema_version is invalid")
    if assessment.get("lane") != AGENT_CONTRACT_LANE:
        raise ValueError("agent contract assessment lane is invalid")
    if assessment.get("machine_schema_version") != machine["schema_version"]:
        raise ValueError("agent contract machine schema binding is stale")
    if assessment.get("machine_registry_version") != machine["registry_version"]:
        raise ValueError("agent contract machine registry binding is stale")
    if assessment.get("machine_contract_digest") != machine["contract_digest"]:
        raise ValueError("agent contract machine contract digest is stale")
    _validate_provenance(assessment.get("provenance"))

    checks = assessment.get("checks")
    if not isinstance(checks, list) or [
        item.get("check_id") if isinstance(item, dict) else None
        for item in checks
    ] != list(CHECK_IDS):
        raise ValueError("agent contract checks must contain D1-D6 in order")

    normalized_checks: list[dict[str, Any]] = []
    for item in checks:
        if not isinstance(item, dict):
            raise ValueError("agent contract check assessment must be an object")
        unknown_check_fields = sorted(
            set(item) - _CHECK_ASSESSMENT_ALLOWED_KEYS
        )
        if unknown_check_fields:
            raise ValueError(
                "agent contract check has unsupported fields: "
                f"{unknown_check_fields}"
            )
        if item.get("status") not in AGENT_CONTRACT_STATUSES:
            raise ValueError("agent contract check status is invalid")
        scope = item.get("claim_scope", item.get("scope"))
        if scope is None:
            scope = CONTRACT_WIRING_SCOPE
        scope = _validate_scope(scope, f"{item['check_id']}")
        rationale = item.get("rationale")
        if not _non_empty_string(rationale):
            raise ValueError(
                f"{item['check_id']} agent contract rationale is required"
            )
        evidence = item.get("evidence", [])
        if not isinstance(evidence, list):
            raise ValueError(f"{item['check_id']} contract evidence must be a list")
        if item["status"] == "PASS" and not evidence:
            raise ValueError(
                f"{item['check_id']} PASS requires contract evidence"
            )
        normalized_checks.append(
            {
                "check_id": item["check_id"],
                "status": item["status"],
                "scope": scope,
                "rationale": rationale.strip(),
                "evidence": [
                    validate_contract_evidence(
                        evidence_item,
                        context=f"{item['check_id']} evidence {index}",
                    )
                    for index, evidence_item in enumerate(evidence, start=1)
                ],
            }
        )

    normalized = {
        "schema_version": assessment["schema_version"],
        "lane": assessment["lane"],
        "machine_contract_digest": assessment["machine_contract_digest"],
        "machine_schema_version": assessment["machine_schema_version"],
        "machine_registry_version": assessment["machine_registry_version"],
        "checks": normalized_checks,
        "provenance": _validate_provenance(assessment["provenance"]),
        "assessment_digest": assessment.get("assessment_digest"),
    }
    expected_digest = agent_contract_assessment_digest(normalized)
    if normalized["assessment_digest"] != expected_digest:
        raise ValueError("agent contract assessment digest is stale")
    normalized["assessment_digest"] = expected_digest
    return normalized


def make_agent_contract_assessment(
    machine_contract: dict[str, Any],
    checks: Iterable[dict[str, Any]] | dict[str, Any],
    *,
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a correctly bound assessment for an external Agent artifact."""

    machine = validate_deterministic_contract(machine_contract)
    if isinstance(checks, dict):
        source = []
        for check_id in CHECK_IDS:
            item = checks[check_id]
            if isinstance(item, str):
                item = {"status": item}
            source.append({"check_id": check_id, **item})
    else:
        source = list(checks)
    if provenance is None:
        provenance = {
            "source_kind": AGENT_PROVENANCE_SOURCE,
            "external": True,
        }
    normalized_checks: list[dict[str, Any]] = []
    for item in source:
        if not isinstance(item, dict):
            normalized_checks.append(item)
            continue
        evidence = item.get("evidence", [])
        normalized_checks.append(
            {
                "check_id": item.get("check_id"),
                "status": item.get("status"),
                "scope": item.get(
                    "claim_scope", item.get("scope", CONTRACT_WIRING_SCOPE)
                ),
                "rationale": item.get("rationale", ""),
                "evidence": [
                    validate_contract_evidence(
                        evidence_item,
                        context=f"{item.get('check_id', 'unknown')} evidence {index}",
                    )
                    for index, evidence_item in enumerate(evidence, start=1)
                ],
            }
        )
    value: dict[str, Any] = {
        "schema_version": AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION,
        "lane": AGENT_CONTRACT_LANE,
        "machine_contract_digest": machine["contract_digest"],
        "machine_schema_version": machine["schema_version"],
        "machine_registry_version": machine["registry_version"],
        "checks": normalized_checks,
        "provenance": provenance,
        "assessment_digest": None,
    }
    value["assessment_digest"] = agent_contract_assessment_digest(value)
    value = validate_agent_contract_assessment(value, machine)
    return value


def _as_items(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, dict):
        return list(value.values())
    if isinstance(value, (list, tuple, set, frozenset)):
        return list(value)
    return [value]


def _item_applies(item: Any, check_id: str) -> bool:
    if not isinstance(item, dict):
        return True
    item_check = item.get("check_id", item.get("deterministic_check"))
    return item_check in {None, check_id}


def _context_failure(
    value: Any,
    check_id: str,
    *,
    failure_keys: frozenset[str],
    failure_values: frozenset[str] = frozenset(),
) -> bool:
    for item in _as_items(value):
        if not _item_applies(item, check_id):
            continue
        if isinstance(item, bool):
            if item:
                return True
            continue
        if isinstance(item, str):
            if item.strip().upper() in failure_values:
                return True
            continue
        if not isinstance(item, dict):
            continue
        for key in failure_keys:
            candidate = item.get(key)
            if candidate is True:
                return True
            if isinstance(candidate, str) and (
                candidate.strip().upper() in failure_values
            ):
                return True
            if isinstance(candidate, (list, tuple, set, frozenset)) and candidate:
                return True
    return False


def check_eligibility(
    machine_check: dict[str, Any],
    *,
    hard_gates: Any = None,
    runtime_contradictions: Any = None,
    dependency_failures: Any = None,
) -> dict[str, Any]:
    """Explain whether an unavailable machine check may be overlaid."""

    if not isinstance(machine_check, dict):
        raise ValueError("machine check must be an object")
    check_id = machine_check.get("check_id")
    status = machine_check.get("status")
    reasons: list[str] = []
    if check_id not in CHECK_IDS:
        reasons.append("UNKNOWN_CHECK")
    if status not in UNAVAILABLE_CHECK_STATUSES:
        reasons.append("MACHINE_CHECK_NOT_UNAVAILABLE")
    if machine_check.get("proven_finding_ids"):
        reasons.append("PROVEN_FINDING")
    if (
        machine_check.get("blocking_finding_ids")
        or machine_check.get("blocking") is True
    ):
        reasons.append("BLOCKING_FINDING")
    if (
        machine_check.get("blocked_by")
        or machine_check.get("dependency_failure") is True
        or str(machine_check.get("dependency_status", "")).upper()
        in {"FAIL", "FAILED", "BLOCKED", "ERROR"}
    ):
        reasons.append("DEPENDENCY_FAILURE")
    if machine_check.get("missing_inputs"):
        reasons.append("DEPENDENCY_FAILURE")
    if machine_check.get("hard_gate") is True:
        reasons.append("HARD_GATE")
    if _context_failure(
        dependency_failures,
        check_id,
        failure_keys=frozenset(
            {"failed", "failure", "dependency_failure", "blocked", "status"}
        ),
        failure_values=frozenset(
            {"FAIL", "FAILED", "BLOCKED", "ERROR", "NOT_ASSESSABLE"}
        ),
    ):
        reasons.append("DEPENDENCY_FAILURE")
    if _context_failure(
        hard_gates,
        check_id,
        failure_keys=frozenset(
            {"triggered", "hard_gate", "failed", "status", "result"}
        ),
        failure_values=frozenset(
            {"FAIL", "FAILED", "REJECT", "TRIGGERED", "NOT_ASSESSABLE"}
        ),
    ):
        reasons.append("HARD_GATE")
    if _context_failure(
        runtime_contradictions,
        check_id,
        failure_keys=frozenset(
            {
                "usable_runtime_contradiction",
                "runtime_contradiction",
                "contradiction",
                "failed",
                "status",
            }
        ),
        failure_values=frozenset(
            {
                "FAIL",
                "FAILED",
                "CONTRADICTED",
                "CONTRADICTION",
                "USABLE_CONTRADICTION",
            }
        ),
    ):
        reasons.append("USABLE_RUNTIME_CONTRADICTION")

    # A check-local runtime status is relevant only when explicitly marked as a
    # contradiction.  A plain unavailable status must not be invented into a
    # runtime failure.
    if machine_check.get("usable_runtime_contradiction") is True:
        reasons.append("USABLE_RUNTIME_CONTRADICTION")
    if machine_check.get("runtime_contradiction") is True:
        reasons.append("USABLE_RUNTIME_CONTRADICTION")
    if str(machine_check.get("runtime_status", "")).upper() in {
        "CONTRADICTED",
        "CONTRADICTION",
        "USABLE_CONTRADICTION",
    }:
        reasons.append("USABLE_RUNTIME_CONTRADICTION")

    unique_reasons = list(dict.fromkeys(reasons))
    return {
        "check_id": check_id,
        "eligible": not unique_reasons,
        "reason_codes": unique_reasons,
        "reasons": [
            "Eligible unavailable check."
            if not unique_reasons
            else "Check cannot be overlaid: " + ", ".join(unique_reasons)
        ],
    }


def _effective_repair_summary(
    machine: dict[str, Any], checks: list[dict[str, Any]]
) -> dict[str, Any]:
    required_findings = deepcopy(
        machine["repair_summary"].get("required_findings", [])
    )
    required_ids = [
        item["finding_id"]
        for item in required_findings
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    ]
    failed_or_unavailable = any(
        item["status"] in UNAVAILABLE_CHECK_STATUSES or item["status"] == "FAIL"
        for item in checks
    )
    if required_findings:
        state = "REQUIRED"
        reason = (
            "Machine-proven OPEN deterministic blockers remain authoritative; "
            "Agent adjudication cannot suppress them."
        )
    elif failed_or_unavailable:
        state = "NOT_APPLICABLE"
        reason = (
            "One or more deterministic checks remain unavailable or failed "
            "after contract adjudication."
        )
    else:
        state = "CLEAN"
        reason = (
            "All D1-D6 checks are effective PASS or advisory-only after "
            "eligible unavailable checks were adjudicated."
        )
    return {
        "schema_version": machine["schema_version"],
        "registry_version": machine["registry_version"],
        "machine_contract_digest": machine["contract_digest"],
        "state": state,
        "required_findings": required_findings,
        "required_finding_ids": required_ids,
        "reason": reason,
        "complete": state == "CLEAN",
    }


def derive_effective_contract(
    machine_contract: dict[str, Any],
    assessment: dict[str, Any],
    *,
    hard_gates: Any = None,
    runtime_contradictions: Any = None,
    dependency_failures: Any = None,
    agent_quality_findings: Any = None,
) -> dict[str, Any]:
    """Derive an effective contract without changing machine evidence.

    ``agent_quality_findings`` is accepted solely to make the lane boundary
    explicit to callers; it is never read into the effective deterministic
    contract and cannot make a check clean.
    """

    machine = validate_deterministic_contract(machine_contract)
    adjudication = validate_agent_contract_assessment(assessment, machine)
    by_id = {item["check_id"]: item for item in adjudication["checks"]}
    effective_checks: list[dict[str, Any]] = []
    eligibility_records: list[dict[str, Any]] = []
    machine_status = {
        item["check_id"]: item["status"] for item in machine["checks"]
    }

    for original in machine["checks"]:
        item = deepcopy(original)
        check_id = original["check_id"]
        agent_item = by_id[check_id]
        eligibility = check_eligibility(
            original,
            hard_gates=hard_gates,
            runtime_contradictions=runtime_contradictions,
            dependency_failures=dependency_failures,
        )
        status = original["status"]
        applied = (
            original["status"] in UNAVAILABLE_CHECK_STATUSES
            and agent_item["status"] == "PASS"
            and eligibility["eligible"]
        )
        if applied:
            status = "PASS"
        item["machine_status"] = original["status"]
        item["status"] = status
        item["effective_status"] = status
        item["machine_reason"] = original.get("reason")
        item["adjudication_status"] = agent_item["status"]
        item["adjudication_scope"] = agent_item["scope"]
        item["adjudication_applied"] = applied
        item["adjudication_eligibility"] = eligibility
        if applied:
            item["reason"] = (
                "Machine check was unavailable and an eligible external "
                "contract-wiring PASS established effective availability."
            )
        effective_checks.append(item)
        eligibility_records.append(
            {
                "check_id": check_id,
                "agent_status": agent_item["status"],
                "eligible": eligibility["eligible"],
                "applied": applied,
                "reason_codes": eligibility["reason_codes"],
            }
        )

    effective: dict[str, Any] = {
        "schema_version": EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION,
        "registry_version": machine["registry_version"],
        "check_registry": deepcopy(machine["check_registry"]),
        "lane": "deterministic_core",
        "machine_contract": deepcopy(machine),
        "machine_contract_digest": machine["contract_digest"],
        "machine_status": {
            "checks": machine_status,
            "repair_summary_state": machine["repair_summary"]["state"],
        },
        "checks": effective_checks,
        "repair_summary": _effective_repair_summary(
            machine, effective_checks
        ),
        "adjudication": {
            "schema_version": adjudication["schema_version"],
            "assessment_digest": adjudication["assessment_digest"],
            "machine_contract_digest": adjudication["machine_contract_digest"],
            "provenance": deepcopy(adjudication["provenance"]),
            "eligible_check_ids": [
                item["check_id"]
                for item in eligibility_records
                if item["eligible"]
            ],
            "applied_check_ids": [
                item["check_id"]
                for item in eligibility_records
                if item["applied"]
            ],
            "checks": eligibility_records,
            "lane_isolation": {
                "agent_quality_findings_merged": False,
                "agent_quality_findings_supplied": bool(agent_quality_findings),
                "machine_findings_preserved": True,
            },
        },
        "effective_contract_digest": None,
    }
    effective["effective_contract_digest"] = effective_contract_digest(effective)
    return effective


def validate_effective_contract(value: Any) -> dict[str, Any]:
    """Validate the additive effective-contract artifact and its transitions."""

    if not isinstance(value, dict):
        raise ValueError("effective deterministic contract must be an object")
    if value.get("schema_version") != EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION:
        raise ValueError("effective deterministic contract schema_version is invalid")
    machine = validate_deterministic_contract(value.get("machine_contract"))
    if value.get("machine_contract_digest") != machine["contract_digest"]:
        raise ValueError("effective machine contract digest is stale")
    if value.get("registry_version") != machine["registry_version"]:
        raise ValueError("effective deterministic registry is stale")
    if value.get("check_registry") != machine["check_registry"]:
        raise ValueError("effective deterministic check registry is stale")
    machine_status = value.get("machine_status")
    if not isinstance(machine_status, dict):
        raise ValueError("effective machine_status is invalid")
    if machine_status.get("checks") != {
        item["check_id"]: item["status"] for item in machine["checks"]
    }:
        raise ValueError("effective machine check statuses are stale")
    if machine_status.get("repair_summary_state") != machine["repair_summary"]["state"]:
        raise ValueError("effective machine repair status is stale")
    checks = value.get("checks")
    if not isinstance(checks, list) or [
        item.get("check_id") if isinstance(item, dict) else None
        for item in checks
    ] != list(CHECK_IDS):
        raise ValueError("effective checks must contain D1-D6 in order")
    machine_by_id = {item["check_id"]: item for item in machine["checks"]}
    for item in checks:
        if not isinstance(item, dict):
            raise ValueError("effective check must be an object")
        check_id = item["check_id"]
        source = machine_by_id[check_id]
        if item.get("machine_status") != source["status"]:
            raise ValueError("effective machine status is stale")
        if item.get("finding_ids") != source.get("finding_ids"):
            raise ValueError("effective contract suppressed machine findings")
        if item.get("blocking_finding_ids") != source.get(
            "blocking_finding_ids"
        ):
            raise ValueError("effective contract suppressed machine blockers")
        if item.get("status") not in CHECK_STATUSES:
            raise ValueError("effective check status is invalid")
        if item.get("effective_status") != item["status"]:
            raise ValueError("effective check status mirror is stale")
        eligibility = item.get("adjudication_eligibility")
        if not isinstance(eligibility, dict) or not isinstance(
            eligibility.get("eligible"), bool
        ):
            raise ValueError("effective check eligibility is invalid")
        applied = item.get("adjudication_applied")
        if not isinstance(applied, bool):
            raise ValueError("effective check adjudication flag is invalid")
        expected_applied = (
            source["status"] in UNAVAILABLE_CHECK_STATUSES
            and item.get("adjudication_status") == "PASS"
            and eligibility["eligible"]
        )
        if applied is not expected_applied:
            raise ValueError("effective check adjudication is stale")
        if item["status"] != source["status"] and not (
            source["status"] in UNAVAILABLE_CHECK_STATUSES
            and source["status"] != "FAIL"
            and item["status"] == "PASS"
            and applied
        ):
            raise ValueError("effective contract contains an unauthorized status transition")
    adjudication = value.get("adjudication")
    if not isinstance(adjudication, dict):
        raise ValueError("effective adjudication is missing")
    if adjudication.get("machine_contract_digest") != machine["contract_digest"]:
        raise ValueError("effective adjudication machine digest is stale")
    if not _non_empty_string(adjudication.get("assessment_digest")):
        raise ValueError("effective adjudication assessment digest is missing")
    _validate_provenance(adjudication.get("provenance"))
    expected_eligible_ids = [
        item["check_id"]
        for item in checks
        if item["adjudication_eligibility"]["eligible"]
    ]
    expected_applied_ids = [
        item["check_id"] for item in checks if item["adjudication_applied"]
    ]
    if adjudication.get("eligible_check_ids") != expected_eligible_ids:
        raise ValueError("effective eligible check list is stale")
    if adjudication.get("applied_check_ids") != expected_applied_ids:
        raise ValueError("effective applied check list is stale")
    if adjudication.get("checks") != [
        {
            "check_id": item["check_id"],
            "agent_status": item["adjudication_status"],
            "eligible": item["adjudication_eligibility"]["eligible"],
            "applied": item["adjudication_applied"],
            "reason_codes": item["adjudication_eligibility"]["reason_codes"],
        }
        for item in checks
    ]:
        raise ValueError("effective adjudication check records are stale")
    lane_isolation = adjudication.get("lane_isolation")
    if not isinstance(lane_isolation, dict) or (
        lane_isolation.get("agent_quality_findings_merged") is not False
        or lane_isolation.get("machine_findings_preserved") is not True
    ):
        raise ValueError("effective lane isolation is invalid")

    summary = value.get("repair_summary")
    expected_summary = _effective_repair_summary(machine, checks)
    if summary != expected_summary:
        raise ValueError("effective repair summary is stale")
    if value.get("effective_contract_digest") != effective_contract_digest(value):
        raise ValueError("effective contract digest is stale")
    return value


def resolve_publication_contract(
    machine_contract: Any,
    effective_contract: Any = None,
    assessment: Any = None,
) -> dict[str, Any]:
    """Return the strictly validated contract used for publication decisions.

    With no Agent adjudication, the machine contract is the effective
    publication contract.  When an effective artifact is present, its
    assessment, machine copy, and self-binding digest must all match the
    separately persisted machine contract.
    """

    machine = validate_deterministic_contract(machine_contract)
    if effective_contract is None:
        if assessment is not None:
            raise ValueError(
                "agent contract assessment lacks an effective deterministic contract"
            )
        return machine
    if assessment is None:
        raise ValueError(
            "effective deterministic contract lacks its assessment"
        )
    adjudication = validate_agent_contract_assessment(assessment, machine)
    effective = validate_effective_contract(effective_contract)
    if effective.get("machine_contract") != machine:
        raise ValueError("effective deterministic contract machine copy differs")
    if (
        effective.get("adjudication", {}).get("assessment_digest")
        != adjudication["assessment_digest"]
    ):
        raise ValueError("effective deterministic assessment binding differs")
    return effective


# Explicit aliases make the seam easy to discover for Review integration.
validate_agent_contract_wiring = validate_agent_contract_assessment
validate_external_assessment = validate_agent_contract_assessment
build_agent_contract_assessment = make_agent_contract_assessment
assessment_digest = agent_contract_assessment_digest
merge_effective_contract = derive_effective_contract
build_effective_contract = derive_effective_contract
effective_contract = derive_effective_contract
validate_effective_deterministic_contract = validate_effective_contract
publication_contract = resolve_publication_contract
eligible_unavailable_check = check_eligibility

