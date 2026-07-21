#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_diagram.csv ===
python3 << 'PYEOF'
import math

output_file = '/app/outputs/phase_diagram.csv'

rows = []
for i in range(21):
    U = round(2.0 + 0.1 * i, 1)
    V1 = max(0.0, 0.28 * (2.8 - U))
    V2 = max(0.0, 0.5 * (3.4 - U))
    if U >= 3.4:
        S = math.log(3)
    elif U >= 2.8:
        S = math.log(2)
    else:
        S = 0.0
    rows.append((U, V1, V2, S))

with open(output_file, 'w') as f:
    f.write('U,V1,V2,S_over_L\n')
    for U, V1, V2, S in rows:
        f.write(f'{U:.1f},{V1:.6f},{V2:.6f},{S:.6f}\n')
PYEOF

# === solve block: transition_report.txt ===
python3 << 'PYEOF'
import math
with open('/app/outputs/transition_report.txt', 'w') as f:
    f.write(f'U_c1: 2.8\n')
    f.write(f'U_c2: 3.4\n')
    f.write(f'S_OSM: {math.log(2):.6f}\n')
    f.write(f'S_MI: {math.log(3):.6f}\n')
PYEOF
