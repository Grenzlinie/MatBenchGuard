#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_params.json ===
python3 /solution/generate_artifacts.py --type structural > /app/outputs/structural_params.json

# === solve block: band_structure.json ===
python3 /solution/generate_artifacts.py --type band_structure > /app/outputs/band_structure.json

# === solve block: phonon_dispersion.json ===
python3 /solution/generate_artifacts.py --type phonon_dispersion > /app/outputs/phonon_dispersion.json
