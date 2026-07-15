#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "eT_star_LiP": 1.56,
  "eT_star_ZnP": 1.84,
  "C_LiP_dyn_per_cm": 44400,
  "C_ZnP_dyn_per_cm": 65400
}
FFEOF
