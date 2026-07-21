#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: poles_all_N.csv ===
python3 /solution/run.py

# === solve block: transmission_coefficient_N.csv ===
echo 'written by previous step'

# === solve block: band_edges_comparison.csv ===
echo 'written by previous step'
