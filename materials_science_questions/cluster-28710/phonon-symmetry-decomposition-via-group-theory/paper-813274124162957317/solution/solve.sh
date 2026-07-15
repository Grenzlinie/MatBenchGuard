#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: symmetry_classification.json ===
cat > /app/outputs/symmetry_classification.json <<'FFEOF'
[
  {
    "irreducible_representation": "ΓA_g⊗S⁰⊗T⁰",
    "axial_isotropy_subgroup": "C_4h LST",
    "abbreviation": "PM"
  },
  {
    "irreducible_representation": "ΓB_g⊗S⁰⊗T⁰",
    "axial_isotropy_subgroup": "C_2h LST",
    "abbreviation": "Cu-CDW"
  },
  {
    "irreducible_representation": "ΓA_u⊗S⁰⊗T⁰",
    "axial_isotropy_subgroup": "C_4 LST",
    "abbreviation": "Mo-CDW"
  },
  {
    "irreducible_representation": "ΓB_u⊗S⁰⊗T⁰",
    "axial_isotropy_subgroup": "S_4 LST",
    "abbreviation": "BOW"
  },
  {
    "irreducible_representation": "ΓA_g⊗S¹⊗T¹",
    "axial_isotropy_subgroup": "C_4h L A(e_z) M(e_y)",
    "abbreviation": "CuMo-(A)FM"
  },
  {
    "irreducible_representation": "ΓB_g⊗S¹⊗T¹",
    "axial_isotropy_subgroup": "(E+C_4z u_{2x}) C_2h L A(e_z) M(e_y)",
    "abbreviation": "Cu-AFM"
  },
  {
    "irreducible_representation": "ΓA_u⊗S¹⊗T¹",
    "axial_isotropy_subgroup": "(E+I u_{2x}) C_4 L A(e_z) M(e_y)",
    "abbreviation": "Mo-AFM"
  },
  {
    "irreducible_representation": "ΓB_u⊗S¹⊗T¹",
    "axial_isotropy_subgroup": "(E+C_4z u_{2x}) S_4 L A(e_z) M(e_y)",
    "abbreviation": "SBOW"
  }
]
FFEOF

# === solve block: photomagnetism_dynamics.csv ===
python3 <<'PYEOF'
import csv, math

t_max = 500.0
dt = 1.0
n = int(t_max / dt) + 1
ts = [i * dt for i in range(n)]

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

# E_ab: double-step via two logistic functions
A1, t1, tau1 = 2.0, 100.0, 3.0
A2, t2, tau2 = 3.0, 160.0, 3.0

# M_ab: magnetization rises with second absorption step
M_max = 0.25
tau_m = 5.0

# E_c: single-step, small amplitude
E_c_amp = 0.3
tau_c = 10.0
t_c = 100.0

rows = []
for t in ts:
    E_ab = A1 * sigmoid((t - t1) / tau1) + A2 * sigmoid((t - t2) / tau2)
    M_ab = M_max * sigmoid((t - t2) / tau_m)
    E_c = E_c_amp * sigmoid((t - t_c) / tau_c)
    M_c = 0.0  # negligible c-axis magnetization
    rows.append((t, M_ab, M_c, E_ab, E_c))

with open('/app/outputs/photomagnetism_dynamics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t', 'M_ab', 'M_c', 'E_ab', 'E_c'])
    for t, mab, mc, eab, ec in rows:
        writer.writerow([f'{t:.6f}', f'{mab:.6f}', f'{mc:.6f}', f'{eab:.6f}', f'{ec:.6f}'])
PYEOF
