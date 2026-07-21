#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
echo 'Oracle solve.sh starting...'

# === solve block: specific_heat_maxima.csv ===
python3 /solution/generate_csv.py specific_heat /app/outputs/specific_heat_maxima.csv

# === solve block: susceptibility_maxima.csv ===
python3 /solution/generate_csv.py susceptibility /app/outputs/susceptibility_maxima.csv

# === solve block: phase_diagram_points.csv ===
python3 /solution/generate_csv.py phase_diagram /app/outputs/phase_diagram_points.csv

# === solve finalize ===
echo 'All oracle artifacts written.'
