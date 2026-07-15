#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: expansion_ratios.json ===
cat > /app/outputs/expansion_ratios.json <<'FFEOF'
{
  "delta_a": 0.62,
  "delta_b": 1.0,
  "delta_c": 0.49,
  "ratio_vector": [0.62, 1.0, 0.49]
}
FFEOF
