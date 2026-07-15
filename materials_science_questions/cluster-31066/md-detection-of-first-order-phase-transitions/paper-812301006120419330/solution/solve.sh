#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lattice_constants_300K.csv ===
python3 /solution/write_data.py lattice_constants_300K.csv

# === solve block: ca_ratio_vs_T.csv ===
python3 /solution/write_data.py ca_ratio_vs_T.csv

# === solve block: potential_energy_vs_T.csv ===
python3 /solution/write_data.py potential_energy_vs_T.csv
