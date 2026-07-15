#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: mixed_doses.csv ===
python3 /solution/helper.py "$OUTDIR/mixed_doses.csv"

# === solve block: penelope_doses.csv ===
python3 /solution/helper.py "$OUTDIR/penelope_doses.csv"

# === solve block: lineal_energies.csv ===
python3 /solution/helper.py "$OUTDIR/lineal_energies.csv"
