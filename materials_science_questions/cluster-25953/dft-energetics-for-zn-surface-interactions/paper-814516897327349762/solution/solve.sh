#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_energies.json ===
python3 -c "
import json
data = [
  {'orientation': 'WUR(10-10)', 'a_ang': 3.32, 'b_ang': 5.34, 'h_ang': 9.39, 'alpha_avg_deg': 112.7, 'theta_deg': 10, 'E_f_eV_per_A2': 0.058},
  {'orientation': 'BCT(010)', 'a_ang': 5.70, 'b_ang': 3.31, 'h_ang': 8.69, 'alpha_avg_deg': 117.9, 'theta_deg': 6, 'E_f_eV_per_A2': 0.049},
  {'orientation': 'ZB(110)', 'a_ang': 3.31, 'b_ang': 4.60, 'h_ang': 11.41, 'alpha_avg_deg': 111.8, 'theta_deg': 28, 'E_f_eV_per_A2': 0.067},
  {'orientation': 'CUB(100)', 'a_ang': 6.34, 'b_ang': 6.34, 'h_ang': 10.05, 'alpha_avg_deg': 129.8, 'theta_deg': 12, 'E_f_eV_per_A2': 0.078},
  {'orientation': 'h-BN(0001)', 'a_ang': 3.39, 'b_ang': 3.39, 'h_ang': 7.11, 'alpha_avg_deg': 109.5, 'theta_deg': 0, 'E_f_eV_per_A2': 0.049},
  {'orientation': 'WUR(0001)', 'a_ang': 6.62, 'b_ang': 6.62, 'h_ang': 8.11, 'alpha_avg_deg': 109.5, 'theta_deg': 0, 'E_f_eV_per_A2': 0.086}
]
with open('/app/outputs/structural_energies.json','w') as f: json.dump(data, f, indent=2)
"

# === solve block: band_gaps.json ===
python3 -c "
import json
data = [
  {'orientation': 'WUR(10-10)', 'E_g_film_eV': 2.25, 'E_g_bulk_eV': 2.20, 'delta_E_g_eV': 0.05},
  {'orientation': 'BCT(010)', 'E_g_film_eV': 2.37, 'E_g_bulk_eV': 2.20, 'delta_E_g_eV': 0.17},
  {'orientation': 'ZB(110)', 'E_g_film_eV': 2.31, 'E_g_bulk_eV': 2.09, 'delta_E_g_eV': 0.22},
  {'orientation': 'CUB(100)', 'E_g_film_eV': 2.71, 'E_g_bulk_eV': 2.68, 'delta_E_g_eV': 0.03},
  {'orientation': 'h-BN(0001)', 'E_g_film_eV': 2.66, 'E_g_bulk_eV': 2.31, 'delta_E_g_eV': 0.35},
  {'orientation': 'WUR(0001)', 'E_g_film_eV': 1.62, 'E_g_bulk_eV': 2.20, 'delta_E_g_eV': -0.58}
]
with open('/app/outputs/band_gaps.json','w') as f: json.dump(data, f, indent=2)
"

# === solve block: dielectric_constants.json ===
python3 -c "
import json
data = [
  {'orientation': 'WUR(10-10)', 'epsilon_inf_xx': 4.04, 'epsilon_inf_yy': 4.12, 'epsilon_inf_zz': 3.72},
  {'orientation': 'BCT(010)', 'epsilon_inf_xx': 4.09, 'epsilon_inf_yy': 4.09, 'epsilon_inf_zz': 3.69},
  {'orientation': 'ZB(110)', 'epsilon_inf_xx': 3.96, 'epsilon_inf_yy': 3.88, 'epsilon_inf_zz': 3.72},
  {'orientation': 'CUB(100)', 'epsilon_inf_xx': 3.46, 'epsilon_inf_yy': 3.46, 'epsilon_inf_zz': 3.19},
  {'orientation': 'h-BN(0001)', 'epsilon_inf_xx': 4.53, 'epsilon_inf_yy': 4.53, 'epsilon_inf_zz': 4.09},
  {'orientation': 'WUR(0001)', 'epsilon_inf_xx': 4.22, 'epsilon_inf_yy': 4.22, 'epsilon_inf_zz': 3.97}
]
with open('/app/outputs/dielectric_constants.json','w') as f: json.dump(data, f, indent=2)
"

# === solve block: absorption_anisotropy.json ===
python3 -c "
import json
data = [
  {'orientation': 'WUR(10-10)', 'theta_deg': 10, 'Delta_eV': -0.4, 'epsilon_ratio_xy_z': 1.0968},
  {'orientation': 'BCT(010)', 'theta_deg': 6, 'Delta_eV': -0.6, 'epsilon_ratio_xy_z': 1.1084},
  {'orientation': 'ZB(110)', 'theta_deg': 28, 'Delta_eV': -0.2, 'epsilon_ratio_xy_z': 1.0538},
  {'orientation': 'CUB(100)', 'theta_deg': 12, 'Delta_eV': -0.4, 'epsilon_ratio_xy_z': 1.0846},
  {'orientation': 'h-BN(0001)', 'theta_deg': 0, 'Delta_eV': -0.6, 'epsilon_ratio_xy_z': 1.1076},
  {'orientation': 'WUR(0001)', 'theta_deg': 0, 'Delta_eV': 0.0, 'epsilon_ratio_xy_z': 1.0630}
]
with open('/app/outputs/absorption_anisotropy.json','w') as f: json.dump(data, f, indent=2)
"
