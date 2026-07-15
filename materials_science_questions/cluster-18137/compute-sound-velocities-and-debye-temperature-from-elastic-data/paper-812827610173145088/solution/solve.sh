#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_properties.json ===
cat > /app/outputs/elastic_properties.json <<'EOF'
{
  "CuRh2S4": {
    "B": 106.20,
    "G": 25.05,
    "E": 69.67,
    "nu": 0.39,
    "B_over_G": 4.23,
    "A": 1.74,
    "Cauchy_pressure": 64.44,
    "sigma_P": 0.47,
    "rho": 4.91,
    "v_t": 5332.14,
    "v_l": 2258.72,
    "v_m": 2553.63,
    "theta_D": 294.23
  },
  "CuRh2Se4": {
    "B": 94.60,
    "G": 19.53,
    "E": 54.81,
    "nu": 0.40,
    "B_over_G": 4.84,
    "A": 0.99,
    "Cauchy_pressure": 62.04,
    "sigma_P": 0.35,
    "rho": 6.55,
    "v_t": 4291.65,
    "v_l": 1726.75,
    "v_m": 1955.63,
    "theta_D": 215.57
  }
}
EOF
