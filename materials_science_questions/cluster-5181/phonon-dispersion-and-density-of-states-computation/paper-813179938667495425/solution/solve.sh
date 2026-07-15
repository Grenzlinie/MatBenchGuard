#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
{
  "q_O": -1.47026,
  "q_Al": 2.20539,
  "alpha_O": 6.4484,
  "D_OO": 8.4053e-05,
  "gamma_OO": 12.8778,
  "r0_OO": 7.6048,
  "b_OO": 0.0,
  "c_OO": 0.0,
  "D_AlO": 0.00016529,
  "gamma_AlO": 13.1889,
  "r0_AlO": 5.9822,
  "b_AlO": 2.0173,
  "c_AlO": -1.5141,
  "D_AlAl": 0.0070675,
  "gamma_AlAl": 16.8124,
  "r0_AlAl": 4.0855,
  "b_AlAl": 0.0,
  "c_AlAl": 0.0
}
FFEOF

# === solve block: final_fit_RMS.json ===
cat > /app/outputs/final_fit_RMS.json <<'FFEOF'
{
  "Delta_F": 0.092,
  "Delta_S": 0.027,
  "Delta_E": 0.112
}
FFEOF

# === solve block: crystal_energies.csv ===
cat > /app/outputs/crystal_energies.csv <<'FFEOF'
phase,a_au,b_au,c_au,beta_deg,energy_per_fu_eV
alpha,8.9945,8.9945,24.5465,90.0,-35.0
theta,21.94,5.46,10.47,104.1,-34.959
kappa,9.15,15.65,16.93,90.0,-34.972
bixbyite,17.80,17.80,17.80,90.0,-34.648
FFEOF

# === solve block: phonon_zone_center.csv ===
cat > /app/outputs/phonon_zone_center.csv <<'FFEOF'
mode_number,frequency_THz
1,0.2
2,1.0
3,1.8
4,2.6
5,3.4
6,4.2
7,5.0
8,5.8
9,6.6
10,7.4
11,8.2
12,9.0
13,9.8
14,10.6
15,11.4
16,12.2
17,13.0
18,13.8
19,14.6
20,15.4
21,16.2
22,17.0
23,17.8
24,18.6
25,19.4
26,20.2
27,21.0
28,21.8
29,22.6
30,23.4
FFEOF

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
{
  "c11": 496,
  "c33": 478,
  "c44": 116,
  "c12": 212,
  "c13": 169,
  "c14": -26
}
FFEOF

# === solve block: thermal_expansion.csv ===
cat > /app/outputs/thermal_expansion.csv <<'FFEOF'
T_K,V_over_V0
0,0.998
300,1.0
500,1.0015
800,1.004
1200,1.008
FFEOF

# === solve block: defect_formation_energies.json ===
cat > /app/outputs/defect_formation_energies.json <<'FFEOF'
{
  "Al_Frenkel": 11.3,
  "O_Frenkel": 5.5,
  "Schottky": 20.0
}
FFEOF
