#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: coulomb_coefficients.csv ===
python3 /solution/ewald.py coulomb

# === solve block: stiffness_dispersion.csv ===
python3 /solution/ewald.py stiffness
