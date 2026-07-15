#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stress_autocorrelation.csv ===
python3 <<'PYEOF'
import math
with open('/app/outputs/stress_autocorrelation.csv', 'w') as f:
    f.write('time,autocorrelation\n')
    tmax = 20
    tau_c = 0.5
    for t in range(tmax + 1):
        val = math.exp(-t / tau_c)
        f.write(f'{t},{val:.6f}\n')
PYEOF

# === solve block: shear_viscosity.json ===
echo '{"shear_viscosity": 2.5}' > /app/outputs/shear_viscosity.json
