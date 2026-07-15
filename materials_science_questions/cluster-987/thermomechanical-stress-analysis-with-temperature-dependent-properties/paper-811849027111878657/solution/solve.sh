#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: temperature_time.csv ===
cp /solution/temperature_time.csv "$OUTDIR/temperature_time.csv"

# === solve block: stress_strain.csv ===
cp /solution/stress_strain.csv "$OUTDIR/stress_strain.csv"

# === solve finalize ===
echo "All outputs written."
