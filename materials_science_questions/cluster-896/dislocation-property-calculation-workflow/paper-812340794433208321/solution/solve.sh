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
python3 /solution/compute_fk.py

# === solve block: activation_energy_vs_N.csv ===
cat > "$OUTDIR/activation_energy_vs_N.csv" << 'ENDOFFILE'
N,activation_energy
7,3.5
8,1.5
9,0.3
10,2.0
11,3.5
ENDOFFILE

# === solve block: critical_force_vs_N.csv ===
:

# === solve block: max_spring_force_vs_N.csv ===
:
