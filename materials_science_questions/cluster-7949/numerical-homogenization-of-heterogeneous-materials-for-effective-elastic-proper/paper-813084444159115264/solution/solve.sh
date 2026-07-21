#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/compute.py

# === solve block: effective_stiffness_matrix.json ===
# effective_stiffness_matrix.json is already written by /solution/compute.py

# === solve block: validation_summary.json ===
# already written by compute.py
