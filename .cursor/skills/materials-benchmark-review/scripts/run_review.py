#!/usr/bin/env python3
"""Run the dual-lane materials review.

Deterministic code checks and Agent paper-grounded quality assessment form one
default path. Only an established NON_MAT classification may skip paper.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from audit_package import static_audit
from agent_contract_wiring import validate_agent_contract_assessment
from dynamic_checker_probe import TASK_FAMILY_ATTACKS, dynamic_checker_probe
from deterministic_contract import UNAVAILABLE_CHECK_STATUSES
from finalize_audit_output import (
    finalize_audit,
    synthesize_report,
)
from prepare_audit_output import (
    AGENT_ASSESSMENT_PENDING,
    AGENT_CONTRACT_PENDING,
    AGENT_CONTRACT_REQUEST_RELATIVE_PATH,
    QUALITY_EVIDENCE_ROLES,
    archive_agent_contract_request,
    bind_external_evidence,
    locate_root,
    validate_agent_contract_request,
    prepare_workspace,
    write_agent_contract_request,
    record_paper_input_hashes,
    skill_root,
    validate_paper_boundary,
    write_audit_attestation,
    new_audit_id,
)
from artifact_schema import (
    AGENT_ASSESSMENT_SCHEMA_VERSION,
    CHECKER_TESTS_SCHEMA_VERSION,
    RESOURCE_CHECKS_SCHEMA_VERSION,
)
from probe_resources import probe_resources
from review_path_policy import (
    EXECUTION_CLAIM,
    REVIEW_LANE,
    default_review_output_dir,
    require_external_output_dir,
)
from review_lock import ReviewOutputLock
import sandbox_runtime
from run_context import (
    PackageRunLock,
    RunContextError,
    load_context,
    now,
    snapshot_package,
    status,
    transition,
    complete,
    write_content_root,
    write_json_atomic,
)


PAPER_DIMENSIONS = {
    "instruction_fidelity",
    "data_fidelity",
    "method_fidelity",
    "gold_provenance",
    "checker_fidelity",
}
PAPER_STATUSES = {"PASS", "WARNING", "FAIL", "NOT_ASSESSABLE"}
REPRODUCTION_TYPES = {
    "EXACT_REPRODUCTION",
    "METHOD_REIMPLEMENTATION",
    "SCIENTIFIC_EXTENSION",
}
TAXONOMY_EVIDENCE_DIMENSIONS = {
    "computation_task",
    "research_domain",
    "material_system.primary",
    "material_system.secondary",
}
PACKAGE_EVIDENCE_ROLES = frozenset(QUALITY_EVIDENCE_ROLES)
MATERIALS_QUALIFICATION_AXES = {
    "object",
    "data",
    "operation",
    "endpoint",
    "domain_dependence",
}
MATERIALS_QUALIFICATION_CLASSES = {
    "MAT_CORE",
    "MAT_METHOD",
    "MAT_WRAPPER",
    "NON_MAT",
    "AMBIGUOUS",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def taxonomy_categories(taxonomy: dict[str, Any], dimension: str) -> set[str]:
    return set(
        taxonomy["dimensions"][dimension]["categories"]
    )


def validate_taxonomy_labels(
    labels: Any, taxonomy: dict[str, Any]
) -> dict[str, Any]:
    if not isinstance(labels, dict):
        raise ValueError("assessment taxonomy must be an object")
    computation = labels.get("computation_task")
    domains = labels.get("research_domain")
    system = labels.get("material_system")
    if (
        not isinstance(computation, list)
        or not computation
        or not all(isinstance(item, str) for item in computation)
    ):
        raise ValueError("computation_task must be a non-empty string list")
    if (
        not isinstance(domains, list)
        or not domains
        or not all(isinstance(item, str) for item in domains)
    ):
        raise ValueError("research_domain must be a non-empty string list")
    if not isinstance(system, dict):
        raise ValueError("material_system must be an object")
    primary = system.get("primary")
    secondary = system.get("secondary")
    if not isinstance(primary, str):
        raise ValueError("material_system.primary must be a string")
    if not isinstance(secondary, list) or not all(
        isinstance(item, str) and item for item in secondary
    ):
        raise ValueError("material_system.secondary must be a string list")

    checks = {
        "computation_task": (
            computation,
            taxonomy_categories(taxonomy, "computation_task"),
        ),
        "research_domain": (
            domains,
            taxonomy_categories(taxonomy, "research_domain"),
        ),
        "material_system.primary": (
            [primary],
            taxonomy_categories(taxonomy, "material_system"),
        ),
    }
    for name, (values, allowed) in checks.items():
        unknown = sorted(set(values) - allowed)
        if unknown:
            raise ValueError(f"unknown {name} labels: {unknown}")
    return {
        "computation_task": list(dict.fromkeys(computation)),
        "research_domain": list(dict.fromkeys(domains)),
        "material_system": {
            "primary": primary,
            "secondary": list(dict.fromkeys(secondary)),
        },
    }


def validate_package_quote(
    root: Path,
    package_file: Any,
    package_quote: Any,
    context: str,
) -> tuple[str, str]:
    if not all(
        isinstance(part, str) and part.strip()
        for part in (package_file, package_quote)
    ):
        raise ValueError(f"{context} requires package_file and package_quote")
    normalized_file = Path(package_file)
    allowed = package_file == "instruction.md" or (
        package_file.startswith("tests/")
        and ".." not in normalized_file.parts
        and normalized_file.is_absolute() is False
    )
    if not allowed:
        raise ValueError(
            f"{context} uses unsupported package evidence file: {package_file}"
        )
    package_path = root / package_file
    if not package_path.is_file():
        raise ValueError(
            f"{context} evidence file does not exist: {package_file}"
        )
    package_text = package_path.read_text(
        encoding="utf-8", errors="replace"
    )
    if package_quote not in package_text:
        raise ValueError(
            f"{context} package quote is not present in {package_file}"
        )
    return package_file, package_quote


def expected_taxonomy_evidence(
    labels: dict[str, Any],
) -> set[tuple[str, str]]:
    return {
        *(("computation_task", label) for label in labels["computation_task"]),
        *(("research_domain", label) for label in labels["research_domain"]),
        ("material_system.primary", labels["material_system"]["primary"]),
        *(
            ("material_system.secondary", label)
            for label in labels["material_system"]["secondary"]
        ),
    }


def validate_taxonomy_evidence(
    root: Path,
    evidence: Any,
    labels: dict[str, Any],
) -> list[dict[str, str]]:
    if not isinstance(evidence, list):
        raise ValueError("taxonomy_evidence must be a list")
    normalized: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    expected = expected_taxonomy_evidence(labels)
    for index, item in enumerate(evidence, start=1):
        if not isinstance(item, dict):
            raise ValueError(
                f"taxonomy evidence {index} must be an object"
            )
        dimension = item.get("dimension")
        label = item.get("label")
        if dimension not in TAXONOMY_EVIDENCE_DIMENSIONS:
            raise ValueError(
                f"taxonomy evidence {index} has invalid dimension: {dimension!r}"
            )
        if not isinstance(label, str) or not label:
            raise ValueError(f"taxonomy evidence {index} requires a label")
        pair = (dimension, label)
        if pair not in expected:
            raise ValueError(
                f"taxonomy evidence {index} references an unselected label: "
                f"{dimension}={label}"
            )
        package_file, package_quote = validate_package_quote(
            root,
            item.get("package_file"),
            item.get("package_quote"),
            f"taxonomy evidence {index}",
        )
        normalized.append(
            {
                "dimension": dimension,
                "label": label,
                "package_file": package_file,
                "package_quote": package_quote,
            }
        )
        seen.add(pair)
    missing = sorted(expected - seen)
    if missing:
        dimension, label = missing[0]
        raise ValueError(
            f"missing taxonomy evidence for {dimension}: {label}"
        )
    return normalized


def validate_materials_qualification(
    root: Path, qualification: Any
) -> dict[str, Any] | None:
    if qualification is not None:
        if not isinstance(qualification, dict):
            raise ValueError("materials_qualification must be an object")
        classification = qualification.get("classification")
        rationale = qualification.get("rationale")
        evidence = qualification.get("evidence")
        if classification not in MATERIALS_QUALIFICATION_CLASSES:
            raise ValueError(
                f"invalid materials qualification: {classification!r}"
            )
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError("materials_qualification requires a rationale")
        if not isinstance(evidence, list):
            raise ValueError("materials_qualification evidence must be a list")
        normalized_evidence: list[dict[str, str]] = []
        seen_axes: set[str] = set()
        for index, item in enumerate(evidence, start=1):
            if not isinstance(item, dict):
                raise ValueError(
                    f"materials qualification evidence {index} must be an object"
                )
            axis = item.get("axis")
            if axis not in MATERIALS_QUALIFICATION_AXES:
                raise ValueError(
                    f"materials qualification evidence {index} has invalid axis: {axis!r}"
                )
            package_file, package_quote = validate_package_quote(
                root,
                item.get("package_file"),
                item.get("package_quote"),
                f"materials qualification evidence {index}",
            )
            normalized_evidence.append(
                {
                    "axis": axis,
                    "package_file": package_file,
                    "package_quote": package_quote,
                }
            )
            seen_axes.add(axis)
        required_axes = (
            MATERIALS_QUALIFICATION_AXES
            if classification in {"MAT_CORE", "MAT_METHOD"}
            else {"object", "operation", "endpoint", "domain_dependence"}
        )
        missing_axes = sorted(required_axes - seen_axes)
        if missing_axes:
            raise ValueError(
                "materials_qualification is missing evidence for: "
                + ", ".join(missing_axes)
            )
        return {
            "classification": classification,
            "rationale": rationale,
            "evidence": normalized_evidence,
            "authoritative": True,
        }
    return None


def validate_paper_dimensions(
    root: Path, assessment: dict[str, Any]
) -> dict[str, Any]:
    """Validate Agent paper-grounded fidelity dimensions (dual-lane default)."""
    reproduction_type = assessment.get(
        "reproduction_type", "METHOD_REIMPLEMENTATION"
    )
    if reproduction_type not in REPRODUCTION_TYPES:
        raise ValueError(f"invalid reproduction_type: {reproduction_type!r}")
    dimensions = assessment.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != PAPER_DIMENSIONS:
        raise ValueError(
            "paper assessment dimensions must be exactly "
            f"{sorted(PAPER_DIMENSIONS)}"
        )
    validate_paper_boundary(root)
    paper_text = (root / "paper/paper.md").read_text(
        encoding="utf-8", errors="replace"
    )
    normalized_dimensions: dict[str, Any] = {}
    for name in sorted(PAPER_DIMENSIONS):
        value = dimensions[name]
        if not isinstance(value, dict):
            raise ValueError(f"{name} must be an object")
        status = value.get("status")
        rationale = value.get("rationale")
        evidence = value.get("evidence")
        if status not in PAPER_STATUSES:
            raise ValueError(f"invalid {name} status: {status!r}")
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError(f"{name} requires a rationale")
        if not isinstance(evidence, list) or (
            status != "NOT_ASSESSABLE" and not evidence
        ):
            raise ValueError(f"{name} requires at least one evidence item")
        if status == "NOT_ASSESSABLE" and evidence:
            raise ValueError(
                f"{name} NOT_ASSESSABLE requires an empty evidence list"
            )
        normalized_evidence = []
        for index, item in enumerate(evidence, start=1):
            if not isinstance(item, dict):
                raise ValueError(f"{name} evidence {index} must be an object")
            paper_quote = item.get("paper_quote")
            package_file = item.get("package_file")
            package_quote = item.get("package_quote")
            if not all(
                isinstance(part, str) and part.strip()
                for part in (paper_quote, package_file, package_quote)
            ):
                raise ValueError(
                    f"{name} evidence {index} requires paper_quote, "
                    "package_file, and package_quote"
                )
            if paper_quote not in paper_text:
                raise ValueError(
                    f"{name} paper quote is not present in paper/paper.md"
                )
            package_file, package_quote = validate_package_quote(
                root,
                package_file,
                package_quote,
                f"{name} evidence {index}",
            )
            normalized_evidence.append(
                {
                    "paper_quote": paper_quote,
                    "package_file": package_file,
                    "package_quote": package_quote,
                }
            )
        normalized_dimensions[name] = {
            "status": status,
            "rationale": rationale.strip(),
            "evidence": normalized_evidence,
        }
    return {
        "reproduction_type": reproduction_type,
        "dimensions": normalized_dimensions,
    }


def validate_agent_assessment(root: Path, path: Path) -> dict[str, Any]:
    """Validate Agent assessment for the dual-lane review path."""
    resolved_path = path.expanduser().resolve()
    if resolved_path.is_relative_to(root.resolve()):
        raise ValueError(
            "agent assessment must be outside the Harbor 题包"
        )
    if not resolved_path.is_file():
        raise FileNotFoundError(
            f"agent assessment is missing: {resolved_path}"
        )
    assessment = read_json(resolved_path)
    if not isinstance(assessment, dict):
        raise ValueError("agent assessment must be an object")
    taxonomy = read_json(
        skill_root() / "references/materials-taxonomy.json"
    )
    normalized_taxonomy = validate_taxonomy_labels(
        assessment.get("taxonomy"), taxonomy
    )
    normalized: dict[str, Any] = {
        "schema_version": AGENT_ASSESSMENT_SCHEMA_VERSION,
        "taxonomy": normalized_taxonomy,
        "taxonomy_evidence": validate_taxonomy_evidence(
            root,
            assessment.get("taxonomy_evidence"),
            normalized_taxonomy,
        ),
        "taxonomy_source": taxonomy["source"],
        "review_lane": REVIEW_LANE,
    }
    qualification = validate_materials_qualification(
        root, assessment.get("materials_qualification")
    )
    if qualification is None:
        raise ValueError(
            "dual-lane assessment requires authoritative materials_qualification"
        )
    normalized["materials_qualification"] = qualification
    if qualification["classification"] == "NON_MAT":
        if (
            "reproduction_type" in assessment
            or "dimensions" in assessment
        ):
            raise ValueError(
                "NON_MAT assessment must not claim paper fidelity"
            )
        normalized["paper_skipped"] = True
        normalized["paper_skip_reason"] = (
            "Paper read skipped because materials_qualification established "
            "NON_MAT."
        )
        return normalized
    normalized.update(validate_paper_dimensions(root, assessment))
    normalized["paper_skipped"] = False
    if "repair_findings" in assessment:
        from repair_findings import validate_repair_findings

        normalized["repair_findings"] = validate_repair_findings(
            root, assessment.get("repair_findings")
        )
    return normalized


def checker_skipped_by_static_gate(
    root: Path, output: Path, reason: str = "STATIC_GATE"
) -> dict[str, Any]:
    result = {
        "schema_version": CHECKER_TESTS_SCHEMA_VERSION,
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
        "runtime": {
            "verifier_entrypoint": "tests/test.sh",
            "runtime_provenance": "sandbox",
            "direct_checker_harness": False,
            "status": "NOT_ASSESSABLE",
            "reason": reason,
        },
        "solution_content_inspected": False,
        "solution_oracle": {
            "used": False,
            "status": "NOT_RUN",
            "positive_mock_available": False,
            "attempted": False,
            "setup_attempted": False,
            "setup_prepared": False,
            "producer_started": False,
            "executed": False,
            "scientific_evidence": False,
        },
        "pass_threshold": None,
        "tests": [],
        "findings": [],
        "usable_reward_count": 0,
        "runtime_provenance": {
            "status": "NOT_ASSESSABLE",
            "entrypoint": "tests/test.sh",
            "runtime_provenance": "sandbox",
            "reason": reason,
            "cases_executed": 0,
        },
        "probe_coverage": {
            probe_class: {
                "status": (
                    "NOT_APPLICABLE"
                    if probe_class in {"process_evidence", "component_isolation"}
                    else "NOT_ASSESSABLE"
                ),
                "reason": (
                    "process evidence is not a dynamic fixture or "
                    "checker-probe target"
                    if probe_class == "process_evidence"
                    else "component isolation is Agent-quality evidence and has no deterministic fixture API"
                    if probe_class == "component_isolation"
                    else reason
                ),
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                    **(
                        {
                            "source_bindings_verified": False,
                            "runtime_bindings_verified": False,
                            "cases_planned": 0,
                            "cases_executed": 0,
                        }
                        if probe_class == "component_isolation"
                        else {}
                    ),
                },
                **(
                    {
                        "files": {},
                        "instrumentation": "NONE",
                    }
                    if probe_class == "process_evidence"
                    else {}
                ),
            }
            for probe_class in (
                "positive",
                "negative",
                "discrimination",
                "equivalence",
                "component_isolation",
            )
        },
        "limitations": [
            "Checker probes were skipped because the checker contract was not runnable."
        ],
    }
    result["probe_coverage"]["negative"]["subcoverage"] = {
        "task_family_attacks": {
            attack: {
                "status": "NOT_ASSESSABLE",
                "reason": reason,
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "cases": [],
                    "modes": [],
                },
            }
            for attack in TASK_FAMILY_ATTACKS
        }
    }
    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return result


def resources_skipped_by_static_gate(
    root: Path,
    output: Path,
    parse_status: str,
) -> dict[str, Any]:
    result = {
        "schema_version": RESOURCE_CHECKS_SCHEMA_VERSION,
        "status": "NOT_ASSESSED",
        "summary": {
            "resource_count": 0,
            "finding_count": 0,
            "e2_recommended": False,
        },
        "resources": [],
        "findings": [],
        "limitations": [
            "Resource probes were skipped because resources.json is "
            f"{parse_status}."
        ],
    }
    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return result


def pre_paper_hard_gate_codes(
    static_result: dict[str, Any],
    resource_result: dict[str, Any],
    materials_qualification: dict[str, Any] | None,
) -> list[str]:
    codes = {
        issue.get("code")
        for issue in static_result.get("issues", [])
        if issue.get("code")
        in {
            "UNRECOVERABLE_TASK_DEFINITION",
            "CHECKER_CORE_TASK_UNASSESSED",
        }
    }
    codes.update(
        finding.get("code")
        for finding in resource_result.get("findings", [])
        if finding.get("code") == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
    )
    if (
        materials_qualification is not None
        and materials_qualification.get("classification") == "NON_MAT"
    ):
        codes.add("NON_MATERIALS_TASK")
    ordered = (
        "NON_MATERIALS_TASK",
        "UNRECOVERABLE_TASK_DEFINITION",
        "CHECKER_CORE_TASK_UNASSESSED",
        "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
    )
    return [code for code in ordered if code in codes]


def _execution_evidence() -> dict[str, Any]:
    return {
        "status": "NOT_ASSESSED",
        "claim": EXECUTION_CLAIM,
        "scientific_reproduction": False,
        "environment": None,
        "environment_verified": False,
        "runtime_provenance": "sandbox",
        "verifies_resources": [],
        "returncode": None,
        "stdout": "",
        "stderr": "",
        "reason": (
            "Dual-lane review executes the Harbor verifier entrypoint but not "
            "the scientific workflow."
        ),
        "review_lane": REVIEW_LANE,
    }


def _load_prepared_inputs(temp_dir: Path) -> tuple[
    dict[str, Any], dict[str, Any], dict[str, Any]
]:
    return (
        read_json(temp_dir / "evidence/static_checks/audit_static.json"),
        read_json(temp_dir / "checker_tests.json"),
        read_json(temp_dir / "resource_checks.json"),
    )


def _pending_result(
    root: Path,
    output_dir: Path,
    request: dict[str, Any],
) -> dict[str, Any]:
    return {
        "benchmark_root": str(root),
        "audit_output_dir": str(output_dir),
        "audit_temp_dir": request.get(
            "audit_temp_dir",
            str(output_dir / ".benchmark_audit_tmp"),
        ),
        "request_path": str(
            output_dir / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
        ),
        "status": AGENT_CONTRACT_PENDING,
        "review_status": AGENT_CONTRACT_PENDING,
        "verdict": "NOT_ASSESSABLE",
        "review_verdict": "NOT_ASSESSABLE",
        "disposition": "NOT_ASSESSABLE",
        "publishability": "EVIDENCE_PENDING",
        "publishable": False,
        "deterministic_status": "NOT_APPLICABLE",
        "machine_contract_digest": request.get("machine_contract_digest"),
        "machine_status": request.get("machine_status"),
        "message": (
            "Deterministic preparation is persisted. Supply a valid "
            "--agent-contract-assessment to resume without rerunning probes."
        ),
    }


def _assessment_pending_result(
    root: Path,
    *,
    output_dir: Path | None = None,
    message: str,
    assessment_path: Path | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "benchmark_root": str(root),
        "status": AGENT_ASSESSMENT_PENDING,
        "review_status": AGENT_ASSESSMENT_PENDING,
        "verdict": "NOT_ASSESSABLE",
        "publishable": False,
        "deterministic_status": "NOT_APPLICABLE",
        "message": message,
    }
    if output_dir is not None:
        payload["audit_output_dir"] = str(output_dir)
    if assessment_path is not None:
        payload["assessment_path"] = str(assessment_path)
    return payload


def try_load_agent_assessment(
    root: Path,
    assessment_path: Path | None,
) -> tuple[dict[str, Any] | None, str | None]:
    """Return (assessment, error). Missing/invalid yields an error string."""

    if assessment_path is None:
        return None, "paper Agent assessment is required before dual-lane Review"
    resolved = assessment_path.expanduser().resolve()
    if not resolved.is_file():
        return None, f"paper Agent assessment is missing: {resolved}"
    try:
        return validate_agent_assessment(root, resolved), None
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, f"paper Agent assessment is invalid: {exc}"


def assessment_required_for_purpose(output_purpose: str) -> bool:
    """Equal-depth re-audit always requires an inherited paper assessment."""

    return output_purpose == "reaudit"


def agent_contract_pending_eligible(
    machine_contract: dict[str, Any],
    report: dict[str, Any],
) -> bool:
    """Return whether an unavailable contract may pause for adjudication."""

    summary = machine_contract.get("repair_summary")
    if not isinstance(summary, dict) or summary.get("state") != "NOT_APPLICABLE":
        return False
    checks = machine_contract.get("checks")
    if not isinstance(checks, list) or not checks:
        return False
    if not any(
        isinstance(check, dict)
        and check.get("check_id") == "D6"
        and check.get("status") in UNAVAILABLE_CHECK_STATUSES
        for check in checks
    ):
        return False
    if any(
        not isinstance(check, dict)
        or check.get("status") == "FAIL"
        or check.get("proven_finding_ids")
        or check.get("blocking_finding_ids")
        or check.get("trace_status") == "FAILED"
        or check.get("usable_runtime_contradiction") is True
        or check.get("runtime_contradiction") is True
        or str(check.get("runtime_status", "")).upper()
        in {"CONTRADICTED", "CONTRADICTION", "FAILED"}
        for check in checks
    ):
        return False
    hard_gates = report.get("hard_gates")
    if isinstance(hard_gates, list) and any(
        isinstance(gate, dict) and gate.get("status") != "PASS"
        for gate in hard_gates
    ):
        return False
    for finding in report.get("findings", []):
        if not isinstance(finding, dict):
            continue
        lane = finding.get("lane")
        if lane in {"agent_quality", "quality_results"}:
            # This fallback answers only D6 scoring-chain availability.
            # Unrelated Agent-quality findings remain in the queue after D6 is
            # resolved and therefore must not suppress the request.
            continue
        if lane != "deterministic_core":
            continue
        evidence = finding.get("evidence")
        if isinstance(evidence, dict) and (
            evidence.get("usable_runtime_contradiction") is True
            or evidence.get("runtime_contradiction") is True
        ):
            return False
        if (
            finding.get("proven_defect") is True
            or finding.get("blocking") is True
            or finding.get("advisory") is not True
        ):
            return False
    return True


def _run_review_locked(
    input_path: Path,
    agent_assessment_path: Path | None = None,
    agent_contract_assessment_path: Path | None = None,
    resource_timeout: float = 8,
    allow_private_network: bool = False,
    audit_output_dir: Path | None = None,
    output_purpose: str = "review",
    run_id: str | None = None,
    lock: ReviewOutputLock | None = None,
    attestation_output_path: Path | None = None,
    *,
    require_agent_assessment: bool | None = None,
) -> dict[str, Any]:
    root = locate_root(input_path)
    output_dir = resolve_output_destination(
        root, audit_output_dir, purpose=output_purpose
    )
    sandbox_runtime.ensure_env()
    skip_paper = False
    agent_assessment: dict[str, Any] | None = None
    agent_contract_assessment: dict[str, Any] | None = None
    paper_skip_reason: str | None = None
    must_require_assessment = (
        assessment_required_for_purpose(output_purpose)
        if require_agent_assessment is None
        else require_agent_assessment
    )
    if agent_assessment_path is not None:
        agent_assessment, assessment_error = try_load_agent_assessment(
            root,
            agent_assessment_path.expanduser().resolve(),
        )
        if agent_assessment is None:
            if must_require_assessment:
                return _assessment_pending_result(
                    root,
                    output_dir=output_dir,
                    message=assessment_error
                    or "paper Agent assessment is invalid",
                    assessment_path=agent_assessment_path,
                )
            raise ValueError(
                assessment_error or "paper Agent assessment is invalid"
            )
        skip_paper = bool(agent_assessment.get("paper_skipped"))
        if skip_paper:
            paper_skip_reason = agent_assessment.get("paper_skip_reason")
    elif must_require_assessment:
        return _assessment_pending_result(
            root,
            output_dir=output_dir,
            message=(
                "equal-depth re-audit requires the inherited paper Agent "
                "assessment; deterministic-only fallback is not permitted"
            ),
        )
    request_path = output_dir / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    existing_request = request_path.is_file()
    pending_request: dict[str, Any] | None = None
    if existing_request:
        try:
            request_preview = read_json(request_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            raise ValueError(
                "agent contract request is unreadable"
            ) from exc
        pending_audit_id = request_preview.get("audit_id")
        if not isinstance(pending_audit_id, str) or not pending_audit_id:
            raise ValueError("agent contract request audit ID is invalid")
        temp_dir = (
            output_dir / ".benchmark_audit_tmp" / pending_audit_id
        )
        pending_request = validate_agent_contract_request(root, temp_dir)
        if agent_assessment_path is None:
            quality_path = temp_dir / "agent_quality/assessment.json"
            if quality_path.is_file():
                stored_quality = read_json(quality_path)
                stored_assessment = (
                    stored_quality.get("assessment")
                    if isinstance(stored_quality, dict)
                    else None
                )
                if isinstance(stored_assessment, dict) and stored_assessment:
                    agent_assessment = stored_assessment
                    skip_paper = bool(stored_assessment.get("paper_skipped"))
                    if skip_paper:
                        paper_skip_reason = stored_assessment.get(
                            "paper_skip_reason"
                        )
            if must_require_assessment and agent_assessment is None:
                return _assessment_pending_result(
                    root,
                    output_dir=output_dir,
                    message=(
                        "equal-depth re-audit is paused: inherited paper "
                        "Agent assessment is absent from the prepared workspace"
                    ),
                )
        context = read_json(temp_dir / "audit_context.json")
        if context.get("skip_paper") is not skip_paper:
            raise ValueError("agent contract request paper mode is stale")
        if agent_contract_assessment_path is None:
            pending = _pending_result(root, output_dir, pending_request)
            if attestation_output_path is not None:
                pending["audit_attestation"] = (
                    "NOT_AVAILABLE_AGENT_CONTRACT_PENDING"
                )
            return pending
        static_result, checker_result, resource_result = (
            _load_prepared_inputs(temp_dir)
        )
    else:
        context = prepare_workspace(
            root,
            output_dir,
            skip_paper=skip_paper,
            run_id=run_id,
        )
        temp_dir = Path(context["audit_temp_dir"])
        static_result = static_audit(
            root, temp_dir / "evidence/static_checks/audit_static.json"
        )
        static_fatal = any(
            issue["severity"] == "FATAL"
            for issue in static_result["issues"]
        )
        checker_ready = all(
            static_result["parse_status"].get(role) == "ok"
            for role in (
                "tests/checker.py",
                "tests/grading_spec.json",
                "tests/test.sh",
            )
        ) and (
            static_result.get("contract_map", {})
            .get("checker_analysis", {})
            .get("parse_status")
            == "OK"
        )
        if static_fatal or not checker_ready:
            checker_result = checker_skipped_by_static_gate(
                root,
                temp_dir / "checker_tests.json",
                reason=(
                    "HARBOR_VERIFIER_ENTRYPOINT_MISSING"
                    if static_result["parse_status"].get("tests/test.sh")
                    != "ok"
                    else "REQUIRED_CHECKER_MISSING_OR_UNPARSEABLE"
                    if not checker_ready
                    else "STATIC_FATAL_GATE"
                ),
            )
        else:
            checker_result = dynamic_checker_probe(
                root,
                temp_dir / "checker_tests.json",
            )
        resource_result = probe_resources(
            root,
            temp_dir / "resource_checks.json",
            timeout=resource_timeout,
            allow_private_network=allow_private_network,
        )
    execution_evidence = _execution_evidence()
    if agent_assessment is not None and not skip_paper:
        record_paper_input_hashes(root, temp_dir)
    external_bindings = bind_external_evidence(
        temp_dir,
        agent_assessment_path if agent_assessment is not None else None,
        agent_contract_assessment_path,
    )
    report = synthesize_report(
        root,
        temp_dir,
        static_result,
        checker_result,
        resource_result=resource_result,
        execution_evidence=execution_evidence,
        agent_assessment=agent_assessment,
        paper_skip_reason=paper_skip_reason,
        external_bindings=external_bindings,
    )
    machine_contract = report["deterministic_contract"]
    if agent_contract_assessment_path is not None:
        agent_contract_assessment = validate_agent_contract_assessment(
            read_json(agent_contract_assessment_path.expanduser().resolve()),
            machine_contract,
        )
        report = synthesize_report(
            root,
            temp_dir,
            static_result,
            checker_result,
            resource_result=resource_result,
            execution_evidence=execution_evidence,
            agent_assessment=agent_assessment,
            agent_contract_assessment=agent_contract_assessment,
            paper_skip_reason=paper_skip_reason,
            external_bindings=external_bindings,
        )
        if (
            pending_request is not None
            and report["deterministic_contract"].get("contract_digest")
            != pending_request.get("machine_contract_digest")
        ):
            raise ValueError(
                "agent contract resume machine contract digest is stale"
            )
        unavailable_not_proven = any(
            item.get("status") == "NOT_PROVEN"
            and next(
                (
                    check.get("status")
                    for check in machine_contract.get("checks", [])
                    if check.get("check_id") == item.get("check_id")
                ),
                None,
            )
            in UNAVAILABLE_CHECK_STATUSES
            for item in agent_contract_assessment.get("checks", [])
            if isinstance(item, dict)
        )
        if pending_request is not None and unavailable_not_proven:
            pending = _pending_result(root, output_dir, pending_request)
            pending["agent_contract_status"] = "NOT_PROVEN"
            pending["message"] = (
                "Agent D6 assessment did not prove the scoring chain. "
                "The prepared Review remains EVIDENCE_PENDING and resumable."
            )
            return pending
    elif agent_contract_pending_eligible(machine_contract, report):
        request = write_agent_contract_request(
            root, temp_dir, machine_contract
        )
        return _pending_result(root, output_dir, request)
    result = finalize_audit(
        root,
        output_dir=output_dir,
        temp_dir=temp_dir,
        lock=lock,
    )
    result["agent_contract_status"] = (
        "APPLIED" if agent_contract_assessment is not None else "NOT_SUPPLIED"
    )
    if existing_request:
        archived_request = archive_agent_contract_request(
            output_dir, result.get("audit_id", context.get("audit_id"))
        )
        if archived_request is not None:
            result["agent_contract_request_archive"] = str(archived_request)
    if attestation_output_path is not None:
        result["audit_attestation"] = write_audit_attestation(
            Path(result["benchmark_root"]),
            attestation_output_path,
            audit_dir=Path(result["audit_dir"]),
        )
    return result


def run_review(
    input_path: Path,
    agent_assessment_path: Path | None = None,
    agent_contract_assessment_path: Path | None = None,
    resource_timeout: float = 8,
    allow_private_network: bool = False,
    audit_output_dir: Path | None = None,
    output_purpose: str = "review",
    attestation_output_path: Path | None = None,
    *,
    require_agent_assessment: bool | None = None,
) -> dict[str, Any]:
    root = locate_root(input_path)
    output_dir = resolve_output_destination(
        root, audit_output_dir, purpose=output_purpose
    )
    run_id = new_audit_id()
    with ReviewOutputLock(output_dir, run_id) as lock:
        try:
            return _run_review_locked(
                input_path,
                agent_assessment_path=agent_assessment_path,
                agent_contract_assessment_path=agent_contract_assessment_path,
                resource_timeout=resource_timeout,
                allow_private_network=allow_private_network,
                audit_output_dir=output_dir,
                output_purpose=output_purpose,
                run_id=run_id,
                lock=lock,
                attestation_output_path=attestation_output_path,
                require_agent_assessment=require_agent_assessment,
            )
        except Exception:
            own_temp = output_dir / ".benchmark_audit_tmp" / run_id
            if own_temp.is_dir() and not own_temp.is_symlink():
                shutil.rmtree(own_temp)
            raise


def run_review_context(run_dir: Path) -> dict[str, Any]:
    """Run Review using the immutable package/run relationship in context.json."""

    run_dir = run_dir.expanduser().resolve()
    context = load_context(run_dir)
    package = Path(context["package_path"])
    assessment = run_dir / "agent_assessment.json"
    contract_assessment = run_dir / "agent_contract" / "assessment.json"
    with PackageRunLock(run_dir):
        current = status(run_dir)
        if current["state"] not in {
            "ASSIGNED",
            "AGENT_ASSESSMENT_PENDING",
            "AGENT_CONTRACT_PENDING",
            "REVIEWING",
        }:
            raise RunContextError(
                f"Review cannot start from state {current['state']}"
            )
        loaded_assessment, assessment_error = try_load_agent_assessment(
            package,
            assessment if assessment.is_file() else None,
        )
        if loaded_assessment is None:
            pending = _assessment_pending_result(
                package,
                output_dir=run_dir / "audit",
                message=assessment_error
                or "paper Agent assessment is required before dual-lane Review",
                assessment_path=assessment,
            )
            if current["state"] == "ASSIGNED":
                transition(
                    run_dir,
                    "AGENT_ASSESSMENT_PENDING",
                    review_result=pending,
                )
            elif current["state"] == "AGENT_ASSESSMENT_PENDING":
                # Idempotent pause: keep diagnostics, never freeze A0/formal audit.
                write_json_atomic(
                    run_dir / "status.json",
                    {
                        **current,
                        "review_result": pending,
                        "updated_at": now(),
                    },
                )
            else:
                # Never continue a contract overlay or mid-review without paper assessment.
                transition(
                    run_dir,
                    "AGENT_ASSESSMENT_PENDING",
                    review_result=pending,
                )
            return pending
        if current["state"] in {
            "ASSIGNED",
            "AGENT_ASSESSMENT_PENDING",
            "AGENT_CONTRACT_PENDING",
        }:
            transition(run_dir, "REVIEWING")
        try:
            if not (run_dir / "snapshot").exists():
                snapshot_package(package, run_dir)
            supplied_contract_assessment = None
            if contract_assessment.is_file():
                candidate = read_json(contract_assessment)
                if candidate:
                    supplied_contract_assessment = contract_assessment
            result = run_review(
                package,
                agent_assessment_path=assessment,
                agent_contract_assessment_path=supplied_contract_assessment,
                audit_output_dir=run_dir / "audit",
                output_purpose="run",
                attestation_output_path=run_dir / "audit_attestation.json",
                require_agent_assessment=True,
            )
            if result.get("status") == AGENT_ASSESSMENT_PENDING:
                transition(
                    run_dir,
                    "AGENT_ASSESSMENT_PENDING",
                    review_result=result,
                )
                return result
            if result.get("status") == AGENT_CONTRACT_PENDING:
                request = run_dir / "audit" / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
                if request.is_file():
                    shutil.copy2(request, run_dir / AGENT_CONTRACT_REQUEST_RELATIVE_PATH)
                transition(run_dir, "AGENT_CONTRACT_PENDING", review_result=result)
                return result
            write_content_root(run_dir, "A0")
            transition(run_dir, "REVIEWED", review_result=result)
            summary = result.get("summary", {})
            verdict = result.get("review_verdict") or (
                summary.get("final_verdict") if isinstance(summary, dict) else None
            )
            if verdict == "PASS":
                complete(run_dir, outcome="NOT_REQUIRED", repair_status="NOT_REQUIRED")
            elif verdict == "REJECT":
                complete(run_dir, outcome="ABANDONED", repair_status="ABANDONED")
            return result
        except Exception as exc:
            transition(run_dir, "FAILED", error=str(exc))
            raise


def resolve_output_destination(
    root: Path,
    output_dir: Path | None,
    *,
    purpose: str,
) -> Path:
    """Resolve only the canonical initial-review or re-audit workspace."""
    if purpose not in {"review", "reaudit", "run"}:
        raise ValueError(f"unsupported output purpose: {purpose}")
    if purpose == "run":
        resolved = output_dir.expanduser().resolve() if output_dir else None
        if resolved is None or resolved == root or resolved.is_relative_to(root):
            raise ValueError("run audit output must remain outside the Harbor package")
        return resolved
    if output_dir is None:
        if purpose != "review":
            raise ValueError("re-audit output directory must be explicit")
        return default_review_output_dir(root)
    return require_external_output_dir(root, output_dir, purpose=purpose)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Dual-lane materials review "
            f"(review_lane={REVIEW_LANE})."
        )
    )
    parser.add_argument(
        "--run-dir",
        required=True,
        help="the sole public run context for a review lifecycle",
    )
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        result = run_review_context(Path(arguments.run_dir))
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"materials review failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
