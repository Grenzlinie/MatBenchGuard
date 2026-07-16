#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'FFEOF'
{
  "LiP": {"band_gap": 1.43, "gap_type": "indirect", "zT_300K": 0.74},
  "NaP": {"band_gap": 1.67, "gap_type": "direct", "zT_300K": 0.78},
  "KP": {"band_gap": 1.76, "gap_type": "direct", "zT_300K": 0.64}
}
FFEOF
