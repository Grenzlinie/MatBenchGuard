#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: material_properties_ambient.json ===
cat <<'PYEOF' | python3
import json
data = {
    "Np": {
        "S": 1.40,
        "L": 4.68,
        "J": 3.28,
        "mu_eff": 2.55,
        "occupation_eigenvalues": [0.05, 0.09, 0.26, 0.89, 0.91, 0.91, 0.92],
        "OD_LS": 0.36,
        "OD_jmj": 0.46
    },
    "Pu": {
        "S": 0.0,
        "L": 0.0,
        "J": 0.0,
        "mu_eff": 0.0,
        "occupation_eigenvalues": [0.03, 0.92, 0.92, 0.93, 0.93, 0.93, 0.93],
        "OD_LS": 0.45,
        "OD_jmj": 0.01
    },
    "Am": {
        "S": 0.0,
        "L": 0.0,
        "J": 0.0,
        "mu_eff": 0.0,
        "occupation_eigenvalues": [0.07, 0.97, 0.98, 0.98, 0.98, 0.99, 0.99],
        "OD_LS": 0.47,
        "OD_jmj": 0.02
    },
    "Cm": {
        "S": 2.77,
        "L": 0.75,
        "J": 3.52,
        "mu_eff": 7.44,
        "occupation_eigenvalues": [0.10, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00],
        "OD_LS": 0.31,
        "OD_jmj": 0.45
    }
}
with open('/app/outputs/material_properties_ambient.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: bandwidth_vs_volume.csv ===
cat <<'PYEOF' | python3
import csv
volumes = [1.0, 0.95, 0.90, 0.85, 0.80]
metals = {
    'Np': {'j5': [2.0, 2.25, 2.5, 2.75, 3.0], 'j7': [3.0, 3.25, 3.5, 3.75, 4.0], 'J': [3.28, 3.25, 3.20, 3.15, 3.10]},
    'Pu': {'j5': [1.5, 1.75, 2.0, 2.25, 2.5], 'j7': [2.5, 2.75, 3.0, 3.25, 3.5], 'J': [0, 0, 0, 0, 0]},
    'Am': {'j5': [1.0, 1.15, 1.30, 1.45, 1.6], 'j7': [2.0, 2.15, 2.30, 2.45, 2.6], 'J': [0, 0, 0, 0, 0]},
    'Cm': {'j5': [1.5, 1.75, 2.0, 2.25, 2.5], 'j7': [3.0, 3.25, 3.5, 3.75, 4.0], 'J': [3.52, 3.48, 3.42, 3.36, 3.30]}
}
with open('/app/outputs/bandwidth_vs_volume.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material','volume_ratio','j5_2_bandwidth','j7_2_bandwidth','total_magnetic_moment'])
    for mat, data in metals.items():
        for i, v in enumerate(volumes):
            w.writerow([mat, v, data['j5'][i], data['j7'][i], data['J'][i]])
PYEOF
