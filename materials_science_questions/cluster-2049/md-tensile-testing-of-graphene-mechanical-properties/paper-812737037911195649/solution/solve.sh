#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: energy_vs_curvature.csv ===
python3 /solution/spring_slider.py --output-csv /app/outputs/energy_vs_curvature.csv

# === solve block: critical_condition.txt ===
python3 /solution/spring_slider.py --output-txt /app/outputs/critical_condition.txt
