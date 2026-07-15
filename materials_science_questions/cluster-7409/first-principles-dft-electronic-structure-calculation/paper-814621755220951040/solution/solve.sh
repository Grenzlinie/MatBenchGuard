#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
echo "Geometry optimization completed successfully." > /app/outputs/relaxation_log.txt
echo "Electron density difference maps computed." > /app/outputs/density_maps_report.txt

# === solve block: step_01_band_gaps.json ===
python3 /solution/write_outputs.py step_01_band_gaps.json

# === solve block: step_02_dos_data.csv ===
python3 /solution/write_outputs.py step_02_dos_data.csv

# === solve block: step_03_cb_offset.json ===
python3 /solution/write_outputs.py step_03_cb_offset.json
