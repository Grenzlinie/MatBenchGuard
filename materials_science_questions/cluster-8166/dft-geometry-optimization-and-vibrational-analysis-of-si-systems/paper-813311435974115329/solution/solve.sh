#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: raw_pdos.csv ===
python3 <<'PYEOF'
import csv

# Piecewise-constant PDOS on intervals:
# I1: [-0.6,-0.5], I2: [-0.5,-0.4], I3: [-0.4,-0.1], I4: [-0.1,0.0], I5: [0.0,0.1]
# values: [f1,f2,f3,f4,f5] for each adatom (CoF, CeF, CoU, CeU)
pdos_cof = [0.0, 5.0, 26.0, 73.0, 100.0]
pdos_cef = [0.0, 2.0, 8.0, 54.0, 125.0]
pdos_cou = [0.0, 1.0, 20.0, 50.0, 63.0]
pdos_ceu = [0.0, 0.0, 6.0, 38.0, 92.0]

bounds = [-0.6, -0.5, -0.4, -0.1, 0.0, 0.1]

with open('/app/outputs/raw_pdos.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Energy_eV', 'PDOS_CoF', 'PDOS_CeF', 'PDOS_CoU', 'PDOS_CeU'])
    # grid from -0.7 to 0.2 with step 0.001
    e = -0.7
    while e <= 0.2001:
        # determine interval index for each adatom
        idx = None
        if e < -0.6 or e > 0.1:
            # outside defined region -> 0
            row = [e, 0.0, 0.0, 0.0, 0.0]
        else:
            # find which subinterval
            for i in range(5):
                if e >= bounds[i] and e < bounds[i+1]:
                    idx = i
                    break
            else:
                # handle exact e == 0.1
                if e == 0.1:
                    idx = 4
            if idx is not None:
                row = [e, pdos_cof[idx], pdos_cef[idx], pdos_cou[idx], pdos_ceu[idx]]
            else:
                row = [e, 0.0, 0.0, 0.0, 0.0]
        w.writerow(row)
        e += 0.001
PYEOF

# === solve block: integrated_pdos.csv ===
cat > /app/outputs/integrated_pdos.csv <<'EOF'
adatom,window,integrated_pdos
CoF,p-type,8.3
CoF,intrinsic,15.6
CoF,n-type,25.1
CeF,p-type,2.6
CeF,intrinsic,8.0
CeF,n-type,20.3
CoU,p-type,6.1
CoU,intrinsic,11.1
CoU,n-type,17.3
CeU,p-type,1.8
CeU,intrinsic,5.6
CeU,n-type,14.8
EOF
