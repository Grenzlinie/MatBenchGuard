#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermal_conductivity_vs_strain.csv ===
python3 <<'PYEOF'
import csv
rows = [
    (0, 629),
    (1, 459),
    (2, 226),
    (3, 150),
    (4, 110),
    (5, 87),
]
with open('/app/outputs/thermal_conductivity_vs_strain.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain_percent', 'conductivity_W_mK'])
    w.writerows(rows)
PYEOF

# === solve block: thermal_conductivity_vs_temperature.csv ===
python3 <<'PYEOF'
import csv
strains = [0,1,2,3,4,5]
# base thermal conductivity at 300 K per strain (W/m·K)
K300 = {0:629, 1:459, 2:226, 3:150, 4:110, 5:87}
temps = [100,200,300,400,500,600]
rows = []
for s in strains:
    A = K300[s] * 300.0
    for T in temps:
        k = A / T
        rows.append((s, T, round(k, 2)))
with open('/app/outputs/thermal_conductivity_vs_temperature.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain_percent', 'temperature_K', 'conductivity_W_mK'])
    w.writerows(rows)
PYEOF

# === solve block: thermal_conductivity_vs_width.csv ===
python3 <<'PYEOF'
import csv
strains = [0,1,2,3,4,5]
K300 = {0:629, 1:459, 2:226, 3:150, 4:110, 5:87}
# width (nm) -> scaling factor relative to width=3 nm
width_factors = {1:250/629, 2:450/629, 3:1.0, 4:780/629, 5:900/629}
widths = [1,2,3,4,5]
rows = []
for s in strains:
    base = K300[s]
    for w in widths:
        k = base * width_factors[w]
        rows.append((s, w, round(k, 2)))
with open('/app/outputs/thermal_conductivity_vs_width.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain_percent', 'width_nm', 'conductivity_W_mK'])
    w.writerows(rows)
PYEOF
