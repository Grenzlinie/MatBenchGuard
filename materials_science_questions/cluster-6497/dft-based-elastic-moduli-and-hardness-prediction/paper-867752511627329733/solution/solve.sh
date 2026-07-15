#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_constants_pressure.csv ===
python3 /solution/gen.py elastic_constants_pressure

# === solve block: anisotropy.csv ===
python3 /solution/gen.py anisotropy

# === solve block: c44_temperature.csv ===
python3 /solution/gen.py c44_temperature

# === solve block: rh_elastic_moduli.csv ===
python3 /solution/gen.py rh_elastic_moduli

# === solve finalize ===
echo 'All reference outputs generated.'
