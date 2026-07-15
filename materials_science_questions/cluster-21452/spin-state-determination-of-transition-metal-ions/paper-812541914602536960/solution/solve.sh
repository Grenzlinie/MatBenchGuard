#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_chiT_values.csv ===
python3 /solution/compute_chiT.py "$OUTDIR/step_01_chiT_values.csv" && sed -i '1i compound,T,chiT' "$OUTDIR/step_01_chiT_values.csv"
