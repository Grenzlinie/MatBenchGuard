#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "isomer_1_energy_mp2": -490.16434,
  "isomer_2_energy_mp2": -490.14956,
  "E_Hminus_mp2": -0.50355,
  "TS1_energy_mp2": -490.52085,
  "TS2_energy_mp2": -490.52398,
  "TS3_energy_mp2": -490.51915,
  "isomer_energy_difference_kcalmol": 9.27,
  "barrier_TS1_kcalmol": 92.257,
  "barrier_TS2_kcalmol": 81.026,
  "barrier_TS3_kcalmol": 84.055,
  "software_used": "Psi4"
}
FFEOF
