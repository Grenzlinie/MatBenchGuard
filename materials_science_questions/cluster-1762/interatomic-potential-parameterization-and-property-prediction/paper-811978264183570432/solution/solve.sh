#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_bulk_moduli.csv ===
python3 << 'PYEOF'
import math

B1 = 814.0
B2 = 693.0
r0_CaF2 = 0.23655
r0_SrF2 = 0.25096

v_ratio = (r0_SrF2 / r0_CaF2) ** 3

compositions = [
    ('CaF2', 0.0),
    ('Ca90Sr10F2', 0.1),
    ('Ca80Sr20F2', 0.2),
    ('Ca70Sr30F2', 0.3),
    ('Ca50Sr50F2', 0.5),
    ('Ca40Sr60F2', 0.6),
    ('Ca30Sr70F2', 0.7),
    ('Ca10Sr90F2', 0.9),
    ('SrF2', 1.0),
]

with open('/app/outputs/computed_bulk_moduli.csv', 'w') as f:
    f.write('composition,B_kbar\n')
    for comp, x in compositions:
        num = 1.0 + x * (v_ratio - 1.0)
        denom = 1.0 + x * ((B1 / B2) * v_ratio - 1.0)
        B = num / denom * B1
        f.write(f'{comp},{B}\n')
PYEOF
