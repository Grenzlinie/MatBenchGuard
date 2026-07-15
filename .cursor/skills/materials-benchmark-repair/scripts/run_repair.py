#!/usr/bin/env python3
"""Apply one deterministic repair on a full isolated Harbor package copy."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True


SAFE_JSON_FILES = {"resources.json"}
ASSISTED_JSON_FILES = {
    "manifest.json",
    "resources.json",
    "steps.json",
    "tests/grading_spec.json",
}
SENSITIVE_FILES = {
    "instruction.md",
    "steps.json",
    "tests/checker.py",
    "tests/grading_spec.json",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def validate_external_plan(root: Path, plan_path: Path) -> dict[str, Any]:
    resolved = plan_path.expanduser().resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("repair plan must be outside the Harbor 题包")
    plan = read_json(resolved)
    if not isinstance(plan, dict) or plan.get("schema_version") != "0.1":
        raise ValueError("repair plan must use schema_version 0.1")
    if plan.get("repair_class") not in {"SAFE_AUTO_FIX", "ASSISTED_FIX"}:
        raise ValueError("repair_class must be SAFE_AUTO_FIX or ASSISTED_FIX")
    if not isinstance(plan.get("justification"), str) or not plan[
        "justification"
    ].strip():
        raise ValueError("repair plan requires a justification")
    operations = plan.get("operations")
    tests = plan.get("regression_tests")
    if not isinstance(operations, list) or len(operations) != 1:
        raise ValueError("repair plan requires exactly one operation")
    if not isinstance(tests, list) or not tests:
        raise ValueError("repair plan requires regression tests")
    return plan


def validate_fresh_audit(
    root: Path, plan: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    audit = root / "benchmark_audit"
    report = read_json(audit / "audit_report.json")
    manifest = read_json(audit / "audit_manifest.json")
    disposition = read_json(audit / "disposition.json")
    if plan.get("audit_id") != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
    if disposition.get("route") != "REPAIR_QUEUE":
        raise ValueError("authoritative audit is not routed to REPAIR_QUEUE")
    findings = {
        item["finding_id"]: item for item in report.get("findings", [])
    }
    finding_id = plan.get("finding_id")
    if finding_id not in findings:
        raise ValueError("repair plan finding_id is not open in the audit")
    for relative, expected in manifest.get("input_hashes", {}).items():
        relative_path = Path(relative)
        if (
            relative_path.is_absolute()
            or ".." in relative_path.parts
            or relative_path.parts[0] == "solution"
        ):
            raise ValueError("audit manifest contains an unsafe input path")
        source = root / relative_path
        if not source.is_file() or sha256_file(source) != expected:
            raise ValueError(f"stale audit: input changed since review: {relative}")
    return report, manifest, findings[finding_id]


def validated_relative_file(
    root: Path,
    relative: Any,
    plan: dict[str, Any],
) -> Path:
    if not isinstance(relative, str):
        raise ValueError("operation file must be a relative string")
    relative_path = Path(relative)
    allowed = (
        SAFE_JSON_FILES
        if plan["repair_class"] == "SAFE_AUTO_FIX"
        else ASSISTED_JSON_FILES
    )
    if (
        relative_path.as_posix() not in allowed
        or relative_path.is_absolute()
        or ".." in relative_path.parts
    ):
        raise ValueError(
            "repair json_set targets an unsupported file"
        )
    path = root / relative_path
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def json_path_value(value: Any, tokens: Any) -> tuple[bool, Any]:
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("JSON path must be a non-empty token list")
    current = value
    for token in tokens:
        if isinstance(token, int) and isinstance(current, list):
            if token < 0 or token >= len(current):
                return False, None
            current = current[token]
        elif isinstance(token, str) and isinstance(current, dict):
            if token not in current:
                return False, None
            current = current[token]
        else:
            return False, None
    return True, current


def set_json_path(value: Any, tokens: list[Any], replacement: Any) -> None:
    current = value
    for token in tokens[:-1]:
        if isinstance(token, int) and isinstance(current, list):
            if token < 0 or token >= len(current):
                raise ValueError("JSON operation path index is out of range")
            current = current[token]
        elif isinstance(token, str) and isinstance(current, dict):
            if token not in current:
                raise ValueError("JSON operation parent path is missing")
            current = current[token]
        else:
            raise ValueError("JSON operation path does not match the document")
    final = tokens[-1]
    if isinstance(final, int) and isinstance(current, list):
        if final < 0 or final >= len(current):
            raise ValueError("JSON operation final index is out of range")
        current[final] = replacement
    elif isinstance(final, str) and isinstance(current, dict):
        current[final] = replacement
    else:
        raise ValueError("JSON operation final token is invalid")


def apply_operation(
    candidate: Path,
    operation: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    if operation.get("type") != "json_set":
        raise ValueError("repair operations currently support only json_set")
    path = validated_relative_file(candidate, operation.get("file"), plan)
    before_hash = sha256_file(path)
    document = read_json(path)
    tokens = operation.get("path")
    if plan["repair_class"] == "SAFE_AUTO_FIX" and not (
        isinstance(tokens, list)
        and len(tokens) == 4
        and tokens[0] == "resources"
        and isinstance(tokens[1], int)
        and tokens[2:] == ["access", "evidence"]
    ):
        raise ValueError(
            "SAFE_AUTO_FIX may only add exact public evidence to a resource"
        )
    set_json_path(document, tokens, operation.get("value"))
    write_json(path, document)
    return {
        "operation": "json_set",
        "file": path.relative_to(candidate).as_posix(),
        "json_path": tokens,
        "before_hash": before_hash,
        "after_hash": sha256_file(path),
    }


def regression_result(
    root: Path,
    specification: dict[str, Any],
    plan: dict[str, Any],
) -> bool:
    if specification.get("type") != "json_path_equals":
        raise ValueError("unsupported regression test type")
    path = validated_relative_file(root, specification.get("file"), plan)
    present, value = json_path_value(
        read_json(path),
        specification.get("path"),
    )
    return present and value == specification.get("expected")


def run_equal_depth_review(
    candidate: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    runner = (
        Path(__file__).resolve().parents[2]
        / "materials-benchmark-review"
        / "scripts"
        / "run_review.py"
    )
    configuration = report["configuration"]
    command = [
        sys.executable,
        str(runner),
        str(candidate),
        "--paper-mode",
        configuration["paper_mode"],
        "--execution-level",
        configuration["execution_level"],
    ]
    optional_arguments = {
        "known_valid_output": "--known-valid-output",
        "agent_assessment": "--agent-assessment",
        "e2_smoke_plan": "--e2-smoke-plan",
    }
    for key, flag in optional_arguments.items():
        raw = plan.get(key)
        if raw is not None:
            external = Path(str(raw)).expanduser().resolve()
            if external.is_relative_to(candidate.resolve()):
                raise ValueError(f"{key} must remain external to the candidate")
            command.extend([flag, str(external)])
    process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError(
            "equal-depth re-audit failed: " + process.stderr[-2000:]
        )
    reaudit = read_json(candidate / "benchmark_audit/audit_report.json")
    if (
        reaudit["configuration"]["paper_mode"] != configuration["paper_mode"]
        or reaudit["configuration"]["execution_level"]
        != configuration["execution_level"]
    ):
        raise ValueError("re-audit evidence depth differs from the original")
    return reaudit


def replace_paths(value: Any, old: str, new: str) -> Any:
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [replace_paths(item, old, new) for item in value]
    if isinstance(value, dict):
        return {
            key: replace_paths(item, old, new)
            for key, item in value.items()
        }
    return value


def rebase_audit_paths(candidate: Path, final_root: Path) -> None:
    audit = candidate / "benchmark_audit"
    old = str(candidate)
    new = str(final_root)
    for path in audit.rglob("*"):
        if not path.is_file() or path.name == "audit_manifest.json":
            continue
        if path.suffix in {".json", ".jsonl"}:
            if path.suffix == ".jsonl":
                lines = [
                    json.dumps(
                        replace_paths(json.loads(line), old, new),
                        ensure_ascii=False,
                    )
                    for line in path.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                path.write_text(
                    "".join(line + "\n" for line in lines),
                    encoding="utf-8",
                )
            else:
                write_json(path, replace_paths(read_json(path), old, new))
        elif path.suffix in {".md", ".log"}:
            path.write_text(
                path.read_text(encoding="utf-8").replace(old, new),
                encoding="utf-8",
            )
    manifest_path = audit / "audit_manifest.json"
    manifest = replace_paths(read_json(manifest_path), old, new)
    manifest["benchmark_root"] = new
    manifest["output_hashes"] = dict(
        sorted(
            (
                path.relative_to(audit).as_posix(),
                sha256_file(path),
            )
            for path in audit.rglob("*")
            if path.is_file()
            and path.name not in {"audit_manifest.json", "audit_context.json"}
        )
    )
    write_json(manifest_path, manifest)


def root_cause_id(report: dict[str, Any], plan: dict[str, Any]) -> str:
    value = f"{report['audit_id']}:{plan['finding_id']}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def history_root_for(root: Path) -> Path:
    return root.parent / ".benchmark_repair_history"


def prior_attempts(root: Path, root_cause: str) -> list[dict[str, Any]]:
    history_root = history_root_for(root)
    if not history_root.is_dir():
        return []
    attempts = []
    for path in history_root.glob("*/attempt_manifest.json"):
        try:
            value = read_json(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if (
            isinstance(value, dict)
            and value.get("root_cause") == root_cause
            and value.get("status") in {"ROLLED_BACK", "ABANDONED", "PUBLISHED"}
        ):
            attempts.append(value)
    return sorted(attempts, key=lambda item: item["attempt_number"])


def preflight_stop(plan: dict[str, Any]) -> tuple[str, str] | None:
    if plan["repair_class"] != "ASSISTED_FIX":
        return None
    approval = plan.get("approval")
    if not isinstance(approval, dict) or approval.get("approved") is not True:
        return (
            "AWAITING_APPROVAL",
            "ASSISTED_FIX requires explicit approval before copying or mutation.",
        )
    if not all(
        isinstance(approval.get(key), str) and approval[key].strip()
        for key in ("approved_by", "approved_at")
    ):
        return (
            "AWAITING_APPROVAL",
            "Approved ASSISTED_FIX requires approver identity and timestamp.",
        )
    sensitive = any(
        operation.get("file") in SENSITIVE_FILES
        for operation in plan["operations"]
    )
    evidence = approval.get("evidence")
    if sensitive and (not isinstance(evidence, list) or not evidence):
        return (
            "BLOCKED_EVIDENCE",
            "Gold, scientific endpoint, key parameter, and scoring changes "
            "require explicit approval evidence.",
        )
    return None


def record_control_stop(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    root_cause: str,
    status: str,
    reason: str,
) -> dict[str, Any]:
    stop_id = (
        time.strftime("repair-stop-%Y%m%dT%H%M%SZ-", time.gmtime())
        + uuid.uuid4().hex[:8]
    )
    history_root = history_root_for(root)
    destination = history_root / stop_id
    destination.mkdir(parents=True)
    manifest = {
        "schema_version": "0.1",
        "repair_id": stop_id,
        "root_cause": root_cause,
        "attempt_number": 0,
        "status": status,
        "audit_id": report["audit_id"],
        "finding_id": plan["finding_id"],
        "repair_class": plan["repair_class"],
        "reason": reason,
        "package_mutated": False,
        "recorded_at": time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        ),
    }
    write_json(destination / "attempt_manifest.json", manifest)
    return {
        "status": status,
        "root_cause": root_cause,
        "history_root": str(history_root),
        "attempt_manifest": str(destination / "attempt_manifest.json"),
        "reason": reason,
    }


def repair(root: Path, plan_path: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir() or not (root / "solution").is_dir():
        raise ValueError("input must be a complete Harbor 题包")
    plan = validate_external_plan(root, plan_path)
    report, audit_manifest, finding = validate_fresh_audit(root, plan)
    root_cause = root_cause_id(report, plan)
    prior = prior_attempts(root, root_cause)
    if len(prior) >= 2 or any(
        item["status"] == "ABANDONED" for item in prior
    ):
        return {
            "status": "ABANDONED",
            "root_cause": root_cause,
            "history_root": str(history_root_for(root)),
            "attempts": len(prior),
            "reason": "Two failed attempts exhausted the root-cause limit.",
        }
    stop = preflight_stop(plan)
    if stop is not None:
        status, reason = stop
        return record_control_stop(
            root,
            report,
            plan,
            root_cause,
            status,
            reason,
        )
    attempt_number = len(prior) + 1
    repair_id = (
        time.strftime("repair-%Y%m%dT%H%M%SZ-", time.gmtime())
        + uuid.uuid4().hex[:8]
    )
    workspace = root.parent / ".benchmark_repair_tmp" / repair_id
    history = root.parent / ".benchmark_repair_history" / repair_id
    if workspace.exists() or history.exists():
        raise FileExistsError("repair workspace already exists")
    workspace.parent.mkdir(exist_ok=True)
    workspace.mkdir()
    snapshot = workspace / "snapshot"
    candidate = workspace / "candidate"
    try:
        shutil.copytree(root, snapshot)
        shutil.copytree(snapshot, candidate)
        regression_tests = []
        for specification in plan["regression_tests"]:
            regression_tests.append(
                {
                    "specification": specification,
                    "before_passed": regression_result(
                        snapshot,
                        specification,
                        plan,
                    ),
                }
            )
        if any(item["before_passed"] for item in regression_tests):
            raise ValueError("regression test must fail before the repair")
        changes = [
            apply_operation(candidate, operation, plan)
            for operation in plan["operations"]
        ]
        for item in regression_tests:
            item["after_passed"] = regression_result(
                candidate,
                item["specification"],
                plan,
            )
        if not all(item["after_passed"] for item in regression_tests):
            raise ValueError("regression test did not pass after the repair")
        reaudit = run_equal_depth_review(candidate, report, plan)
        if reaudit["summary"]["final_verdict"] != "PASS":
            raise ValueError("equal-depth re-audit did not produce PASS")
        if any(
            item["title"] == finding["title"]
            for item in reaudit.get("findings", [])
        ):
            raise ValueError("target finding remains open after re-audit")

        repair_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "status": "PUBLISHED",
            "finding_id": plan["finding_id"],
            "finding_code": finding["title"],
            "repair_class": plan["repair_class"],
            "source_audit_id": report["audit_id"],
            "source_audit_input_hashes": audit_manifest["input_hashes"],
            "justification": plan["justification"],
            "changes": changes,
            "regression_tests": regression_tests,
            "reaudit": {
                "audit_id": reaudit["audit_id"],
                "paper_mode": reaudit["configuration"]["paper_mode"],
                "execution_level": reaudit["configuration"]["execution_level"],
                "verdict": reaudit["summary"]["final_verdict"],
            },
            "atomic_publish": True,
            "published_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
            ),
        }
        write_json(
            candidate / "benchmark_repair/repair_manifest.json",
            repair_manifest,
        )
        rebase_audit_paths(candidate, root)

        history.mkdir(parents=True)
        snapshot.rename(history / "snapshot")
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "status": "PUBLISHED",
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
            ),
        }
        write_json(history / "attempt_manifest.json", attempt_manifest)
        original = history / "original"
        root.rename(original)
        try:
            candidate.rename(root)
        except Exception:
            original.rename(root)
            raise
        shutil.rmtree(workspace, ignore_errors=True)
        return {
            "repair_id": repair_id,
            "status": "PUBLISHED",
            "benchmark_root": str(root),
            "history_dir": str(history),
            "history_root": str(history_root_for(root)),
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "audit_id": reaudit["audit_id"],
        }
    except Exception as exc:  # noqa: BLE001
        status = "ROLLED_BACK" if attempt_number == 1 else "ABANDONED"
        history.mkdir(parents=True, exist_ok=True)
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "status": status,
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": str(exc),
            "snapshot_preserved": (history / "snapshot").is_dir(),
            "candidate_preserved": (history / "candidate").is_dir(),
            "package_mutated": False,
            "recorded_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
            ),
        }
        write_json(history / "attempt_manifest.json", attempt_manifest)
        if workspace.exists():
            shutil.rmtree(workspace, ignore_errors=True)
        return {
            "repair_id": repair_id,
            "status": status,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "history_dir": str(history),
            "history_root": str(history_root_for(root)),
            "attempt_manifest": str(history / "attempt_manifest.json"),
            "reason": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root")
    parser.add_argument("--plan", required=True)
    arguments = parser.parse_args()
    try:
        result = repair(
            Path(arguments.benchmark_root),
            Path(arguments.plan),
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "PUBLISHED" else 3
    except Exception as exc:  # noqa: BLE001
        print(f"materials repair failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
