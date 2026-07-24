#!/usr/bin/env python3
"""Build corpus_manifest.json + init state dir from a source corpus root.

A "package" is any directory that directly contains instruction.md AND task.toml
(the Harbor package leaf). Package ids are stored relative to QA_SRC so they map
1:1 to both the read-only source and the QA_ROOT output tree.

Env:
  QA_SRC   read-only source corpus root (required)
  QA_ROOT  work/output root (default: /personal/qa_review)
"""
import json, os

SRC = os.environ["QA_SRC"]
ROOT = os.environ.get("QA_ROOT", "/personal/qa_review")

pkgs = []
for r, d, files in os.walk(SRC):
    if "instruction.md" in files and "task.toml" in files:
        pkgs.append(os.path.relpath(r, SRC))
pkgs.sort()

os.makedirs(ROOT, exist_ok=True)
os.makedirs(os.path.join(ROOT, "state"), exist_ok=True)
with open(os.path.join(ROOT, "corpus_manifest.json"), "w") as f:
    json.dump({"src_root": SRC, "packages": pkgs}, f, indent=0)
for name in ("assigned.json", "done.json"):
    p = os.path.join(ROOT, "state", name)
    if not os.path.exists(p):
        json.dump({}, open(p, "w"))
print(f"manifest: {len(pkgs)} packages -> {ROOT}/corpus_manifest.json")
