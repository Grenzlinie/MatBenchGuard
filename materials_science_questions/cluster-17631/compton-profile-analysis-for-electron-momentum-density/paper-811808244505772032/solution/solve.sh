#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
chmod +x /solution/gen.py

# === solve block: compton_profiles.csv ===
python3 /solution/gen.py compton

# === solve block: acar_profiles.csv ===
python3 /solution/gen.py acar

# === solve block: anisotropy_cp.csv ===
python3 /solution/gen.py anisotropy_cp

# === solve block: anisotropy_acar.csv ===
python3 /solution/gen.py anisotropy_acar
