#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calibration_constant.json ===
cat > /app/outputs/calibration_constant.json <<'FFEOF'
{
  "C": 1800
}
FFEOF
