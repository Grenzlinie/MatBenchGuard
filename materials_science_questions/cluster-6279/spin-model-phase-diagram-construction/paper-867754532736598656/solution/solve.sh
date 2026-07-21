#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_boundary_T0.csv ===
python3 /solution/generate_csv.py phase_boundary_T0 > "$OUTDIR/phase_boundary_T0.csv"

# === solve block: phase_boundary_T0.15.csv ===
python3 /solution/generate_csv.py phase_boundary_T0.15 > "$OUTDIR/phase_boundary_T0.15.csv"

# === solve block: diquark_condensate_mu0.4_Lambda0.8.csv ===
python3 /solution/generate_csv.py diquark_04 > "$OUTDIR/diquark_condensate_mu0.4_Lambda0.8.csv"

# === solve block: diquark_condensate_mu0.8.csv ===
python3 /solution/generate_csv.py diquark_08 > "$OUTDIR/diquark_condensate_mu0.8.csv"
