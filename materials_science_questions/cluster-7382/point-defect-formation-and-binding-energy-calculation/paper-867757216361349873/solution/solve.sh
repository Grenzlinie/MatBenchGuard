#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: strain_effect.json ===
cat > /app/outputs/strain_effect.json <<'FFEOF'
{
  "compressive_strain_2pct_delta_meV": 75,
  "tensile_strain_2pct_delta_meV": -5
}
FFEOF
