#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: zero_T_phases.csv ===
python3 /solution/make_outputs.py /app/outputs/zero_T_phases.csv

# === solve block: transition_temperatures.csv ===
python3 /solution/make_outputs.py /app/outputs/transition_temperatures.csv

# === solve block: susceptibility_trend.csv ===
python3 /solution/make_outputs.py /app/outputs/susceptibility_trend.csv
