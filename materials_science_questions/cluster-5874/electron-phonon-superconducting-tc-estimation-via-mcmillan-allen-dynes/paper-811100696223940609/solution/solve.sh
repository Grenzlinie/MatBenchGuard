#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: eliashberg_results.json ===
cat > /app/outputs/eliashberg_results.json <<'FFEOF'
{
  "H3S": {
    "conventional": {
      "mu_star": 0.204,
      "delta_0": 33.816,
      "ratio_2delta_Tc": 4.41,
      "m_eff_ratio": 2.736,
      "R_C": 2.47,
      "R_H": 0.136
    },
    "vertex_corrected": {
      "mu_star": 0.185,
      "delta_0": 33.816,
      "ratio_2delta_Tc": 4.41,
      "m_eff_ratio": 2.736,
      "R_C": 2.47,
      "R_H": 0.136
    }
  },
  "PH3": {
    "conventional": {
      "mu_star": 0.088,
      "delta_0": 14.488,
      "ratio_2delta_Tc": 4.15,
      "m_eff_ratio": 2.136,
      "R_C": 1.99,
      "R_H": 0.150
    },
    "vertex_corrected": {
      "mu_star": 0.083,
      "delta_0": 14.488,
      "ratio_2delta_Tc": 4.15,
      "m_eff_ratio": 2.136,
      "R_C": 1.99,
      "R_H": 0.150
    }
  }
}
FFEOF
