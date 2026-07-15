#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cluster_results.csv ===
python3 << 'PYEOF'
import csv, os

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
csv_path = os.path.join(outdir, 'cluster_results.csv')
header = ['temperature', 'model', 'cluster_size', 'all_clusters_count', 'unique_clusters_count', 'average_lifetime_ps']

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
# The actual MD simulation and cluster analysis should populate this file.
PYEOF
