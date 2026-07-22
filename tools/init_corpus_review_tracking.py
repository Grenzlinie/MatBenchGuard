#!/usr/bin/env python3
"""Generate or merge materials corpus review-tracking JSON.

Records reviewed / not-reviewed status only. No claims, leases, lock tokens,
whitelist, skill imports, or auto-scoring.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = REPO_ROOT / "materials_science_questions"
DEFAULT_OUTPUT = DEFAULT_CORPUS / "corpus_review_tracking.json"
SCHEMA_VERSION = "materials-corpus-review-tracking/1.0"

MANAGEMENT_DIR_NAMES = frozenset(
    {
        "review_outputs",
        "review_records",
        ".review_records",
        "benchmark_audit",
        "benchmark_audit_history",
        ".benchmark_audit_tmp",
        ".benchmark_repair_tmp",
        ".benchmark_repair_history",
        "repair_history",
        "benchmark_repair_history",
    }
)
IGNORED_FILE_NAMES = frozenset({"corpus_review_tracking.json"})

HUMAN_FIELDS = (
    "review_status",
    "review_verdict",
    "publishability",
    "repair_status",
    "last_audit_id",
    "audit_output_dir",
    "last_reviewed_at",
    "reviewer",
    "notes",
)


def _is_management(path: Path) -> bool:
    return bool(set(path.parts) & MANAGEMENT_DIR_NAMES)


def discover_packages(corpus_root: Path) -> list[Path]:
    """Return Harbor package roots under corpus_root in stable order."""
    root = corpus_root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"corpus root is not a directory: {root}")
    packages: list[Path] = []
    for instruction in sorted(root.rglob("instruction.md")):
        if _is_management(instruction) or instruction.name in IGNORED_FILE_NAMES:
            continue
        package = instruction.parent
        try:
            relative = package.relative_to(root)
        except ValueError:
            continue
        # Corpus identity is exactly <cluster>/<theme>/paper-<id>. Nested
        # lookalikes, management trees, and symlink-backed identities are not
        # Harbor package records.
        if len(relative.parts) != 3 or not package.name.startswith("paper-"):
            continue
        identity_paths = [root / Path(*relative.parts[:index]) for index in range(1, 4)]
        if instruction.is_symlink() or any(path.is_symlink() for path in identity_paths):
            continue
        if not (package / "tests").is_dir():
            continue
        packages.append(package.resolve())
    packages = sorted(packages, key=lambda path: path.relative_to(root).as_posix())
    return packages


def package_record(corpus_root: Path, package: Path, discovery_rank: int) -> dict[str, Any]:
    relative = package.relative_to(corpus_root)
    parts = relative.parts
    if len(parts) < 3:
        raise ValueError(f"unexpected package path shape: {relative.as_posix()}")
    cluster, theme, paper = parts[0], parts[1], parts[2]
    package_id = relative.as_posix()
    return {
        "package_id": package_id,
        "cluster": cluster,
        "theme": theme,
        "paper": paper,
        "discovery_rank": discovery_rank,
        "has_instruction": (package / "instruction.md").is_file(),
        "has_checker": (package / "tests/checker.py").is_file(),
        "has_grading_spec": (package / "tests/grading_spec.json").is_file(),
        "has_paper": (package / "paper/paper.md").is_file(),
        "has_solution_oracle": (package / "solution").exists(),
        "review_status": "pending",
        "review_verdict": None,
        "publishability": None,
        "repair_status": "not_applicable",
        "last_audit_id": None,
        "audit_output_dir": None,
        "last_reviewed_at": None,
        "reviewer": None,
        "notes": None,
    }


def merge_record(fresh: dict[str, Any], previous: dict[str, Any] | None) -> dict[str, Any]:
    if not previous:
        return fresh
    merged = dict(fresh)
    for field in HUMAN_FIELDS:
        if field in previous:
            merged[field] = previous[field]
    return merged


def build_tracking(
    corpus_root: Path,
    *,
    previous: dict[str, Any] | None = None,
) -> dict[str, Any]:
    root = corpus_root.expanduser().resolve()
    prior_by_id: dict[str, dict[str, Any]] = {}
    if previous is not None:
        records = previous.get("records")
        if isinstance(records, list):
            for item in records:
                if isinstance(item, dict) and isinstance(item.get("package_id"), str):
                    prior_by_id[item["package_id"]] = item
    packages = discover_packages(root)
    records = [
        merge_record(
            package_record(root, package, rank),
            prior_by_id.get(package.relative_to(root).as_posix()),
        )
        for rank, package in enumerate(packages, start=1)
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "corpus_root": str(root),
        "package_count": len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize or merge materials corpus review tracking JSON."
    )
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=DEFAULT_CORPUS,
        help="materials_science_questions root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="tracking JSON path (default: <corpus>/corpus_review_tracking.json)",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="preserve human-updated fields while resyncing corpus packages",
    )
    arguments = parser.parse_args()
    previous = None
    if arguments.merge and arguments.output.is_file():
        previous = json.loads(arguments.output.read_text(encoding="utf-8"))
        if not isinstance(previous, dict):
            raise SystemExit("existing tracking file must be a JSON object")
    payload = build_tracking(arguments.corpus_root, previous=previous)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(arguments.output.resolve()),
                "package_count": payload["package_count"],
                "merged": bool(previous),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
