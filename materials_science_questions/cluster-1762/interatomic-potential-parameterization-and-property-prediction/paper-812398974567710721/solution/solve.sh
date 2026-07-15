#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: fig4_relative_energies.csv ===
python3 /solution/generate_outputs.py fig4 "$OUTDIR/fig4_relative_energies.csv"

# === solve block: fig5_relative_energies.csv ===
python3 /solution/generate_outputs.py fig5 "$OUTDIR/fig5_relative_energies.csv"
