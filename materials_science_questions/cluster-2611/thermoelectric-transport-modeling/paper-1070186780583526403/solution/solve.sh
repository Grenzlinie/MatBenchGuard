#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_mu_T.csv ===
python3 /solution/generate_data.py step_01 > "/app/outputs/step_01_mu_T.csv"

# === solve block: step_02_resistivity_zero_field.csv ===
python3 /solution/generate_data.py step_02 > "/app/outputs/step_02_resistivity_zero_field.csv"

# === solve block: step_03_hall_resistivity.csv ===
python3 /solution/generate_data.py step_03 > "/app/outputs/step_03_hall_resistivity.csv"

# === solve block: step_04_magnetoresistance.csv ===
python3 /solution/generate_data.py step_04 > "/app/outputs/step_04_magnetoresistance.csv"
