#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: simulated_scattered_spectrum.csv ===
# Generate scattered electron spectrum with gap at 140 keV
python3 /solution/generate_spectrum.py > "$OUTDIR/simulated_scattered_spectrum.csv"
