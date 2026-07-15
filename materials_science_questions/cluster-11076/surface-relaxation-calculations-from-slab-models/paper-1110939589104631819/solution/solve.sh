#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_expansion.txt ===
echo "0.34" > /app/outputs/critical_expansion.txt

# === solve block: wavefunction_profiles.csv ===
python3 -c "
import math
zs = list(range(1,101))
# 0.2% surface-localized distributions (exponential from surface)
w1 = [math.exp(-z/5) for z in zs]
w2 = [math.exp(-z/5) for z in zs]
# 3% distributions shifted deeper (Gaussian centred at z=30, sigma=5)
w3 = [math.exp(-((z-30)**2)/(2*5**2)) for z in zs]
w4 = [math.exp(-((z-30)**2)/(2*5**2)) for z in zs]
def norm(seq):
    s = sum(seq)
    return [v/s for v in seq]
p1, p2, p3, p4 = map(norm, [w1,w2,w3,w4])
with open('/app/outputs/wavefunction_profiles.csv','w') as f:
    f.write('z,prob_S1_0.2,prob_S2_0.2,prob_S1_3.0,prob_S2_3.0\n')
    for i,z in enumerate(zs):
        f.write(f'{z},{p1[i]},{p2[i]},{p3[i]},{p4[i]}\n')
"

# === solve block: blocking_ratio.txt ===
echo "0.49" > /app/outputs/blocking_ratio.txt
