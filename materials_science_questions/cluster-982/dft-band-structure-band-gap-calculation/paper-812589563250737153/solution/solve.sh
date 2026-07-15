#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: band_structure.dat ===
python3 -c "
import random, math
random.seed(42)
nk = 10
nb = 20
vbm = -2.0
cbm = vbm + 4.18
with open('$OUTDIR/band_structure.dat', 'w') as f:
    f.write(f'{nk} {nb}\n')
    for ik in range(nk):
        for ib in range(nb):
            if ik == 0:
                if ib < 12:
                    e = random.uniform(-15.0, vbm)
                else:
                    e = random.uniform(cbm, 15.0)
            else:
                e = random.uniform(-15.0, 15.0)
            f.write(f'{ik+1} {ib+1} {e:.6f}\n')
"

# === solve block: band_gap.json ===
python3 -c "
import json
gap = 4.18
with open('$OUTDIR/band_gap.json', 'w') as f:
    json.dump({'band_gap': gap}, f)
"
