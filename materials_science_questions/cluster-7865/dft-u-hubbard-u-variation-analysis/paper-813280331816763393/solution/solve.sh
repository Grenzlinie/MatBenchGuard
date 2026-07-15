#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: energy_moment.csv ===
python3 << 'PYEOF'
import csv

# lattice constants in Angstrom
a_vals = [3.97, 3.85, 3.75, 3.70]
# φ values (fraction of 2π)
phi_vals = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20]

# Parameters for ΔE(φ) = A*(φ - φ_min)² - A*φ_min² (except a=3.70 where ΔE = A*φ²)
params = {
    3.97: {"phi_min": 0.05, "A": 2.0, "M_base": 3.5},
    3.85: {"phi_min": 0.09, "A": 1.2345679, "M_base": 3.0},
    3.75: {"phi_min": 0.16, "A": 0.5859375, "M_base": 2.5},
    3.70: {"phi_min": 0.0,  "A": 2.0, "M_base": 2.0},
}

rows = []
for a in a_vals:
    p = params[a]
    phi_min = p["phi_min"]
    A = p["A"]
    M_base = p["M_base"]
    for phi in phi_vals:
        if a != 3.70:
            delta_E = A * ((phi - phi_min)**2 - phi_min**2)
        else:
            delta_E = A * (phi**2)
        total_energy = round(delta_E, 6)
        fe_spin_moment = round(M_base, 2)
        rows.append([a, phi, total_energy, fe_spin_moment])

with open('/app/outputs/energy_moment.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'phi', 'total_energy', 'fe_spin_moment'])
    writer.writerows(rows)
PYEOF
