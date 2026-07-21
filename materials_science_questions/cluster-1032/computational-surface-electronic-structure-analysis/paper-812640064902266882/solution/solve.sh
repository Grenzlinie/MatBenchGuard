#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_eigenvalues_ry.json ===
cat > /app/outputs/band_eigenvalues_ry.json <<'FFEOF'
{
  "Gamma": {
    "Gamma1_s": -0.850,
    "Gamma3_dxy": -0.680,
    "Gamma4_dx2y2": -0.440,
    "Gamma5_dxz_dyz": -0.580
  },
  "M": {
    "M3_dxy": -0.640,
    "M4_dx2y2": -0.420,
    "M5_dxz_dyz": -0.560
  },
  "splittings": {
    "Delta_Gamma25_prime": 0.100,
    "Delta_Gamma12": 0.410
  }
}
FFEOF
