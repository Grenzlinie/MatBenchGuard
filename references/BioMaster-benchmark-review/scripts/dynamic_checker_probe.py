#!/usr/bin/env python3
"""Run generic synthetic probes against a benchmark checker.

The script patches common absolute sandbox paths into an isolated temporary
workspace. It does not inspect or execute solution files.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any


def safe_extract(zpath: Path, dest: Path) -> None:
    with zipfile.ZipFile(zpath) as zf:
        for member in zf.infolist():
            target = (dest / member.filename).resolve()
            if not str(target).startswith(str(dest.resolve()) + os.sep):
                raise ValueError(f"unsafe zip path: {member.filename}")
        zf.extractall(dest)


def locate_root(path: Path) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    temp = None
    if path.is_file() and path.suffix.lower() == ".zip":
        temp = tempfile.TemporaryDirectory(prefix="checker_probe_input_")
        safe_extract(path, Path(temp.name))
        path = Path(temp.name)
    candidates = []
    for checker in path.rglob("tests/checker.py"):
        if "solution" in checker.parts or "__MACOSX" in checker.parts:
            continue
        root = checker.parent.parent
        score = sum((root / rel).exists() for rel in ["instruction.md", "steps.json", "tests/grading_spec.json"])
        candidates.append((-score, len(root.parts), root))
    if not candidates:
        raise ValueError("could not locate tests/checker.py")
    candidates.sort()
    return candidates[0][2], temp


def basename(value: Any) -> str:
    return str(value or "").replace("\\", "/").split("/")[-1]


def grading_steps(spec: dict[str, Any]) -> list[dict[str, Any]]:
    return spec.get("steps", spec.get("checks", [])) or []


def match_step(spec: dict[str, Any], filename: str) -> dict[str, Any] | None:
    for step in grading_steps(spec):
        if basename(step.get("output_file")) == filename:
            return step
    return None


def json_fixture(output: dict[str, Any], step: dict[str, Any] | None, mode: str) -> dict[str, Any]:
    schema = output.get("schema", {}) or {}
    required = schema.get("required", {}) or {}
    fields = list(required.keys()) if isinstance(required, dict) else list(required)
    data: dict[str, Any] = {}
    for field in fields:
        if mode == "gold" and step and step.get("field") == field and "target_value" in step:
            data[field] = step["target_value"]
        elif mode == "nonfinite":
            data[field] = float("nan")
        elif mode == "random":
            data[field] = random.uniform(-1000, 1000)
        else:
            data[field] = 0
    return data


def csv_fixture(output: dict[str, Any], step: dict[str, Any] | None, mode: str) -> tuple[list[str], list[dict[str, Any]]]:
    schema = output.get("schema", {}) or {}
    raw_cols = schema.get("required_columns", []) or []
    columns = [c.get("name") if isinstance(c, dict) else str(c) for c in raw_cols]
    rows: list[dict[str, Any]] = []
    expected = (step or {}).get("expected_entries", []) or []
    if mode in {"gold", "duplicate", "nonfinite"} and expected:
        for exp in expected:
            row: dict[str, Any] = {}
            for col in columns:
                if col in exp:
                    value = exp[col]
                elif f"{col}_gold" in exp:
                    value = exp[f"{col}_gold"]
                elif col in {"score", "value", "metric", "fph"} and "target_value" in (step or {}):
                    value = (step or {})["target_value"]
                else:
                    value = ""
                if mode == "nonfinite" and col in {"score", "value", "metric", "fph"}:
                    value = "nan"
                row[col] = value
            rows.append(row)
        if mode == "duplicate":
            rows = rows + rows
    elif mode == "random":
        row = {c: "random" for c in columns}
        for c in columns:
            if c in {"score", "value", "metric", "fph"}:
                row[c] = random.uniform(-1000, 1000)
        rows.append(row)
    return columns, rows


def write_case_outputs(out_dir: Path, spec: dict[str, Any], mode: str) -> list[str]:
    created = []
    contract = spec.get("output_contract", {}) or {}
    for output in contract.get("outputs", []) or []:
        filename = basename(output.get("file"))
        if not filename:
            continue
        path = out_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        fmt = str(output.get("format", "")).lower()
        step = match_step(spec, filename)
        if fmt == "json":
            data = json_fixture(output, step, mode)
            path.write_text(json.dumps(data, allow_nan=True), encoding="utf-8")
        elif fmt in {"csv", "tsv"}:
            cols, rows = csv_fixture(output, step, mode)
            delim = "\t" if fmt == "tsv" else ","
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=cols, delimiter=delim)
                writer.writeheader()
                writer.writerows(rows)
        else:
            path.write_text("" if mode == "empty" else "synthetic\n", encoding="utf-8")
        created.append(filename)
    return created


def run_case(root: Path, checker_text: str, spec: dict[str, Any], case_name: str, mode: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"checker_probe_{case_name}_") as tmp:
        base = Path(tmp)
        tests_dir = base / "tests"
        outputs_dir = base / "app" / "outputs"
        logs_dir = base / "logs" / "verifier"
        tests_dir.mkdir(parents=True)
        outputs_dir.mkdir(parents=True)
        logs_dir.mkdir(parents=True)
        spec_path = tests_dir / "grading_spec.json"
        spec_path.write_text(json.dumps(spec, indent=2), encoding="utf-8")

        created: list[str] = []
        if mode != "missing":
            created = write_case_outputs(outputs_dir, spec, mode)

        patched = checker_text
        patched = patched.replace("/tests/grading_spec.json", str(spec_path))
        patched = patched.replace("/app/outputs", str(outputs_dir))
        patched = patched.replace("/logs/verifier", str(logs_dir))
        checker_path = base / "checker_patched.py"
        checker_path.write_text(patched, encoding="utf-8")

        proc = subprocess.run(
            [sys.executable, str(checker_path)],
            cwd=str(root),
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        reward_path = logs_dir / "reward.txt"
        breakdown_path = logs_dir / "breakdown.json"
        reward = None
        if reward_path.exists():
            try:
                reward = float(reward_path.read_text(encoding="utf-8").strip())
            except ValueError:
                reward = reward_path.read_text(encoding="utf-8", errors="replace")
        breakdown = None
        if breakdown_path.exists():
            try:
                breakdown = json.loads(breakdown_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                breakdown = breakdown_path.read_text(encoding="utf-8", errors="replace")
        return {
            "case": case_name,
            "mode": mode,
            "created_outputs": created,
            "returncode": proc.returncode,
            "reward": reward,
            "breakdown": breakdown,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
            "crashed": proc.returncode != 0,
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="benchmark directory or zip")
    parser.add_argument("--output", default="checker_probe.json")
    args = parser.parse_args()

    input_temp = None
    try:
        root, input_temp = locate_root(Path(args.input).expanduser().resolve())
        checker_path = root / "tests/checker.py"
        spec_path = root / "tests/grading_spec.json"
        checker_text = checker_path.read_text(encoding="utf-8", errors="replace")
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        random.seed(17)

        cases = [
            ("missing_outputs", "missing"),
            ("empty_valid_shape", "empty"),
            ("random_baseline", "random"),
            ("minimal_gold_shape", "gold"),
            ("duplicate_gold_rows", "duplicate"),
            ("nonfinite_values", "nonfinite"),
        ]
        results = [run_case(root, checker_text, spec, name, mode) for name, mode in cases]
        pass_threshold = float(spec.get("pass_threshold", 1.0))
        minimal = next(r for r in results if r["case"] == "minimal_gold_shape")
        declared_evidence = []
        steps_path = root / "steps.json"
        if steps_path.exists():
            steps = json.loads(steps_path.read_text(encoding="utf-8"))
            declared_evidence = sorted({basename(s.get("evidence")) for s in steps if basename(s.get("evidence"))})

        findings = []
        if minimal.get("reward") is not None and isinstance(minimal["reward"], float):
            if minimal["reward"] >= pass_threshold and declared_evidence:
                findings.append(
                    {
                        "severity": "FATAL",
                        "code": "MINIMAL_OUTPUT_BYPASSES_EVIDENCE",
                        "message": "a minimal target-shaped submission passes without declared supporting evidence",
                        "reward": minimal["reward"],
                        "pass_threshold": pass_threshold,
                        "omitted_evidence": declared_evidence,
                    }
                )
        for result in results:
            if result["crashed"]:
                findings.append(
                    {
                        "severity": "HIGH",
                        "code": "CHECKER_CRASH",
                        "message": f"checker crashed for case {result['case']}",
                        "stderr": result["stderr"],
                    }
                )
        nonfinite = next(r for r in results if r["case"] == "nonfinite_values")
        if isinstance(nonfinite.get("reward"), float) and nonfinite["reward"] >= pass_threshold:
            findings.append(
                {
                    "severity": "FATAL",
                    "code": "NONFINITE_VALUES_PASS",
                    "message": "NaN or non-finite values can receive a passing reward",
                    "reward": nonfinite["reward"],
                }
            )
        empty = next(r for r in results if r["case"] == "empty_valid_shape")
        if isinstance(empty.get("reward"), float) and empty["reward"] >= pass_threshold:
            findings.append(
                {
                    "severity": "FATAL",
                    "code": "EMPTY_SHAPE_PASSES",
                    "message": "empty but schema-shaped outputs receive a passing reward",
                    "reward": empty["reward"],
                }
            )

        expected_by_case = {
            "missing_outputs": "Score near zero without crashing",
            "empty_valid_shape": "Score near zero without crashing",
            "random_baseline": "Score below the pass threshold",
            "minimal_gold_shape": "Must not pass when load-bearing evidence is omitted",
            "duplicate_gold_rows": "Duplicates must not inflate score",
            "nonfinite_values": "Non-finite values must be rejected or score near zero",
        }
        tests = []
        for index, result in enumerate(results, start=1):
            tests.append({
                "test_id": f"CHECKER-{index:03d}",
                "test_type": result["case"],
                "description": result["case"].replace("_", " "),
                "expected_behavior": expected_by_case[result["case"]],
                "observed_score": result.get("reward"),
                "observed_status": "CRASH" if result.get("crashed") else "COMPLETED",
                "exit_code": result.get("returncode"),
                "hard_gate_triggered": any(f.get("severity") == "FATAL" and f.get("code") in {"MINIMAL_OUTPUT_BYPASSES_EVIDENCE", "NONFINITE_VALUES_PASS", "EMPTY_SHAPE_PASSES"} for f in findings),
                "evidence": result,
            })
        output = {
            "schema_version": "1.0",
            "benchmark_root": str(root),
            "checker_path": str(checker_path.relative_to(root)),
            "solution_content_inspected": False,
            "pass_threshold": pass_threshold,
            "declared_supporting_evidence": declared_evidence,
            "tests": tests,
            "monotonicity": {"tested": False, "passed": None, "scores": {}},
            "findings": findings,
            "limitations": [
                "gold-shaped fixtures are generated from grading_spec and do not prove scientific correctness",
                "the script does not create task-specific attacks such as whole-genome coverage or identifier collisions",
                "quality-gradient and metamorphic tests require task-specific fixtures",
                "checker behavior that depends on external services or compiled tools may require container execution",
            ],
        }
        Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"cases": len(results), "findings": len(findings), "output": args.output}, indent=2))
        return 0
    except subprocess.TimeoutExpired as exc:
        print(f"checker probe timed out: {exc}", file=sys.stderr)
        return 3
    except Exception as exc:  # noqa: BLE001
        print(f"checker probe failed: {exc}", file=sys.stderr)
        return 2
    finally:
        if input_temp is not None:
            input_temp.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
