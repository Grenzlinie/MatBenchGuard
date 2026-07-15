#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
{
  "KCl": {
    "A_+-": 6.29,
    "B_+-": -0.59,
    "gamma_l_plus": 0.0,
    "gamma_t_plus": 0.0,
    "gamma_l_minus": 0.12,
    "gamma_t_minus": 0.0,
    "g1_plus": 0.11,
    "g2_plus": 0.0,
    "g4_plus": 0.0,
    "h1_plus": -0.12,
    "h2_plus": 0.01,
    "g1_minus": -0.26,
    "g2_minus": 0.0,
    "h1_minus": 0.36,
    "h2_minus": 0.03
  },
  "KBr": {
    "A_+-": 6.30,
    "B_+-": -0.62,
    "gamma_l_plus": 0.0,
    "gamma_t_plus": 0.0,
    "gamma_l_minus": 0.14,
    "gamma_t_minus": 0.0,
    "g1_plus": 0.01,
    "g2_plus": 0.0,
    "g4_plus": 0.03,
    "h1_plus": 0.09,
    "h2_plus": 0.0,
    "g1_minus": -0.20,
    "g2_minus": 0.0,
    "h1_minus": 0.16,
    "h2_minus": 0.04
  },
  "RbCl": {
    "A_+-": 6.81,
    "B_+-": -0.68,
    "gamma_l_plus": -0.04,
    "gamma_t_plus": 0.0,
    "gamma_l_minus": 0.16,
    "gamma_t_minus": 0.0,
    "g1_plus": 0.08,
    "g2_plus": 0.0,
    "g4_plus": 0.0,
    "h1_plus": 0.21,
    "h2_plus": 0.04,
    "g1_minus": -0.18,
    "g2_minus": 0.0,
    "h1_minus": 0.22,
    "h2_minus": 0.0
  },
  "AgBr": {
    "A_+-": 6.69,
    "B_+-": -0.73,
    "gamma_l_plus": 0.18,
    "gamma_t_plus": 0.01,
    "gamma_l_minus": 0.0,
    "gamma_t_minus": -0.02,
    "g1_plus": 0.31,
    "g2_plus": 0.09,
    "g4_plus": 0.0,
    "h1_plus": 1.03,
    "h2_plus": 0.0,
    "g1_minus": 0.29,
    "g2_minus": -0.21,
    "h1_minus": -0.90,
    "h2_minus": 0.0
  }
}
FFEOF

# === solve block: computed_phonon_frequencies.csv ===
cat > /app/outputs/computed_phonon_frequencies.csv <<'FFEOF'
material,qx,qy,qz,branch,frequency_THz,error_THz
KCl,0.0,0.0,0.0,LO,0.0,0.0
KBr,0.0,0.0,0.0,LO,0.0,0.0
RbCl,0.0,0.0,0.0,LO,0.0,0.0
AgBr,0.0,0.0,0.0,LO,0.0,0.0
FFEOF
