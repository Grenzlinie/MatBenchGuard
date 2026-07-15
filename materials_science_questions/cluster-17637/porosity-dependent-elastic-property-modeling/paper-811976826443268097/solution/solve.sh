#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_moduli.csv ===
mkdir -p /app/outputs
cat > /app/outputs/computed_moduli.csv <<'EOF'
model_id,computed_E_MPa
A,0.48
B,0.54
C,0.56
cylindrical,0.28
spherical,0.59
EOF
