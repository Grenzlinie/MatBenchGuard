#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: valley_populations.csv ===
python3 /solution/generate_outputs.py valley_populations /app/outputs/valley_populations.csv

# === solve block: lo_phonon_spectrum_2ps.csv ===
python3 /solution/generate_outputs.py spectrum_2ps /app/outputs/lo_phonon_spectrum_2ps.csv

# === solve block: lo_phonon_spectrum_2_5ps.csv ===
python3 /solution/generate_outputs.py spectrum_2_5ps /app/outputs/lo_phonon_spectrum_2_5ps.csv
