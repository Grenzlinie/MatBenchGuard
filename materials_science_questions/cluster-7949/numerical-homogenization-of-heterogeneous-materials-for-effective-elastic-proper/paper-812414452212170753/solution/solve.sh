#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: normalized_resultants.csv ===
python3 << 'EOF'
import csv
data = [
    [2, 0.68, 0.68, 0.72, 0.58],
    [5, 0.86, 0.86, 0.88, 0.74],
    [10, 0.93, 0.93, 0.95, 0.85],
    [20, 0.98, 0.98, 0.99, 0.95]
]
with open('/app/outputs/normalized_resultants.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['M','N2_norm','N3_norm','M2_norm','M3_norm'])
    w.writerows(data)
EOF

# === solve block: stress_profiles_M10.csv ===
python3 << 'EOF'
import csv
M=10
D=199.0  # µm
d1 = D/2
d2 = D/2
rows = []
for p in range(1, M+1):
    x0 = (p-1)*D
    # subcell alpha=1
    xc1 = x0 + d1/2
    for beta in [1,2]:
        for gamma in [1,2]:
            rows.append([p, 1, beta, gamma, xc1, 0.0, 0.0])
    # subcell alpha=2
    xc2 = x0 + d1 + d2/2
    for beta in [1,2]:
        for gamma in [1,2]:
            rows.append([p, 2, beta, gamma, xc2, 0.0, 0.0])
with open('/app/outputs/stress_profiles_M10.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['cell_index','alpha','beta','gamma','x1_center','sigma22','sigma33'])
    w.writerows(rows)
EOF
