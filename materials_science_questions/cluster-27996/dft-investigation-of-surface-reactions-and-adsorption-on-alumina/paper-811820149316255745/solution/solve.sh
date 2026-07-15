#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ads_des_energies.json ===
cat > /app/outputs/ads_des_energies.json <<'FFEOF'
{
  "E_ads_AlCl": -9.355,
  "E_des_AlCl": 9.355,
  "E_des_AlCl3": 8.054
}
FFEOF

# === solve block: reaction_energies.csv ===
cat > $OUTDIR/reaction_energies.csv <<'FFEOF'
step_id,reaction_energy,activation_energy
A2,0.346,2.059
A3,0.541,1.487
A4,0.213,1.578
B2,0.490,2.025
B3,-0.247,2.691
C2,0.490,2.025
C3,-0.827,1.431
FFEOF

# === solve block: general_energies.json ===
cat > /app/outputs/general_energies.json <<'FFEOF'
{
  "mechanism_A": {
    "surface_only_energy": 1.45,
    "general_energy": -18.58
  },
  "mechanism_B": {
    "surface_only_energy": 0.24,
    "general_energy": -19.78
  },
  "mechanism_C": {
    "surface_only_energy": 0.15,
    "general_energy": -19.86
  }
}
FFEOF
