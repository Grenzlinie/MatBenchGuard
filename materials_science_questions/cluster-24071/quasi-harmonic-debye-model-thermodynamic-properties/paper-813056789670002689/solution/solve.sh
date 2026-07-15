#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_e_v_data.csv ===
python3 /solution/generate_data.py /app/outputs/step_01_e_v_data.csv

# === solve block: step_02_dielectric_function.csv ===
python3 /solution/generate_data.py /app/outputs/step_02_dielectric_function.csv

# === solve block: step_03_thermal_properties.csv ===
python3 /solution/generate_data.py /app/outputs/step_03_thermal_properties.csv

# === solve block: results.json ===
python3 /solution/generate_data.py /app/outputs/results.json
