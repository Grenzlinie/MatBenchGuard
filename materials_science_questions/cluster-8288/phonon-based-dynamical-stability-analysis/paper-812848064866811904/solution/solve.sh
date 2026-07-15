#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy h5py
python3 /solution/generate_outputs.py

# === solve block: lattice_constants.csv ===
:

# === solve block: absorption_onsets.csv ===
:

# === solve block: static_refractive_index.csv ===
:

# === solve block: plasmon_peak_energies.csv ===
:
