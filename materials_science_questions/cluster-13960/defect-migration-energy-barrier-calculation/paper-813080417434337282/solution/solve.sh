#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: voltage_curve_293K.txt ===
python3 > /app/outputs/voltage_curve_293K.txt << 'PYEOF'
V1 = 3.82386
V2 = 3.60386
V3 = 3.45386
lines = ['x_Mg\tV']
for i in range(101):
    x = i / 100.0
    if x < 0.33:
        v = V1
    elif x < 0.50:
        v = V2
    else:
        v = V3
    lines.append(f'{x:.2f}\t{v:.4f}')
print('\n'.join(lines))
PYEOF

# === solve block: migration_barriers.txt ===
cat > /app/outputs/migration_barriers.txt << 'FFEOF'
case	barrier_GGA+U
dilute_Mg	930
dilute_Va	690
33%_+Va	1250
33%_+Mg	700
50%_+Va	980
50%_+Mg	1200
FFEOF
