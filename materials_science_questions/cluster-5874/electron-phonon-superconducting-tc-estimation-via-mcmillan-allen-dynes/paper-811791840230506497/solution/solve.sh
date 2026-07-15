#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: enthalpy_curves.csv ===
python3 /solution/generate_assets.py enthalpy > /app/outputs/enthalpy_curves.csv

# === solve block: C2_c_relaxed.cif ===
python3 /solution/generate_assets.py c2c_cif > /app/outputs/C2_c_relaxed.cif

# === solve block: P2_1_c_relaxed.cif ===
python3 /solution/generate_assets.py p21c_cif > /app/outputs/P2_1_c_relaxed.cif

# === solve block: tc_at_45GPa.txt ===
python3 /solution/generate_assets.py tc > /app/outputs/tc_at_45GPa.txt
