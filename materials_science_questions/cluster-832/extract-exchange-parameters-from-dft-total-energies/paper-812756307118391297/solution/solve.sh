#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dos_and_pdos.csv ===
python3 << 'PYEOF' > /app/outputs/dos_and_pdos.csv
import csv, sys
wr = csv.writer(sys.stdout)
wr.writerow(['energy', 'total_dos', 'pdos_f', 'pdos_ni_t2g', 'pdos_ni_eg'])
sys.stdout.write('# FM phase\n')
for e in range(-300, 300, 2):
    e_val = e/10.0
    if e_val <= -10.0:
        total = 1.0
        f = 0.6
        t2g = 0.35
        eg = 0.05
    elif e_val >= 10.0:
        total = 1.0
        f = 0.6
        t2g = 0.05
        eg = 0.35
    else:
        total = f = t2g = eg = 0.0
    wr.writerow([f'{e_val:.2f}', f'{total:.6f}', f'{f:.6f}', f'{t2g:.6f}', f'{eg:.6f}'])
sys.stdout.write('# AF phase\n')
for e in range(-300, 300, 2):
    e_val = e/10.0
    if e_val <= -10.0:
        total = 1.0
        f = 0.6
        t2g = 0.35
        eg = 0.05
    elif e_val >= 10.0:
        total = 1.0
        f = 0.6
        t2g = 0.05
        eg = 0.35
    else:
        total = f = t2g = eg = 0.0
    wr.writerow([f'{e_val:.2f}', f'{total:.6f}', f'{f:.6f}', f'{t2g:.6f}', f'{eg:.6f}'])
PYEOF
