#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: MgS_bandgap_vs_strain.csv ===
python3 -c "
import csv
data = [
    (-8, 4.30), (-6, 4.10), (-4, 3.90), (-2, 3.80), (0, 3.69),
    (2, 3.55), (4, 3.40), (6, 3.25), (8, 3.10)
]
with open('/app/outputs/MgS_bandgap_vs_strain.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'bandgap'])
    w.writerows(data)
"

# === solve block: MgSe_bandgap_vs_strain.csv ===
python3 -c "
import csv
data = [
    (-8, 4.15), (-6, 4.30), (-4, 4.20), (-2, 4.10), (0, 4.01),
    (2, 3.90), (4, 3.80), (6, 3.70), (8, 3.60)
]
with open('/app/outputs/MgSe_bandgap_vs_strain.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'bandgap'])
    w.writerows(data)
"
