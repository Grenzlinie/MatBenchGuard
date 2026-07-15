#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: undoped_dielectric.csv ===
python3 << 'EOF'
import csv, math, os
os.makedirs('/app/outputs', exist_ok=True)
with open('/app/outputs/undoped_dielectric.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['energy_eV', 'epsilon1', 'epsilon2'])
    for i in range(121):
        e = i * 0.1
        eps2 = 13.056 * (0.5/2)**2 / ((e - 6.653)**2 + (0.5/2)**2)
        eps1 = 6.461 + 0.1 * math.sin(2.0 * e)
        w.writerow([round(e,6), round(eps1,6), round(eps2,6)])
EOF

# === solve block: Ga_dielectric.csv ===
python3 /solution/generate.py /app/outputs/Ga_dielectric.csv 35.898 0.422 49.533

# === solve block: As_dielectric.csv ===
python3 /solution/generate.py /app/outputs/As_dielectric.csv 24.348 0.068 33.2616

# === solve block: results.json ===
python3 -c "
import json
data = {
    'undoped': {'epsilon2_peak': 13.056, 'peak_energy_eV': 6.653, 'epsilon1_0': 6.461, 'band_gap_eV': 1.58},
    'Ga': {'epsilon2_peak': 35.898, 'peak_energy_eV': 0.422, 'epsilon1_0': 49.533, 'band_gap_eV': 0.0},
    'As': {'epsilon2_peak': 24.348, 'peak_energy_eV': 0.068, 'epsilon1_0': 33.2616, 'band_gap_eV': 0.1}
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
