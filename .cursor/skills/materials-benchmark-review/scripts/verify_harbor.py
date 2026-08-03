#!/usr/bin/env python3
"""Verify Harbor core files and keep Review/Repair evidence outside packages."""

from __future__ import annotations

import os


PUB = os.path.join(os.environ.get("QA_ROOT", "/personal/qa-review"), "_publish")
CORE = {
    "instruction.md", "manifest.json", "paper/paper.md", "resources.json",
    "steps.json", "task.toml", "tests/checker.py", "tests/grading_spec.json",
    "tests/test.sh",
}
EVIDENCE_MARKERS = (
    "core_review", "core_repair", "review_report", "checker_observations",
    "candidate/", "evidence/", "__pycache__", ".pyc",
)

packages = []
for root, dirs, files in os.walk(PUB):
    if "solution" in dirs:
        dirs.remove("solution")
    if "instruction.md" in files and "task.toml" in files:
        packages.append(root)

missing_core, invalid_core, evidence_leak, extras = [], [], [], []
exact = 0
for package in packages:
    have = set()
    for root, dirs, files in os.walk(package):
        relative_root = os.path.relpath(root, package)
        if relative_root == "solution" or relative_root.startswith(f"solution{os.sep}"):
            dirs[:] = []
            continue
        for filename in files:
            have.add(os.path.relpath(os.path.join(root, filename), package))
    missing = CORE - have
    extra = have - CORE
    if missing:
        missing_core.append((os.path.relpath(package, PUB), sorted(missing)))
    test_entrypoint = os.path.join(package, "tests/test.sh")
    if os.path.isfile(test_entrypoint):
        with open(test_entrypoint, encoding="utf-8", errors="replace") as handle:
            content = handle.read()
        reasons = []
        if not content.strip():
            reasons.append("empty")
        if not content.startswith("#!"):
            reasons.append("missing shebang")
        if not os.stat(test_entrypoint).st_mode & 0o111:
            reasons.append("not executable")
        if reasons:
            invalid_core.append((os.path.relpath(package, PUB), "tests/test.sh", reasons))
    leaked = sorted(entry for entry in extra if any(marker in entry for marker in EVIDENCE_MARKERS))
    if leaked:
        evidence_leak.append((os.path.relpath(package, PUB), leaked))
    if extra:
        extras.append((os.path.relpath(package, PUB), sorted(extra)))
    if have == CORE:
        exact += 1

print(f"packages: {len(packages)}  exact-core-only: {exact}  with-extras: {len(extras)}")
print(f"MISSING core (FAIL): {len(missing_core)}")
for item in missing_core[:40]:
    print("  MISS", item)
print(f"INVALID core (FAIL): {len(invalid_core)}")
for item in invalid_core[:40]:
    print("  INVALID", item)
print(f"REVIEW/pycache leak (FAIL): {len(evidence_leak)}")
for item in evidence_leak[:40]:
    print("  LEAK", item)
ok = not missing_core and not invalid_core and not evidence_leak
print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
