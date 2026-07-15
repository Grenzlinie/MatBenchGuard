#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gap_absi.txt ===
echo '2.58' > /app/outputs/band_gap_absi.txt

# === solve block: shg_powder_absi.txt ===
echo '1.81' > /app/outputs/shg_powder_absi.txt

# === solve block: shg_d22_absi.txt ===
echo '2.87' > /app/outputs/shg_d22_absi.txt

# === solve block: shg_powder_abi.txt ===
echo '1.27' > /app/outputs/shg_powder_abi.txt
