#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_lengths.csv ===
python3 -u <<'PYEOF'
import math

def comp_lc(us):
    # us = understress (tau_p-tau_0)/tau_p, < 0.4
    # blending near 0: lc ~ 0.418*us, near 0.4: lc ~ 0.03333/(0.4-us)
    A = 0.03333
    return 0.418 * us + A * (1.0/(0.4 - us) - 2.5)

def comp_ac(us):
    # ac ~ 0.579 at us=0, diverges as 0.012732/(0.4-us)^2
    C = 0.012732
    return 0.579 - C/(0.4**2) + C/((0.4 - us)**2)

understress_values = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.38, 0.40, 0.45, 0.50, 0.55, 0.60]
with open('/app/outputs/critical_lengths.csv', 'w') as f:
    f.write('critical_HF_length,critical_slip_length,understress_normalized\n')
    for us in understress_values:
        if us >= 0.4:
            f.write(f'stable,stable,{us}\n')
        else:
            lc = comp_lc(us)
            ac = comp_ac(us)
            f.write(f'{lc:.4f},{ac:.4f},{us}\n')
PYEOF
