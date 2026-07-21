#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: order_parameters.csv ===
python3 /solution/generate_outputs.py --output "$OUTDIR/order_parameters.csv" --mode order_params

# === solve block: phase_diagram.csv ===
python3 /solution/generate_outputs.py --output "$OUTDIR/phase_diagram.csv" --mode phase_diagram --input "$OUTDIR/order_parameters.csv"

# === solve block: fermi_dispersions.json ===
python3 /solution/generate_outputs.py --output "$OUTDIR/fermi_dispersions.json" --mode fermi_dispersions --input "$OUTDIR/order_parameters.csv"
