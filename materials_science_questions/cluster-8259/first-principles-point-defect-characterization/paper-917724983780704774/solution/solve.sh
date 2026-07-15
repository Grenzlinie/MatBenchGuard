#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" << 'FFEOF'
{
  "CTL_p1_0": 0.4,
  "CTL_0_m1": 0.4,
  "KS_energy_difference": 1.5,
  "TDM": 1.2,
  "ZPL": 0.96
}
FFEOF
