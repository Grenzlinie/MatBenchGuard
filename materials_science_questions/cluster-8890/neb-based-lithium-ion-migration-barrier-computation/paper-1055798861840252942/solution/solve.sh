#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: acd_z_profile.csv ===
python3 /solution/generate_acd.py z /app/outputs/acd_z_profile.csv

# === solve block: acd_x_profile.csv ===
python3 /solution/generate_acd.py x /app/outputs/acd_x_profile.csv
