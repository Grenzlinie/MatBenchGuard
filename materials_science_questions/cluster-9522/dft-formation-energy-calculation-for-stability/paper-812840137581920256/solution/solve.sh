#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pristine_gb_properties.csv ===
cat > /app/outputs/pristine_gb_properties.csv <<'FFEOF'
model,direction,youngs_modulus_GPa,ultimate_tensile_strength_GPa,critical_failure_strain_pct
pristine_hBN,zz,678,133,27.9
pristine_hBN,am,611,116,23.9
GB_6_5_5_6,ww,634,99,17.4
GB_1_3_3_1,ww,562,79,14.5
FFEOF

# === solve block: strain_rate_effect.csv ===
cat > /app/outputs/strain_rate_effect.csv <<'FFEOF'
model,strain_rate_s-1,ultimate_tensile_strength_GPa
GB_2_1_1_2,1e8,77
GB_2_1_1_2,1e9,80
GB_2_1_1_2,1e10,199
FFEOF

# === solve block: temperature_effect.csv ===
cat > /app/outputs/temperature_effect.csv <<'FFEOF'
model,temperature_K,ultimate_tensile_strength_GPa
GB_2_1_1_2,1,98
GB_2_1_1_2,300,77
GB_2_1_1_2,1100,43
FFEOF
