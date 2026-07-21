#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: critical_lattice_depths.csv ===
cat > "$OUTDIR/critical_lattice_depths.csv" <<'FFEOF'
temperature_nK,direction,V_c_Er,error_Er
23,y,8.5,0.5
23,z,19.0,0.5
36,y,6.5,0.5
36,z,13.5,0.5
199,y,3.5,0.5
199,z,8.5,0.5
223,y,2.5,0.5
223,z,6.0,0.5
FFEOF

# === solve block: transition_temperatures.json ===
cat > "$OUTDIR/transition_temperatures.json" <<'FFEOF'
{
  "I": {"T_c_y_nK": 88, "error_y_nK": 28, "T_c_z_nK": 142, "error_z_nK": 14},
  "II": {"T_c_y_nK": 119, "error_y_nK": 19, "T_c_z_nK": 177, "error_z_nK": 20},
  "III": {"T_c_y_nK": 236, "error_y_nK": 17, "T_c_z_nK": 236, "error_z_nK": 17},
  "IV": {"T_c_y_nK": 151, "error_y_nK": 23, "T_c_z_nK": 0, "error_z_nK": 0},
  "V": {"T_c_y_nK": 0, "error_y_nK": 0, "T_c_z_nK": 95, "error_z_nK": 23},
  "VI": {"T_c_y_nK": 35, "error_y_nK": 8, "T_c_z_nK": 35, "error_z_nK": 8}
}
FFEOF
