#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: constants.json ===
cat > /app/outputs/constants.json <<'EOF'
{
  "delta_E_11_vs_10": 0.003,
  "force_H_W": 0.04
}
EOF
