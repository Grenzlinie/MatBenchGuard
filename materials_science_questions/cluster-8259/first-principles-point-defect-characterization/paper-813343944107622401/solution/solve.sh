#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy ase

# === solve block: 66-sph-1_final.xyz ===
python3 /solution/generate_outputs.py "$OUTDIR"

# === solve block: 66-sup_final.xyz ===
python3 /solution/generate_outputs.py "$OUTDIR"

# === solve block: coordination_errors.json ===
python3 /solution/generate_outputs.py "$OUTDIR"
