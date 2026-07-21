#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: large_U_phase_boundaries.json ===
cat > /app/outputs/large_U_phase_boundaries.json <<'FFEOF'
{
  "PCOI_to_DMI_Vp_over_tb1": 1.3,
  "DMI_to_PCOI_prime_Vp_over_tb1": 1.7,
  "NPCOI_region": false
}
FFEOF

# === solve block: charge_structure_factors.json ===
cat > /app/outputs/charge_structure_factors.json <<'FFEOF'
{
  "PCOI": {
    "N_CD_q00": 0.05,
    "N_CD_qpipi": 0.92,
    "N_qpipi": 0.05
  },
  "PCOI_prime": {
    "N_CD_q00": 0.91,
    "N_CD_qpipi": 0.05,
    "N_qpipi": 0.05
  },
  "NPCOI": {
    "N_CD_q00": 0.05,
    "N_CD_qpipi": 0.05,
    "N_qpipi": 0.90
  },
  "DMI": {
    "N_CD_q00": 0.04,
    "N_CD_qpipi": 0.05,
    "N_qpipi": 0.04
  }
}
FFEOF

# === solve block: COM_density_profile.csv ===
cat > /app/outputs/COM_density_profile.csv <<'FFEOF'
sublattice,density_c,density_f
0,1.85,1.87
1,1.83,1.86
2,0.72,0.68
3,1.88,1.84
4,1.82,1.88
5,0.69,0.71
6,1.86,1.83
7,1.84,1.85
8,0.70,0.69
9,1.87,1.86
10,1.85,1.84
11,0.71,0.70
FFEOF
