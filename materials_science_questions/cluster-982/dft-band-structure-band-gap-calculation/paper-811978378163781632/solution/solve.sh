#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -e
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/generate_outputs.py

# === solve block: dos.dat ===
true

# === solve block: band_gap.txt ===
true
