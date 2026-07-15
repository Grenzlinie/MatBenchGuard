#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_structural_properties.csv ===
python3 /solution/generate_outputs.py structural_properties

# === solve block: step_02_transition_pressure.txt ===
python3 /solution/generate_outputs.py transition_pressure

# === solve block: step_03_piezoelectric_e33.txt ===
python3 /solution/generate_outputs.py piezoelectric

# === solve block: step_04_phonon_frequency.csv ===
python3 /solution/generate_outputs.py phonon_frequency
