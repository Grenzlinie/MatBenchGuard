#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# Compute exact classical nucleation free-energy barriers
python3 << 'PYEOF'
import math
delta_Ts = [1, 2, 5, 10, 20, 30, 40, 50]
B = 0.85
c3 = (16*math.pi/3) * B * (100*B)**2
c2 = 4 * B * (100*B)
with open("/app/outputs/homogeneous_3d_barrier.csv", "w") as f:
    f.write("delta_T,G_dimensionless\n")
    for dT in delta_Ts:
        f.write(f"{dT},{c3 / dT**2}\n")
with open("/app/outputs/heterogeneous_2d_smooth_barrier.csv", "w") as f:
    f.write("delta_T,G_dimensionless\n")
    for dT in delta_Ts:
        f.write(f"{dT},{c2 / dT}\n")
PYEOF
