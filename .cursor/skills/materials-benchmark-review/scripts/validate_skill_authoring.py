#!/usr/bin/env python3
"""Validate the paired materials Review and Repair skill contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True


SKILL_NAMES = {
    "materials-benchmark-review",
    "materials-benchmark-repair",
}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md lacks YAML frontmatter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("SKILL.md has unterminated frontmatter") from exc
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = path.read_text(encoding="utf-8")
    try:
        metadata = frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]
    if metadata.get("name") != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name mismatch")
    if len(metadata.get("description", "")) < 40:
        errors.append(f"{skill_dir.name}: description is not discoverable")
    if "## Completion" not in text:
        errors.append(f"{skill_dir.name}: missing explicit completion conditions")
    if len(text.splitlines()) > 250:
        errors.append(f"{skill_dir.name}: SKILL.md exceeds progressive disclosure limit")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        if not (skill_dir / target).is_file():
            errors.append(
                f"{skill_dir.name}: missing referenced file {target}"
            )
    return errors


def validate() -> dict[str, object]:
    skills_root = Path(__file__).resolve().parents[2]
    errors: list[str] = []
    for name in sorted(SKILL_NAMES):
        errors.extend(validate_skill(skills_root / name))
    expected_runners = {
        "materials-benchmark-review": "scripts/run_review.py",
        "materials-benchmark-repair": "scripts/run_repair.py",
    }
    for name, relative in expected_runners.items():
        if not (skills_root / name / relative).is_file():
            errors.append(f"{name}: missing public runner {relative}")
    taxonomy_sources = list(
        skills_root.glob("*/references/materials-taxonomy.json")
    )
    if len(taxonomy_sources) != 1:
        errors.append("materials taxonomy must have exactly one versioned source")
    review_text = (
        skills_root / "materials-benchmark-review/SKILL.md"
    ).read_text(encoding="utf-8")
    if "references/materials-taxonomy.json" not in review_text:
        errors.append("Review skill does not disclose its taxonomy source")
    return {
        "status": "FAIL" if errors else "PASS",
        "skills": sorted(SKILL_NAMES),
        "taxonomy_sources": len(taxonomy_sources),
        "errors": errors,
    }


def main() -> int:
    try:
        result = validate()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "PASS" else 2
    except Exception as exc:  # noqa: BLE001
        print(f"skill authoring validation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
