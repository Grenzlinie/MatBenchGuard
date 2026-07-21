#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetization_low_energy.csv ===
python3 /solution/generate_csv.py low /app/outputs/magnetization_low_energy.csv

# === solve block: magnetization_high_energy.csv ===
python3 /solution/generate_csv.py high /app/outputs/magnetization_high_energy.csv

# === solve finalize ===
echo "All outputs written."
