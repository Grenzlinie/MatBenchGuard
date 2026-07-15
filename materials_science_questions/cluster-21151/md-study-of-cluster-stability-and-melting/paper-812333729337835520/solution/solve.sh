#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_power_spectrum_xe55.csv ===
python3 /solution/generate_spectra.py xe55 /app/outputs/step_01_power_spectrum_xe55.csv

# === solve block: step_02_power_spectrum_ar_arxexe.csv ===
python3 /solution/generate_spectra.py ar_arxe /app/outputs/step_02_power_spectrum_ar_arxexe.csv

# === solve block: step_03_power_spectrum_xe_arxexe.csv ===
python3 /solution/generate_spectra.py xe_arxe /app/outputs/step_03_power_spectrum_xe_arxexe.csv
