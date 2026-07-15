#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_displacements.csv ===
python3 /solution/write_outputs.py step_01_displacements.csv

# === solve block: step_02_surface_params.csv ===
python3 /solution/write_outputs.py step_02_surface_params.csv

# === solve block: step_03_energy_scans.csv ===
python3 /solution/write_outputs.py step_03_energy_scans.csv

# === solve block: step_04_band_gap.csv ===
python3 /solution/write_outputs.py step_04_band_gap.csv
