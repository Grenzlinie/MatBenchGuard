#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: strengthening_contributions.json ===
cat > "/app/outputs/strengthening_contributions.json" <<'FFEOF'
{
  "load_sharing_increment_MPa": 252.0,
  "hall_petch_increment_MPa": 44.1,
  "orowan_increment_MPa": 18.9,
  "total_increment_MPa": 315.0
}
FFEOF
