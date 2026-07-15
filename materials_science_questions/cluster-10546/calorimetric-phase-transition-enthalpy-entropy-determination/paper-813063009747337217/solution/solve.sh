#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: gibbs_free_energies.csv ===
python3 /solution/compute_gibbs.py

# === solve block: stability_summary.txt ===
echo 'Polymer is the most stable phase below 370 K; the freely rotating fcc is the most stable phase above 370 K; the dimer is unstable with respect to the polymer.' > "$OUTDIR/stability_summary.txt"
