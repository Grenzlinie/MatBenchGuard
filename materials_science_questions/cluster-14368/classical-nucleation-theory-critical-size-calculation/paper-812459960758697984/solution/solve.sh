#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: characteristic_params.json ===
python3 /solution/compute.py characteristic_params.json

# === solve block: psychrometric_temperature.csv ===
python3 /solution/compute.py psychrometric_temperature.csv

# === solve block: droplet_lifetime.csv ===
python3 /solution/compute.py droplet_lifetime.csv
