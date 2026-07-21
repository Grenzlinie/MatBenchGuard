#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "total_hydration_number": 13.3,
  "oxide_region_count": 3.7,
  "methyl_region_count": 9.6,
  "oxide_D_sign": "positive",
  "methyl_D_sign": "negative"
}
FFEOF
