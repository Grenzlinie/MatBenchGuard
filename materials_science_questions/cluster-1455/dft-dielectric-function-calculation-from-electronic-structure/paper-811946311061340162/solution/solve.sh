#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gap.json ===
python3 -c "import json; json.dump({'indirect_gap': 3.764, 'direct_gap': 3.799}, open('${OUTDIR}/band_gap.json', 'w'))"

# === solve block: phonon_modes.json ===
python3 /solution/generate_outputs.py phonon_modes.json

# === solve block: dielectric_tensor.json ===
python3 /solution/generate_outputs.py dielectric_tensor.json
