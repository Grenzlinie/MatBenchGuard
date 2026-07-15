#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: thermodynamic_functions.csv ===
python3 /solution/compute.py csv "${OUTDIR}"/thermodynamic_functions.csv

# === solve block: consistency_check.json ===
python3 /solution/compute.py json "${OUTDIR}"/consistency_check.json
