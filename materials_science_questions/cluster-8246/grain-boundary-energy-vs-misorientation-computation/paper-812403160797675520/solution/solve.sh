#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: intensity_curves.csv ===
mkdir -p "$OUTDIR"
python3 /solution/compute_curves.py "$OUTDIR/intensity_curves.csv"
