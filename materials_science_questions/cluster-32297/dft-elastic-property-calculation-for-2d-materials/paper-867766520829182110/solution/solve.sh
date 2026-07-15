#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: structural_properties.json ===
python3 /solution/write_outputs.py structural

# === solve block: electronic_properties.json ===
python3 /solution/write_outputs.py electronic

# === solve block: mechanical_properties.json ===
python3 /solution/write_outputs.py mechanical

# === solve block: dielectric_properties.json ===
python3 /solution/write_outputs.py dielectric
