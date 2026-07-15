#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table1.csv ===
python3 -c "
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ('APW', 0.476, 0.327, 1.112, 0.022, 0.001, 1.062),
    ('RAPW', 0.594, 0.369, 0.958, 0.018, 0.002, 1.059),
]
with open(os.path.join(outdir, 'table1.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['calculation','n_s','n_p','n_d','n_f','n_g','n_out'])
    w.writerows(rows)
"

# === solve block: table2.csv ===
# Write Table 2 (spin-orbit-resolved)
cat > "$OUTDIR/table2.csv" <<'EOF'
state,n_state
s1/2,0.594
p3/2,0.259
p1/2,0.110
d5/2,0.545
d3/2,0.413
f7/2,0.010
f5/2,0.008
g9/2,0.001
g7/2,0.001
n_out,1.059
EOF
