#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dos.csv ===
python3 /solution/generate_data.py dos.csv

# === solve block: band_structure.csv ===
python3 /solution/generate_data.py band_structure.csv

# === solve block: frozen_phonon_shifts.csv ===
cat > /app/outputs/frozen_phonon_shifts.csv <<'FFEOF'
distortion,band_name,energy_shift
elongation,pi*_band,-0.52
rotation,pi*_band,0.45
FFEOF
