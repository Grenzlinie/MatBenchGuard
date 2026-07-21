#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: sb_bts_band_structure.csv ===
python3 /solution/compute_bands.py /app/outputs/sb_bts_band_structure.csv sb

# === solve block: bi_bts_band_structure.csv ===
python3 /solution/compute_bands.py /app/outputs/bi_bts_band_structure.csv bi
