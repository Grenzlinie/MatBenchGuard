#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: simulated_uptakes.json ===
cat > /app/outputs/simulated_uptakes.json <<'JSONEOF'
{
  "dispersion_swnt_wt%": 0.40,
  "dispersion_slit_wt%": 1.50,
  "chemisorption_swnt_wt%": 3.20,
  "chemisorption_slit_wt%": 9.50
}
JSONEOF
