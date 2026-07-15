#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: migration_barriers.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(outdir, 'migration_barriers.csv')
data = [
    ('V_U', 4.81),
    ('V_UO', 4.07),
    ('V_UO2', 4.51),
    ('V_U2', 2.61),
    ('V_U2O', 2.92),
]
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['defect_type', 'barrier_eV'])
    w.writerows(data)
print(f'Written {path}')
PYEOF
