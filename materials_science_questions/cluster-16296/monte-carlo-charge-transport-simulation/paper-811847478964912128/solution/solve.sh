#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: mobilities.json ===
cat > "/app/outputs/mobilities.json" <<'FFEOF'
{
  "Al0.15In0.85Sb_mu": 9400,
  "AlSb_mu": 525,
  "InAs_mu": 28000,
  "InSb_mu": 67000
}
FFEOF
