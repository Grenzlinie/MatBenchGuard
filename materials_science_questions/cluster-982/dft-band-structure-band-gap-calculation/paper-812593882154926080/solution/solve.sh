#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_elastic_constants.json ===
cat > /app/outputs/step_01_elastic_constants.json <<'FFEOF'
{
  "c11": 1715.3,
  "c12": -283.5,
  "c44": 1187.5
}
FFEOF

# === solve block: step_02_mechanical_properties.json ===
cat > /app/outputs/step_02_mechanical_properties.json <<'FFEOF'
{
  "bulk_modulus": 381.0,
  "youngs_modulus": 1691.0,
  "shear_modulus": 1113.0,
  "poisson_ratio": -0.241
}
FFEOF

# === solve block: step_03_band_gap.json ===
cat > /app/outputs/step_03_band_gap.json <<'FFEOF'
{
  "band_gap": 2.52,
  "vbm_kpoint": "L",
  "cbm_kpoint": "X"
}
FFEOF
