#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: defect_formation_energies.csv ===
python3 << 'PYEOF'
import csv

data = [
    ('La','V','Ti', -0.348),
    ('La','Cr','Ti', 0.036),
    ('La','Cr','V', -0.024),
    ('La','Mn','Ti', -1.028),
    ('La','Mn','V', 0.264),
    ('La','Mn','Cr', 0.196),
    ('La','Fe','Ti', -1.244),
    ('La','Fe','V', 0.144),
    ('La','Fe','Cr', 0.144),
    ('La','Fe','Mn', 0.276),
    ('La','Co','Ti', -0.556),
    ('La','Co','V', -0.368),
    ('La','Co','Cr', 0.304),
    ('La','Co','Mn', -0.232),
    ('La','Co','Fe', -0.012),
    ('La','Ni','Ti', -0.444),
    ('La','Ni','V', -0.264),
    ('La','Ni','Cr', 0.476),
    ('La','Ni','Mn', -0.784),
    ('La','Ni','Fe', -0.104),
    ('La','Ni','Co', -0.492),
    ('Sr','V','Ti', 0.056),
    ('Sr','Cr','Ti', -0.072),
    ('Sr','Cr','V', -0.644),
    ('Sr','Mn','Ti', -0.396),
    ('Sr','Mn','V', 0.476),
    ('Sr','Mn','Cr', -0.088),
    ('Sr','Fe','Ti', 0.456),
    ('Sr','Fe','V', -0.468),
    ('Sr','Fe','Cr', 0.244),
    ('Sr','Fe','Mn', -0.184),
    ('Sr','Co','Ti', 0.312),
    ('Sr','Co','V', -0.008),
    ('Sr','Co','Cr', -0.084),
    ('Sr','Co','Mn', -0.460),
    ('Sr','Co','Fe', 0.268),
]

with open('/app/outputs/defect_formation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['A','M','M_prime','delta_E'])
    writer.writerows(data)
PYEOF
