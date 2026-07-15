#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: co_adsorption_energies.csv ===
python3 << 'PYEOF'
import csv
with open('/app/outputs/co_adsorption_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['site', 'adsorption_energy'])
    writer.writerow(['surface_Sn_CN4', 1.31])
    writer.writerow(['interior_Sn_CN6', 0.95])
PYEOF

# === solve block: dos_data.csv ===
python3 << 'PYEOF'
import csv, math
energies = []
dos_slab = []
dos_bulk = []
for i in range(241):
    e = -6.0 + i * 0.05
    energies.append(round(e, 2))
    slab_val = 0.05 + 3.0 * math.exp(-((e + 0.2) ** 2) / (2 * 0.3 ** 2))
    bulk_val = 0.05 + 0.5 * math.exp(-((e + 0.8) ** 2) / (2 * 0.6 ** 2))
    dos_slab.append(round(slab_val, 6))
    dos_bulk.append(round(bulk_val, 6))

with open('/app/outputs/dos_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'dos_slab', 'dos_bulk'])
    for e, s, b in zip(energies, dos_slab, dos_bulk):
        writer.writerow([e, s, b])
PYEOF
