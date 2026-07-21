#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_radii.csv ===
python3 /solution/solver.py critical_radii "$OUTDIR"

# === solve block: coherent_energy_validation.json ===
python3 /solution/solver.py validation_energy "$OUTDIR"
