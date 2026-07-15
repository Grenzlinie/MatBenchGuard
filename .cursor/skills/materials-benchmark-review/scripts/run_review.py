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
    REQUIRED_ROLES,
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
TAXONOMY_EVIDENCE_DIMENSIONS = {
    "computation_task",
    "research_domain",
    "material_system.primary",
    "material_system.secondary",
}
PACKAGE_EVIDENCE_ROLES = frozenset(REQUIRED_ROLES)


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
    if package_file not in PACKAGE_EVIDENCE_ROLES:
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
    if paper_mode == "no_paper":
        if "reproduction_type" in assessment or "dimensions" in assessment:
            raise ValueError(
                "no_paper assessment must not claim paper fidelity"
            )
        return normalized

    reproduction_type = assessment.get("reproduction_type")
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
            "reproduction_type": reproduction_type,
            "dimensions": normalized_dimensions,
        }
    )
    return normalized


def checker_skipped_by_static_gate(
    root: Path, output: Path
) -> dict[str, Any]:
    result = {
        "schema_version": "0.1",
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
        "solution_content_inspected": False,
        "pass_threshold": None,
        "tests": [],
        "findings": [],
        "usable_reward_count": 0,
        "limitations": [
            "E1 checker probes were skipped because an E0 FATAL gate failed."
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
    if static_fatal:
        checker_result = checker_skipped_by_static_gate(
            root, temp_dir / "checker_tests.json"
        )
    else:
        checker_result = dynamic_checker_probe(
            root,
            temp_dir / "checker_tests.json",
            known_valid_output=known_valid_output,
        )
    resource_parse_status = static_result["parse_status"].get(
        "resources.json", "missing"
    )
    if resource_parse_status == "ok":
        resource_result = probe_resources(
            root,
            temp_dir / "resource_checks.json",
            timeout=resource_timeout,
            allow_private_network=allow_private_network,
        )
    else:
        resource_result = resources_skipped_by_static_gate(
            root,
            temp_dir / "resource_checks.json",
            resource_parse_status,
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
    synthesize_report(
        root,
        temp_dir,
        static_result,
        checker_result,
        resource_result=resource_result,
        execution_evidence=execution_evidence,
        agent_assessment=agent_assessment,
        paper_skip_reason=paper_skip_reason,
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
