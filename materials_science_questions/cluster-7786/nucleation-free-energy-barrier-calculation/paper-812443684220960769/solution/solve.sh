#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_albon_dunning_curve.csv ===
python3 /solution/generate_outputs.py step_01

# === solve block: step_02_cabrera_vermilyea_curve.csv ===
python3 /solution/generate_outputs.py step_02

# === solve block: step_03_conclusion.txt ===
echo 'No plateau region observed in any of the calculated curves.' > /app/outputs/step_03_conclusion.txt
