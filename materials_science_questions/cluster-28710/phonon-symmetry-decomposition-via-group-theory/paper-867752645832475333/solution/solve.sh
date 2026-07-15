#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: space_groups.json ===
mkdir -p /app/outputs
python3 /solution/generate.py space_groups > /app/outputs/space_groups.json

# === solve block: irreps.json ===
mkdir -p /app/outputs
python3 /solution/generate.py irreps > /app/outputs/irreps.json

# === solve block: selection_rules.json ===
mkdir -p /app/outputs
python3 /solution/generate.py selection_rules > /app/outputs/selection_rules.json

# === solve block: raman_tensors.json ===
mkdir -p /app/outputs
python3 /solution/generate.py raman_tensors > /app/outputs/raman_tensors.json
