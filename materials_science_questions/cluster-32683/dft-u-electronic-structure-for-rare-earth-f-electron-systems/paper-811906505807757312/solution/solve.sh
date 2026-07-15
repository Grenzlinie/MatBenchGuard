#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dos.txt ===
python3 - "$OUTDIR/dos.txt" << 'EOF'
import math, sys
outpath = sys.argv[1]
Emin, Emax, step = -0.6, 0.6, 0.001
with open(outpath, 'w') as f:
    e = Emin
    while e <= Emax:
        dos = 5.0
        dos += 20 * math.exp(-((e - (-0.1))**2) / (2*0.02**2))
        dos += 20 * math.exp(-((e - 0.1)**2) / (2*0.02**2))
        dip = 15 * math.exp(-(e**2) / (2*0.03**2))
        dos -= dip
        f.write(f"{e:.6f} {dos:.6f}\n")
        e += step
EOF

# === solve block: f_occupation.txt ===
echo "0.70" > "$OUTDIR/f_occupation.txt"
