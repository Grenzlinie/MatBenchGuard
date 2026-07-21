#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: w0_values.json ===
python3 /solution/compute.py w0

# === solve block: free_energy_difference.csv ===
python3 /solution/compute.py energy
