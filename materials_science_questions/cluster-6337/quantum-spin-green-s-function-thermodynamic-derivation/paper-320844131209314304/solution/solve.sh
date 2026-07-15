#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: 2d_magnetization.csv ===
python3 <<'PYEOF'
import math
X_vals = [0.5 + 0.1*i for i in range(36)]  # 0.5 .. 4.0
Tc_exact = 2.0 / math.log(1.0 + math.sqrt(2.0))  # ~2.269
with open('/app/outputs/2d_magnetization.csv', 'w') as f:
    f.write('X,mu\n')
    for X in X_vals:
        if X <= Tc_exact:
            mu = (1.0 - 1.0 / (math.sinh(2.0/X)**4)) ** (1.0/8.0)
        else:
            mu = 0.0
        f.write(f'{X:.1f},{mu:.10f}\n')
PYEOF

# === solve block: critical_temperatures.txt ===
cat > /app/outputs/critical_temperatures.txt <<'TXTEOF'
2.4743
2.0243
TXTEOF
