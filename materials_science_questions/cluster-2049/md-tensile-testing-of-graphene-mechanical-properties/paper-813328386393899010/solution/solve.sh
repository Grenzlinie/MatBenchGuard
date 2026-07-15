#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: buckling_strains.csv ===
python3 /solution/write_outputs.py buckling

# === solve block: free_energy_minima.csv ===
python3 /solution/write_outputs.py free_energy

# === solve block: shape_profiles.csv ===
python3 /solution/write_outputs.py shape
