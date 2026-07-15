#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: predicted_elastic_constants.json ===
cat > /app/outputs/predicted_elastic_constants.json <<'EOF'
{
  "C11": 600,
  "C12": 127,
  "C44": 140,
  "dC11_dP": 11.3,
  "dC12_dP": 1.7,
  "dC44_dP": 0.15,
  "d2C11_dP2": -0.13,
  "d2C12_dP2": -0.05,
  "d2C44_dP2": -0.01,
  "K_prime": 4.88,
  "K_doubleprime": -0.084
}
EOF
