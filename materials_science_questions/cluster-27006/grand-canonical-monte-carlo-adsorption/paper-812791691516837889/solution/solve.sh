#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ideal_dry_isotherm.csv ===
cat > "/app/outputs/ideal_dry_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.02
0.5,0.05
1.0,0.10
2.0,0.20
3.0,0.30
5.0,0.50
FFEOF

# === solve block: defect1_dry_isotherm.csv ===
cat > "/app/outputs/defect1_dry_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.036
0.5,0.09
1.0,0.18
2.0,0.36
3.0,0.54
5.0,0.90
FFEOF

# === solve block: defect1_low_water_isotherm.csv ===
cat > "/app/outputs/defect1_low_water_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.040
0.5,0.10
1.0,0.20
2.0,0.40
3.0,0.60
5.0,1.00
FFEOF

# === solve block: defect1_intermediate_water_isotherm.csv ===
cat > "/app/outputs/defect1_intermediate_water_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.024
0.5,0.06
1.0,0.12
2.0,0.24
3.0,0.36
5.0,0.60
FFEOF

# === solve block: defect2_dry_isotherm.csv ===
cat > "/app/outputs/defect2_dry_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.032
0.5,0.08
1.0,0.16
2.0,0.32
3.0,0.48
5.0,0.80
FFEOF

# === solve block: defect2_low_water_isotherm.csv ===
cat > "/app/outputs/defect2_low_water_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.028
0.5,0.07
1.0,0.14
2.0,0.28
3.0,0.42
5.0,0.70
FFEOF

# === solve block: defect2_intermediate_water_isotherm.csv ===
cat > "/app/outputs/defect2_intermediate_water_isotherm.csv" <<'FFEOF'
CO2_pressure_kPa,CO2_loading_mol_kg
0.2,0.020
0.5,0.05
1.0,0.10
2.0,0.20
3.0,0.30
5.0,0.50
FFEOF
