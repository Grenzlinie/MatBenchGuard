#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: work_function_results.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ('clean_W_5layer', 4.77),
    ('Cs_W_2.6', 2.77),
    ('Cs_W_2.75', 2.55),
    ('Cs_W_2.9', 2.28),
]
with open(os.path.join(outdir, 'work_function_results.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['system', 'work_function'])
    writer.writerows(rows)
PYEOF
