#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/compute.py

# === solve block: dispersion_curves.csv ===
echo -n

# === solve block: absorption_ideal.csv ===
echo -n

# === solve block: absorption_pure_ZnTe.csv ===
echo -n

# === solve block: absorption_CdZnTe.csv ===
echo -n

# === solve finalize ===
echo 'All artifacts written.'
