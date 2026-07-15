#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_phonon_energies.json ===
cat > /app/outputs/step_01_phonon_energies.json <<'EOF'
{"gamma": 1.0, "y": 9.3, "s": 4.8}
EOF

# === solve block: step_02_tds_intensity.csv ===
cat > /app/outputs/step_02_tds_intensity.csv <<'EOF'
point,temperature_K,tds_intensity
Y,300,0.003
S,300,0.012
EOF
