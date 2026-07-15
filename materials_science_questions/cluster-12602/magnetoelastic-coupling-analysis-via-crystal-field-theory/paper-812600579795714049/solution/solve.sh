#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute_susceptibilities.py --temp-min 5 --temp-max 100 --num-temp 100 --output-dir "$OUTDIR"

# === solve block: chi_M1.csv ===
echo 'chi_M1.csv already written by compute_susceptibilities.py'

# === solve block: chi_M3.csv ===
echo 'chi_M3.csv already written by compute_susceptibilities.py'
