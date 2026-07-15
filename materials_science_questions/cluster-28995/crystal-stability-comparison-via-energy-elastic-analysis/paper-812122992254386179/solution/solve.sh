#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structure_dependent_energy_components.json ===
cat > "$OUTDIR/structure_dependent_energy_components.json" <<'FFEOF'
{
  "sc": {
    "E_M_alpha_rs": -0.917131,
    "E2": -0.115173,
    "E3_I_over_alpha_rs": -0.046477,
    "E3_II_over_alpha_rs": 0.013132,
    "E3_III_over_alpha_rs": -0.014367
  },
  "fcc": {
    "E_M_alpha_rs": -0.933611,
    "E2": -0.091307,
    "E3_I_over_alpha_rs": -0.038199,
    "E3_II_over_alpha_rs": 0.0065132,
    "E3_III_over_alpha_rs": -0.0043511
  },
  "bcc": {
    "E_M_alpha_rs": -0.933669,
    "E2": -0.090386,
    "E3_I_over_alpha_rs": -0.038089,
    "E3_II_over_alpha_rs": 0.0061756,
    "E3_III_over_alpha_rs": -0.0039338
  }
}
FFEOF

# === solve block: elastic_constant_coefficients.json ===
cat > "$OUTDIR/elastic_constant_coefficients.json" <<'FFEOF'
{
  "sc": {
    "A_M": 0.93113,
    "A2": -3.53460,
    "A3_I": -1.53616,
    "A3_II": 1.31036,
    "A3_III": -6.11017,
    "B_M": -0.10657,
    "B2": 0.18397,
    "B3_I": 0.06533,
    "B3_II": -0.05608,
    "B3_III": 0.12223
  },
  "fcc": {
    "A_M": 0.04309,
    "A2": 0.00529,
    "A3_I": -0.01663,
    "A3_II": -0.00944,
    "A3_III": 0.01515,
    "B_M": 0.19311,
    "B2": -0.29385,
    "B3_I": -0.09517,
    "B3_II": 0.08246,
    "B3_III": -0.10223
  },
  "bcc": {
    "A_M": 0.05104,
    "A2": -0.12387,
    "A3_I": -0.02193,
    "A3_II": 0.03842,
    "A3_III": -0.04527,
    "B_M": 0.19047,
    "B2": -0.23752,
    "B3_I": -0.08835,
    "B3_II": 0.05876,
    "B3_III": -0.06198
  }
}
FFEOF

# === solve block: crossing_pressure.json ===
cat > "$OUTDIR/crossing_pressure.json" <<'FFEOF'
{
  "P_c_a_u": 0.101,
  "P_c_pt_fcc_a_u": 0.40
}
FFEOF

# === solve block: pt_ground_state_energy.json ===
cat > "$OUTDIR/pt_ground_state_energy.json" <<'FFEOF'
{
  "E_pt_Ry": -1.103
}
FFEOF
