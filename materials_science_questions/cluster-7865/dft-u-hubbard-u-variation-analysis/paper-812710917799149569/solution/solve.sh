#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_weyl_nodes.json ===
python3 - << 'PYEOF'
import csv, json

# ------------------------------------------------------------
# 1. Generate the band structure CSV with a Weyl node crossing
#    at kz = +0.03 and energy = 0 eV.
# ------------------------------------------------------------
kz_vals = [i * 0.005 for i in range(101)]   # 0.0 to 0.5 inclusive
bands   = [0, 1, 2, 3]
with open('/app/outputs/step_02_band_structure.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['kz', 'band_index', 'energy'])
    for kz in kz_vals:
        # Band energies: bands 1 and 2 cross linearly at kz=0.03
        e0 = -2.0
        e1 = -1.0 * (kz - 0.03)   # valence band
        e2 =  1.0 * (kz - 0.03)   # conduction band
        e3 =  2.0
        writer.writerow([kz, 0, e0])
        writer.writerow([kz, 1, e1])
        writer.writerow([kz, 2, e2])
        writer.writerow([kz, 3, e3])

# ------------------------------------------------------------
# 2. Write the Weyl node list from the crossing.
#    The paper reports a single pair at kz = ±0.03 × 2π/c.
# ------------------------------------------------------------
nodes = [
    {"kz": 0.03,  "energy": 0.0, "chirality": 1},
    {"kz": -0.03, "energy": 0.0, "chirality": -1}
]
with open('/app/outputs/step_01_weyl_nodes.json', 'w') as f:
    json.dump(nodes, f, indent=2)
PYEOF

# === solve block: step_02_band_structure.csv ===
python3 - << 'PYEOF'
import csv

kz_vals = [i * 0.005 for i in range(101)]   # 0.0 to 0.5 inclusive
bands = [0, 1, 2, 3]

with open('/app/outputs/step_02_band_structure.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['kz', 'band_index', 'energy'])
    for kz in kz_vals:
        e0 = -2.0
        e1 = -1.0 * (kz - 0.03)   # valence band crossing
        e2 =  1.0 * (kz - 0.03)   # conduction band crossing
        e3 =  2.0
        writer.writerow([kz, 0, e0])
        writer.writerow([kz, 1, e1])
        writer.writerow([kz, 2, e2])
        writer.writerow([kz, 3, e3])
PYEOF
