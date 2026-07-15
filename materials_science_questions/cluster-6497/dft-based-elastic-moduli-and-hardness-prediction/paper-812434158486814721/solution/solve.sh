#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: physical_properties.csv ===
python3 << 'EOF'
import csv, os

# Glass compositions: La2O3 5%, BaO 10%, V2O5 20%, B2O3 (65-x)%, Bi2O3 x%
xs = [0, 3, 6, 9, 12, 15]
# Oxygen packing density values from the paper (BVBL0 to BVBL15)
opd = [89.52, 85.96, 83.01, 80.53, 78.42, 76.61]

# Molecular weights (g/mol)
mw = {
    'B2O3': 69.62,
    'V2O5': 181.88,
    'BaO': 153.33,
    'La2O3': 325.82,
    'Bi2O3': 465.96
}
# Oxygen atoms per formula unit
n_oxy = {'B2O3': 3, 'V2O5': 5, 'BaO': 1, 'La2O3': 3, 'Bi2O3': 3}

out_path = '/app/outputs/physical_properties.csv'
with open(out_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['glass_code', 'density_g_cm3', 'molar_volume_cm3_mol',
                'oxygen_molar_volume_cm3_mol', 'oxygen_packing_density_cm3_mol'])
    for i, x in enumerate(xs):
        code = f'BVBL{x}'
        fracs = {
            'La2O3': 0.05,
            'BaO': 0.10,
            'V2O5': 0.20,
            'B2O3': (65 - x) / 100.0,
            'Bi2O3': x / 100.0
        }
        M_glass = sum(fracs[ox] * mw[ox] for ox in mw)
        # total oxygen atoms per formula unit (constant 3.2 for all x)
        total_O = sum(fracs[ox] * n_oxy[ox] for ox in n_oxy)
        OPD_val = opd[i]
        V_m = 1000.0 * total_O / OPD_val          # molar volume (cm³/mol)
        rho = M_glass / V_m                       # density (g/cm³)
        V_oxy = 1000.0 / OPD_val                  # oxygen molar volume (cm³/mol)
        w.writerow([code, f'{rho:.4f}', f'{V_m:.2f}', f'{V_oxy:.2f}', f'{OPD_val:.2f}'])
EOF

# === solve block: mechanical_moduli.csv ===
python3 /solution/compute_all.py mechanical

# === solve block: mac_table.csv ===
python3 /solution/compute_all.py mac
