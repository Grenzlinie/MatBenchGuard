#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p /app/outputs /tmp/outputs
python3 /solution/generate_all_outputs.py

# === solve block: dielectric_function_Nb3O7OH.csv ===
cp /tmp/outputs/dielectric_function_Nb3O7OH.csv "$OUTDIR/dielectric_function_Nb3O7OH.csv"

# === solve block: dielectric_function_HNb2O5.csv ===
cp /tmp/outputs/dielectric_function_HNb2O5.csv "$OUTDIR/dielectric_function_HNb2O5.csv"

# === solve block: optical_conductivity_Nb3O7OH.csv ===
cp /tmp/outputs/optical_conductivity_Nb3O7OH.csv "$OUTDIR/optical_conductivity_Nb3O7OH.csv"

# === solve block: optical_conductivity_HNb2O5.csv ===
cp /tmp/outputs/optical_conductivity_HNb2O5.csv "$OUTDIR/optical_conductivity_HNb2O5.csv"

# === solve block: summary_values.json ===
cp /tmp/outputs/summary_values.json "$OUTDIR/summary_values.json"
