#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_aggregate_data.csv ===
python3 /solution/generate_csv.py step01

# === solve block: step_02_bending_trend.csv ===
python3 /solution/generate_csv.py step02
