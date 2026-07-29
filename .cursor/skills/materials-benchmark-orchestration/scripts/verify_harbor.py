#!/usr/bin/env python3
"""Verify every package under QA_ROOT/_publish has all required Harbor core
files, no audit artifacts, and no in-scope __pycache__. solution/** is excluded
from inspection. Missing core files or leaked in-scope audit artifacts are
flagged as failures.

Env: QA_ROOT (default /personal/qa_review)
"""
import os

PUB = os.path.join(os.environ.get("QA_ROOT", "/personal/qa_review"), "_publish")
CORE = {
    "instruction.md",
    "manifest.json",
    "paper/paper.md",
    "resources.json",
    "steps.json",
    "task.toml",
    "tests/checker.py",
    "tests/grading_spec.json",
    "tests/test.sh",
}
AUDIT = ("agent_final_decision", "repair_report", "reaudit", "mechanical_evidence",
         "checker_observations", ".done", "snapshot/", "candidate/", "__pycache__", ".pyc")

pkgs = []
for root, dirs, files in os.walk(PUB):
    if "solution" in dirs:
        dirs.remove("solution")
    if "instruction.md" in files and "task.toml" in files:
        pkgs.append(root)

missing_core, invalid_core, audit_leak, extras = [], [], [], []
exact = 0
for p in pkgs:
    have = set()
    for r, d, fs in os.walk(p):
        relative_root = os.path.relpath(r, p)
        if relative_root == "solution" or relative_root.startswith(
            f"solution{os.sep}"
        ):
            d[:] = []
            continue
        for fn in fs:
            have.add(os.path.relpath(os.path.join(r, fn), p))
    miss = CORE - have
    extra = have - CORE
    if miss:
        missing_core.append((os.path.relpath(p, PUB), sorted(miss)))
    test_entrypoint = os.path.join(p, "tests/test.sh")
    if os.path.isfile(test_entrypoint):
        with open(test_entrypoint, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        reasons = []
        if not text.strip():
            reasons.append("empty")
        if not text.startswith("#!"):
            reasons.append("missing shebang")
        if not os.stat(test_entrypoint).st_mode & 0o111:
            reasons.append("not executable")
        if reasons:
            invalid_core.append(
                (os.path.relpath(p, PUB), "tests/test.sh", reasons)
            )
    if any(any(h in e for h in AUDIT) for e in extra):
        audit_leak.append((os.path.relpath(p, PUB), sorted(e for e in extra if any(h in e for h in AUDIT))))
    if extra:
        extras.append((os.path.relpath(p, PUB), sorted(extra)))
    if have == CORE:
        exact += 1

print(f"packages: {len(pkgs)}  exact-core-only: {exact}  with-extras: {len(extras)}")
print(f"MISSING core (FAIL): {len(missing_core)}")
for x in missing_core[:40]:
    print("  MISS", x)
print(f"INVALID core (FAIL): {len(invalid_core)}")
for x in invalid_core[:40]:
    print("  INVALID", x)
print(f"AUDIT/pycache leak (FAIL): {len(audit_leak)}")
for x in audit_leak[:40]:
    print("  LEAK", x)
ok = not missing_core and not invalid_core and not audit_leak
print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
