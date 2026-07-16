#!/usr/bin/env python3
"""Run the first end-to-end no-paper E1 materials benchmark review slice."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from audit_package import static_audit
from dynamic_checker_probe import dynamic_checker_probe
from finalize_audit_output import finalize_audit, synthesize_report
from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    bind_external_evidence,
    locate_root,
    prepare_workspace,
    record_paper_input_hashes,
    skill_root,
    validate_paper_boundary,
)
from probe_resources import probe_resources, run_e2_smoke


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
PAPER_TRIGGERS = {
    "SCIENTIFIC_CONFLICT",
    "NECESSARY_INFORMATION_MISSING",
    "GOLD_PROVENANCE_UNCERTAIN",
    "EXPLICIT_REPRODUCTION_CLAIM",
}
PAPER_TRIGGER_ADJUDICATION_STATUSES = {"TRIGGERED", "NOT_TRIGGERED"}
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


def validate_agent_assessment(
    root: Path, path: Path, paper_mode: str
) -> dict[str, Any]:
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
        "schema_version": "0.1",
        "taxonomy": normalized_taxonomy,
        "taxonomy_evidence": validate_taxonomy_evidence(
            root,
            assessment.get("taxonomy_evidence"),
            normalized_taxonomy,
        ),
        "taxonomy_source": taxonomy["source"],
    }
    qualification = assessment.get("materials_qualification")
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
        normalized["materials_qualification"] = {
            "classification": classification,
            "rationale": rationale,
            "evidence": normalized_evidence,
            "authoritative": True,
        }
    if paper_mode == "no_paper":
        adjudication = assessment.get("paper_trigger_adjudication")
        if not isinstance(adjudication, list) or {
            item.get("trigger")
            for item in adjudication
            if isinstance(item, dict)
        } != PAPER_TRIGGERS:
            raise ValueError(
                "paper_trigger_adjudication must cover exactly "
                f"{sorted(PAPER_TRIGGERS)}"
            )
        normalized_adjudication: list[dict[str, Any]] = []
        for index, item in enumerate(adjudication, start=1):
            if not isinstance(item, dict):
                raise ValueError(
                    f"paper trigger adjudication {index} must be an object"
                )
            trigger = item.get("trigger")
            status = item.get("status")
            rationale = item.get("rationale")
            evidence = item.get("evidence")
            if status not in PAPER_TRIGGER_ADJUDICATION_STATUSES:
                raise ValueError(
                    f"paper trigger adjudication {trigger} has invalid status"
                )
            if not isinstance(rationale, str) or not rationale.strip():
                raise ValueError(
                    f"paper trigger adjudication {trigger} requires a rationale"
                )
            if not isinstance(evidence, list) or not evidence:
                raise ValueError(
                    f"paper trigger adjudication {trigger} requires evidence"
                )
            normalized_evidence: list[dict[str, str]] = []
            for evidence_index, evidence_item in enumerate(evidence, start=1):
                if not isinstance(evidence_item, dict):
                    raise ValueError(
                        f"paper trigger adjudication {trigger} evidence "
                        f"{evidence_index} must be an object"
                    )
                package_file, package_quote = validate_package_quote(
                    root,
                    evidence_item.get("package_file"),
                    evidence_item.get("package_quote"),
                    f"paper trigger adjudication {trigger} evidence "
                    f"{evidence_index}",
                )
                normalized_evidence.append(
                    {
                        "package_file": package_file,
                        "package_quote": package_quote,
                    }
                )
            normalized_adjudication.append(
                {
                    "trigger": trigger,
                    "status": status,
                    "rationale": rationale.strip(),
                    "evidence": normalized_evidence,
                }
            )
        normalized["paper_trigger_adjudication"] = normalized_adjudication
        if (
            "paper_triggers" in assessment
            or "reproduction_type" in assessment
            or "dimensions" in assessment
        ):
            raise ValueError(
                "no_paper assessment must not claim paper fidelity"
            )
        return normalized

    triggers = assessment.get("paper_triggers")
    if (
        not isinstance(triggers, list)
        or not triggers
        or not all(isinstance(item, str) for item in triggers)
    ):
        raise ValueError("paper_grounded assessment requires paper_triggers")
    unknown_triggers = sorted(set(triggers) - PAPER_TRIGGERS)
    if unknown_triggers:
        raise ValueError(f"unknown paper triggers: {unknown_triggers}")
    adjudication = assessment.get("paper_trigger_adjudication")
    if not isinstance(adjudication, list) or {
        item.get("trigger")
        for item in adjudication
        if isinstance(item, dict)
    } != PAPER_TRIGGERS:
        raise ValueError(
            "paper_trigger_adjudication must cover exactly "
            f"{sorted(PAPER_TRIGGERS)}"
        )
    normalized_adjudication: list[dict[str, Any]] = []
    for index, item in enumerate(adjudication, start=1):
        if not isinstance(item, dict):
            raise ValueError(
                f"paper trigger adjudication {index} must be an object"
            )
        trigger = item.get("trigger")
        status = item.get("status")
        rationale = item.get("rationale")
        evidence = item.get("evidence")
        if status not in PAPER_TRIGGER_ADJUDICATION_STATUSES:
            raise ValueError(
                f"paper trigger adjudication {trigger} has invalid status"
            )
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError(
                f"paper trigger adjudication {trigger} requires a rationale"
            )
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(
                f"paper trigger adjudication {trigger} requires evidence"
            )
        normalized_evidence: list[dict[str, str]] = []
        for evidence_index, evidence_item in enumerate(evidence, start=1):
            if not isinstance(evidence_item, dict):
                raise ValueError(
                    f"paper trigger adjudication {trigger} evidence "
                    f"{evidence_index} must be an object"
                )
            package_file, package_quote = validate_package_quote(
                root,
                evidence_item.get("package_file"),
                evidence_item.get("package_quote"),
                f"paper trigger adjudication {trigger} evidence "
                f"{evidence_index}",
            )
            normalized_evidence.append(
                {
                    "package_file": package_file,
                    "package_quote": package_quote,
                }
            )
        normalized_adjudication.append(
            {
                "trigger": trigger,
                "status": status,
                "rationale": rationale.strip(),
                "evidence": normalized_evidence,
            }
        )
    if {
        item["trigger"]
        for item in normalized_adjudication
        if item["status"] == "TRIGGERED"
    } != set(triggers):
        raise ValueError(
            "paper_triggers must equal the TRIGGERED adjudication set"
        )
    normalized["paper_trigger_adjudication"] = normalized_adjudication
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
    paper_path = root / "paper/paper.md"
    validate_paper_boundary(root)
    paper_text = paper_path.read_text(encoding="utf-8", errors="replace")
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
    normalized.update(
        {
            "paper_triggers": list(dict.fromkeys(triggers)),
            "reproduction_type": reproduction_type,
            "dimensions": normalized_dimensions,
        }
    )
    return normalized


def checker_skipped_by_static_gate(
    root: Path, output: Path, reason: str = "STATIC_GATE"
) -> dict[str, Any]:
    result = {
        "schema_version": "0.1",
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
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
        "probe_coverage": {
            probe_class: {
                "status": "NOT_ASSESSABLE",
                "reason": reason,
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
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
                        "instrumentation": "PYTHON_FILE_ACCESS_TRACE",
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
                "process_evidence",
            )
        },
        "limitations": [
            "E1 checker probes were skipped because the checker contract was not runnable."
        ],
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
        "schema_version": "0.1",
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


def run_review(
    input_path: Path,
    known_valid_output: Path | None,
    paper_mode: str = "no_paper",
    agent_assessment_path: Path | None = None,
    execution_level: str = "E1",
    resource_timeout: float = 8,
    e2_smoke_plan: Path | None = None,
    allow_private_network: bool = False,
) -> dict[str, Any]:
    root = locate_root(input_path)
    context = prepare_workspace(root, paper_mode, execution_level)
    temp_dir = Path(context["audit_temp_dir"])
    static_result = static_audit(
        root, temp_dir / "evidence/static_checks/audit_static.json"
    )
    static_fatal = any(
        issue["severity"] == "FATAL" for issue in static_result["issues"]
    )
    checker_ready = all(
        static_result["parse_status"].get(role) == "ok"
        for role in ("tests/checker.py", "tests/grading_spec.json")
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
                "REQUIRED_CHECKER_MISSING_OR_UNPARSEABLE"
                if not checker_ready
                else "STATIC_FATAL_GATE"
            ),
        )
    else:
        checker_result = dynamic_checker_probe(
            root,
            temp_dir / "checker_tests.json",
            known_valid_output=known_valid_output,
        )
    resource_result = probe_resources(
        root,
        temp_dir / "resource_checks.json",
        timeout=resource_timeout,
        allow_private_network=allow_private_network,
    )
    if execution_level == "E2":
        if e2_smoke_plan is None:
            raise ValueError("E2 requires --e2-smoke-plan")
        execution_evidence = run_e2_smoke(
            root,
            e2_smoke_plan,
            resource_result,
        )
    else:
        if e2_smoke_plan is not None:
            raise ValueError("--e2-smoke-plan is only valid for E2")
        execution_evidence = {
            "status": "NOT_ASSESSED",
            "claim": "E1_CHECKER_ONLY",
            "scientific_reproduction": False,
            "environment": None,
            "environment_verified": False,
            "verifies_resources": [],
            "returncode": None,
            "stdout": "",
            "stderr": "",
            "reason": "E1 executes checker probes but not the scientific workflow.",
        }
    agent_assessment: dict[str, Any] | None = None
    paper_skip_reason: str | None = None
    if paper_mode == "paper_grounded" and static_fatal:
        paper_skip_reason = (
            "Paper-grounded review was skipped because the no-paper E1 "
            "stage triggered an unrecoverable Hard gate."
        )
    elif agent_assessment_path is not None:
        agent_assessment = validate_agent_assessment(
            root,
            agent_assessment_path.expanduser().resolve(),
            paper_mode,
        )
        if paper_mode == "paper_grounded":
            record_paper_input_hashes(root, temp_dir)
    elif paper_mode == "paper_grounded":
        raise ValueError(
            "paper_grounded mode requires --agent-assessment after the "
            "no-paper gate passes"
        )
    external_bindings = bind_external_evidence(
        temp_dir,
        known_valid_output,
        agent_assessment_path if agent_assessment is not None else None,
    )
    synthesize_report(
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
    return finalize_audit(root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Harbor 题包 directory")
    parser.add_argument(
        "--paper-mode",
        choices=["no_paper", "paper_grounded"],
        default="no_paper",
    )
    parser.add_argument(
        "--execution-level", choices=["E1", "E2"], default="E1"
    )
    parser.add_argument(
        "--known-valid-output",
        help="independently justified public output directory",
    )
    parser.add_argument(
        "--resource-timeout",
        type=float,
        default=8,
        help="per-resource network timeout in seconds",
    )
    parser.add_argument(
        "--e2-smoke-plan",
        help="external E2 smoke plan JSON",
    )
    parser.add_argument(
        "--allow-private-network",
        action="store_true",
        help="allow private/loopback resource URLs in a controlled test environment",
    )
    parser.add_argument(
        "--agent-assessment",
        help="Agent-authored paper fidelity and taxonomy assessment JSON",
    )
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        result = run_review(
            Path(arguments.input),
            (
                Path(arguments.known_valid_output)
                if arguments.known_valid_output
                else None
            ),
            paper_mode=arguments.paper_mode,
            agent_assessment_path=(
                Path(arguments.agent_assessment)
                if arguments.agent_assessment
                else None
            ),
            execution_level=arguments.execution_level,
            resource_timeout=arguments.resource_timeout,
            e2_smoke_plan=(
                Path(arguments.e2_smoke_plan)
                if arguments.e2_smoke_plan
                else None
            ),
            allow_private_network=arguments.allow_private_network,
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"materials review failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
