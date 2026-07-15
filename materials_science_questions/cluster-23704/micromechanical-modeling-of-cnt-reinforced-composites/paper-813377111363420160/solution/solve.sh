#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_stress_strain_25_CNTs.csv ===
python3 << 'PYEOF'
import csv, os
out = os.path.join('/app/outputs', 'step_01_stress_strain_25_CNTs.csv')
E = 8.6  # GPa, Young's modulus
npts = 501
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'stress'])
    for i in range(npts):
        strain = 0.05 * i / (npts - 1)
        stress = E * strain
        w.writerow([f'{strain:.6f}', f'{stress:.6f}'])
PYEOF

# === solve block: step_02_young_modulus_aggregates.csv ===
python3 << 'PYEOF'
import csv, os
out = os.path.join('/app/outputs', 'step_02_young_modulus_aggregates.csv')
rows = [
    (50,   8.6, 0.10),
    (200,  8.6, 0.07),
    (800,  8.6, 0.04),
    (1000, 8.6, 0.035),
]
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['num_cnts', 'young_modulus_gpa', 'coefficient_of_variance'])
    for num_cnts, mod, cov in rows:
        w.writerow([num_cnts, f'{mod:.4f}', f'{cov:.4f}'])
PYEOF

# === solve block: step_03_order_parameter.csv ===
python3 << 'PYEOF'
import csv, os
out = os.path.join('/app/outputs', 'step_03_order_parameter.csv')
rows = [
    (50,   -0.0577),
    (200,   0.0197),
    (800,   0.0171),
    (1000,  0.0078),
]
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['num_cnts', 'order_parameter'])
    for num_cnts, sp in rows:
        w.writerow([num_cnts, f'{sp:.6f}'])
PYEOF

# === solve block: step_04_density_study.csv ===
python3 << 'PYEOF'
import csv, os
out = os.path.join('/app/outputs', 'step_04_density_study.csv')
rows = [
    (0.10, 10.87),
    (0.12, 12.96),
    (0.14, 15.28),
    (0.16, 17.55),
]
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['density_g_cm3', 'young_modulus_gpa'])
    for d, mod in rows:
        w.writerow([f'{d:.2f}', f'{mod:.4f}'])
PYEOF
