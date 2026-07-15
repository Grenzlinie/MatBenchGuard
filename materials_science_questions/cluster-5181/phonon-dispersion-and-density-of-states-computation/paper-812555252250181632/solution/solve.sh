#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_dispersion.json ===
python3 /solution/generate_phonon_dispersion.py

# === solve block: thermal_conductivity.json ===
cat > /app/outputs/thermal_conductivity.json <<'EOFJSON'
{"[100]": 10.68, "[010]": 20.78, "[001]": 12.61}
EOFJSON

# === solve block: accumulated_thermal_conductivity.csv ===
python3 /solution/generate_accumulated_kappa.py
