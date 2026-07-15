#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
cat > /tmp/oracle_helpers.py << 'PYEOF'
import numpy as np
import csv
import json

def write_properties(path):
    data = [
        {"alloy": "Al3Sc", "lattice_constant_a": 4.108, "formation_energy_deltaH": -0.4683,
         "C11": 182, "C12": 39, "C44": 74, "bulk_modulus_B": 87, "shear_modulus_G": 72.9,
         "young_modulus_E": 171.0, "B_G_ratio": 1.19, "cauchy_pressure_C12_minus_C44": -34.6,
         "poisson_ratio_v": 0.172, "anisotropy_factor_A": 1.04},
        {"alloy": "Al3(Sc0.5Y0.5)", "lattice_constant_a": 4.186, "formation_energy_deltaH": -0.4446,
         "C11": 167, "C12": 38, "C44": 64, "bulk_modulus_B": 81, "shear_modulus_G": 64.5,
         "young_modulus_E": 152.8, "B_G_ratio": 1.25, "cauchy_pressure_C12_minus_C44": -26.6,
         "poisson_ratio_v": 0.185, "anisotropy_factor_A": 0.99},
        {"alloy": "Al3(Sc0.5Ti0.5)", "lattice_constant_a": 4.043, "formation_energy_deltaH": -0.4255,
         "C11": 185, "C12": 51, "C44": 69, "bulk_modulus_B": 95, "shear_modulus_G": 68.2,
         "young_modulus_E": 165.2, "B_G_ratio": 1.40, "cauchy_pressure_C12_minus_C44": -18.2,
         "poisson_ratio_v": 0.211, "anisotropy_factor_A": 1.03},
        {"alloy": "Al3(Sc0.5Zr0.5)", "lattice_constant_a": 4.107, "formation_energy_deltaH": -0.4679,
         "C11": 182, "C12": 51, "C44": 68, "bulk_modulus_B": 95, "shear_modulus_G": 67.2,
         "young_modulus_E": 163.1, "B_G_ratio": 1.41, "cauchy_pressure_C12_minus_C44": -17.3,
         "poisson_ratio_v": 0.213, "anisotropy_factor_A": 1.05},
        {"alloy": "Al3(Sc0.5Hf0.5)", "lattice_constant_a": 4.097, "formation_energy_deltaH": -0.4324,
         "C11": 182, "C12": 52, "C44": 70, "bulk_modulus_B": 96, "shear_modulus_G": 68.3,
         "young_modulus_E": 165.5, "B_G_ratio": 1.40, "cauchy_pressure_C12_minus_C44": -18.3,
         "poisson_ratio_v": 0.211, "anisotropy_factor_A": 1.08},
        {"alloy": "Al3(Sc0.5V0.5)", "lattice_constant_a": 4.006, "formation_energy_deltaH": -0.3012,
         "C11": 177, "C12": 61, "C44": 71, "bulk_modulus_B": 99, "shear_modulus_G": 65.9,
         "young_modulus_E": 161.9, "B_G_ratio": 1.51, "cauchy_pressure_C12_minus_C44": -10.4,
         "poisson_ratio_v": 0.229, "anisotropy_factor_A": 1.22},
        {"alloy": "Al3(Sc0.5Nb0.5)", "lattice_constant_a": 4.051, "formation_energy_deltaH": -0.3821,
         "C11": 177, "C12": 65, "C44": 72, "bulk_modulus_B": 103, "shear_modulus_G": 65.7,
         "young_modulus_E": 162.4, "B_G_ratio": 1.56, "cauchy_pressure_C12_minus_C44": -6.8,
         "poisson_ratio_v": 0.236, "anisotropy_factor_A": 1.28},
        {"alloy": "Al3(Sc0.5Ta0.5)", "lattice_constant_a": 4.053, "formation_energy_deltaH": -0.3206,
         "C11": 174, "C12": 67, "C44": 68, "bulk_modulus_B": 103, "shear_modulus_G": 61.9,
         "young_modulus_E": 154.6, "B_G_ratio": 1.66, "cauchy_pressure_C12_minus_C44": -0.2,
         "poisson_ratio_v": 0.250, "anisotropy_factor_A": 1.27}
    ]
    fieldnames = ["alloy", "lattice_constant_a", "formation_energy_deltaH",
                  "C11", "C12", "C44", "bulk_modulus_B", "shear_modulus_G",
                  "young_modulus_E", "B_G_ratio", "cauchy_pressure_C12_minus_C44",
                  "poisson_ratio_v", "anisotropy_factor_A"]
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def write_dos(path):
    alloys = ["Al3Sc", "Al3(Sc0.5Ti0.5)", "Al3(Sc0.5V0.5)", "Al3(Sc0.5Zr0.5)", "Al3(Sc0.5Nb0.5)"]
    gap_positions = {"Al3Sc": 0.5, "Al3(Sc0.5Ti0.5)": 0.2, "Al3(Sc0.5V0.5)": -0.2,
                     "Al3(Sc0.5Zr0.5)": 0.3, "Al3(Sc0.5Nb0.5)": -0.3}
    energies = np.arange(-10.0, 5.01, 0.1)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["alloy", "energy_eV", "total_DOS", "partial_Al_s", "partial_Al_p", "partial_TM_d", "partial_Sc_d"])
        for alloy in alloys:
            als = 1.0 * np.exp(-((energies+8.0)/1.5)**2 / 2) + 0.8 * np.exp(-((energies+5.0)/1.5)**2 / 2)
            alp = 1.2 * np.exp(-((energies+2.5)/1.2)**2 / 2) + 0.4 * np.exp(-((energies+0.5)/1.0)**2 / 2)
            scd = 0.8 * np.exp(-((energies+0.3)/1.0)**2 / 2)
            if alloy == "Al3Sc":
                tmd = np.zeros_like(energies)
            else:
                tmd = 1.0 * np.exp(-((energies+1.0)/1.0)**2 / 2)
            sum_comp = als + alp + tmd + scd
            sum_comp_safe = np.where(sum_comp < 1e-6, 1e-6, sum_comp)
            gap = gap_positions[alloy]
            envelope = 1 - 0.8 * np.exp(-((energies - gap)/0.5)**2 / 2)
            total = envelope * sum_comp
            frac_als = als / sum_comp_safe
            frac_alp = alp / sum_comp_safe
            frac_tmd = tmd / sum_comp_safe
            frac_scd = scd / sum_comp_safe
            for e, t, a_s, a_p, t_d, s_d in zip(energies, total, frac_als, frac_alp, frac_tmd, frac_scd):
                writer.writerow([alloy, e, t, a_s, a_p, t_d, s_d])

def write_charge(path):
    alloys = ["Al3Sc", "Al3(Sc0.5Y0.5)", "Al3(Sc0.5Zr0.5)", "Al3(Sc0.5Nb0.5)"]
    a_dict = {"Al3Sc": 4.108, "Al3(Sc0.5Y0.5)": 4.186, "Al3(Sc0.5Zr0.5)": 4.107, "Al3(Sc0.5Nb0.5)": 4.051}
    result = {}
    step = 0.1
    sigma = 0.7
    for alloy in alloys:
        a = a_dict[alloy]
        L = 2 * a
        n_intervals = int(np.ceil(L / step))
        nx = n_intervals + 1
        xs = np.linspace(0, L, nx)
        ys = np.linspace(0, L, nx)
        X, Y = np.meshgrid(xs, ys, indexing='xy')
        density = np.zeros_like(X)
        # Al atom at center
        dx = X - 0.5*L
        dy = Y - 0.5*L
        density += 3.0 * np.exp(-(dx**2+dy**2)/(2*sigma**2))
        # corner species assignments
        if alloy == "Al3Sc":
            sc_corners = [(0,0),(L,0),(0,L),(L,L)]
            tm_corners = []
        else:
            sc_corners = [(0,0),(L,L)]
            tm_corners = [(L,0),(0,L)]
        # Sc contributions
        for cx, cy in sc_corners:
            dx = X - cx
            dy = Y - cy
            density += 2.0 * np.exp(-(dx**2+dy**2)/(2*sigma**2))
        # TM contributions
        if tm_corners:
            if "Y" in alloy:
                amp_TM = 2.0
            elif "Zr" in alloy:
                amp_TM = 1.8
            elif "Nb" in alloy:
                amp_TM = 1.6
            else:
                amp_TM = 2.0
            for cx, cy in tm_corners:
                dx = X - cx
                dy = Y - cy
                density += amp_TM * np.exp(-(dx**2+dy**2)/(2*sigma**2))
        # extra blob at Al-TM midpoint to control trend
        mid_x, mid_y = 0.25*L, 0.25*L
        amp_mid = {
            "Al3Sc": 1.5,
            "Al3(Sc0.5Y0.5)": 1.35,
            "Al3(Sc0.5Zr0.5)": 1.2,
            "Al3(Sc0.5Nb0.5)": 1.05
        }[alloy]
        dx = X - mid_x
        dy = Y - mid_y
        density += amp_mid * np.exp(-(dx**2+dy**2)/(2*sigma**2))
        density_T = density.T   # shape (nx, ny) → grid[i][j] corresponds to (xs[i], ys[j])
        result[alloy] = {
            "x_grid": xs.tolist(),
            "y_grid": ys.tolist(),
            "density": density_T.tolist()
        }
    with open(path, 'w') as f:
        json.dump(result, f, indent=2)
PYEOF

# === solve block: properties.csv ===
python3 -c "import sys; sys.path.insert(0,'/tmp'); from oracle_helpers import write_properties; write_properties('$OUTDIR/properties.csv')"

# === solve block: dos_data.csv ===
python3 -c "import sys; sys.path.insert(0,'/tmp'); from oracle_helpers import write_dos; write_dos('$OUTDIR/dos_data.csv')"

# === solve block: charge_density_001.json ===
python3 -c "import sys; sys.path.insert(0,'/tmp'); from oracle_helpers import write_charge; write_charge('$OUTDIR/charge_density_001.json')"
