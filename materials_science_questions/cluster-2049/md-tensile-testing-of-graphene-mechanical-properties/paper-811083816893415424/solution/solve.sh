#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_data.py

# === solve block: step01_energy_strain.csv ===
cp /tmp/step01_energy_strain.csv /app/outputs/step01_energy_strain.csv

# === solve block: step02_derived_properties.json ===
cp /tmp/step02_derived_properties.json /app/outputs/step02_derived_properties.json

# === solve block: step03_band_gap_C.txt ===
cp /tmp/step03_band_gap_C.txt /app/outputs/step03_band_gap_C.txt

# === solve finalize ===
rm -f /tmp/step01_energy_strain.csv /tmp/step02_derived_properties.json /tmp/step03_band_gap_C.txt
