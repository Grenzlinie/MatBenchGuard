#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: periods.json ===
cat > /app/outputs/periods.json <<'FFEOF'
{
  "spheroidal_L2": 0.013,
  "spheroidal_L3": 0.009,
  "spheroidal_L4": 0.007,
  "torsional_L2": 0.018,
  "torsional_L3": 0.013,
  "torsional_L4": 0.010
}
FFEOF
