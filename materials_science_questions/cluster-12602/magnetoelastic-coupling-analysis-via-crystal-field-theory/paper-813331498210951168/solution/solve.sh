#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: quadrupole_susceptibilities.csv ===
python3 /solution/helper.py susceptibilities /app/outputs

# === solve block: elastic_constants.csv ===
python3 /solution/helper.py elastic /app/outputs
