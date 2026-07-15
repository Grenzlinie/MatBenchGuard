#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > "/app/outputs/band_gaps.json" <<'FFEOF'
{
  "gap_1D": 1.268,
  "gap_2D": 1.53
}
FFEOF
