#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy || true
mkdir -p /app/outputs

# === solve block: monometallic_optimized_geometry.xyz ===
python3 /solution/gen_outputs.py

# === solve block: bimetallic_optimized_geometry.xyz ===
python3 /solution/gen_outputs.py

# === solve block: structural_parameters.json ===
python3 /solution/gen_outputs.py
