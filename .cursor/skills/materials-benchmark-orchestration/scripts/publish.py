#!/usr/bin/env python3
"""Assemble clean, publishable Harbor packages into QA_ROOT/_publish.

PASS      -> copy the unchanged source package (from QA_SRC).
REPAIRED  -> copy the clean repaired package (QA_ROOT/<pkg>/candidate).
No audit files are ever included. Strips __pycache__/*.pyc. Resumable
(skips packages already present in _publish).

Env:
  QA_ROOT  work/output root (default: /personal/qa_review)
  QA_SRC   read-only source corpus root (required for PASS packages)
"""
import json, glob, os, shutil

ROOT = os.environ.get("QA_ROOT", "/personal/qa_review")
SRC = os.environ.get("QA_SRC") or json.load(open(os.path.join(ROOT, "corpus_manifest.json"))).get("src_root")
PUB = os.path.join(ROOT, "_publish")
os.chdir(ROOT)
os.makedirs(PUB, exist_ok=True)

pass_pkgs, repaired_pkgs = [], []
for f in glob.glob("**/agent_final_decision.json", recursive=True):
    if "/candidate/" in f or "/snapshot/" in f or f.startswith("_publish/"):
        continue
    pkg = os.path.dirname(f)
    if not os.path.exists(os.path.join(pkg, ".done")):
        continue
    try:
        d = json.load(open(f))
    except Exception:
        continue
    outcome = None
    rr = os.path.join(pkg, "repair_report.json")
    if os.path.exists(rr):
        try:
            outcome = json.load(open(rr)).get("outcome")
        except Exception:
            pass
    if outcome == "REPAIRED":
        repaired_pkgs.append(pkg)
    elif d.get("verdict") == "PASS":
        pass_pkgs.append(pkg)


def strip_artifacts(root):
    for r, dirs, files in os.walk(root):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(r, "__pycache__"), ignore_errors=True)
            dirs.remove("__pycache__")
        for fn in files:
            if fn.endswith(".pyc"):
                os.remove(os.path.join(r, fn))


def copy_pkg(srcdir, pkg):
    dst = os.path.join(PUB, pkg)
    if os.path.isdir(dst):
        return "skip"
    if not os.path.isdir(srcdir):
        return "missing"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    tmp = dst + ".tmp"
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)
    shutil.copytree(srcdir, tmp)
    strip_artifacts(tmp)
    os.replace(tmp, dst)
    return "ok"


stats = {"ok": 0, "skip": 0, "missing": 0}
for pkg in pass_pkgs:
    stats[copy_pkg(os.path.join(SRC, pkg), pkg)] += 1
for pkg in repaired_pkgs:
    stats[copy_pkg(os.path.join(pkg, "candidate"), pkg)] += 1

open(os.path.join(PUB, "_PUBLISH_MANIFEST.txt"), "w").write(
    f"publishable_total={len(pass_pkgs)+len(repaired_pkgs)}\n"
    f"pass_as_is={len(pass_pkgs)}\nrepaired={len(repaired_pkgs)}\n"
    f"copied_ok={stats['ok']} skipped_existing={stats['skip']} missing_src={stats['missing']}\n"
    "PASS = unchanged source package; REPAIRED = clean repaired package "
    "(QA_ROOT/<pkg>/candidate). No audit files; __pycache__ stripped.\n")
print("pass:", len(pass_pkgs), "repaired:", len(repaired_pkgs), "stats:", stats)
