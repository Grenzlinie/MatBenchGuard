#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: raman_spectrum_2.33eV.csv ===
python3 /solution/generate_spectra.py full_spectrum

# === solve block: overtone_only_2D_contribution.csv ===
python3 /solution/generate_spectra.py overtone_2D

# === solve block: extracted_peak_positions.json ===
python3 /solution/generate_spectra.py extract_peaks
