#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
OUTDIR=/app/outputs
cat > "$OUTDIR/computed_properties.csv" <<'FFEOF'
compound,a_PBE_U,a_HSE,J,Eg_without_SOC,Eg_with_SOC,direct_indirect,Tc_Ising,Tc_Heisenberg,MAE,ΔV,m_e_x,m_e_y,m_h_x,m_h_y,E1e_x,E1e_y,E1h_x,E1h_y,C_2D_x,C_2D_y,μ_e_x,μ_e_y,μ_h_x,μ_h_y
LiCrS2,3.56,3.51,7.03,2.30,2.24,indirect,640,209,0.07,4.42,,,,,,,,,,,,
LiCrSe2,3.76,3.70,8.11,2.21,2.02,direct,820,237,0.10,3.69,,,,,,,,,,,,
LiCrTe2,4.06,4.02,9.91,1.38,0.99,indirect,880,285,0.15,2.99,,,,,,,,,,,,
NaCrS2,3.66,3.61,7.50,1.01,0.92,indirect,690,217,0.10,3.20,0.82,0.74,,,,1.74,1.72,,,80.20,80.48,839.0,1057.6,,
NaCrSe2,3.86,3.80,7.81,0.91,0.77,direct,760,226,0.11,3.16,0.93,0.78,0.56,0.51,1.61,1.60,1.98,2.07,65.40,64.87,621.1,887.0,1132.5,1239.2
NaCrTe2,4.14,4.11,8.52,0.83,0.59,direct,780,234,0.46,3.02,0.94,0.22,0.30,0.27,1.24,2.71,2.33,2.17,49.72,49.53,779.5,2945.5,2166.5,3071.6
FFEOF
