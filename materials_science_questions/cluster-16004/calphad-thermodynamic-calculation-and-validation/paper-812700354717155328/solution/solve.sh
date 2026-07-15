#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ternary_coefficients.json ===
cat > /app/outputs/ternary_coefficients.json <<'FFEOF'
{
  "Ti": 8.862,
  "Cr": -4.497,
  "Co": -1.229,
  "Mo": -2.574
}
FFEOF

# === solve block: multicomponent_coefficients.json ===
cat > /app/outputs/multicomponent_coefficients.json <<'FFEOF'
{
  "K_Ti": 8.862,
  "K_Cr": -4.497,
  "K_Co": -1.229,
  "K_Mo": -2.574,
  "F_TiCr": 0.8166,
  "F_TiCo": 0.0916,
  "F_CrCo": -4.337,
  "H_TiCrCo": 0.3211
}
FFEOF
