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


def run_review(
    input_path: Path, known_valid_output: Path | None
) -> dict[str, Any]:
    root = locate_root(input_path)
    context = prepare_workspace(root, "no_paper", "E1")
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
    synthesize_report(root, temp_dir, static_result, checker_result)
    return finalize_audit(root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Harbor 题包 directory")
    parser.add_argument(
        "--paper-mode", choices=["no_paper"], default="no_paper"
    )
    parser.add_argument(
        "--execution-level", choices=["E1"], default="E1"
    )
    parser.add_argument(
        "--known-valid-output",
        help="independently justified public output directory",
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
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"materials review failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
