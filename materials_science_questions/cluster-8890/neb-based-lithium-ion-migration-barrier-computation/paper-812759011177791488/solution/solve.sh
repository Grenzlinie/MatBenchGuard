#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lisi_correlation.csv ===
# Write LiSi correlation CSV
python3 << 'PYEOF'
import csv
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ['LiSi-St-1', 5.0e-6, 67.2],
    ['LiSi-St-2', 11.3e-6, 73.4],
    ['LiSi-St-3', 6.5e-6, 68.5],
    ['LiSi-St-4', 8.0e-6, 70.0],
    ['LiSi-St-5', 12.0e-6, 75.0],
]

path = os.path.join(outdir, 'lisi_correlation.csv')
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['structure_id', 'D_Li', 'channel_area_fraction'])
    writer.writerows(rows)
PYEOF

# === solve block: li2si_correlation.csv ===
# Write Li2Si correlation CSV
python3 << 'PYEOF'
import csv
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ['Li2Si-St-1', 5.0e-6, 3500],
    ['Li2Si-St-2', 6.5e-6, 3200],
    ['Li2Si-St-3', 7.0e-6, 2900],
    ['Li2Si-St-4', 8.5e-6, 2600],
    ['Li2Si-St-5', 10.0e-6, 2300],
]

path = os.path.join(outdir, 'li2si_correlation.csv')
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['structure_id', 'D_Li', 'total_microstructures'])
    writer.writerows(rows)
PYEOF

# === solve finalize ===
echo "Oracle artifacts written."
