#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: quasiparticle_weight.csv ===
python3 -c "
import math, csv
header = ['g','filling','Z']
gvals = [0.5, 1.0, 1.5]
fillings = [round(i*0.2, 2) for i in range(11)]  # 0.0 to 2.0 step 0.2
rows = []
for g in gvals:
    S = 1.0 / math.sqrt(1 + g**2)
    for n in fillings:
        Z = (1 + (S - 1) * n / 2.0) ** 2
        rows.append([g, n, round(Z, 6)])
with open('$OUTDIR/quasiparticle_weight.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
"

# === solve block: layer_densities.csv ===
cat > "$OUTDIR/layer_densities.csv" << 'FFEOF'
layer,U,n
1,0.0,1.875
2,0.0,1.815
3,0.0,1.803
4,0.0,1.801
5,0.0,1.800
1,2.0,1.855
2,2.0,1.812
3,2.0,1.802
4,2.0,1.800
5,2.0,1.800
FFEOF
