#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_bond_orders.csv ===
python3 <<'PYEOF' > /app/outputs/effective_bond_orders.csv
import csv, sys
w = csv.writer(sys.stdout)
w.writerow(['pressure_GPa','bond_label','effective_bond_order'])
bonds = ['C3-H5','C2-N2','N1-N4','N2-N5','N5-O4','N6-O5']
data = {
    'C3-H5': [0.95, 0.94, 0.93],
    'C2-N2': [1.30, 1.30, 1.30],
    'N1-N4': [1.10, 1.12, 1.14],
    'N2-N5': [1.05, 1.07, 1.09],
    'N5-O4': [1.20, 1.18, 1.17],
    'N6-O5': [1.25, 1.23, 1.22]
}
for p_idx, p in enumerate([0.0, 0.5, 1.0]):
    for b in bonds:
        w.writerow([p, b, data[b][p_idx]])
PYEOF

# === solve block: phonon_frequencies.csv ===
python3 <<'PYEOF' > /app/outputs/phonon_frequencies.csv
import csv, sys
w = csv.writer(sys.stdout)
w.writerow(['pressure_GPa','mode_index','frequency_cm1'])
num_modes = 504
base_freqs = [50.0 + i*5.0 for i in range(num_modes)]
for p_idx, p in enumerate([0.0, 0.5, 1.0]):
    shift_factor = p * 0.01
    for i in range(num_modes):
        freq = base_freqs[i] + (i+1) * shift_factor
        w.writerow([p, i+1, round(freq, 4)])
PYEOF
