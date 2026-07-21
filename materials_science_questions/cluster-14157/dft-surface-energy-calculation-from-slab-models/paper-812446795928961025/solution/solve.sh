#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_energy_results.csv ===
python3 <<'PYEOF'
import csv

rows = [
    {'metal': 'Cs', 'n_plus': 1.33e-3, 'b0': 1.82, 'b1': 2.16, 'sigma0': 3.13e-5, 'sigma1': 4.01e-5, 'mu1': -5.39e-2},
    {'metal': 'Rb', 'n_plus': 1.67e-3, 'b0': 1.81, 'b1': 2.12, 'sigma0': 3.84e-5, 'sigma1': 5.05e-5, 'mu1': -5.54e-2},
    {'metal': 'K',  'n_plus': 1.95e-3, 'b0': 1.80, 'b1': 2.08, 'sigma0': 4.38e-5, 'sigma1': 5.89e-5, 'mu1': -5.65e-2},
    {'metal': 'Na', 'n_plus': 3.77e-3, 'b0': 1.74, 'b1': 1.75, 'sigma0': 7.07e-5, 'sigma1': 11.1e-5, 'mu1': -6.19e-2},
    {'metal': 'Li', 'n_plus': 6.92e-3, 'b0': 1.68, 'b1': 1.24, 'sigma0': 8.6e-5,  'sigma1': 18.7e-5, 'mu1': -6.48e-2},
]

with open('/app/outputs/surface_energy_results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['metal','n_plus','b0','b1','sigma0','sigma1','mu1'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: critical_charge_Na.csv ===
python3 <<'PYEOF'
import csv

# W+ = 3.7 eV -> atomic units (1 eV = 0.036749322... a.u.)
W_plus_au = 3.7 * 0.036749322

with open('/app/outputs/critical_charge_Na.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['R', 'Z_star'])
    for R in range(5, 31):
        Z_star = W_plus_au * R + 0.5
        writer.writerow([R, Z_star])
PYEOF
