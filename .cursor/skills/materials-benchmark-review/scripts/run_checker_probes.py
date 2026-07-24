#!/usr/bin/env python3
"""Run checker cases in disposable path-rewritten workspaces.

This runner records observations only. It never labels a benchmark finding or
decides whether an observed reward is scientifically appropriate.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

SCHEMA = "materials-checker-probe-observations/1.0"
BUILTINS = ("missing_output", "empty_output", "malformed_output", "random_or_constant", "duplicate_records", "non_finite_values", "minimal_exploit")
AGENT_CASES = ("valid_positive", "quality_gradient", "semantic_equivalence", "component_isolation")


def load_contract(package: Path) -> list[dict[str, Any]]:
    path = package / "tests/grading_spec.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    contract = value.get("output_contract") if isinstance(value, dict) else None
    outputs = contract.get("outputs") if isinstance(contract, dict) else None
    return [item for item in outputs if isinstance(item, dict)] if isinstance(outputs, list) else []


def output_name(item: dict[str, Any]) -> str:
    return Path(str(item.get("file") or "")).name


def required_fields(item: dict[str, Any]) -> list[str]:
    schema = item.get("schema") if isinstance(item.get("schema"), dict) else {}
    fields = schema.get("required", [])
    if isinstance(fields, dict): return [str(x) for x in fields]
    if isinstance(fields, list): return [str(x.get("name") if isinstance(x, dict) else x) for x in fields]
    return []


def required_columns(item: dict[str, Any]) -> list[str]:
    schema = item.get("schema") if isinstance(item.get("schema"), dict) else {}
    fields = schema.get("required_columns", [])
    if isinstance(fields, list): return [str(x.get("name") if isinstance(x, dict) else x) for x in fields]
    return []


def write_case(outputs_dir: Path, outputs: list[dict[str, Any]], case: str) -> list[str]:
    created = []
    if case == "missing_output": return created
    outputs_dir.mkdir(parents=True, exist_ok=True)
    for item in outputs:
        name = output_name(item)
        if not name: continue
        path = outputs_dir / name
        fmt = str(item.get("format") or path.suffix.lstrip(".")).lower()
        if case == "empty_output":
            path.write_bytes(b"")
        elif case == "malformed_output":
            path.write_text("{malformed\n" if fmt in {"json", "jsonl"} else "\x00malformed\n", encoding="utf-8")
        elif fmt == "json":
            fields = required_fields(item)
            value = {field: (float("nan") if case == "non_finite_values" else 0.123) for field in fields}
            if case == "minimal_exploit": value = {fields[0]: 0.123} if fields else {}
            path.write_text(json.dumps(value, allow_nan=True) + "\n", encoding="utf-8")
        elif fmt == "jsonl":
            fields = required_fields(item)
            row = {field: (float("nan") if case == "non_finite_values" else 0.123) for field in fields}
            lines = [row, row] if case == "duplicate_records" else [row]
            path.write_text("".join(json.dumps(x, allow_nan=True) + "\n" for x in lines), encoding="utf-8")
        elif fmt in {"csv", "tsv"}:
            columns = required_columns(item) or ["value"]
            delim = "\t" if fmt == "tsv" else ","
            value = "nan" if case == "non_finite_values" else "0.123"
            rows = [[value for _ in columns]]
            if case == "duplicate_records": rows.append(list(rows[0]))
            if case == "minimal_exploit": rows = [[value] + ["" for _ in columns[1:]]]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle, delimiter=delim); writer.writerow(columns); writer.writerows(rows)
        else:
            path.write_text("nan\n" if case == "non_finite_values" else "0.123\n", encoding="utf-8")
        created.append(name)
    return created


def rewrite_paths(tests: Path, outputs: Path, logs: Path) -> list[str]:
    rewritten = []
    replacements = {
        "/tests": str(tests), "/app/outputs": str(outputs),
        "/logs/verifier": str(logs / "verifier"),
    }
    for path in tests.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".py", ".sh", ".json", ".toml", ".yaml", ".yml"}: continue
        try: text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        updated = text
        for old, new in replacements.items(): updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8"); rewritten.append(path.relative_to(tests).as_posix())
    return rewritten


def read_result(logs: Path) -> tuple[Any, Any, list[str]]:
    limitations = []
    reward: Any = None; breakdown: Any = None
    reward_path = logs / "verifier/reward.txt"
    breakdown_path = logs / "verifier/breakdown.json"
    if reward_path.is_file():
        try:
            reward = float(reward_path.read_text(encoding="utf-8").strip())
            if not math.isfinite(reward): limitations.append("reward is non-finite")
        except Exception as exc: limitations.append(f"reward unreadable: {exc}")
    else: limitations.append("reward.txt was not produced")
    if breakdown_path.is_file():
        try: breakdown = json.loads(breakdown_path.read_text(encoding="utf-8"))
        except Exception as exc: limitations.append(f"breakdown unreadable: {exc}")
    return reward, breakdown, limitations


def run_one(package: Path, case_id: str, source_dir: Path | None, timeout: float) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="materials-probe-") as temporary:
        workspace = Path(temporary); tests = workspace / "tests"; outputs = workspace / "outputs"; logs = workspace / "logs"
        shutil.copytree(package / "tests", tests)
        if source_dir is not None:
            if not source_dir.is_dir():
                return {"case_id": case_id, "status": "NOT_ASSESSED", "limitations": [f"case directory missing: {source_dir}"]}
            shutil.copytree(source_dir, outputs)
            created = sorted(p.relative_to(outputs).as_posix() for p in outputs.rglob("*") if p.is_file())
        else:
            created = write_case(outputs, load_contract(package), case_id)
        rewritten = rewrite_paths(tests, outputs, logs)
        entrypoint = tests / "test.sh"
        if not entrypoint.is_file():
            return {"case_id": case_id, "status": "NOT_ASSESSED", "created_outputs": created, "limitations": ["tests/test.sh is missing"]}
        env = os.environ.copy(); env.update({"MATERIALS_PROBE_WORKSPACE": str(workspace), "PYTHONDONTWRITEBYTECODE": "1"})
        try:
            completed = subprocess.run(["bash", str(entrypoint)], cwd=workspace, env=env, capture_output=True, text=True, timeout=timeout, check=False)
            reward, breakdown, limitations = read_result(logs)
            status = "OBSERVED" if completed.returncode == 0 and reward is not None and not limitations else "UNUSABLE"
            return {
                "case_id": case_id, "status": status, "created_outputs": created,
                "returncode": completed.returncode, "reward": reward, "breakdown": breakdown,
                "stdout": completed.stdout[-8000:], "stderr": completed.stderr[-8000:],
                "rewritten_test_files": rewritten, "duration_seconds": round(time.monotonic() - started, 3),
                "limitations": limitations,
            }
        except subprocess.TimeoutExpired as exc:
            return {"case_id": case_id, "status": "UNUSABLE", "created_outputs": created, "duration_seconds": round(time.monotonic() - started, 3), "limitations": [f"timeout after {timeout}s"], "stdout": (exc.stdout or "")[-8000:] if isinstance(exc.stdout, str) else "", "stderr": (exc.stderr or "")[-8000:] if isinstance(exc.stderr, str) else ""}


def parse_cases(values: list[str]) -> dict[str, Path]:
    result = {}
    for value in values:
        if "=" not in value: raise ValueError("--case must be NAME=OUTPUT_DIR")
        name, path = value.split("=", 1)
        if name not in AGENT_CASES: raise ValueError(f"unsupported supplied case: {name}")
        result[name] = Path(path).expanduser().resolve()
    return result


def run(package: Path, supplied: dict[str, Path], timeout: float, *, execute: bool = True) -> dict[str, Any]:
    package = package.expanduser().resolve()
    if not (package / "tests").is_dir(): raise ValueError("package tests directory is missing")
    if not execute:
        return {
            "schema_version": SCHEMA, "package_root": str(package),
            "authority": "MECHANICAL_OBSERVATIONS_ONLY", "may_decide_findings_or_verdict": False,
            "observations": [{"case_id": name, "status": "NOT_ASSESSED", "limitations": ["Checker execution was explicitly disabled with --no-execute."]} for name in (*BUILTINS, *AGENT_CASES)],
            "global_limitations": ["Checker code was not executed because --no-execute was requested."],
        }
    observations = [run_one(package, name, None, timeout) for name in BUILTINS]
    for name in AGENT_CASES:
        observations.append(run_one(package, name, supplied[name], timeout) if name in supplied else {"case_id": name, "status": "NOT_ASSESSED", "limitations": ["Agent-supplied case directory was not provided."]})
    return {
        "schema_version": SCHEMA, "package_root": str(package),
        "authority": "MECHANICAL_OBSERVATIONS_ONLY", "may_decide_findings_or_verdict": False,
        "observations": observations,
        "global_limitations": ["Path rewriting runs an isolated local approximation of the Harbor checker. Agent must assess environment equivalence and scientific meaning."],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path); parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case", action="append", default=[], metavar="NAME=OUTPUT_DIR")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--no-execute", action="store_true", help="collect an explicit NOT_ASSESSED record without running checker code")
    args = parser.parse_args(); result = run(args.package, parse_cases(args.case), args.timeout, execute=not args.no_execute)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "observations": len(result["observations"]), "authority": result["authority"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
