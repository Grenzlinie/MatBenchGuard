#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sinusoidal_grating_results.json ===
cat > /app/outputs/sinusoidal_grating_results.json <<'FFEOF'
{
  "a": 0.446,
  "b": 0.026,
  "Lambda_min": 1.87,
  "d_zero": 33.1
}
FFEOF
