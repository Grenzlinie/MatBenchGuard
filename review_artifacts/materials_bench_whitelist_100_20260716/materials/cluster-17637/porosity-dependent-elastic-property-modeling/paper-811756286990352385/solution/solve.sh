#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_stress_strain_comparison.csv ===
python3 /solution/generate_data.py step01 /app/outputs/step_01_stress_strain_comparison.csv

# === solve block: step_02_stress_strain_porosity.csv ===
python3 /solution/generate_data.py step02 /app/outputs/step_02_stress_strain_porosity.csv
