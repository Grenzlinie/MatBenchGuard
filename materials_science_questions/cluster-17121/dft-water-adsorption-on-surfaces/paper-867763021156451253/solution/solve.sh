#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: global_minimum_energies.csv ===
python3 /solution/write_energies.py

# === solve block: monomer_orientation.txt ===
python3 /solution/write_monomer.py
