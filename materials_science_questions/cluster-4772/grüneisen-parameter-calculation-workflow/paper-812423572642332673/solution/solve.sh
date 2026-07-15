#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phonon_results.csv ===
python3 /solution/write_phonon_results.py "$OUTDIR"

# === solve block: thermodynamic_results.csv ===
python3 /solution/write_thermo_results.py "$OUTDIR"
