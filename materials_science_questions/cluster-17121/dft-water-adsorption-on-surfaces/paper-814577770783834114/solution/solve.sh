#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: density_profile.csv ===
python3 /solution/generate_density.py /app/outputs/density_profile.csv

# === solve block: vibrational_dos_oxygen.csv ===
python3 /solution/generate_dos.py oxygen /app/outputs/vibrational_dos_oxygen.csv

# === solve block: vibrational_dos_hydrogen.csv ===
python3 /solution/generate_dos.py hydrogen /app/outputs/vibrational_dos_hydrogen.csv
