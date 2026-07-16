#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagram_data.csv ===
python3 /solution/generate_outputs.py phase_diagram

# === solve block: T0_vs_Ni.csv ===
python3 /solution/generate_outputs.py t0

# === solve block: Ms_vs_Ni.csv ===
python3 /solution/generate_outputs.py ms

# === solve block: enthalpy_vs_Ni.csv ===
python3 /solution/generate_outputs.py enthalpy

# === solve block: stress_rate_vs_Ni.csv ===
python3 /solution/generate_outputs.py stress
