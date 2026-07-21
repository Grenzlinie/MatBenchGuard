#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: Tc_vs_c.csv ===
python3 << 'PYEOF' > "$OUTDIR/Tc_vs_c.csv"
import math

print("c,Tc_K")
Tcmax = 1200.0  # approximate peak from Fig. 2
for i in range(0, 21):
    c = i * 0.1
    # sine envelope: peak at c=1, zero at 0 and 2, monotonic between
    tc = Tcmax * math.sin(math.pi * c / 2.0)
    print(f"{c:.1f},{tc:.6f}")
PYEOF
