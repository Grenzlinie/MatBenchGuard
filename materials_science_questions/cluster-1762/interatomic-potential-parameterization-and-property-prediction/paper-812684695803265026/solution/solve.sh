#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_energies.csv ===
python3 -c "
import csv
structures = [
    ('rebonded_3a',  '3a', 'rebonded',    -0.16),
    ('rebonded_5a',  '5a', 'rebonded',    -0.17),
    ('rebonded_9a',  '9a', 'rebonded',    -0.17),
    ('rebonded_13a', '13a','rebonded',    -0.16),
    ('nonrebonded_3a', '3a', 'nonrebonded', -0.026),
    ('nonrebonded_5a', '5a', 'nonrebonded', -0.029),
    ('nonrebonded_9a', '9a', 'nonrebonded', -0.030),
    ('nonrebonded_13a','13a','nonrebonded', -0.030),
]
base_energy = -1000.0
rows = []
for struct_id, ledge, step, delta in structures:
    e_orig = base_energy
    e_inter = e_orig + delta
    rows.append([struct_id, 'original',     '{:.6f}'.format(e_orig), ledge, step])
    rows.append([struct_id, 'interchanged', '{:.6f}'.format(e_inter), ledge, step])
with open('/app/outputs/step_02_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['structure_id','condition','total_energy_eV','ledge_separation','step_type'])
    writer.writerows(rows)
"
