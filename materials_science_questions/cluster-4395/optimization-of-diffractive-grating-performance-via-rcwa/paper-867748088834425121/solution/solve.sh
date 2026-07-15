#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reflectivity_contour.csv ===
python3 /solution/generate.py contour "$OUTDIR/reflectivity_contour.csv"

# === solve block: reflectivity_spectrum.csv ===
python3 /solution/generate.py spectrum "$OUTDIR/reflectivity_spectrum.csv"

# === solve block: angle_scan.csv ===
python3 /solution/generate.py angle "$OUTDIR/angle_scan.csv"
