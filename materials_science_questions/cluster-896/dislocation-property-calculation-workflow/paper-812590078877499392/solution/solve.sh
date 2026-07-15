#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: vacancy_results.json ===
python3 /solution/gen_outputs.py vacancy_results.json

# === solve block: dislocation_results.json ===
python3 /solution/gen_outputs.py dislocation_results.json

# === solve block: angular_correlation_vacancy.csv ===
python3 /solution/gen_outputs.py angular_correlation_vacancy.csv

# === solve block: angular_correlation_dislocation_z.csv ===
python3 /solution/gen_outputs.py angular_correlation_dislocation_z.csv

# === solve block: angular_correlation_dislocation_x.csv ===
python3 /solution/gen_outputs.py angular_correlation_dislocation_x.csv

# === solve block: angular_correlation_dislocation_y.csv ===
python3 /solution/gen_outputs.py angular_correlation_dislocation_y.csv
