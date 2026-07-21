#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_chi_peak.json ===
python3 /solution/generate_outputs.py step_01_chi_peak.json

# === solve block: step_02_pairing_suscept.json ===
python3 /solution/generate_outputs.py step_02_pairing_suscept.json

# === solve block: step_03_AFM_structure_factor.json ===
python3 /solution/generate_outputs.py step_03_AFM_structure_factor.json

# === solve block: step_04_CDW_charge_correlation.json ===
python3 /solution/generate_outputs.py step_04_CDW_charge_correlation.json
