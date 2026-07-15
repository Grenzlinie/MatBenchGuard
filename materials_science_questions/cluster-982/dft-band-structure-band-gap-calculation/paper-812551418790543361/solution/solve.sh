#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gap_result.json ===
cat > "$OUTDIR/band_gap_result.json" << 'JSONEOF'
{
  "indirect_gap_ev": 1.29,
  "vbm_kpoint": [0.0, 0.0, 0.0],
  "cbm_kpoint": [0.5, 0.5, 0.5]
}
JSONEOF
