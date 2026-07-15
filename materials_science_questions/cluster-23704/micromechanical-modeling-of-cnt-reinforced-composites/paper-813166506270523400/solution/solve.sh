#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: predicted_moduli.csv ===
python3 -c "
E1 = 4.0
G1 = 78.0
Gmin = 5.0
gamma = {1: G1, 10: 18.5, 20: 10.3}
rows = []
for vf in [1, 10, 20]:
    G = gamma[vf]
    E = E1 * ((G1 - Gmin) / (G - Gmin)) ** 2
    rows.append(f'{vf},{E}')
with open('/app/outputs/predicted_moduli.csv', 'w') as f:
    f.write('Vf,predicted_E\n')
    f.write('\n'.join(rows))
    f.write('\n')
"
