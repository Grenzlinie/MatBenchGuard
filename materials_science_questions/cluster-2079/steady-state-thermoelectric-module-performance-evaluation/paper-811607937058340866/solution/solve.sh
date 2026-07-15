#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_figure1_data.csv ===
python3 /solution/compute.py step1

# === solve block: step_02_figure2_data.csv ===
python3 /solution/compute.py step2
