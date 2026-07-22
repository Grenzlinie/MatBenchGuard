"""Normalized dual-lane OPEN repair queue (D1-D6 + Agent-quality).

Review emits repairable Agent-quality findings as first-class queue entries
with ``lane: agent_quality``. They never fabricate a D1-D6
``deterministic_check``. Machine D statuses remain authoritative and separate.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Iterable

from artifact_schema import REPAIR_FINDINGS_SCHEMA_VERSION
from deterministic_contract import (
    QUALITY_RESULT_CODES,
    finding_lane,
    annotate_findings as annotate_deterministic_findings,
)


REPAIR_LANES = frozenset({"deterministic_core", "agent_quality"})
REPAIR_SCOPES = frozenset(
    {
        "DETERMINISTIC_WIRING",
        "CHECKER_ROBUSTNESS",
        "INSTRUCTION_CONTRACT",
        "SCORING_SEMANTICS",
        "DIRECT_INPUT_REFERENCE",
        "SCIENCE_SEMANTICS",
        # Narrow D6 AUTO_FIX subclass retained for unique wiring proofs.
        "UNIQUE_SCORING_WIRING",
    }
)
REAUDIT_REQUIRED_SCOPES = frozenset(
    {
        "CHECKER_ROBUSTNESS",
        "INSTRUCTION_CONTRACT",
        "SCORING_SEMANTICS",
        "DIRECT_INPUT_REFERENCE",
        "SCIENCE_SEMANTICS",
    }
)
DIRECT_DETERMINISTIC_ELIGIBLE_SCOPES = frozenset(
    {
        "DETERMINISTIC_WIRING",
        "UNIQUE_SCORING_WIRING",
    }
)
C_DIMENSIONS = frozenset(
    {f"C0{index}" for index in range(1, 8)}
)
_HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
_AGENT_LANES = frozenset({"agent_quality", "quality_results"})

# Explicit Agent-authored fairness / science codes that are not probe-derived.
_AGENT_CHECKER_ROBUSTNESS_CODES = frozenset(
    {
        "CHECKER_NONFINITE_BYPASS",
        "CHECKER_DUPLICATE_COUNTING",
        "CHECKER_DIRECTION_INVERSION",
        "CHECKER_ORDER_SENSITIVITY",
        "CHECKER_MISSING_OUTPUT_ENFORCEMENT",
        "CHECKER_INEFFECTIVE_REWARD_LINKAGE",
        "CHECKER_GAMING_SUBMISSION",
        "ADVERSARIAL_OUTPUT_PASSES",
        "KNOWN_VALID_OUTPUT_REJECTED",
        "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
        "SCIENTIFIC_INVARIANCE_VIOLATION",
        "SINGLE_COMPONENT_CAN_PASS",
    }
)
_AGENT_SCORING_CODES = frozenset(
    {
        "SCORING_DIRECTION_UNJUSTIFIED",
        "TOLERANCE_UNJUSTIFIED",
        "THRESHOLD_UNJUSTIFIED",
        "GOLD_UNJUSTIFIED",
    }
)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def is_agent_quality_lane(finding: dict[str, Any]) -> bool:
    return finding_lane(finding) in _AGENT_LANES


def default_repair_lane(finding: dict[str, Any]) -> str:
    if is_agent_quality_lane(finding):
        return "agent_quality"
    if finding_lane(finding) == "deterministic_core":
        return "deterministic_core"
    return "agent_quality"


def default_repair_scope(finding: dict[str, Any]) -> str:
    evidence = finding.get("evidence")
    if isinstance(evidence, dict):
        scoped = evidence.get("repair_scope")
        if scoped in REPAIR_SCOPES:
            return str(scoped)
    explicit = finding.get("repair_scope")
    if explicit in REPAIR_SCOPES:
        return str(explicit)

    code = finding.get("title", finding.get("code"))
    lane = finding_lane(finding)
    check_id = finding.get("deterministic_check")

    if lane in _AGENT_LANES or code in QUALITY_RESULT_CODES:
        if isinstance(code, str) and code.startswith("INDISPENSABLE_DIRECT_INPUT"):
            return "DIRECT_INPUT_REFERENCE"
        if code in _AGENT_SCORING_CODES or (
            isinstance(code, str) and "GOLD" in code
        ):
            return "SCORING_SEMANTICS"
        if code in _AGENT_CHECKER_ROBUSTNESS_CODES or code in QUALITY_RESULT_CODES:
            return "CHECKER_ROBUSTNESS"
        if isinstance(code, str) and code.startswith("PAPER_"):
            name = code.removeprefix("PAPER_")
            if name.startswith(("INSTRUCTION_", "DATA_", "METHOD_")):
                return "SCIENCE_SEMANTICS"
            if "GOLD" in name:
                return "SCORING_SEMANTICS"
            return "SCIENCE_SEMANTICS"
        return "SCIENCE_SEMANTICS"

    if check_id == "D1":
        return "DETERMINISTIC_WIRING"
    if check_id == "D2":
        return "INSTRUCTION_CONTRACT"
    if check_id in {"D3", "D4"}:
        return "DETERMINISTIC_WIRING"
    if check_id == "D5":
        return "DETERMINISTIC_WIRING"
    if check_id == "D6":
        return "SCORING_SEMANTICS"
    if isinstance(code, str) and code.startswith("INDISPENSABLE_DIRECT_INPUT"):
        return "DIRECT_INPUT_REFERENCE"
    return "DETERMINISTIC_WIRING"


def default_dimension(finding: dict[str, Any]) -> str:
    explicit = finding.get("dimension")
    if explicit in C_DIMENSIONS:
        return str(explicit)
    # Lazy import avoids a finalize↔repair cycle at module import time.
    from finalize_audit_output import scored_dimension_v11_for

    mapped = scored_dimension_v11_for(finding)
    if mapped in C_DIMENSIONS:
        return mapped
    return "C07" if is_agent_quality_lane(finding) else "C02"


def annotate_repair_metadata(
    findings: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Attach repair_lane / repair_scope / dimension without inventing D checks."""

    annotated = annotate_deterministic_findings(findings)
    result: list[dict[str, Any]] = []
    for item in annotated:
        entry = dict(item)
        lane = finding_lane(entry)
        repair_lane = default_repair_lane(entry)
        if repair_lane == "agent_quality":
            entry["deterministic_check"] = None
            entry["blocking"] = False
            # Queue identity is always agent_quality; keep probe provenance
            # under judgment_type / original lane when present.
            if lane in _AGENT_LANES:
                entry["lane"] = lane
        entry["repair_lane"] = repair_lane
        entry["repair_scope"] = default_repair_scope(entry)
        entry["dimension"] = default_dimension(entry)
        entry["publication_hint"] = (
            "DIRECT_DETERMINISTIC_ELIGIBLE"
            if entry["repair_scope"] in DIRECT_DETERMINISTIC_ELIGIBLE_SCOPES
            and repair_lane == "deterministic_core"
            else "REAUDIT_REQUIRED"
        )
        result.append(entry)
    return result


def _safe_package_relative(root: Path, relative: str, context: str) -> Path:
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError(f"{context} package path is missing")
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"{context} package path is unsafe: {relative}")
    resolved_root = root.expanduser().resolve()
    path = (resolved_root / candidate).resolve()
    if not path.is_relative_to(resolved_root):
        raise ValueError(f"{context} package path escapes the Harbor package")
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"{context} package path is not a regular file")
    return path


def _validate_evidence_item(
    root: Path, item: Any, context: str
) -> dict[str, str]:
    if not isinstance(item, dict):
        raise ValueError(f"{context} must be an object")
    package_file = item.get("package_file")
    package_quote = item.get("package_quote")
    source_hash = item.get("source_hash")
    if not isinstance(package_quote, str) or not package_quote.strip():
        raise ValueError(f"{context} requires an exact package_quote")
    if not isinstance(source_hash, str) or not _HASH_RE.match(source_hash):
        raise ValueError(f"{context} source_hash must be sha256:<64 hex>")
    path = _safe_package_relative(root, package_file, context)
    text = path.read_text(encoding="utf-8", errors="replace")
    if package_quote not in text:
        raise ValueError(
            f"{context} package quote is not present in {package_file}"
        )
    actual = _sha256_file(path)
    if actual != source_hash:
        raise ValueError(
            f"{context} source_hash does not match {package_file}"
        )
    return {
        "package_file": Path(package_file).as_posix(),
        "package_quote": package_quote,
        "source_hash": source_hash,
    }


def validate_repair_finding(
    root: Path, value: Any, *, index: int | None = None
) -> dict[str, Any]:
    context = (
        f"repair_findings[{index}]" if index is not None else "repair finding"
    )
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be an object")
    finding_id = value.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id.strip():
        raise ValueError(f"{context} requires finding_id")
    lane = value.get("lane", "agent_quality")
    repair_lane = value.get("repair_lane", "agent_quality")
    if lane != "agent_quality" or repair_lane != "agent_quality":
        raise ValueError(
            f"{context} Agent repair finding must use lane/repair_lane "
            "agent_quality"
        )
    if value.get("deterministic_check") is not None:
        raise ValueError(
            f"{context} must not set deterministic_check "
            "(Agent findings never fabricate a D1-D6 check)"
        )
    repair_scope = value.get("repair_scope")
    if repair_scope not in REPAIR_SCOPES:
        raise ValueError(f"{context} has invalid repair_scope taxonomy")
    severity = value.get("severity")
    if severity not in {"FATAL", "HIGH", "MEDIUM", "LOW"}:
        raise ValueError(f"{context} has invalid severity")
    status = value.get("status", "OPEN")
    if status not in {"OPEN", "RESOLVED", "CLOSED", "FIXED"}:
        raise ValueError(f"{context} has invalid status")
    repairable = value.get("repairable")
    if not isinstance(repairable, bool):
        raise ValueError(f"{context} requires boolean repairable")
    dimension = value.get("dimension")
    if dimension not in C_DIMENSIONS:
        raise ValueError(f"{context} dimension must be one of C01-C07")
    title = value.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"{context} requires title")
    observed = value.get("observed_fact") or value.get("message")
    if not isinstance(observed, str) or not observed.strip():
        raise ValueError(f"{context} requires observed_fact")
    evidence = value.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError(f"{context} requires at least one evidence citation")
    normalized_evidence = [
        _validate_evidence_item(root, item, f"{context} evidence {offset}")
        for offset, item in enumerate(evidence, start=1)
    ]
    affected = value.get("affected_files")
    if affected is None:
        affected_files = sorted(
            {
                item["package_file"]
                for item in normalized_evidence
            }
        )
    else:
        if not isinstance(affected, list) or not affected:
            raise ValueError(f"{context} affected_files must be a non-empty list")
        affected_files = []
        for path in affected:
            _safe_package_relative(root, path, f"{context} affected_files")
            affected_files.append(Path(str(path)).as_posix())
    return {
        "finding_id": finding_id.strip(),
        "lane": "agent_quality",
        "repair_lane": "agent_quality",
        "repair_scope": repair_scope,
        "severity": severity,
        "status": status,
        "repairable": repairable,
        "dimension": dimension,
        "title": title.strip(),
        "observed_fact": observed.strip(),
        "evidence": normalized_evidence,
        "affected_files": affected_files,
        "deterministic_check": None,
        "publication_hint": (
            "REAUDIT_REQUIRED"
            if repair_scope in REAUDIT_REQUIRED_SCOPES
            else "DIRECT_DETERMINISTIC_ELIGIBLE"
        ),
        "judgment_type": "AGENT_JUDGMENT",
    }


def validate_repair_findings(
    root: Path, values: Any
) -> list[dict[str, Any]]:
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError("repair_findings must be a list")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, item in enumerate(values, start=1):
        entry = validate_repair_finding(root, item, index=index)
        if entry["finding_id"] in seen:
            raise ValueError(
                f"duplicate repair_findings id: {entry['finding_id']}"
            )
        seen.add(entry["finding_id"])
        normalized.append(entry)
    return normalized


def build_agent_repair_findings(
    findings: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Project OPEN repairable Agent-quality findings into queue entries."""

    entries: list[dict[str, Any]] = []
    for raw in findings:
        item = dict(raw)
        if not is_agent_quality_lane(item):
            continue
        if item.get("status", "OPEN") != "OPEN":
            continue
        if item.get("repairable") is not True:
            continue
        evidence = item.get("evidence")
        evidence_refs: list[dict[str, Any]]
        if isinstance(evidence, list):
            evidence_refs = [dict(entry) for entry in evidence if isinstance(entry, dict)]
        elif isinstance(evidence, dict):
            evidence_refs = [dict(evidence)]
        else:
            evidence_refs = []
        for location in item.get("affected_locations") or []:
            if not isinstance(location, dict):
                continue
            evidence_refs.append(
                {
                    "package_file": location.get("file"),
                    "package_quote": location.get("quote"),
                    "line": location.get("line"),
                }
            )
        entries.append(
            {
                "finding_id": item["finding_id"],
                "lane": "agent_quality",
                "repair_lane": "agent_quality",
                "repair_scope": item.get("repair_scope")
                or default_repair_scope(item),
                "severity": item.get("severity"),
                "status": "OPEN",
                "repairable": True,
                "dimension": item.get("dimension") or default_dimension(item),
                "title": item.get("title") or item.get("code"),
                "observed_fact": item.get("observed_fact")
                or item.get("observation")
                or item.get("message"),
                "evidence": evidence_refs,
                "affected_files": list(item.get("affected_files") or []),
                "deterministic_check": None,
                "publication_hint": item.get("publication_hint")
                or "REAUDIT_REQUIRED",
                "judgment_type": item.get("judgment_type") or "AGENT_JUDGMENT",
            }
        )
    entries.sort(key=lambda item: item["finding_id"])
    return entries


def build_complete_open_repair_queue(
    deterministic_contract: dict[str, Any],
    findings: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Complete OPEN queue across machine D blockers and Agent-quality findings."""

    required = list(
        deterministic_contract.get("repair_summary", {}).get(
            "required_findings", []
        )
        or []
    )
    d_entries = [
        {
            "finding_id": item["finding_id"],
            "lane": "deterministic_core",
            "repair_lane": "deterministic_core",
            "repair_scope": item.get("repair_scope")
            or default_repair_scope(item),
            "severity": item.get("severity"),
            "status": item.get("status", "OPEN"),
            "repairable": True,
            "dimension": item.get("dimension"),
            "title": item.get("title") or item.get("finding_code"),
            "deterministic_check": item.get("deterministic_check"),
            "publication_hint": (
                "DIRECT_DETERMINISTIC_ELIGIBLE"
                if (
                    item.get("repair_scope")
                    in DIRECT_DETERMINISTIC_ELIGIBLE_SCOPES
                    or item.get("deterministic_repair_class") == "AUTO_FIX"
                )
                else "REAUDIT_REQUIRED"
            ),
        }
        for item in required
        if item.get("lane") != "agent_quality"
    ]
    agent_entries = build_agent_repair_findings(findings)
    open_findings = d_entries + agent_entries
    open_findings.sort(key=lambda item: item["finding_id"])
    return {
        "schema_version": REPAIR_FINDINGS_SCHEMA_VERSION,
        "open_findings": open_findings,
        "open_finding_ids": [item["finding_id"] for item in open_findings],
        "deterministic_finding_ids": [
            item["finding_id"] for item in d_entries
        ],
        "agent_quality_finding_ids": [
            item["finding_id"] for item in agent_entries
        ],
        "deterministic_state": deterministic_contract.get(
            "repair_summary", {}
        ).get("state"),
    }


def apply_agent_quality_repair_gate(
    *,
    verdict: str,
    score: float | None,
    hard_gate: bool,
    evidence_gaps: list[str],
    findings: Iterable[dict[str, Any]],
) -> tuple[str, str | None]:
    """Route OPEN repairable Agent findings to CONDITIONAL / REPAIR_QUEUE.

    Hard Gates, evidence gaps, and REJECT remain non-Repair routes. Machine
    D1-D6 statuses are unchanged by this gate.
    """

    del score  # score remains authoritative elsewhere; gate is finding-driven
    if hard_gate or evidence_gaps:
        return verdict, None
    if verdict in {"REJECT", "NOT_ASSESSABLE"}:
        return verdict, None
    open_agent = [
        item
        for item in findings
        if isinstance(item, dict)
        and is_agent_quality_lane(item)
        and item.get("status", "OPEN") == "OPEN"
        and item.get("repairable") is True
    ]
    if not open_agent:
        return verdict, None
    if verdict == "PASS":
        return (
            "CONDITIONAL",
            "D1-D6 is CLEAN (or otherwise non-blocking), but one or more "
            "OPEN repairable Agent-quality findings require Repair.",
        )
    return verdict, None


def agent_sources_from_repair_findings(
    repair_findings: Iterable[dict[str, Any]],
) -> list[tuple[dict[str, Any], str, str]]:
    """Convert validated Agent repair findings into synthesize_report sources."""

    sources: list[tuple[dict[str, Any], str, str]] = []
    for item in repair_findings:
        sources.append(
            (
                {
                    "finding_id": item["finding_id"],
                    "severity": item["severity"],
                    "code": item["title"],
                    "message": item["observed_fact"],
                    "affected_files": list(item.get("affected_files") or []),
                    "evidence": {
                        "repair_findings": True,
                        "repair_scope": item["repair_scope"],
                        "dimension": item["dimension"],
                        "citations": item.get("evidence", []),
                    },
                    "lane": "agent_quality",
                    "repairable": item.get("repairable", True),
                },
                "AGENT_QUALITY",
                "AGENT_QUALITY_REPAIR",
            )
        )
    return sources
