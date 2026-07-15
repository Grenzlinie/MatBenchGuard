#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: order_params_p06.csv ===
python3 /solution/gen.py order_params_p06.csv

# === solve block: ocf_data_p06.csv ===
python3 /solution/gen.py ocf_data_p06.csv

# === solve block: melting_line.csv ===
python3 /solution/gen.py melting_line.csv

# === solve block: structural_anomaly.csv ===
python3 /solution/gen.py structural_anomaly.csv
