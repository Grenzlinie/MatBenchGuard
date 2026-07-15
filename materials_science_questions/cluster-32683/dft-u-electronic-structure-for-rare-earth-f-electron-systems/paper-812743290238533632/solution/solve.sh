#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'FFEOF'
{
  "indirect_gap": 0.67,
  "direct_gap_X": 1.0,
  "f_band_top": 0.30
}
FFEOF
