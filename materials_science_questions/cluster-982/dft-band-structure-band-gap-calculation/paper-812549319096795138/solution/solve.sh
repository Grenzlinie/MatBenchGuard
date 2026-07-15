#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_structure_results.json ===
cat > /app/outputs/band_structure_results.json <<'FFEOF'
{
  "band_gap_ev": 3.49,
  "direct_or_indirect": "indirect",
  "vbm_kpoint": [0.5, 0.5, 0.0],
  "cbm_kpoint": [0.0, 0.0, 0.0]
}
FFEOF
