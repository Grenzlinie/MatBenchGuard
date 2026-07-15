#!/usr/bin/env python3
"""Execute isolated E1 submissions against the real Harbor checker."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from prepare_audit_output import basename, iter_public_files, locate_root


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def grading_steps(specification: dict[str, Any]) -> list[dict[str, Any]]:
    return specification.get("steps", specification.get("checks", [])) or []


def matching_step(
    specification: dict[str, Any], filename: str
) -> dict[str, Any] | None:
    for step in grading_steps(specification):
        if basename(step.get("output_file")) == filename:
            return step
    return None


def table_value(column: str, mode: str) -> Any:
    normalized = column.lower()
    if normalized == "direction":
        return "100"
    if normalized == "mode":
        return "L"
    if mode == "nonfinite":
        return "nan"
    if mode == "random":
        return random.uniform(-1000, 1000)
    return 0


def write_synthetic_outputs(
    output_dir: Path, specification: dict[str, Any], mode: str
) -> list[str]:
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        path = output_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        output_format = str(output.get("format", "")).lower()
        schema = output.get("schema", {}) or {}
        step = matching_step(specification, filename)
        if output_format == "json":
            required = schema.get("required", {}) or {}
            fields = (
                list(required.keys())
                if isinstance(required, dict)
                else list(required)
            )
            value = {
                field: (
                    float("nan")
                    if mode == "nonfinite"
                    else random.uniform(-1000, 1000)
                    if mode == "random"
                    else (step or {}).get("target_value", 0)
                )
                for field in fields
            }
            path.write_text(
                json.dumps(value, allow_nan=True), encoding="utf-8"
            )
        elif output_format in {"csv", "tsv"}:
            raw_columns = schema.get("required_columns", []) or []
            columns = [
                item.get("name") if isinstance(item, dict) else str(item)
                for item in raw_columns
            ]
            delimiter = "\t" if output_format == "tsv" else ","
            rows: list[dict[str, Any]] = []
            if mode in {"random", "minimal", "nonfinite", "duplicate"}:
                rows = [
                    {
                        column: table_value(column, mode)
                        for column in columns
                    }
                ]
                if mode == "duplicate":
                    rows *= 2
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle, fieldnames=columns, delimiter=delimiter
                )
                writer.writeheader()
                writer.writerows(rows)
        else:
            path.write_text(
                "" if mode == "empty" else "synthetic\n", encoding="utf-8"
            )
        created.append(filename)
    return created


def reject_solution_fixture(root: Path, source_dir: Path) -> Path:
    source_dir = source_dir.expanduser().resolve()
    solution_dir = (root / "solution").resolve()
    if source_dir == solution_dir or source_dir.is_relative_to(solution_dir):
        raise ValueError("known-valid output cannot come from solution/")
    if not source_dir.is_dir():
        raise ValueError(f"known-valid output is not a directory: {source_dir}")
    return source_dir


def copy_known_valid_outputs(
    root: Path,
    source_dir: Path,
    output_dir: Path,
    specification: dict[str, Any],
) -> list[str]:
    source_dir = reject_solution_fixture(root, source_dir)
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        source = (source_dir / filename).resolve()
        if source.parent != source_dir or not source.is_file():
            raise FileNotFoundError(
                f"known-valid output is missing contracted file: {filename}"
            )
        destination = output_dir / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        created.append(filename)
    return created


def retain_one_known_valid_row(
    output_dir: Path, specification: dict[str, Any]
) -> None:
    """Turn a public valid table into a sparse but value-correct submission."""
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        output_format = str(output.get("format", "")).lower()
        if output_format not in {"csv", "tsv"}:
            continue
        path = output_dir / basename(output.get("file"))
        delimiter = "\t" if output_format == "tsv" else ","
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle, delimiter=delimiter))
        if not rows:
            continue
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=list(rows[-1]), delimiter=delimiter
            )
            writer.writeheader()
            writer.writerow(rows[-1])


def copy_public_package(root: Path, destination: Path) -> None:
    """Copy the checker runtime context without solution or audit artifacts."""
    for source in iter_public_files(root):
        relative = source.relative_to(root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def run_checker_case(
    root: Path,
    checker_text: str,
    specification: dict[str, Any],
    case_name: str,
    mode: str,
    known_valid_output: Path | None,
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"materials_checker_{case_name}_") as tmp:
        base = Path(tmp)
        package_dir = base / "package"
        tests_dir = base / "tests"
        outputs_dir = base / "app" / "outputs"
        logs_dir = base / "logs" / "verifier"
        copy_public_package(root, package_dir)
        tests_dir.mkdir(parents=True)
        outputs_dir.mkdir(parents=True)
        logs_dir.mkdir(parents=True)
        specification_path = tests_dir / "grading_spec.json"
        specification_path.write_text(
            json.dumps(specification, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        created: list[str] = []
        if mode in {"known_valid", "sparse_known_valid"}:
            if known_valid_output is None:
                raise ValueError("known-valid case requires an output directory")
            created = copy_known_valid_outputs(
                root, known_valid_output, outputs_dir, specification
            )
            if mode == "sparse_known_valid":
                retain_one_known_valid_row(outputs_dir, specification)
        elif mode != "missing":
            created = write_synthetic_outputs(
                outputs_dir, specification, mode
            )

        patched = checker_text
        patched = patched.replace(
            "/tests/grading_spec.json", str(specification_path)
        )
        patched = patched.replace("/app/outputs", str(outputs_dir))
        patched = patched.replace("/logs/verifier", str(logs_dir))
        checker_path = base / "checker_patched.py"
        checker_path.write_text(patched, encoding="utf-8")
        process = subprocess.run(
            [sys.executable, str(checker_path)],
            cwd=package_dir,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        reward: float | str | None = None
        reward_path = logs_dir / "reward.txt"
        if reward_path.exists():
            raw_reward = reward_path.read_text(
                encoding="utf-8", errors="replace"
            ).strip()
            try:
                reward = float(raw_reward)
            except ValueError:
                reward = raw_reward
        breakdown: Any = None
        breakdown_path = logs_dir / "breakdown.json"
        if breakdown_path.exists():
            try:
                breakdown = read_json(breakdown_path)
            except json.JSONDecodeError:
                breakdown = breakdown_path.read_text(
                    encoding="utf-8", errors="replace"
                )
        return {
            "case": case_name,
            "mode": mode,
            "created_outputs": created,
            "returncode": process.returncode,
            "reward": reward,
            "breakdown": breakdown,
            "stdout": process.stdout[-4000:],
            "stderr": process.stderr[-4000:],
            "crashed": process.returncode != 0,
            "runtime_package_contains_solution": (
                package_dir / "solution"
            ).exists(),
        }


def finding(
    severity: str,
    code: str,
    message: str,
    test_type: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "severity": severity,
        "code": code,
        "message": message,
        "test_type": test_type,
        "evidence": evidence,
    }


def evaluate_results(
    results: list[dict[str, Any]], pass_threshold: float
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    adversarial = {
        "missing_outputs",
        "empty_valid_shape",
        "random_baseline",
        "minimal_gold_shape",
        "duplicate_gold_rows",
        "nonfinite_values",
        "sparse_known_valid",
    }
    for result in results:
        case = result["case"]
        if result["runtime_package_contains_solution"]:
            findings.append(
                finding(
                    "FATAL",
                    "SOLUTION_BOUNDARY_VIOLATION",
                    "isolated checker runtime contains solution content",
                    case,
                    {},
                )
            )
        if result["crashed"]:
            findings.append(
                finding(
                    "HIGH",
                    "CHECKER_CRASH",
                    f"checker crashed for {case}",
                    case,
                    {"stderr": result["stderr"]},
                )
            )
        reward = result.get("reward")
        if not isinstance(reward, float) or not math.isfinite(reward):
            findings.append(
                finding(
                    "HIGH",
                    "CHECKER_RESULT_UNUSABLE",
                    f"checker did not emit a numeric reward for {case}",
                    case,
                    {"reward": reward},
                )
            )
            continue
        if case in adversarial and reward >= pass_threshold:
            findings.append(
                finding(
                    "FATAL",
                    "ADVERSARIAL_OUTPUT_PASSES",
                    f"{case} receives a passing checker reward",
                    case,
                    {
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                    },
                )
            )
        if case == "known_valid_public" and reward < pass_threshold:
            findings.append(
                finding(
                    "HIGH",
                    "KNOWN_VALID_OUTPUT_REJECTED",
                    "independently justified public output does not pass",
                    case,
                    {
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                    },
                )
            )
    return findings


def dynamic_checker_probe(
    root: Path, output: Path, known_valid_output: Path | None = None
) -> dict[str, Any]:
    checker_text = (root / "tests/checker.py").read_text(
        encoding="utf-8", errors="replace"
    )
    specification = read_json(root / "tests/grading_spec.json")
    pass_threshold = float(specification.get("pass_threshold", 1.0))
    if not math.isfinite(pass_threshold) or not 0 <= pass_threshold <= 1:
        raise ValueError(
            "pass threshold must be a finite number between zero and one"
        )
    random.seed(17)
    cases = [
        ("missing_outputs", "missing"),
        ("empty_valid_shape", "empty"),
        ("random_baseline", "random"),
        ("minimal_gold_shape", "minimal"),
        ("duplicate_gold_rows", "duplicate"),
        ("nonfinite_values", "nonfinite"),
    ]
    if known_valid_output is not None:
        cases.extend(
            (
                ("known_valid_public", "known_valid"),
                ("sparse_known_valid", "sparse_known_valid"),
            )
        )
    results = [
        run_checker_case(
            root,
            checker_text,
            specification,
            case_name,
            mode,
            known_valid_output,
        )
        for case_name, mode in cases
    ]
    findings = evaluate_results(results, pass_threshold)
    expected = {
        "missing_outputs": "score below pass threshold without crashing",
        "empty_valid_shape": "score below pass threshold without crashing",
        "random_baseline": "score below pass threshold",
        "minimal_gold_shape": "score below pass threshold",
        "duplicate_gold_rows": "duplicates do not create a passing score",
        "nonfinite_values": "non-finite values score below pass threshold",
        "known_valid_public": "independently justified output passes",
        "sparse_known_valid": "a sparse subset cannot pass the full task",
    }
    tests = []
    for index, result in enumerate(results, start=1):
        tests.append(
            {
                "test_id": f"CHECKER-{index:03d}",
                "test_type": result["case"],
                "description": result["case"].replace("_", " "),
                "expected_behavior": expected[result["case"]],
                "observed_score": result.get("reward"),
                "observed_status": (
                    "CRASH" if result["crashed"] else "COMPLETED"
                ),
                "exit_code": result.get("returncode"),
                "hard_gate_triggered": any(
                    item["severity"] == "FATAL"
                    and item["test_type"] == result["case"]
                    for item in findings
                ),
                "evidence": result,
            }
        )
    checker_result = {
        "schema_version": "0.1",
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
        "solution_content_inspected": False,
        "pass_threshold": pass_threshold,
        "tests": tests,
        "findings": findings,
        "usable_reward_count": sum(
            isinstance(result.get("reward"), float)
            and math.isfinite(result["reward"])
            for result in results
        ),
        "limitations": [
            "schema-shaped synthetic outputs do not establish scientific correctness",
            "task-family-specific gradients and metamorphic probes are later slices",
            "external-service or compiled checker dependencies may require container execution",
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(checker_result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return checker_result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="checker_tests.json")
    parser.add_argument("--known-valid-output")
    arguments = parser.parse_args()
    try:
        result = dynamic_checker_probe(
            locate_root(Path(arguments.input)),
            Path(arguments.output).expanduser().resolve(),
            (
                Path(arguments.known_valid_output)
                if arguments.known_valid_output
                else None
            ),
        )
        print(
            json.dumps(
                {
                    "tests": len(result["tests"]),
                    "findings": len(result["findings"]),
                    "output": arguments.output,
                },
                indent=2,
            )
        )
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"checker probe failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
