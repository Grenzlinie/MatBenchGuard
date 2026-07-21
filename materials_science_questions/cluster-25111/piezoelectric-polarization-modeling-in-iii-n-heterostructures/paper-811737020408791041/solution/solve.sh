#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lateral_energies.csv ===
python3 /solution/gen.py lateral > /app/outputs/lateral_energies.csv

# === solve block: vertical_energies.csv ===
python3 /solution/gen.py vertical > /app/outputs/vertical_energies.csv

# === solve block: angle_energies.csv ===
python3 /solution/gen.py angle > /app/outputs/angle_energies.csv

# === solve block: fit_params.json ===
python3 /solution/gen.py fit > /app/outputs/fit_params.json
