#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies_and_masses.csv ===
python3 /solution/generate_energies.py

# === solve block: local_properties.csv ===
python3 /solution/generate_local.py
