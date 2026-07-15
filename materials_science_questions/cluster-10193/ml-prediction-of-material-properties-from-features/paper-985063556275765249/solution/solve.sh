#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_regression_predictions.csv ===
python3 /solution/generate_oracle_data.py step_01 > /app/outputs/step_01_regression_predictions.csv

# === solve block: step_02_classification_predictions_true_energies.csv ===
python3 /solution/generate_oracle_data.py step_02 > /app/outputs/step_02_classification_predictions_true_energies.csv

# === solve block: step_03_classification_predictions_predicted_energies.csv ===
python3 /solution/generate_oracle_data.py step_03 > /app/outputs/step_03_classification_predictions_predicted_energies.csv
