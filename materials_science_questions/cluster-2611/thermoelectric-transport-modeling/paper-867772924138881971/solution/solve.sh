#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: conductivity_mobility.csv ===
printf 'material,conductivity_e2h,mobility_cm2Vs\nInSe-e,20.0,490.0\nP4-h,36.0,640.0\n' > "$OUTDIR/conductivity_mobility.csv"
