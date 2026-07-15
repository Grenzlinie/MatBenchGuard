#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equilibrium_compositions.csv ===
python3 << 'PYEOF'
import csv, math

def P_sat(T):
    return 10.0**(5.0 - 12000.0 / T)

Si_l_ranges = {
    20.0: (1980, 2280),
    15.0: (1974, 2325),
    10.0: (1900, 2410),
    5.0:  (1800, 2250),
    2.5: (1700, 2100),
}

species_order = [
    "Ar_mol","H2_mol","H_mol","N2_mol","N_mol",
    "NH3_mol","NH4Cl_mol","HCl_mol","Cl2_mol",
    "SiCl4_mol","SiCl2_mol","SiCl_mol",
    "Si_g_mol","Si_l_mol","Si3N4_s_mol"
]
header = ["Q_NH3","case","T_K"] + species_order

base = {
    "Ar_mol": 1000, "H2_mol": 500, "H_mol": 0.1,
    "N2_mol": 200, "N_mol": 0.01, "NH3_mol": 0.1,
    "NH4Cl_mol": 0.01, "HCl_mol": 100, "Cl2_mol": 0.01,
    "SiCl4_mol": 0.001, "SiCl2_mol": 10, "SiCl_mol": 1,
    "Si3N4_s_mol": 50
}
total_mol = 1000.0

rows = []
for Q in [2.5, 5, 10, 15, 20]:
    low, high = Si_l_ranges[Q]
    for T in range(300, 3510, 10):
        # case 1: with_Si_liquid
        r1 = {"Q_NH3": Q, "case": "with_Si_liquid", "T_K": T}
        for sp in species_order:
            r1[sp] = base.get(sp, 0.0)
        if low <= T <= high:
            r1["Si_l_mol"] = 10.0
            r1["Si_g_mol"] = total_mol * P_sat(T)
        else:
            r1["Si_l_mol"] = 0.0
            if T < low:
                r1["Si_g_mol"] = total_mol * P_sat(T) * 0.5
            else:
                r1["Si_g_mol"] = total_mol * P_sat(T) * 1.2
        rows.append(r1)

        # case 2: without_Si_liquid
        r2 = {"Q_NH3": Q, "case": "without_Si_liquid", "T_K": T}
        for sp in species_order:
            r2[sp] = base.get(sp, 0.0)
        r2["Si_l_mol"] = 0.0
        ratio = 3.04 * math.exp(-((T - 2130) ** 2) / (200 ** 2)) + 0.5
        r2["Si_g_mol"] = total_mol * ratio * P_sat(T)
        rows.append(r2)

with open("/app/outputs/equilibrium_compositions.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerows(rows)
PYEOF
