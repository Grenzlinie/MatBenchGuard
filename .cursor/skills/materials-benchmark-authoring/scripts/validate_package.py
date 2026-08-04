#!/usr/bin/env python3
"""Static validation for a solution-free Paper2Arm authoring candidate."""

from __future__ import annotations

import argparse
import json
import re
import stat
from pathlib import Path, PurePath, PurePosixPath
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and older
    tomllib = None  # type: ignore[assignment]


BASE_IMAGE = "dp-harbor-registry.cn-zhangjiakou.cr.aliyuncs.com/public/paper2arm-env:v1.0-20260708"
REQUIRED_FILES = (
    "instruction.md",
    "paper/paper.md",
    "paper/images_manifest.json",
    "manifest.json",
    "steps.json",
    "resources.json",
    "task.toml",
    "environment/Dockerfile",
    "tests/grading_spec.json",
    "tests/checker.py",
    "tests/test.sh",
)
REQUIRED_HEADINGS = (
    "Problem background",
    "Approach",
    "Reproduction target",
    "Assets",
    "Workflow steps",
    "Output files",
    "Output contract",
    "How you are scored",
)


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON {path}: {exc}")
        return None


def output_items(spec: dict[str, Any]) -> list[dict[str, Any]]:
    value = spec.get("output_contract", [])
    if isinstance(value, dict):
        if isinstance(value.get("outputs"), list):
            value = value["outputs"]
        else:
            value = [value]
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def canonical_output_path(value: str) -> PurePosixPath | None:
    if "\\" in value:
        return None
    absolute = value if value.startswith("/") else f"/app/outputs/{value}"
    path = PurePosixPath(absolute)
    if (
        not path.is_absolute()
        or path.parts[:3] != ("/", "app", "outputs")
        or len(path.parts) <= 3
        or ".." in path.parts
    ):
        return None
    return path


def load_basic_toml(path: Path) -> dict[str, Any]:
    """Parse the scalar-only task profile when stdlib tomllib is unavailable."""
    text = path.read_text(encoding="utf-8")
    if tomllib is not None:
        return tomllib.loads(text)
    result: dict[str, Any] = {}
    current = result
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            current = result
            for part in line[1:-1].split("."):
                current = current.setdefault(part.strip(), {})
            continue
        if "=" not in line:
            raise ValueError(f"unsupported TOML line: {raw_line}")
        key, raw_value = (part.strip() for part in line.split("=", 1))
        if raw_value.startswith(('"', "'")) and raw_value.endswith(('"', "'")):
            value: Any = raw_value[1:-1]
        elif raw_value.lower() in {"true", "false"}:
            value = raw_value.lower() == "true"
        else:
            try:
                value = int(raw_value)
            except ValueError:
                try:
                    value = float(raw_value)
                except ValueError as exc:
                    raise ValueError(f"unsupported TOML value: {raw_value}") from exc
        current[key] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--authoring-record", type=Path)
    args = parser.parse_args()
    package = args.package.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not package.is_dir():
        errors.append(f"package is not a directory: {package}")
    if (package / "solution").exists():
        errors.append("solution/ is prohibited in authoring candidates")
    for child in package.rglob("*") if package.is_dir() else ():
        try:
            relative_parts = child.relative_to(package).parts
        except ValueError:
            continue
        if any(part.lower() == "solution" for part in relative_parts):
            errors.append(f"solution path component is prohibited: {child.relative_to(package)}")
            break
    for rel in REQUIRED_FILES:
        if not (package / rel).is_file():
            errors.append(f"missing required file: {rel}")
    if errors:
        print(json.dumps({"valid": False, "errors": errors, "warnings": warnings}, indent=2))
        return 1

    instruction = (package / "instruction.md").read_text(encoding="utf-8")
    if re.search(
        r"(?<![A-Za-z0-9_.-])(?:/app/|/)?resources/[A-Za-z0-9_.-]+",
        instruction,
        re.IGNORECASE,
    ):
        errors.append("instruction must mention resource basenames only, never resource paths")
    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+{re.escape(heading)}\s*$", instruction, re.MULTILINE | re.IGNORECASE):
            errors.append(f"instruction missing heading: {heading}")
    forbidden_refs = (
        r"paper/paper\.md",
        r"\bpaper\.md\b",
        r"(?:see|consult|refer to|查看|参见)\s+(?:the\s+)?(?:fig(?:ure)?|table|section|图|表|章节)\b",
    )
    for pattern in forbidden_refs:
        if re.search(pattern, instruction, re.IGNORECASE):
            errors.append(f"instruction contains paper-dependent reference: {pattern}")

    paper_text = (package / "paper" / "paper.md").read_text(encoding="utf-8").strip()
    if len(paper_text) < 1000 or "UniParser Markdown output goes here" in paper_text:
        errors.append("paper/paper.md appears incomplete or placeholder-only")

    manifest = load_json(package / "manifest.json", errors)
    if isinstance(manifest, dict):
        for key in (
            "cluster_id",
            "paper_id",
            "paper_ids",
            "discipline",
            "task_mode",
            "verify_mode",
            "metric_type",
            "prompt_version",
            "n_instances",
            "difficulty",
        ):
            if key not in manifest:
                errors.append(f"manifest missing key: {key}")
        if manifest.get("metric_type") != "paper2arm":
            errors.append("manifest.metric_type must be paper2arm")

    steps = load_json(package / "steps.json", errors)
    if not isinstance(steps, list) or not steps:
        errors.append("steps.json must be a non-empty list")
    elif isinstance(steps, list):
        for index, item in enumerate(steps):
            if not isinstance(item, dict):
                errors.append(f"steps[{index}] must be an object")
                continue
            if item.get("role") not in {"process", "scored", "checked_result"}:
                errors.append(f"steps[{index}].role is invalid")

    resources_doc = load_json(package / "resources.json", errors)
    if isinstance(resources_doc, dict):
        resources = resources_doc.get("resources")
        mappings = resources_doc.get("resources_mapping")
        if not isinstance(resources, list) or not isinstance(mappings, list):
            errors.append("resources and resources_mapping must be lists")
        elif len(resources) != len(mappings):
            errors.append("resources_mapping must be positionally aligned with resources")
        else:
            ids: set[str] = set()
            for index, (resource, mapping) in enumerate(zip(resources, mappings)):
                if not isinstance(resource, dict):
                    errors.append(f"resources[{index}] must be an object")
                    continue
                resource_id = resource.get("id")
                if not isinstance(resource_id, str) or not resource_id:
                    errors.append(f"resources[{index}].id is required")
                elif resource_id in ids:
                    errors.append(f"duplicate resource id: {resource_id}")
                ids.add(str(resource_id))
                access = resource.get("access")
                if isinstance(access, dict) and access.get("method") == "bundled":
                    filename = access.get("filename")
                    if not isinstance(filename, str) or PurePath(filename).name != filename:
                        errors.append(f"bundled resource {resource_id} needs basename access.filename")
                        continue
                    declared_package = access.get("package")
                    if declared_package:
                        relative = PurePosixPath(str(declared_package))
                        if (
                            relative.is_absolute()
                            or ".." in relative.parts
                            or relative.name != filename
                            or not (package / Path(*relative.parts)).is_file()
                        ):
                            errors.append(
                                f"bundled resource package locator is invalid or missing: {declared_package}"
                            )
                    elif not (package / "resources" / filename).is_file():
                        errors.append(f"bundled resource file missing: resources/{filename}")
                    if not isinstance(mapping, dict):
                        errors.append(f"bundled resource {resource_id} needs non-null positional mapping")
                    else:
                        for key in ("resource_type", "resource_unique_key"):
                            if not mapping.get(key):
                                errors.append(f"bundled resource {resource_id} mapping missing {key}")
                        if mapping.get("resource_type") != resource.get("type"):
                            errors.append(
                                f"bundled resource {resource_id} mapping resource_type disagrees with resource.type"
                            )
                    if filename not in instruction:
                        errors.append(f"instruction does not mention bundled filename {filename}")

    try:
        task = load_basic_toml(package / "task.toml")
    except (OSError, ValueError) as exc:
        errors.append(f"invalid task.toml: {exc}")
        task = {}
    if task:
        if task.get("schema_version") != "1.3":
            warnings.append("Paper2Arm corpus profile expects task schema_version 1.3; verify with current Harbor")
        if not isinstance(task.get("task"), dict) or "/" not in str(task["task"].get("name", "")):
            errors.append("task.name must use org/name form")
        environment = task.get("environment", {})
        if environment.get("docker_image") != BASE_IMAGE:
            errors.append("task.toml must use the standard Paper2Arm base image")
        if environment.get("allow_internet") is not True:
            errors.append("task.toml environment.allow_internet must be true")
        if environment.get("build_timeout_sec") != 1800:
            errors.append("task.toml environment.build_timeout_sec must be 1800")
        if task.get("verifier", {}).get("timeout_sec") != 11400:
            errors.append("task.toml verifier.timeout_sec must be 11400")

    docker_lines = [
        line.strip()
        for line in (package / "environment" / "Dockerfile").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if docker_lines[:2] != [f"FROM {BASE_IMAGE}", "WORKDIR /app"]:
        errors.append("environment/Dockerfile must begin with the standard FROM and WORKDIR")
    if any(line.upper().startswith("COPY ") and "RESOURCE" in line.upper() for line in docker_lines):
        errors.append("do not bind authoring resources through Dockerfile COPY")

    grading = load_json(package / "tests" / "grading_spec.json", errors)
    if isinstance(grading, dict):
        if grading.get("quality_tier") != "RESULT_ENHANCED":
            errors.append("grading_spec.quality_tier must be RESULT_ENHANCED")
        if "scoring_tier" in grading:
            errors.append("grading_spec must use quality_tier, not legacy scoring_tier")
        outputs = output_items(grading)
        if not outputs:
            errors.append("grading_spec.output_contract must be non-empty")
        for index, item in enumerate(outputs):
            path = item.get("path") or item.get("file")
            if not isinstance(path, str):
                errors.append(f"output_contract[{index}] needs path/file")
                continue
            canonical = canonical_output_path(path)
            if canonical is None:
                errors.append(
                    f"output contract path must be canonical path under /app/outputs: {path}"
                )
                continue
            if canonical.name not in instruction:
                errors.append(f"instruction does not declare output {canonical.name}")

    checker_text = (package / "tests" / "checker.py").read_text(encoding="utf-8")
    if "TODO: generate checker" in checker_text:
        errors.append("tests/checker.py is still the placeholder")
    for pattern in (r"paper/paper\.md", r"\bpaper\.md\b", r"requests\.", r"urllib\."):
        if re.search(pattern, checker_text):
            errors.append(f"checker contains forbidden dependency: {pattern}")
    expensive = re.compile(r"\b(lammps|pw\.x|vasp|cp2k|gromacs|train(?:ing)?|molecular dynamics)\b", re.IGNORECASE)
    if expensive.search(checker_text):
        warnings.append("checker mentions a primary-compute tool; confirm it does not rerun the task")

    test_sh = package / "tests" / "test.sh"
    test_text = test_sh.read_text(encoding="utf-8")
    if not (test_sh.stat().st_mode & stat.S_IXUSR):
        errors.append("tests/test.sh must be executable")
    if "/logs/verifier/reward" not in test_text:
        errors.append("tests/test.sh must write a Harbor reward file")

    if args.authoring_record:
        record = load_json(args.authoring_record, errors)
        if isinstance(record, dict):
            expected = Path(str(record.get("package_path", "candidate")))
            resolved = expected if expected.is_absolute() else args.authoring_record.parent / expected
            if resolved.resolve() != package:
                errors.append("authoring_record.package_path does not match package")
            record_resources = record.get("resource_records")
            package_resources = (
                resources_doc.get("resources") if isinstance(resources_doc, dict) else None
            )
            if not isinstance(record_resources, list):
                errors.append("authoring_record.resource_records must be a list")
            elif not isinstance(package_resources, list):
                errors.append("package resources must be a list for resource closure")
            else:
                record_by_id = {
                    item.get("resource_id"): item
                    for item in record_resources
                    if isinstance(item, dict) and isinstance(item.get("resource_id"), str)
                }
                package_by_id = {
                    item.get("id"): item
                    for item in package_resources
                    if isinstance(item, dict) and isinstance(item.get("id"), str)
                }
                for resource_id, package_resource in package_by_id.items():
                    record_resource = record_by_id.get(resource_id)
                    if record_resource is None:
                        errors.append(
                            f"package resource {resource_id} is missing from authoring_record.resource_records"
                        )
                        continue
                    access = package_resource.get("access")
                    package_filename = access.get("filename") if isinstance(access, dict) else None
                    record_filename = record_resource.get("filename")
                    if package_filename is not None and not isinstance(record_filename, str):
                        errors.append(
                            f"resource filename is required in authoring record for bundled resource {resource_id}"
                        )
                    elif record_filename is not None and record_filename != package_filename:
                        errors.append(
                            f"resource filename disagrees for {resource_id}: record={record_filename}, package={package_filename}"
                        )
                    record_type = record_resource.get("resource_type")
                    if record_type is not None and record_type != package_resource.get("type"):
                        errors.append(
                            f"resource type disagrees for {resource_id}: record={record_type}, package={package_resource.get('type')}"
                        )
                for resource_id, record_resource in record_by_id.items():
                    if (
                        record_resource.get("availability") == "READY"
                        or record_resource.get("indispensable") is True
                    ) and resource_id not in package_by_id:
                        errors.append(
                            f"ready or indispensable authoring resource {resource_id} is absent from package resources"
                        )

    print(json.dumps({"valid": not errors, "errors": errors, "warnings": warnings}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
