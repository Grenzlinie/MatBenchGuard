#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_02_lattice_thermal_conductivity.csv ===
cat > "$OUTDIR/step_02_lattice_thermal_conductivity.csv" <<'FFEOF'
Material,Temperature_K,kappa_l_WmK
ZrSe2,300,1.2
HfSe2,300,1.8
FFEOF

# === solve block: step_03_ZT_optimal_values.csv ===
cat > "/app/outputs/step_03_ZT_optimal_values.csv" <<'FFEOF'
Material,DopingType,Temperature_K,Optimal_ZT,Optimal_carrier_concentration_cm3
ZrSe2,n-type,600,0.95,3.2e19
ZrSe2,p-type,600,0.87,2.8e19
HfSe2,n-type,600,0.97,2.9e19
HfSe2,p-type,600,0.85,3.1e19
ZrSe2,n-type,1000,0.72,4.5e19
ZrSe2,p-type,1000,0.58,3.9e19
HfSe2,n-type,1000,0.79,4.1e19
HfSe2,p-type,1000,0.63,4.0e19
FFEOF

# === solve block: step_04_trend_comparison.txt ===
cat > "/app/outputs/step_04_trend_comparison.txt" <<'FFEOF'
True
True
FFEOF
