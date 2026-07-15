#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: alpha_eq5.csv ===
python3 -c "
import csv
data = [('Li',45.0e-6),('Na',77.0e-6),('K',90.0e-6),('V',9.3e-6),('Nb',7.3e-6),('Ta',6.6e-6),('Mo',4.9e-6),('W',4.6e-6),('Fe',11.5e-6),('Ca',23.0e-6),('Ni',13.1e-6),('Cu',16.8e-6),('Ag',18.3e-6),('Au',14.0e-6),('Al',20.0e-6),('Pb',28.8e-6),('Pd',15.1e-6),('Pt',9.9e-6),('Ir',4.5e-6),('Be',9.5e-6),('Mg',24.6e-6),('Y',13.5e-6),('Re',6.3e-6),('Ti',7.6e-6),('Zn',27.3e-6),('Cd',29.3e-6),('In',30.6e-6),('Si',2.5e-6),('Ge',5.6e-6)]
with open('/app/outputs/alpha_eq5.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['element','alpha'])
    w.writerows(data)
"

# === solve block: alpha_eq6.csv ===
python3 -c "
import csv
data = [('Li',47.3e-6), ('K',81.4e-6), ('Pb',28.5e-6), ('W',4.4e-6), ('Cu',16.8e-6), ('Au',14.0e-6)]
with open('/app/outputs/alpha_eq6.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['element','alpha'])
    w.writerows(data)
"
