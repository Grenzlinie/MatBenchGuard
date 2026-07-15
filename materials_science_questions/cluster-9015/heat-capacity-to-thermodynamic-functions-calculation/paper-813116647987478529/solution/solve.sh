#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
echo '[Oracle] Writing reference thermodynamic tables...'

# === solve block: thermo_functions_mix1.csv ===
python3 /solution/generate_thermo.py 1 > "$OUTDIR/thermo_functions_mix1.csv"

# === solve block: thermo_functions_mix2.csv ===
python3 /solution/generate_thermo.py 2 > "$OUTDIR/thermo_functions_mix2.csv"

# === solve block: thermo_functions_mix3.csv ===
python3 /solution/generate_thermo.py 3 > "$OUTDIR/thermo_functions_mix3.csv"
