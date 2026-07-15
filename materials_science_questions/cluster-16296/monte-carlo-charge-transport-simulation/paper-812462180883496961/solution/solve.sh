#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: drift_velocity_E20_T10.csv ===
python3 /solution/write_csv.py /app/outputs/drift_velocity_E20_T10.csv 20 10

# === solve block: drift_velocity_E40_T10.csv ===
python3 /solution/write_csv.py /app/outputs/drift_velocity_E40_T10.csv 40 10

# === solve block: drift_velocity_E60_T10.csv ===
python3 /solution/write_csv.py /app/outputs/drift_velocity_E60_T10.csv 60 10

# === solve block: drift_velocity_E60_T300.csv ===
python3 /solution/write_csv.py /app/outputs/drift_velocity_E60_T300.csv 60 300
