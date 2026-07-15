#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy  # needed only if we use numpy; we'll avoid it

# === solve block: dcs_delta_si.csv ===
# Generate ΔDCS CSV using helper
python3 /solution/generate_dcs_delta.py

# === solve block: eta_na_si.csv ===
# Generate η_na CSV using helper
python3 /solution/generate_eta_na.py

# === solve block: eta_mt_si.csv ===
# Generate η_mt CSV using helper
python3 /solution/generate_eta_mt.py
