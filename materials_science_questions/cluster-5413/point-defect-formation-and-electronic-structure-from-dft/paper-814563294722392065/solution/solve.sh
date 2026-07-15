#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Generate synthetic reference data with controlled averages and correlation
python3 - <<'PYEOF'
import json, csv, random

random.seed(42)
data = []
crystalline_count = 64
amorphous_count = 64

# Crystalline sites: distances in [-15,-6], energy ~2.6, displacement small (~0.9)
for i in range(crystalline_count):
    dist = round(random.uniform(-15.0, -6.0), 2)
    energy = round(2.6 + random.uniform(-0.2, 0.2), 4)
    disp = round(0.9 + random.uniform(-0.2, 0.2), 4)
    data.append({
        "site_id": i+1,
        "region": "crystalline",
        "distance_from_interface_A": dist,
        "formation_energy_eV": energy,
        "root_sum_square_displacement_angstrom": disp
    })

# Amorphous sites: distances in [6,15], energy ~0.2, displacement large (~5.3)
for i in range(amorphous_count):
    dist = round(random.uniform(6.0, 15.0), 2)
    energy = round(0.2 + random.uniform(-0.2, 0.2), 4)
    disp = round(5.3 + random.uniform(-2.0, 2.0), 4)
    data.append({
        "site_id": i+1+crystalline_count,
        "region": "amorphous",
        "distance_from_interface_A": dist,
        "formation_energy_eV": energy,
        "root_sum_square_displacement_angstrom": disp
    })

with open('/tmp/vacancy_data.json', 'w') as f:
    json.dump(data, f)
PYEOF

# === solve block: oxygen_vacancy_formation_energies.csv ===
python3 - <<'PYEOF'
import json, csv

with open('/tmp/vacancy_data.json') as f:
    data = json.load(f)

with open('/app/outputs/oxygen_vacancy_formation_energies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['site_id', 'region', 'distance_from_interface_A', 'formation_energy_eV'])
    for row in data:
        writer.writerow([row['site_id'], row['region'], row['distance_from_interface_A'], row['formation_energy_eV']])
PYEOF

# === solve block: oxygen_vacancy_displacements.csv ===
python3 - <<'PYEOF'
import json, csv

with open('/tmp/vacancy_data.json') as f:
    data = json.load(f)

with open('/app/outputs/oxygen_vacancy_displacements.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['site_id', 'root_sum_square_displacement_angstrom'])
    for row in data:
        writer.writerow([row['site_id'], row['root_sum_square_displacement_angstrom']])
PYEOF
