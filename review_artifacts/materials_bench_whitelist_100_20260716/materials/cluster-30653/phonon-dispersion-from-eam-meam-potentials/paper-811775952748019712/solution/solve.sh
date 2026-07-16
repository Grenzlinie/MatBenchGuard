#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: liquid_properties.csv ===
python3 /solution/write_outputs.py liquid_properties.csv

# === solve block: crystal_properties.csv ===
python3 /solution/write_outputs.py crystal_properties.csv

# === solve block: shock_hugoniot.csv ===
python3 /solution/write_outputs.py shock_hugoniot.csv

# === solve block: melting_temperatures.csv ===
python3 /solution/write_outputs.py melting_temperatures.csv
