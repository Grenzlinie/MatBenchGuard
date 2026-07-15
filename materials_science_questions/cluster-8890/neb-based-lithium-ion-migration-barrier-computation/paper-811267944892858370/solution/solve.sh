#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
python3 /solution/write_outputs.py --type binding --outfile /app/outputs/binding_energies.csv

# === solve block: diffusion_barriers.csv ===
python3 /solution/write_outputs.py --type barrier --outfile /app/outputs/diffusion_barriers.csv
