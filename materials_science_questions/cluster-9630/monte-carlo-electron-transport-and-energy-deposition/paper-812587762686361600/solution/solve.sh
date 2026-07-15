#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/generate.py

# === solve block: trapped_charge_profile_5keV.csv ===
true

# === solve block: surface_potential_time_series_5keV.csv ===
true

# === solve block: trapped_charge_profile_10keV.csv ===
true

# === solve block: surface_potential_time_series_10keV.csv ===
true
