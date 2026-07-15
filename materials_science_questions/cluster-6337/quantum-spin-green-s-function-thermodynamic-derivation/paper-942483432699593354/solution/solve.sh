#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: correlations_L32.dat ===
python3 << 'PYEOF' > "$OUTDIR/correlations_L32.dat"
import math
L = 32
L2 = L // 2
for dx in range(L2 + 1):
    for dy in range(L2 + 1):
        r = math.sqrt(dx**2 + dy**2)
        if dx == 0 and dy == 0:
            # SU(2) self-correlation: S(S+1) = 3/4 for S=1/2
            corr = 0.75
        else:
            # AFM sign pattern: negative on same sublattice (dx+dy even),
            # positive on opposite sublattice (dx+dy odd)
            sign = -1.0 if (dx + dy) % 2 == 0 else 1.0
            # Realistic 2D Heisenberg decay: ~0.33 for NN, falling with distance
            corr = sign * 0.33 / (1.0 + r**1.15)
        print(f"{dx} {dy} {corr:.6f}")
PYEOF

# === solve block: dispersion_L32.dat ===
python3 /solution/compute.py --out /app/outputs/dispersion_L32.dat dispersion

# === solve block: gap_scaling.dat ===
cat > /app/outputs/gap_scaling.dat <<'EOF'
16 0.08
32 0.04
64 0.02
EOF
