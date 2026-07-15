#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: h_vs_t.csv ===
python3 /solution/write_h_vs_t.py

# === solve block: ratios.csv ===
python3 /solution/write_ratios.py
