#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_data_h0p125.csv ===
python3 /solution/generate_grid.py 0.125 > "$OUTDIR/phase_data_h0p125.csv"

# === solve block: phase_data_h0p35.csv ===
python3 /solution/generate_grid.py 0.35 > "$OUTDIR/phase_data_h0p35.csv"

# === solve block: phase_data_h0p375.csv ===
python3 /solution/generate_grid.py 0.375 > "$OUTDIR/phase_data_h0p375.csv"

# === solve block: phase_data_h1p3.csv ===
python3 /solution/generate_grid.py 1.3 > "$OUTDIR/phase_data_h1p3.csv"

# === solve block: phase_data_h1p5.csv ===
python3 /solution/generate_grid.py 1.5 > "$OUTDIR/phase_data_h1p5.csv"
