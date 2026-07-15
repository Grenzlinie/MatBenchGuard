#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: breaking_forces.csv ===
python3 /solution/generate_outputs.py --csv > /app/outputs/breaking_forces.csv

# === solve block: energy_curves.json ===
python3 /solution/generate_outputs.py --json > /app/outputs/energy_curves.json
