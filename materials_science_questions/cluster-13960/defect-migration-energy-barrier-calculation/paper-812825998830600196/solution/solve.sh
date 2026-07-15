#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
python3 /solution/oracle_data_writer.py formation_energies.csv

# === solve block: binding_energies.csv ===
python3 << 'EOF'
import csv, os
out_dir = os.environ['OUTDIR']
with open(os.path.join(out_dir, 'formation_energies.csv'), newline='') as f:
    rows = list(csv.DictReader(f))
ef1_groove = None
ef1_vacancy = None
for row in rows:
    if int(row['N_He']) == 1:
        ef1_groove = float(row['E_f_groove_eV'])
        ef1_vacancy = float(row['E_f_vacancy_eV'])
        break
if ef1_groove is None:
    raise ValueError('Missing N_He=1 in formation_energies.csv')
results = []
for row in rows:
    n = int(row['N_He'])
    if n < 2:
        continue
    groove = float(row['E_f_groove_eV'])
    vacancy = float(row['E_f_vacancy_eV'])
    eb_groove = n * ef1_groove - groove
    eb_vacancy = n * ef1_vacancy - vacancy
    results.append((n, round(eb_groove, 2), round(eb_vacancy, 2)))
with open(os.path.join(out_dir, 'binding_energies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N_He', 'E_b_groove_eV', 'E_b_vacancy_eV'])
    for n, g, v in results:
        writer.writerow([n, f'{g:.2f}', f'{v:.2f}'])
EOF

# === solve block: migration_barriers.csv ===
python3 /solution/oracle_data_writer.py migration_barriers.csv

# === solve block: max_occupancy.json ===
python3 /solution/oracle_data_writer.py max_occupancy.json
