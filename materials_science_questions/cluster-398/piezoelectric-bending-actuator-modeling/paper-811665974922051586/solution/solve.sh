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
python3 /solution/simulate.py "$OUTDIR"

# === solve block: strain_vs_E.csv ===
[ -f "$OUTDIR/strain_vs_E.csv" ]

# === solve block: max_strain_vs_thickness.csv ===
[ -f "$OUTDIR/max_strain_vs_thickness.csv" ]
