#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy sympy scipy
python3 /solution/compute.py

# === solve block: structural_coefficients.csv ===
# written inside /solution/compute.py

# === solve block: phase_boundaries.csv ===
# written inside /solution/compute.py
