#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: concentrations_variable.csv ===
python3 /solution/generate_data.py --output concentrations_variable.csv

# === solve block: concentrations_fixed.csv ===
python3 /solution/generate_data.py --output concentrations_fixed.csv

# === solve block: magnetization.csv ===
python3 /solution/generate_data.py --output magnetization.csv
