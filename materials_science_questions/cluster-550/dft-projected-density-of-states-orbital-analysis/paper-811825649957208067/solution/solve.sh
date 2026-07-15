#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/gen_data.py

# === solve block: band_gap_CuAlS2.txt ===
echo '1.94' > "$OUTDIR/band_gap_CuAlS2.txt"

# === solve block: dos_total_CuAlS2.csv ===
:  # written by gen_data.py

# === solve block: dos_partial_CuAlS2.csv ===
:  # written by gen_data.py

# === solve block: dielectric_function_CuAlS2.csv ===
:  # written by gen_data.py

# === solve block: refractive_index_CuAlS2.txt ===
echo '2.26' > "$OUTDIR/refractive_index_CuAlS2.txt"
