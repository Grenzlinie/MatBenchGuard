#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_dispersion.csv ===
cat > /app/outputs/step_01_dispersion.csv <<'EOF'
azimuth,k_parallel,binding_energy
GammaY,0.0,5.40
GammaY,0.1,5.50
GammaY,0.2,5.60
GammaY,0.3,5.70
GammaY,0.4,5.80
GammaY,0.5,5.90
GammaY,0.6,6.00
GammaY,0.7,6.10
GammaY,0.8,6.20
GammaY,0.9,6.30
GammaX,0.0,5.40
GammaX,0.1,5.41
GammaX,0.2,5.39
GammaX,0.3,5.42
GammaX,0.4,5.40
GammaX,0.5,5.41
GammaX,0.6,5.39
GammaX,0.7,5.40
GammaX,0.8,5.41
GammaX,0.9,5.40
EOF
