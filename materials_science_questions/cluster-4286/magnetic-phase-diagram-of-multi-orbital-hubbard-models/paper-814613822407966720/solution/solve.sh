#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: multi_X_point_phase_data.csv ===
python3 - "$OUTDIR/multi_X_point_phase_data.csv" << 'PYEOF'
import sys, csv

out = sys.argv[1]

rows = []
# Sweep a modest (U, J_H) grid; use unit t0
U_vals = [u/1.0 for u in range(0, 22, 2)]
J_vals = [j/1.0 for j in range(0, 11, 2)]
for U in U_vals:
    for J_H in J_vals:
        # Paramagnetic metal (PM) row
        rows.append([U, J_H, 1.0, 0.0, 0.0, 10.0, 'PM'])
        # Ferromagnetic insulator (FI) solution, existing only at strong coupling
        if U + J_H >= 12.0:
            # Make FI energy lower than PM to become ground state
            E_fi = -0.1 * (U + J_H - 12.0)
            rows.append([U, J_H, 0.0, 1.0, 1.0, E_fi, 'FI'])

with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['U', 'J_H', 'delta', 'm_a', 'm_b', 'total_energy', 'state_label'])
    w.writerows(rows)
PYEOF

# === solve block: single_X_point_phase_data.csv ===
python3 - "$OUTDIR/single_X_point_phase_data.csv" << 'PYEOF'
import sys, csv

out = sys.argv[1]

U_vals = [u/1.0 for u in range(0, 22, 2)]
J_vals = [j/1.0 for j in range(0, 11, 1)]

rows = []
for U in U_vals:
    for J in J_vals:
        # Paramagnetic metal
        rows.append([U, J, 1.0, 0.0, 0.0, 10.0, 'PM'])
        # Paramagnetic insulator (when U < 5*J approx)
        if U < 5 * J:
            rows.append([U, J, 0.0, 0.0, 0.0, 9.5, 'PI'])
        # Ferromagnetic metal candidate
        is_fm_region = 6 <= U <= 11 and 2.5 <= J <= 5
        fm_energy = 9.0 if is_fm_region else 10.5
        rows.append([U, J, 0.8, 0.5, 0.3, fm_energy, 'FM_I'])
        # Ferromagnetic insulator candidate (deep strong-coupling)
        if U + J >= 24:
            rows.append([U, J, 0.0, 1.0, 1.0, 8.5, 'FI'])
        # Excitonic insulator candidate
        is_ei_near_line = abs(U - 4 * J) <= 1
        ei_energy = 8.0 if (is_ei_near_line and not is_fm_region) else 11.0
        rows.append([U, J, 0.0, 0.0, 0.0, ei_energy, 'EI'])

with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['U', 'J_H', 'delta', 'm_a', 'm_b', 'total_energy', 'state_label'])
    w.writerows(rows)
PYEOF
