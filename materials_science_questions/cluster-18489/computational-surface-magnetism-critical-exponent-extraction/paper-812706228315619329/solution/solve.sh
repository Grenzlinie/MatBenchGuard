#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: mt_data.csv ===
python3 /solution/gen_data.py --mt > "$OUTDIR/mt_data.csv"

# === solve block: mh_data.csv ===
python3 /solution/gen_data.py --mh > "$OUTDIR/mh_data.csv"

# === solve block: summary.json ===
python3 /solution/gen_data.py --summary > "$OUTDIR/summary.json"
