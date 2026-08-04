#!/usr/bin/env python3
"""Create a materials authoring workspace with a single-file Oracle fixture."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"
PACKAGE_TEMPLATE = ASSETS / "package-template"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_text(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--task-name", required=True)
    parser.add_argument("--task-description", default="TODO: paper-grounded materials task")
    parser.add_argument("--cluster-id", default="unassigned")
    args = parser.parse_args()

    pdf = args.pdf.expanduser().resolve()
    if not pdf.is_file():
        parser.error(f"PDF not found: {pdf}")
    if pdf.suffix.lower() != ".pdf":
        parser.error("--pdf must point to a .pdf file")
    if "/" not in args.task_name:
        parser.error("--task-name must use org/name form")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.paper_id):
        parser.error("--paper-id must be one safe path component using letters, digits, dot, underscore, or hyphen")
    workspace = args.output_root.expanduser().resolve() / args.paper_id
    if workspace.exists():
        parser.error(f"workspace already exists: {workspace}")

    source_dir = workspace / "source"
    evidence_dir = workspace / "evidence"
    review_dir = workspace / "independent_review"
    candidate = workspace / "candidate"
    source_dir.mkdir(parents=True)
    evidence_dir.mkdir()
    review_dir.mkdir()
    shutil.copytree(PACKAGE_TEMPLATE, candidate)

    frozen_pdf = source_dir / pdf.name
    shutil.copy2(pdf, frozen_pdf)
    pdf_hash = sha256_file(frozen_pdf)

    instruction_template = (
        SKILL_ROOT.parent
        / "materials-benchmark-review"
        / "assets"
        / "instruction_template.md"
    )
    if not instruction_template.is_file():
        raise SystemExit(f"Review instruction template not found: {instruction_template}")
    shutil.copy2(instruction_template, candidate / "instruction.md")
    (candidate / "paper" / "paper.md").write_text(
        "<!-- UniParser Markdown output goes here. -->\n", encoding="utf-8"
    )

    replacements = {
        "TASK_NAME": args.task_name,
        "TASK_DESCRIPTION": args.task_description,
        "PAPER_ID": args.paper_id,
        "CLUSTER_ID": args.cluster_id,
        "AUTHORING_ID": f"author-{args.paper_id}",
        "PDF_PATH": str(frozen_pdf),
        "PDF_SHA256": pdf_hash,
    }
    for rel in ("task.toml", "manifest.json"):
        render_text(candidate / rel, replacements)

    record = json.loads((ASSETS / "authoring_record_template.json").read_text())
    serialized = json.dumps(record, ensure_ascii=False, indent=2)
    for key, value in replacements.items():
        serialized = serialized.replace("{{" + key + "}}", value)
    (workspace / "authoring_record.json").write_text(serialized + "\n", encoding="utf-8")

    test_sh = candidate / "tests" / "test.sh"
    test_sh.chmod(test_sh.stat().st_mode | 0o111)
    checker = candidate / "tests" / "checker.py"
    checker.chmod(checker.stat().st_mode | 0o111)
    solve_sh = candidate / "solution" / "solve.sh"
    solve_sh.chmod(solve_sh.stat().st_mode | 0o111)

    print(workspace)
    print(f"pdf_sha256={pdf_hash}")
    print("next=Parse the frozen PDF with UniParser into candidate/paper/paper.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
