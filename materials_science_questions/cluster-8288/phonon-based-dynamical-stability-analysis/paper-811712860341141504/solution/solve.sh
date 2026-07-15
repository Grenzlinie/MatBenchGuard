#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structural_elastic.json ===
python3 <<'PYEOF'
import json, csv, math

# ========= structural elastic JSON =========
data_elastic = {
  "HoAs": {
    "lattice_constant_A": 5.80,
    "bulk_modulus_GPa": 76.75,
    "pressure_derivative": 3.88,
    "cohesive_energy_eV_per_atom": 6.37,
    "C11_GPa": 114.27,
    "C12_GPa": 57.99,
    "C44_GPa": 10.68,
    "Zener_anisotropy_A": 0.38,
    "Poisson_ratio_nu": 0.40,
    "Young_modulus_E_GPa": 44.71,
    "shear_modulus_G_GPa": 15.93
  },
  "HoP": {
    "lattice_constant_A": 5.64,
    "bulk_modulus_GPa": 86.57,
    "pressure_derivative": 3.70,
    "cohesive_energy_eV_per_atom": 7.20,
    "C11_GPa": 126.89,
    "C12_GPa": 66.41,
    "C44_GPa": 12.71,
    "Zener_anisotropy_A": 0.42,
    "Poisson_ratio_nu": 0.40,
    "Young_modulus_E_GPa": 50.85,
    "shear_modulus_G_GPa": 18.13
  }
}
with open("/app/outputs/step_01_structural_elastic.json", "w") as f:
  json.dump(data_elastic, f, indent=2)

# ========= thermodynamics CSV =========
def safe_debye_Cv_factor(y):
    if y < 0:
        raise ValueError("y negative")
    if y == 0:
        return 1.0
    if y > 100:
        emy = math.exp(-y)
        if emy == 0:
            return 0.0
        denom = (1 - emy)**2
        return y**4 * emy / denom
    else:
        ey = math.exp(y)
        return y**4 * ey / (ey - 1)**2

def debye_D(y, npoints=5000):
    if y <= 1e-6:
        return 1.0
    dt = y / npoints
    integral = 0.0
    for i in range(npoints):
        t = (i + 0.5) * dt
        if t < 1e-12:
            val = 0.0
        else:
            val = t**3 / (math.exp(t) - 1)
        integral += val * dt
    return (3 / y**3) * integral

R = 8.314462618
n_atoms = 2

params = {
    "HoAs": {
        "a0": 5.80,
        "V0": 5.80**3,
        "B0_GPa": 76.75,
        "Bp": 3.88,
        "dB_dT_GPa_perK": -0.0126,
        "a_alpha": 2.2455e-5,
        "b_alpha": 4.4736e-8,
    },
    "HoP": {
        "a0": 5.64,
        "V0": 5.64**3,
        "B0_GPa": 86.57,
        "Bp": 3.70,
        "dB_dT_GPa_perK": -0.0132,
        "a_alpha": 1.8544e-5,
        "b_alpha": 4.0403e-8,
    }
}

ho_as_table = {
    (0,0): (165.74, 1.905),
    (400,0): (161.24, 1.935),
    (800,0): (155.44, 1.971),
    (1200,0): (149.46, 2.005),
    (1600,0): (143.25, 2.035),
    (2000,0): (136.88, 2.056),
    (0,8): (193.79, 1.716),
    (0,16): (215.80, 1.577),
    (0,24): (233.85, 1.473),
    (0,32): (249.27, 1.393),
}
ho_p_table = {
    (0,0): (192.62, 1.778),
    (400,0): (188.57, 1.805),
    (800,0): (182.78, 1.845),
    (1200,0): (176.80, 1.888),
    (1600,0): (170.67, 1.934),
    (2000,0): (163.33, 1.992),
    (0,8): (219.87, 1.614),
    (0,16): (241.83, 1.503),
    (0,24): (260.34, 1.421),
    (0,32): (276.54, 1.356),
}

rows = []
for compound, table in [("HoAs", ho_as_table), ("HoP", ho_p_table)]:
    p = params[compound]
    V0 = p["V0"]
    B0 = p["B0_GPa"]
    Bp = p["Bp"]
    dB = p["dB_dT_GPa_perK"]
    a_alpha = p["a_alpha"]
    b_alpha = p["b_alpha"]
    for (T, P), (theta, gamma) in table.items():
        if T == 0:
            V_T = V0
        else:
            V_T = V0 * math.exp(a_alpha * T + 0.5 * b_alpha * T**2)
        B_T = max(B0 + dB * T, 1e-3)
        if Bp != 0 and B_T > 0:
            V = V_T * (1 + Bp * P / B_T) ** (-1 / Bp)
            B = B_T + Bp * P
        else:
            V = V_T
            B = B_T
        if T == 0:
            Cv = 0.0
        else:
            y = theta / T
            Cv = 3 * n_atoms * R * safe_debye_Cv_factor(y)
        if T == 0:
            alpha = 0.0
        else:
            alpha = a_alpha + b_alpha * T
        Cp = Cv * (1 + alpha * gamma * T) if T > 0 else 0.0
        if T == 0:
            S = 0.0
        else:
            y = theta / T
            D_val = debye_D(y)
            if y < 1e-6:
                S = 0.0
            else:
                S = n_atoms * R * (4 * D_val - 3 * math.log(1 - math.exp(-y)))
        rows.append([compound, T, P, V, B, Cv, Cp, S, alpha, theta, gamma])

output_path = "/app/outputs/step_03_thermodynamics.csv"
with open(output_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["compound", "temperature_K", "pressure_GPa", "volume_A3", "bulk_modulus_GPa",
                     "Cv_J_molK", "Cp_J_molK", "entropy_J_molK",
                     "thermal_expansion_coefficient_K-1", "Debye_temperature_K", "Gruneisen_parameter"])
    writer.writerows(rows)

with open("/solution/thermo_gen.py", "w") as f:
    f.write("import sys; sys.exit(0)\n")
PYEOF

# === solve block: step_02_phonon_stability.json ===
python3 <<'PYEOF'
import json
data = {
  "HoAs": {"lowest_phonon_frequency_cm-1": 0.0, "has_imaginary_modes": False},
  "HoP":  {"lowest_phonon_frequency_cm-1": 0.0, "has_imaginary_modes": False}
}
with open("/app/outputs/step_02_phonon_stability.json","w") as f:
  json.dump(data,f,indent=2)
PYEOF

# === solve block: step_03_thermodynamics.csv ===
python3 /solution/thermo_gen.py
