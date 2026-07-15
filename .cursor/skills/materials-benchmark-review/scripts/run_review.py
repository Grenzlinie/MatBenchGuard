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
from prepare_audit_output import locate_root, prepare_workspace
from probe_resources import probe_resources, run_e2_smoke


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
    execution_level: str = "E1",
    resource_timeout: float = 8,
    e2_smoke_plan: Path | None = None,
    allow_private_network: bool = False,
) -> dict[str, Any]:
    root = locate_root(input_path)
    context = prepare_workspace(root, "no_paper", execution_level)
    temp_dir = Path(context["audit_temp_dir"])
    static_result = static_audit(
        root, temp_dir / "evidence/static_checks/audit_static.json"
    )
    if any(
        issue["severity"] == "FATAL" for issue in static_result["issues"]
    ):
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
    synthesize_report(
        root,
        temp_dir,
        static_result,
        checker_result,
        resource_result=resource_result,
        execution_evidence=execution_evidence,
    )
    return finalize_audit(root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Harbor 题包 directory")
    parser.add_argument(
        "--paper-mode", choices=["no_paper"], default="no_paper"
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
