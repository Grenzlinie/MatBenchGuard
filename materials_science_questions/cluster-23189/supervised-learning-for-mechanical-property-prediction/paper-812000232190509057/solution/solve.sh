#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: equivalent_surrogate.json ===
cat > "$OUTDIR/equivalent_surrogate.json" <<'FFEOF'
{
  "atoms": [2.67],
  "probabilities": [1.0],
  "final_distortion": 1.74e-4
}
FFEOF
