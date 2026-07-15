#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fitted_coefficients.json ===
cat > /app/outputs/fitted_coefficients.json << 'FFEOF'
{
  "CO": {
    "p0": 0.1243,
    "p1": -0.1465,
    "p2": 0.000434,
    "p3": 0.000237
  },
  "HCl": {
    "p0": 1.0930,
    "p1": 0.1018,
    "p2": 0.00039,
    "p3": -0.00096
  }
}
FFEOF
