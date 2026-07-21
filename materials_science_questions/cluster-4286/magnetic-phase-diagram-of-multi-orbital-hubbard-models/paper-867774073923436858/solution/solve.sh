#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phase_diagram.csv ===
python3 /solution/helper.py phase

# === solve block: ldos_anderson_zeroT.csv ===
python3 /solution/helper.py ldos_anderson_zeroT

# === solve block: ldos_finite_td.csv ===
python3 /solution/helper.py ldos_finite_td

# === solve block: ldos_anderson_broadened.csv ===
python3 /solution/helper.py ldos_anderson_broadened

# === solve block: width_vs_T.csv ===
python3 /solution/helper.py width_vs_T
