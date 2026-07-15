#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_properties.csv ===
python3 /solution/compute_properties.py --mode=properties --output="$OUTDIR/step_01_properties.csv"

# === solve block: step_02_kappa_vs_T.csv ===
python3 /solution/compute_properties.py --mode=kappavst --output="$OUTDIR/step_02_kappa_vs_T.csv"
