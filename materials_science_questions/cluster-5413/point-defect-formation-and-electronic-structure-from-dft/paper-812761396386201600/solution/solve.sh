#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_formation_energies.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/step_01_formation_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['layer','E_V_f','E_HeV_f'])
    w.writerow([2,2.63,4.39])
    w.writerow([3,2.88,4.48])
PYEOF

# === solve block: step_02_binding_energies.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/step_02_binding_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect_type','layer','species','binding_energy'])
    w.writerow(['V',2,'H',1.22])
    w.writerow(['V',2,'He',4.39])
    w.writerow(['V',3,'H',1.21])
    w.writerow(['V',3,'He',4.53])
    w.writerow(['HeV',2,'H',1.07])
    w.writerow(['HeV',3,'H',1.07])
PYEOF

# === solve block: step_03_diffusion_barriers.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/step_03_diffusion_barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['diffusion_path','barrier'])
    w.writerow(['He_TIS_to_V',0.10])
    w.writerow(['H_TIS_to_V',0.19])
PYEOF

# === solve block: step_04_desorption_barriers.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/step_04_desorption_barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect','layer','barrier_H'])
    w.writerow(['V',2,0.16])
    w.writerow(['HeV',2,0.00])
PYEOF

# === solve block: step_05_stable_site_count.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/step_05_stable_site_count.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect','layer','num_sites'])
    w.writerow(['V',2,2])
    w.writerow(['HeV',2,4])
PYEOF
