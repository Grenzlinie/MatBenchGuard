#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pure_band_dos.json ===
python3 /solution/generate_artifacts.py pure_band_dos > "$OUTDIR/pure_band_dos.json"

# === solve block: doped_band_dos.json ===
python3 /solution/generate_artifacts.py doped_band_dos > "$OUTDIR/doped_band_dos.json"

# === solve block: mulliken_charges_table.csv ===
python3 /solution/generate_artifacts.py mulliken_charges > "$OUTDIR/mulliken_charges_table.csv"

# === solve block: v_orbital_populations.csv ===
python3 /solution/generate_artifacts.py v_orbital_populations > "$OUTDIR/v_orbital_populations.csv"
