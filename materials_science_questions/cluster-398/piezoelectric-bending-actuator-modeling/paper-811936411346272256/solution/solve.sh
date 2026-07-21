#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: flat_punch_results.json ===
python3 /solution/generate.py flat

# === solve block: cylindrical_punch_results.json ===
python3 /solution/generate.py cyl

# === solve block: intensity_and_indentation.json ===
python3 /solution/generate.py indent
