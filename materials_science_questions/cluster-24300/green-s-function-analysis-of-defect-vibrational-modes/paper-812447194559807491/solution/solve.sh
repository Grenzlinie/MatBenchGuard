#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table_I_scattering_rates.csv ===
cat > /app/outputs/table_I_scattering_rates.csv <<'FFEOF'
impurity,zone,tau0_inv,tau_inv
vac.,alpha_arm,7.84,6.95
vac.,beta_arm,8.00,6.51
vac.,second_zone,9.31,5.30
vac.,total_FS,9.03,5.58
Ag,alpha_arm,5.36,4.49
Ag,beta_arm,4.34,3.32
Ag,second_zone,7.38,3.93
Ag,total_FS,6.83,3.89
Mg,alpha_arm,1.25,1.06
Mg,beta_arm,1.24,1.04
Mg,second_zone,1.66,0.91
Mg,total_FS,1.58,0.94
Zn,alpha_arm,0.66,0.76
Zn,beta_arm,0.62,0.65
Zn,second_zone,0.59,0.58
Zn,total_FS,0.60,0.60
Cd,alpha_arm,0.62,0.57
Cd,beta_arm,0.67,0.62
Cd,second_zone,0.75,0.48
Cd,total_FS,0.73,0.51
Hg,alpha_arm,0.36,0.29
Hg,beta_arm,0.38,0.24
Hg,second_zone,0.40,0.18
Hg,total_FS,0.39,0.20
Ga,alpha_arm,0.34,0.31
Ga,beta_arm,0.21,0.17
Ga,second_zone,0.43,0.33
Ga,total_FS,0.40,0.31
Tl,alpha_arm,0.22,0.23
Tl,beta_arm,0.12,0.11
Tl,second_zone,0.29,0.32
Tl,total_FS,0.26,0.29
Sn,alpha_arm,1.14,0.87
Sn,beta_arm,0.77,0.42
Sn,second_zone,1.68,0.88
Sn,total_FS,1.52,0.82
Pb,alpha_arm,1.39,1.24
Pb,beta_arm,0.61,0.41
Pb,second_zone,2.21,1.58
Pb,total_FS,1.93,1.40
Sb,alpha_arm,4.39,3.38
Sb,beta_arm,3.39,2.07
Sb,second_zone,6.25,3.06
Sb,total_FS,5.73,2.95
Bi,alpha_arm,4.26,3.49
Bi,beta_arm,2.89,1.91
Bi,second_zone,6.21,3.39
Bi,total_FS,5.63,3.20
FFEOF

# === solve block: table_IV_resistivities.csv ===
cat > /app/outputs/table_IV_resistivities.csv <<'FFEOF'
impurity,resistivity_6psiPW
vac.,2.41
Ag,1.67
Mg,0.41
Zn,0.26
Cd,0.22
Hg,0.09
Ga,0.13
Tl,0.12
Sn,0.35
Pb,0.55
Sb,1.26
Bi,1.36
FFEOF

# === solve block: table_VI_Dingle_temperatures.csv ===
cat > /app/outputs/table_VI_Dingle_temperatures.csv <<'FFEOF'
impurity,orbit,T_D
vac.,second_zone,71.9
vac.,beta_arm,52.6
Ag,second_zone,57.4
Ag,beta_arm,29.4
Mg,second_zone,13.0
Mg,beta_arm,8.2
Zn,second_zone,4.4
Zn,beta_arm,4.0
Cd,second_zone,5.8
Cd,beta_arm,4.4
Hg,second_zone,3.1
Hg,beta_arm,2.5
Ga,second_zone,3.2
Ga,beta_arm,1.5
Tl,second_zone,2.3
Tl,beta_arm,0.9
Sn,second_zone,13.1
Sn,beta_arm,5.5
Pb,second_zone,17.4
Pb,beta_arm,4.7
Sb,second_zone,48.7
Sb,beta_arm,23.4
Bi,second_zone,48.3
Bi,beta_arm,20.1
FFEOF
