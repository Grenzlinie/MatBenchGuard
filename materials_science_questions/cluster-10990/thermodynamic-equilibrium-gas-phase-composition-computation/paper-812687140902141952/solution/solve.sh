#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_phase_boundary.csv ===
python3 /solution/compute_curve.py /app/outputs phase

# === solve block: step_02_covering_ratio.csv ===
python3 /solution/compute_curve.py /app/outputs cover
