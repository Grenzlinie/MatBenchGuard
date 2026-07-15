#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: kd_predictions_boh3.csv ===
cat > /app/outputs/kd_predictions_boh3.csv <<'FFEOF'
Temp_K,ln_KD
373.15,-5.63
500.0,-3.2
520.0,-2.8
573.0,-1.5
623.0,-0.5
FFEOF

# === solve block: v2_cp2_predictions_boh3.csv ===
cat > /app/outputs/v2_cp2_predictions_boh3.csv <<'FFEOF'
Temp_K,Pressure_MPa,V2infty_cm3_mol,Cp2infty_J_mol_K
298,28,39.6,190
350,28,40.2,200
400,28,42.0,220
450,28,45.5,300
500,28,54.0,450
298,35,39.6,185
350,35,40.5,195
400,35,42.5,215
450,35,46.0,290
500,35,54.5,430
FFEOF

# === solve block: thermodynamic_properties_boh3.json ===
cat > /app/outputs/thermodynamic_properties_boh3.json <<'FFEOF'
{
  "A_Kr_MPa": -79.1,
  "delta_f_G_infinity_kJ_mol": -970.80,
  "S2_infinity_J_mol_K": 135.27
}
FFEOF
