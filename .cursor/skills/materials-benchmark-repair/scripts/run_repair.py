#!/usr/bin/env python3
"""Repair one audited Harbor package through an isolated atomic workflow."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Iterable

sys.dont_write_bytecode = True

REPAIR_CLASSES = {"SAFE_AUTO_FIX", "ASSISTED_FIX"}
OPERATION_TYPES = {"write_file", "replace_text", "text_replace", "json_set", "delete_file"}
REGRESSION_TYPES = {
    "file_exists",
    "file_absent",
    "file_executable",
    "text_contains",
    "text_not_contains",
    "json_path_equals",
    "command",
}
GENERATED_TOP_LEVEL = {
    "benchmark_audit",
    "benchmark_audit_history",
    "benchmark_repair",
    ".benchmark_audit_tmp",
    ".benchmark_repair_tmp",
}


class PolicyStop(Exception):
    """A non-mutating policy stop reported through the CLI result."""

    def __init__(self, status: str, reason: str) -> None:
        super().__init__(reason)
        self.status = status
        self.reason = reason


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def unique_id(prefix: str) -> str:
    return (
        time.strftime(f"{prefix}-%Y%m%dT%H%M%SZ-", time.gmtime())
        + uuid.uuid4().hex[:8]
    )


def validated_relative(relative: Any, *, context: str) -> Path:
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError(f"{context} must be a non-empty relative path")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or path.as_posix().startswith("/"):
        raise ValueError(f"{context} escapes the Harbor 题包")
    return path


def is_modifiable(relative: Path) -> bool:
    parts = relative.parts
    return (
        relative.as_posix() == "instruction.md"
        or (len(parts) >= 2 and parts[0] in {"tests", "solution"})
    )


def repair_target(root: Path, relative: Any) -> tuple[Path, Path]:
    relative_path = validated_relative(relative, context="operation file")
    if not is_modifiable(relative_path):
        raise ValueError(
            "unsupported repair target; only instruction.md, tests/**, and "
            "solution/** are modifiable"
        )
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise ValueError("repair target may not traverse a symbolic link")
    return root / relative_path, relative_path


def package_path(root: Path, relative: Any, *, context: str) -> tuple[Path, Path]:
    relative_path = validated_relative(relative, context=context)
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise ValueError(f"{context} may not traverse a symbolic link")
    return root / relative_path, relative_path


def validate_external_plan(root: Path, plan_path: Path) -> dict[str, Any]:
    resolved = plan_path.expanduser().resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("repair plan must remain outside the Harbor 题包")
    if not resolved.is_file():
        raise FileNotFoundError(f"repair plan is missing: {resolved}")
    plan = read_json(resolved)
    if not isinstance(plan, dict) or plan.get("schema_version") != "0.1":
        raise ValueError("repair plan must use schema_version 0.1")
    if plan.get("repair_class") not in REPAIR_CLASSES:
        raise ValueError("repair_class must be SAFE_AUTO_FIX or ASSISTED_FIX")
    if not isinstance(plan.get("justification"), str) or not plan[
        "justification"
    ].strip():
        raise ValueError("repair plan requires a justification")
    if not isinstance(plan.get("audit_id"), str) or not plan["audit_id"]:
        raise ValueError("repair plan requires audit_id")
    if not isinstance(plan.get("finding_id"), str) or not plan["finding_id"]:
        raise ValueError("repair plan requires finding_id")
    operations = plan.get("operations")
    regressions = plan.get("regression_tests")
    if not isinstance(operations, list) or not operations:
        raise ValueError("repair plan requires at least one operation")
    if not isinstance(regressions, list) or not regressions:
        raise ValueError("repair plan requires regression tests")
    operation_ids: set[str] = set()
    for operation in operations:
        if not isinstance(operation, dict):
            raise ValueError("every repair operation must be an object")
        operation_id = operation.get("id")
        if not isinstance(operation_id, str) or not operation_id:
            raise ValueError("every repair operation requires a stable id")
        if operation_id in operation_ids:
            raise ValueError(f"duplicate repair operation id: {operation_id}")
        operation_ids.add(operation_id)
        if operation.get("type") not in OPERATION_TYPES:
            raise ValueError(f"unsupported repair operation: {operation.get('type')}")
        repair_target(root, operation.get("file"))
    for specification in regressions:
        if not isinstance(specification, dict):
            raise ValueError("every regression test must be an object")
        if specification.get("type") not in REGRESSION_TYPES:
            raise ValueError(
                f"unsupported regression test type: {specification.get('type')}"
            )
    return plan


def validate_fresh_audit(
    root: Path, plan: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    audit = root / "benchmark_audit"
    report = read_json(audit / "audit_report.json")
    manifest = read_json(audit / "audit_manifest.json")
    disposition = read_json(audit / "disposition.json")
    if plan["audit_id"] != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
    route = disposition.get("route") or report.get("summary", {}).get("disposition")
    if route != "REPAIR_QUEUE":
        raise ValueError("authoritative audit is not routed to REPAIR_QUEUE")
    findings = {
        item.get("finding_id"): item
        for item in report.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }
    if plan["finding_id"] not in findings:
        raise ValueError("repair plan finding_id is not open in the audit")
    input_hashes = manifest.get("input_hashes")
    if not isinstance(input_hashes, dict):
        raise ValueError("audit manifest input_hashes must be an object")
    for relative, expected in input_hashes.items():
        source, relative_path = package_path(
            root, relative, context="audit manifest input path"
        )
        if relative_path.parts[0] in GENERATED_TOP_LEVEL:
            raise ValueError("audit manifest hashes a generated report path")
        if not source.is_file() or sha256_file(source) != expected:
            raise ValueError(f"stale audit: input changed since review: {relative}")
    return report, manifest, findings[plan["finding_id"]]


def evidence_index(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    raw = plan.get("evidence")
    if not isinstance(raw, list) or not raw:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "External Agent repair plans require non-empty evidence.",
        )
    indexed: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            raise PolicyStop("BLOCKED_EVIDENCE", "Evidence items must be objects.")
        evidence_id = item.get("id")
        source = item.get("source")
        quote = item.get("quote")
        if not all(isinstance(value, str) and value.strip() for value in (evidence_id, source, quote)):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Each evidence item requires non-empty id, source, and quote.",
            )
        if evidence_id in indexed:
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"Duplicate evidence id: {evidence_id}"
            )
        source_path = Path(source)
        if not source_path.is_absolute() and ".." not in source_path.parts:
            local = root / source_path
            if local.is_file() and quote not in local.read_text(
                encoding="utf-8", errors="replace"
            ):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"Evidence quote is absent from {source}.",
                )
        if source.startswith("benchmark_audit:"):
            finding_text = json.dumps(report.get("findings", []), ensure_ascii=False)
            if quote not in finding_text:
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "Audit-finding evidence quote is not in the authoritative report.",
                )
        indexed[evidence_id] = item
    return indexed


def linked_evidence(
    operation: dict[str, Any],
    evidence: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    evidence_ids = operation.get("evidence_ids")
    if not isinstance(evidence_ids, list) or not evidence_ids:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} requires linked evidence.",
        )
    if not all(isinstance(item, str) and item in evidence for item in evidence_ids):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} links unknown evidence.",
        )
    return [evidence[item] for item in evidence_ids]


def proposed_text(operation: dict[str, Any]) -> str:
    if operation["type"] == "write_file":
        value = operation.get("content")
    elif operation["type"] in {"replace_text", "text_replace"}:
        value = operation.get("new")
    elif operation["type"] == "json_set":
        value = json.dumps(operation.get("value"), ensure_ascii=False)
    else:
        return ""
    return value if isinstance(value, str) else ""


def solution_fragments(root: Path) -> set[str]:
    solution = root / "solution"
    if not solution.is_dir():
        return set()
    fragments: set[str] = set()
    for path in solution.rglob("*"):
        if not path.is_file() or path.is_symlink() or path.stat().st_size > 2_000_000:
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if len(stripped) >= 12:
                fragments.add(stripped)
    return fragments


def validate_policy(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    if plan.get("core_science_change") is not False:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Plan must declare core_science_change=false; Repair may not "
            "redefine the Harbor package's core science.",
        )
    evidence = evidence_index(root, report, plan)
    hidden_fragments = solution_fragments(root)
    for operation in plan["operations"]:
        _, relative = repair_target(root, operation["file"])
        if relative.parts[0] != "solution":
            continue
        hidden_fragments.update(
            line.strip()
            for line in proposed_text(operation).splitlines()
            if len(line.strip()) >= 12
        )
    for operation in plan["operations"]:
        linked = linked_evidence(operation, evidence)
        _, relative = repair_target(root, operation["file"])
        if relative.as_posix() == "instruction.md":
            if any(
                Path(str(item["source"])).parts[:1] == ("solution",)
                for item in linked
            ):
                raise PolicyStop(
                    "POLICY_VIOLATION",
                    "Solution content cannot be evidence for public instruction.",
                )
            addition = proposed_text(operation)
            if any(fragment in addition for fragment in hidden_fragments):
                raise PolicyStop(
                    "POLICY_VIOLATION",
                    "Repair would leak hidden solution content into instruction.md.",
                )
    return evidence


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


def set_json_path(value: Any, tokens: Any, replacement: Any) -> Any:
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("JSON operation path must be a non-empty token list")
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
    return value


def file_state(path: Path) -> str | None:
    return sha256_file(path) if path.is_file() else None


def apply_operation(candidate: Path, operation: dict[str, Any]) -> dict[str, Any]:
    path, relative = repair_target(candidate, operation["file"])
    before_hash = file_state(path)
    operation_type = operation["type"]
    if operation_type == "write_file":
        content = operation.get("content")
        if not isinstance(content, str):
            raise ValueError("write_file content must be a string")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        if operation.get("executable") is True:
            path.chmod(path.stat().st_mode | 0o111)
    elif operation_type in {"replace_text", "text_replace"}:
        if not path.is_file():
            raise FileNotFoundError(path)
        old = operation.get("old")
        new = operation.get("new")
        if not isinstance(old, str) or not old or not isinstance(new, str):
            raise ValueError("replace_text requires non-empty old and string new")
        content = path.read_text(encoding="utf-8")
        count = operation.get("count", 1)
        if not isinstance(count, int) or count <= 0:
            raise ValueError("replace_text count must be a positive integer")
        if content.count(old) != count:
            raise ValueError(
                "replace_text old content does not occur the declared number of times"
            )
        path.write_text(content.replace(old, new, count), encoding="utf-8")
    elif operation_type == "json_set":
        if not path.is_file():
            raise FileNotFoundError(path)
        document = read_json(path)
        tokens = operation.get("path")
        present, before_value = json_path_value(document, tokens)
        replacement = operation.get("value")
        if (
            any(
                isinstance(token, str) and "threshold" in token.lower()
                for token in tokens
            )
            and present
            and isinstance(before_value, (int, float))
            and isinstance(replacement, (int, float))
            and replacement < before_value
            and not operation.get("evidence_ids")
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Lowering a scoring threshold requires linked evidence.",
            )
        write_json(path, set_json_path(document, tokens, replacement))
    elif operation_type == "delete_file":
        if not path.is_file():
            raise FileNotFoundError(path)
        path.unlink()
    else:  # guarded by plan validation
        raise ValueError(f"unsupported repair operation: {operation_type}")
    after_hash = file_state(path)
    if before_hash == after_hash:
        raise ValueError(f"operation {operation['id']} made no change")
    return {
        "operation_id": operation["id"],
        "operation": operation_type,
        "file": relative.as_posix(),
        "before_hash": before_hash,
        "after_hash": after_hash,
        "evidence_ids": operation["evidence_ids"],
    }


def regression_result(
    root: Path, specification: dict[str, Any]
) -> tuple[bool, dict[str, Any]]:
    kind = specification["type"]
    detail: dict[str, Any] = {}
    try:
        if kind == "command":
            command = specification.get("command")
            if (
                not isinstance(command, list)
                or not command
                or not all(isinstance(item, str) and item for item in command)
            ):
                raise ValueError("command regression requires a string argv list")
            timeout = specification.get("timeout_seconds", 30)
            if not isinstance(timeout, (int, float)) or not 0 < timeout <= 60:
                raise ValueError("command regression timeout must be in (0, 60]")
            process = subprocess.run(
                command,
                cwd=root,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
            expected = specification.get("expected_returncode", 0)
            passed = process.returncode == expected
            if "stdout_contains" in specification:
                passed = passed and specification["stdout_contains"] in process.stdout
            if "stderr_contains" in specification:
                passed = passed and specification["stderr_contains"] in process.stderr
            detail = {
                "returncode": process.returncode,
                "stdout": process.stdout[-2000:],
                "stderr": process.stderr[-2000:],
            }
            return passed, detail
        path, _ = package_path(root, specification.get("file"), context="regression file")
        if kind == "file_exists":
            return path.is_file(), detail
        if kind == "file_absent":
            return not path.exists(), detail
        if kind == "file_executable":
            return path.is_file() and os.access(path, os.X_OK), detail
        if kind == "text_contains":
            return (
                path.is_file()
                and str(specification.get("expected", ""))
                in path.read_text(encoding="utf-8", errors="replace")
            ), detail
        if kind == "text_not_contains":
            return (
                path.is_file()
                and str(specification.get("expected", ""))
                not in path.read_text(encoding="utf-8", errors="replace")
            ), detail
        if kind == "json_path_equals":
            if not path.is_file():
                return False, detail
            present, value = json_path_value(read_json(path), specification.get("path"))
            return present and value == specification.get("expected"), detail
    except (OSError, subprocess.SubprocessError, ValueError, json.JSONDecodeError) as exc:
        return False, {"error": str(exc)}
    raise ValueError(f"unsupported regression test type: {kind}")


def run_regressions(
    root: Path,
    specifications: list[dict[str, Any]],
    phase: str,
    prior: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    results = prior or [{"specification": item} for item in specifications]
    for item in results:
        passed, detail = regression_result(root, item["specification"])
        item[f"{phase}_passed"] = passed
        item[f"{phase}_detail"] = detail
        expected = item["specification"].get(
            f"expected_{phase}", phase == "after"
        )
        if passed is not expected:
            raise ValueError(
                f"regression test {phase} result was {passed}, expected {expected}"
            )
    return results


def iter_package_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in GENERATED_TOP_LEVEL:
            continue
        yield path


def package_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in iter_package_files(root)
    }


def assert_mutation_boundary(
    snapshot: Path,
    candidate: Path,
    operation_files: set[str],
) -> None:
    before = package_hashes(snapshot)
    after = package_hashes(candidate)
    changed = {
        relative
        for relative in set(before) | set(after)
        if before.get(relative) != after.get(relative)
    }
    if not changed.issubset(operation_files):
        raise ValueError(f"repair escaped the modifiable target boundary: {sorted(changed)}")
    if any(not is_modifiable(Path(relative)) for relative in changed):
        raise ValueError("repair modified a read-only package role")


def report_configuration(report: dict[str, Any]) -> tuple[str, str]:
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise ValueError("Review report requires configuration")
    paper_mode = configuration.get("paper_mode")
    execution_level = configuration.get("execution_level")
    if paper_mode not in {"no_paper", "paper_grounded"}:
        raise ValueError("Review report has an unsupported paper_mode")
    if not isinstance(execution_level, str) or not execution_level:
        raise ValueError("Review report requires execution_level")
    return paper_mode, execution_level


def run_equal_depth_review(
    candidate: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    runner = (
        Path(__file__).resolve().parents[2]
        / "materials-benchmark-review/scripts/run_review.py"
    )
    if not runner.is_file():
        raise FileNotFoundError(f"Review runner is missing: {runner}")
    paper_mode, execution_level = report_configuration(report)
    command = [
        sys.executable,
        str(runner),
        str(candidate),
        "--paper-mode",
        paper_mode,
        "--execution-level",
        execution_level,
    ]
    for key, flag in {
        "known_valid_output": "--known-valid-output",
        "agent_assessment": "--agent-assessment",
        "e2_smoke_plan": "--e2-smoke-plan",
    }.items():
        raw = plan.get(key)
        if raw is None:
            continue
        external = Path(str(raw)).expanduser().resolve()
        if external.is_relative_to(candidate.resolve()):
            raise ValueError(f"{key} must remain external to the candidate")
        if not external.exists():
            raise FileNotFoundError(f"{key} is missing: {external}")
        command.extend([flag, str(external)])
    process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError("equal-depth re-audit failed: " + process.stderr[-2000:])
    reaudit = read_json(candidate / "benchmark_audit/audit_report.json")
    if report_configuration(reaudit) != (paper_mode, execution_level):
        raise ValueError("re-audit evidence depth differs from the source audit")
    return reaudit


def finding_key(finding: dict[str, Any]) -> str | None:
    for key in ("code", "title", "finding_code"):
        value = finding.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def validate_reaudit(
    candidate: Path,
    reaudit: dict[str, Any],
    source_finding: dict[str, Any],
) -> None:
    summary = reaudit.get("summary", {})
    disposition_path = candidate / "benchmark_audit/disposition.json"
    disposition = read_json(disposition_path) if disposition_path.is_file() else {}
    verdict = summary.get("final_verdict") or disposition.get("verdict")
    route = summary.get("disposition") or disposition.get("route")
    if verdict != "PASS" or route != "PUBLISH_CANDIDATE":
        raise ValueError("equal-depth re-audit did not route PASS to PUBLISH_CANDIDATE")
    source_key = finding_key(source_finding)
    if source_key and any(
        finding_key(item) == source_key
        for item in reaudit.get("findings", [])
        if isinstance(item, dict)
    ):
        raise ValueError("target finding remains open after re-audit")


def replace_paths(value: Any, old: str, new: str) -> Any:
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [replace_paths(item, old, new) for item in value]
    if isinstance(value, dict):
        return {key: replace_paths(item, old, new) for key, item in value.items()}
    return value


def rebase_audit_paths(candidate: Path, final_root: Path) -> None:
    audit = candidate / "benchmark_audit"
    old = str(candidate)
    new = str(final_root)
    for path in audit.rglob("*"):
        if not path.is_file() or path.name == "audit_manifest.json":
            continue
        if path.suffix == ".json":
            write_json(path, replace_paths(read_json(path), old, new))
        elif path.suffix == ".jsonl":
            lines = [
                json.dumps(
                    replace_paths(json.loads(line), old, new), ensure_ascii=False
                )
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            path.write_text("".join(line + "\n" for line in lines), encoding="utf-8")
        elif path.suffix in {".md", ".log"}:
            path.write_text(
                path.read_text(encoding="utf-8").replace(old, new),
                encoding="utf-8",
            )
    manifest_path = audit / "audit_manifest.json"
    if manifest_path.is_file():
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


def prior_failed_attempts(root: Path, root_cause: str) -> list[dict[str, Any]]:
    history_root = history_root_for(root)
    if not history_root.is_dir():
        return []
    attempts: list[dict[str, Any]] = []
    for path in history_root.glob("*/attempt_manifest.json"):
        try:
            value = read_json(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if (
            isinstance(value, dict)
            and value.get("root_cause") == root_cause
            and value.get("status") in {"ROLLED_BACK", "ABANDONED"}
            and isinstance(value.get("attempt_number"), int)
            and value["attempt_number"] > 0
        ):
            attempts.append(value)
    return sorted(attempts, key=lambda item: item["attempt_number"])


def record_control_stop(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    root_cause: str,
    stop: PolicyStop,
) -> dict[str, Any]:
    repair_id = unique_id("repair-stop")
    history_root = history_root_for(root)
    destination = history_root / repair_id
    destination.mkdir(parents=True)
    write_json(destination / "repair_plan.json", plan)
    manifest = {
        "schema_version": "0.1",
        "repair_id": repair_id,
        "root_cause": root_cause,
        "attempt_number": 0,
        "status": stop.status,
        "audit_id": report["audit_id"],
        "finding_id": plan["finding_id"],
        "repair_class": plan["repair_class"],
        "reason": stop.reason,
        "package_mutated": False,
        "recorded_at": timestamp(),
    }
    write_json(destination / "attempt_manifest.json", manifest)
    return {
        "status": stop.status,
        "root_cause": root_cause,
        "history_root": str(history_root),
        "history_dir": str(destination),
        "attempt_manifest": str(destination / "attempt_manifest.json"),
        "reason": stop.reason,
    }


def package_identity(
    root: Path, *, directory_name: str | None = None
) -> dict[str, Any]:
    identity: dict[str, Any] = {
        "directory_name": directory_name if directory_name is not None else root.name
    }
    manifest = root / "manifest.json"
    if manifest.is_file():
        identity["manifest_hash"] = sha256_file(manifest)
    return identity


def write_repair_reports(
    candidate: Path,
    manifest: dict[str, Any],
) -> None:
    report_dir = candidate / "benchmark_repair"
    write_json(report_dir / "repair_manifest.json", manifest)
    write_json(report_dir / "repair_report.json", manifest)
    report_dir.joinpath("repair_report.md").write_text(
        "\n".join(
            [
                "# Materials Benchmark Repair",
                "",
                f"- Repair ID: {manifest['repair_id']}",
                f"- Status: {manifest['status']}",
                f"- Repair class: {manifest['repair_class']}",
                f"- Source audit: {manifest['source_audit_id']}",
                f"- Finding: {manifest['finding_id']}",
                f"- Attempts used: {manifest['attempt_number']} of 2",
                f"- Equal-depth verdict: {manifest['reaudit']['verdict']}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def repair(root: Path, plan_path: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir() or not (root / "instruction.md").is_file() or not (
        root / "tests"
    ).is_dir():
        raise ValueError("input must be a Harbor 题包 with instruction.md and tests/")
    plan = validate_external_plan(root, plan_path)
    report, audit_manifest, finding = validate_fresh_audit(root, plan)
    root_cause = root_cause_id(report, plan)
    prior = prior_failed_attempts(root, root_cause)
    if len(prior) >= 2 or any(item["status"] == "ABANDONED" for item in prior):
        return {
            "status": "ABANDONED",
            "root_cause": root_cause,
            "history_root": str(history_root_for(root)),
            "attempts": len(prior),
            "reason": "Two failed attempts exhausted the root-cause limit.",
        }
    try:
        evidence = validate_policy(root, report, plan)
    except PolicyStop as stop:
        return record_control_stop(root, report, plan, root_cause, stop)

    attempt_number = len(prior) + 1
    repair_id = unique_id("repair")
    workspace = root.parent / ".benchmark_repair_tmp" / repair_id
    history = history_root_for(root) / repair_id
    if workspace.exists() or history.exists():
        raise FileExistsError("repair workspace already exists")
    workspace.parent.mkdir(exist_ok=True)
    workspace.mkdir()
    snapshot = workspace / "snapshot"
    candidate = workspace / "candidate"
    identity = package_identity(root)
    try:
        shutil.copytree(root, snapshot)
        shutil.copytree(snapshot, candidate)
        regression_tests = run_regressions(
            snapshot, plan["regression_tests"], "before"
        )
        changes = [
            apply_operation(candidate, operation) for operation in plan["operations"]
        ]
        operation_files = {item["file"] for item in changes}
        assert_mutation_boundary(snapshot, candidate, operation_files)
        run_regressions(
            candidate, plan["regression_tests"], "after", regression_tests
        )
        reaudit = run_equal_depth_review(candidate, report, plan)
        validate_reaudit(candidate, reaudit, finding)
        assert_mutation_boundary(snapshot, candidate, operation_files)
        if package_identity(candidate, directory_name=root.name) != identity:
            raise ValueError("repair changed the Harbor package identity")
        paper_mode, execution_level = report_configuration(reaudit)
        repair_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "status": "PUBLISHED",
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "finding_id": plan["finding_id"],
            "finding_code": finding_key(finding),
            "repair_class": plan["repair_class"],
            "package_identity": identity,
            "source_audit_id": report["audit_id"],
            "source_audit_input_hashes": audit_manifest["input_hashes"],
            "justification": plan["justification"],
            "evidence": list(evidence.values()),
            "changes": changes,
            "regression_tests": regression_tests,
            "reaudit": {
                "audit_id": reaudit["audit_id"],
                "paper_mode": paper_mode,
                "execution_level": execution_level,
                "verdict": reaudit["summary"]["final_verdict"],
                "disposition": reaudit["summary"].get("disposition"),
            },
            "atomic_publish": True,
            "published_at": timestamp(),
        }
        write_repair_reports(candidate, repair_manifest)
        rebase_audit_paths(candidate, root)

        history.mkdir(parents=True)
        snapshot.rename(history / "snapshot")
        write_json(history / "repair_plan.json", plan)
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": "PUBLISHED",
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": timestamp(),
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
        write_json(history / "repair_plan.json", plan)
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": status,
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": str(exc),
            "snapshot_preserved": (history / "snapshot").is_dir(),
            "candidate_preserved": (history / "candidate").is_dir(),
            "package_mutated": False,
            "recorded_at": timestamp(),
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
    parser = argparse.ArgumentParser(
        description="Repair one audited materials-science Harbor 题包."
    )
    parser.add_argument("benchmark_root")
    parser.add_argument("--plan", required=True)
    arguments = parser.parse_args()
    try:
        result = repair(Path(arguments.benchmark_root), Path(arguments.plan))
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "PUBLISHED" else 3
    except Exception as exc:  # noqa: BLE001
        print(f"materials repair failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
