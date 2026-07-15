#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pristine_GB_formation_energy.txt ===
echo "0.05" > "$OUTDIR/pristine_GB_formation_energy.txt"

# === solve block: segregation_energies.csv ===
python3 /solution/generate_csv.py "$OUTDIR/segregation_energies.csv"
