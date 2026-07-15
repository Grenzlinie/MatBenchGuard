#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: bulk_ZT_vs_EF.csv ===
python3 /solution/compute_zt.py bulk

# === solve block: surface_ZT_vs_EF.csv ===
python3 /solution/compute_zt.py surface

# === solve block: nanowire_ZT_opt.csv ===
python3 /solution/compute_zt.py nanowire
