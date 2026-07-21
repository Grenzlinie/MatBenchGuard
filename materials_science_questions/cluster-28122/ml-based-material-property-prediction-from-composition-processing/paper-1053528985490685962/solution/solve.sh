#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_anova_contributions.csv ===
python3 /solution/create_artifacts.py step_01_anova_contributions.csv

# === solve block: step_02_nsga2_optimal.csv ===
python3 /solution/create_artifacts.py step_02_nsga2_optimal.csv

# === solve block: step_03_ml_metrics.csv ===
python3 /solution/create_artifacts.py step_03_ml_metrics.csv
