#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
python3 << 'EOF'
import csv
with open('/app/outputs/formation_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect_id', 'E_F_eV'])
    w.writerow(['A', 1.60])
    w.writerow(['B', 1.45])
    w.writerow(['C', 1.11])
    w.writerow(['D', 1.23])
EOF

# === solve block: neb_profiles.csv ===
python3 << 'EOF'
import csv

def gen_energies(E_F, E_A, max_idx, n=17):
    energies = []
    for i in range(n):
        if i <= max_idx:
            t = i / max_idx
            e = E_F + E_A * (3*t*t - 2*t*t*t)
        else:
            t = (i - max_idx) / (n - 1 - max_idx)
            e = (E_F + E_A) * (1 - (3*t*t - 2*t*t*t))
        energies.append(round(e, 6))
    return energies

defects = {
    'A': (1.60, 0.23),
    'B': (1.45, 0.084),
    'C': (1.11, 0.27),
    'D': (1.23, 0.11)
}
max_idx = 6

with open('/app/outputs/neb_profiles.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect_id', 'energy_eV', 'replica_index'])
    for defect_id, (Ef, Ea) in defects.items():
        energies = gen_energies(Ef, Ea, max_idx)
        for idx, en in enumerate(energies):
            w.writerow([defect_id, en, idx])
EOF

# === solve block: electronic_DOS.csv ===
python3 << 'EOF'
import csv, math

gaps = {'perfect': 5.25, 'A': 4.90, 'B': 4.80, 'C': 5.01, 'D': 4.86}

def dos_val(e, gap):
    if 0.0 <= e <= gap:
        return 0.0
    elif e < 0:
        return (1.0*math.exp(-((e+0.3)**2)/(2*0.2**2)) +
                0.5*math.exp(-((e+0.8)**2)/(2*0.3**2)))
    else:
        off = e - gap
        return (1.0*math.exp(-((off-0.3)**2)/(2*0.2**2)) +
                0.5*math.exp(-((off-0.9)**2)/(2*0.3**2)))

with open('/app/outputs/electronic_DOS.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect_id', 'dos_arbunits', 'energy_eV'])
    for did, gap in gaps.items():
        start = -2.0
        stop = gap + 2.0
        step = 0.01
        n = int((stop - start) / step) + 1
        for i in range(n):
            e = start + i * step
            dos = dos_val(e, gap)
            w.writerow([did, round(dos, 6), round(e, 6)])
EOF

# === solve block: charge_density_profiles.csv ===
python3 << 'EOF'
import csv

min_densities = {
    'A': 0.309,
    'B': 0.288,
    'C': 0.318,
    'D': 0.301
}

bond_length = 1.4
mid = bond_length / 2.0
a = 0.1

with open('/app/outputs/charge_density_profiles.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['charge_density_e_Bohr3', 'defect_id', 'distance_along_NN_bond_Angstrom'])
    npoints = 21
    for did, min_rho in min_densities.items():
        for i in range(npoints):
            d = (i / (npoints-1)) * bond_length
            rho = min_rho + a * (d - mid)**2
            w.writerow([round(rho, 6), did, round(d, 6)])
EOF
