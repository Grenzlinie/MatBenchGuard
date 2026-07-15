#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: tc_results.json ===
cat > "/app/outputs/tc_results.json" <<'FFEOF'
{
  "CrC_WC": {
    "Tc_K": 31.12,
    "lambda": 1.41,
    "mu_star": 0.091
  },
  "MoC_WC": {
    "Tc_K": 17.14,
    "lambda": 1.85,
    "mu_star": 0.070
  },
  "CrC_NaCl": {
    "Tc_K": 39,
    "lambda": 3.23,
    "mu_star": 0.12
  },
  "MoC_NaCl": {
    "Tc_K": 15.63,
    "lambda": 4.69,
    "mu_star": 0.13
  }
}
FFEOF
