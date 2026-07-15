#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: tbc_observables.csv ===
python3 /solution/generate_observables.py

# === solve block: sbc_observables.csv ===
python3 /solution/generate_observables.py
