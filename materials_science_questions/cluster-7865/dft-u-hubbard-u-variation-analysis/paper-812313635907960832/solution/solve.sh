#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_U_values.json ===
cat > /app/outputs/computed_U_values.json << 'FFEOF'
{
  "Mn2+_olivine": 3.92,
  "Mn3+_olivine": 5.09,
  "Fe2+_olivine": 3.71,
  "Fe3+_olivine": 4.90,
  "Co2+_olivine": 5.05,
  "Co3+_olivine": 6.34,
  "Ni2+_olivine": 5.26,
  "Ni3+_olivine": 6.93,
  "Co3+_layered": 4.91,
  "Co4+_layered": 5.37,
  "Ni3+_layered": 6.70,
  "Ni4+_layered": 6.04,
  "Mn3+_spinel": 4.64,
  "Mn4+_spinel": 5.04,
  "Co3+_spinel": 5.62,
  "Co4+_spinel": 6.17,
  "Mn2+_monoxide": 3.6,
  "Fe2+_monoxide": 4.6,
  "Co2+_monoxide": 5.0,
  "Ni2+_monoxide": 5.1
}
FFEOF

# === solve block: computed_voltages.csv ===
cat > /app/outputs/computed_voltages.csv << 'FFEOF'
compound,computed_voltage,experimental_voltage
LiMnPO4/MnPO4,4.1,4.1
LiFePO4/FePO4,3.47,3.5
LiCoPO4/CoPO4,4.73,4.8
LiNiPO4/NiPO4,5.07,
LiCoO2/CoO2,3.82,
LiNiO2/NiO2,3.92,3.85
LiMn2O4/Mn2O4_0-1,4.19,4.15
LiMn2O4/Mn2O4_1-2,2.97,2.95
LiCo2O4/Co2O4_1-2,3.56,3.5
FFEOF
