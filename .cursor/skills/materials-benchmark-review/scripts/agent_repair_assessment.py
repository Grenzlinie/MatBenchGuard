"""Agent-authored repair assessment binding the complete OPEN queue.

Repair requires ``materials-agent-repair-assessment/1.0`` before any candidate
mutation. The assessment is CLI-validated, not a human-approval gate. Omission
of an OPEN queue finding, stale bindings, or unapproved operations fail closed.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

from artifact_schema import (
    AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION,
    require_schema,
)
from repair_findings import (
    REPAIR_LANES,
    REPAIR_SCOPES,
    build_complete_open_repair_queue,
    is_agent_quality_lane,
)


DECISIONS = frozenset({"AUTO_FIX", "ASSISTED_FIX", "ABANDON"})
AGENT_VERDICTS = frozenset(
    {"APPROVE_REPAIR", "BLOCKED_EVIDENCE", "ABANDON"}
)
_HASH_RE = re.compile(r"^sha256:[0-9a-fA-F]{64}$")
_AUTO_FIX_SCOPES = frozenset(
    {"DETERMINISTIC_WIRING", "UNIQUE_SCORING_WIRING"}
)


def sha256_json(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def sha256_path(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def report_has_validated_paper_assessment(report: dict[str, Any]) -> bool:
    """Return whether the source audit binds a validated paper assessment."""

    quality = report.get("agent_quality")
    assessment: Any = None
    if isinstance(quality, dict):
        assessment = quality.get("assessment")
        if (
            not isinstance(assessment, dict)
            and quality.get("materials_qualification")
        ):
            assessment = quality
    if isinstance(assessment, dict) and assessment.get(
        "materials_qualification"
    ):
        return True
    top_level = report.get("materials_qualification")
    if isinstance(top_level, dict) and top_level.get("classification"):
        return True
    evidence = report.get("evidence_contract")
    gaps: list[Any] = []
    if isinstance(evidence, dict) and isinstance(evidence.get("gaps"), list):
        gaps = evidence["gaps"]
    elif isinstance(report.get("gaps"), list):
        gaps = report["gaps"]
    gap_set = {item for item in gaps if isinstance(item, str)}
    if {
        "paper_assessment",
        "authoritative_materials_qualification",
    } & gap_set:
        return False
    return False


def source_open_repair_queue(report: dict[str, Any]) -> dict[str, Any]:
    """Return the complete OPEN repair queue for plan/assessment binding."""

    existing = report.get("repair_queue")
    if (
        isinstance(existing, dict)
        and isinstance(existing.get("open_finding_ids"), list)
        and existing["open_finding_ids"]
    ):
        return existing
    contract = report.get("deterministic_contract")
    if not isinstance(contract, dict):
        contract = {}
    findings = report.get("findings")
    if not isinstance(findings, list):
        findings = []
    return build_complete_open_repair_queue(contract, findings)


def _validate_evidence_item(
    item: Any, *, context: str
) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise ValueError(f"{context} evidence entry must be an object")
    source_kind = item.get("source_kind")
    if not isinstance(source_kind, str) or not source_kind.strip():
        raise ValueError(f"{context} evidence requires source_kind")
    exact_quote = item.get("exact_quote")
    if not isinstance(exact_quote, str) or not exact_quote.strip():
        raise ValueError(f"{context} evidence requires exact_quote")
    source_hash = item.get("source_hash")
    if not isinstance(source_hash, str) or _HASH_RE.fullmatch(source_hash) is None:
        raise ValueError(f"{context} evidence requires a valid source_hash")
    return item


def _validate_finding_record(
    item: Any, *, index: int
) -> dict[str, Any]:
    context = f"agent_repair_assessment.findings[{index}]"
    if not isinstance(item, dict):
        raise ValueError(f"{context} must be an object")
    finding_id = item.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id.strip():
        raise ValueError(f"{context} requires finding_id")
    lane = item.get("lane")
    if lane not in REPAIR_LANES:
        raise ValueError(f"{context} requires lane in {sorted(REPAIR_LANES)}")
    decision = item.get("decision")
    if decision not in DECISIONS:
        raise ValueError(f"{context} requires decision in {sorted(DECISIONS)}")
    verdict = item.get("agent_verdict")
    if verdict not in AGENT_VERDICTS:
        raise ValueError(
            f"{context} requires agent_verdict in {sorted(AGENT_VERDICTS)}"
        )
    repair_scope = item.get("repair_scope")
    if repair_scope not in REPAIR_SCOPES:
        raise ValueError(f"{context} requires a known repair_scope")
    if "core_science_change" not in item or not isinstance(
        item.get("core_science_change"), bool
    ):
        raise ValueError(f"{context} requires boolean core_science_change")
    rationale = item.get("rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        raise ValueError(f"{context} requires rationale")
    evidence = item.get("evidence")
    if not isinstance(evidence, list):
        raise ValueError(f"{context} evidence must be a list")
    for eidx, entry in enumerate(evidence):
        _validate_evidence_item(entry, context=f"{context}.evidence[{eidx}]")
    approved = item.get("approved_operation_ids")
    if not isinstance(approved, list) or not all(
        isinstance(op_id, str) and op_id for op_id in approved
    ):
        raise ValueError(
            f"{context} requires approved_operation_ids as a string list"
        )
    if len(approved) != len(set(approved)):
        raise ValueError(f"{context} approved_operation_ids must be unique")

    if decision == "ABANDON" or verdict in {"ABANDON", "BLOCKED_EVIDENCE"}:
        if approved:
            raise ValueError(
                f"{context} ABANDON/BLOCKED_EVIDENCE cannot approve operations"
            )
        if decision == "AUTO_FIX":
            raise ValueError(
                f"{context} ABANDON/BLOCKED_EVIDENCE cannot use AUTO_FIX"
            )
    if decision == "AUTO_FIX":
        if lane != "deterministic_core":
            raise ValueError(
                f"{context} AUTO_FIX is limited to deterministic_core findings"
            )
        if repair_scope not in _AUTO_FIX_SCOPES:
            raise ValueError(
                f"{context} AUTO_FIX requires a unique wiring repair_scope"
            )
        if item.get("core_science_change") is not False:
            raise ValueError(
                f"{context} AUTO_FIX requires core_science_change=false"
            )
        if verdict != "APPROVE_REPAIR":
            raise ValueError(
                f"{context} AUTO_FIX requires agent_verdict=APPROVE_REPAIR"
            )
        if not approved:
            raise ValueError(
                f"{context} AUTO_FIX requires approved_operation_ids"
            )
    if item.get("core_science_change") is True:
        if decision != "ABANDON" and verdict not in {
            "ABANDON",
            "BLOCKED_EVIDENCE",
        }:
            raise ValueError(
                f"{context} unsupported core science change must be "
                "BLOCKED_EVIDENCE or ABANDON"
            )
    if decision == "ASSISTED_FIX":
        if verdict != "APPROVE_REPAIR":
            raise ValueError(
                f"{context} ASSISTED_FIX requires agent_verdict=APPROVE_REPAIR"
            )
        if not approved:
            raise ValueError(
                f"{context} ASSISTED_FIX requires approved_operation_ids"
            )
        if not evidence:
            raise ValueError(
                f"{context} ASSISTED_FIX requires type-matched evidence"
            )
    return item


def validate_agent_repair_assessment_payload(
    assessment: Any,
    *,
    report: dict[str, Any] | None = None,
    expected_audit_id: str | None = None,
    expected_a0: str | None = None,
    expected_package_identity: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate schema and optional source-audit bindings."""

    payload = require_schema(
        assessment,
        AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION,
        "agent repair assessment",
    )
    audit_id = payload.get("audit_id")
    if not isinstance(audit_id, str) or not audit_id:
        raise ValueError("agent repair assessment requires audit_id")
    if expected_audit_id is not None and audit_id != expected_audit_id:
        raise ValueError("agent repair assessment audit_id is stale")
    a0 = payload.get("a0_content_root")
    if not isinstance(a0, str) or _HASH_RE.fullmatch(a0) is None:
        raise ValueError("agent repair assessment requires a0_content_root hash")
    if expected_a0 is not None and a0 != expected_a0:
        raise ValueError("agent repair assessment a0_content_root is stale")
    identity = payload.get("package_identity")
    if not isinstance(identity, dict):
        raise ValueError("agent repair assessment requires package_identity")
    directory_name = identity.get("directory_name")
    if not isinstance(directory_name, str) or not directory_name:
        raise ValueError(
            "agent repair assessment package_identity.directory_name is required"
        )
    if (
        expected_package_identity is not None
        and identity.get("directory_name")
        != expected_package_identity.get("directory_name")
    ):
        raise ValueError("agent repair assessment package_identity is stale")

    findings = payload.get("findings")
    if not isinstance(findings, list) or not findings:
        raise ValueError("agent repair assessment requires a non-empty findings list")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, item in enumerate(findings):
        record = _validate_finding_record(item, index=index)
        finding_id = record["finding_id"]
        if finding_id in seen:
            raise ValueError(
                f"duplicate agent repair assessment finding_id: {finding_id}"
            )
        seen.add(finding_id)
        normalized.append(record)

    if report is not None:
        queue = source_open_repair_queue(report)
        expected_ids = list(queue.get("open_finding_ids") or [])
        if not expected_ids:
            raise ValueError("source audit OPEN repair queue is empty")
        assessed_ids = [item["finding_id"] for item in normalized]
        if assessed_ids != sorted(expected_ids):
            missing = sorted(set(expected_ids) - set(assessed_ids))
            extra = sorted(set(assessed_ids) - set(expected_ids))
            raise ValueError(
                "agent repair assessment must bind the complete OPEN queue"
                + (f"; missing={missing}" if missing else "")
                + (f"; extra={extra}" if extra else "")
            )
        queue_by_id = {
            item["finding_id"]: item
            for item in queue.get("open_findings", [])
            if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
        }
        report_findings = {
            item.get("finding_id"): item
            for item in report.get("findings", [])
            if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
        }
        for record in normalized:
            source = queue_by_id.get(record["finding_id"]) or report_findings.get(
                record["finding_id"]
            )
            if source is None:
                raise ValueError(
                    f"assessment finding is not in the OPEN queue: "
                    f"{record['finding_id']}"
                )
            source_lane = source.get("lane") or source.get("repair_lane")
            if is_agent_quality_lane(source) or source_lane == "agent_quality":
                if record["lane"] != "agent_quality":
                    raise ValueError(
                        f"assessment lane mismatch for {record['finding_id']}"
                    )
                if record["decision"] == "AUTO_FIX":
                    raise ValueError(
                        "Agent-quality findings may not receive AUTO_FIX"
                    )
            elif record["lane"] != "deterministic_core":
                raise ValueError(
                    f"assessment lane mismatch for {record['finding_id']}"
                )
            # Machine FAIL / OPEN facts remain authoritative: the Agent may
            # classify repairability but cannot delete or suppress the finding.
            if (
                isinstance(source, dict)
                and source.get("status") not in {None, "OPEN"}
            ):
                raise ValueError(
                    f"assessment targets a non-OPEN finding: {record['finding_id']}"
                )
    payload = dict(payload)
    payload["findings"] = normalized
    return payload


def load_agent_repair_assessment(
    path: Path,
    *,
    report: dict[str, Any] | None = None,
    expected_audit_id: str | None = None,
    expected_a0: str | None = None,
    expected_package_identity: dict[str, Any] | None = None,
) -> dict[str, Any]:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise FileNotFoundError(
            f"agent repair assessment is missing: {resolved}"
        )
    try:
        payload = json.loads(resolved.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"agent repair assessment is unreadable: {resolved}"
        ) from exc
    return validate_agent_repair_assessment_payload(
        payload,
        report=report,
        expected_audit_id=expected_audit_id,
        expected_a0=expected_a0,
        expected_package_identity=expected_package_identity,
    )


def assessment_approved_operation_ids(
    assessment: dict[str, Any],
) -> dict[str, set[str]]:
    """Map finding_id -> approved operation ids."""

    mapping: dict[str, set[str]] = {}
    for item in assessment.get("findings", []):
        if not isinstance(item, dict):
            continue
        finding_id = item.get("finding_id")
        if not isinstance(finding_id, str):
            continue
        approved = item.get("approved_operation_ids") or []
        mapping[finding_id] = {
            op_id for op_id in approved if isinstance(op_id, str) and op_id
        }
    return mapping


def assessment_decision_by_finding(
    assessment: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    return {
        item["finding_id"]: item
        for item in assessment.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }


def enforce_plan_operations_approved(
    plan: dict[str, Any],
    assessment: dict[str, Any],
) -> None:
    """Fail closed when the plan uses an unapproved operation id."""

    approved = assessment_approved_operation_ids(assessment)
    decisions = assessment_decision_by_finding(assessment)
    for finding in plan.get("findings", []):
        if not isinstance(finding, dict):
            continue
        finding_id = finding.get("finding_id")
        if not isinstance(finding_id, str):
            raise ValueError("plan finding requires finding_id")
        record = decisions.get(finding_id)
        if record is None:
            raise ValueError(
                f"plan finding is missing from agent repair assessment: "
                f"{finding_id}"
            )
        plan_decision = finding.get("repair_class") or finding.get("decision")
        if plan_decision != record.get("decision"):
            raise ValueError(
                f"plan decision for {finding_id} does not match assessment"
            )
        allowed = approved.get(finding_id, set())
        operations = finding.get("operations") or []
        if record.get("decision") == "ABANDON" or record.get(
            "agent_verdict"
        ) in {"ABANDON", "BLOCKED_EVIDENCE"}:
            if operations:
                raise ValueError(
                    f"blocked/abandoned finding may not carry operations: "
                    f"{finding_id}"
                )
            continue
        for operation in operations:
            if not isinstance(operation, dict):
                raise ValueError("plan operation must be an object")
            operation_id = operation.get("id")
            if not isinstance(operation_id, str) or not operation_id:
                raise ValueError("plan operation requires id")
            if operation_id not in allowed:
                raise ValueError(
                    f"plan operation is not approved by agent repair "
                    f"assessment: {operation_id}"
                )


def default_publication_class(
    *,
    lane: str,
    decision: str,
    repair_scope: str | None,
) -> str:
    """Declare publication_class for this slice (publisher not enabled)."""

    if (
        lane == "deterministic_core"
        and decision == "AUTO_FIX"
        and repair_scope in _AUTO_FIX_SCOPES
    ):
        return "DIRECT_DETERMINISTIC"
    return "REAUDIT_REQUIRED"
