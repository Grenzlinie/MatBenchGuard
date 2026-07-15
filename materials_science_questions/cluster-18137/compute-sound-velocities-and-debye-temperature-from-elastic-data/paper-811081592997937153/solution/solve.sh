#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mechanical_thermal_properties.json ===
cat > /app/outputs/mechanical_thermal_properties.json <<'FFEOF'
{
  "G_H": 28,
  "E": 82,
  "sigma": 0.38,
  "B_over_G_H": 4.00,
  "v_l": 4708,
  "v_t": 2113,
  "v_avg": 2383,
  "theta_D": 273
}
FFEOF
