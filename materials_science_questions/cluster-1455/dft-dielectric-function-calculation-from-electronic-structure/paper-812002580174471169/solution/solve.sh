#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
pip install -q --no-cache-dir numpy

# === solve block: spectra.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple 'numpy<2' && python3 /solution/gen_spectra.py
