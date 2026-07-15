#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: homogenization_distances.json ===
cat > '/app/outputs/homogenization_distances.json' <<'FFEOF'
{
  "normalized_steel_95pct_sqrtDt_micrometers": 3.1,
  "hot_rolled_steel_sqrtDt_essentially_complete_micrometers": 25.0
}
FFEOF
