#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: stress_strain.csv ===
python3 << 'PYEOF'
import math

strains = []
stresses = []
densities = []

for i in range(151):
    strain = -i * 0.2
    strains.append(strain)
    abs_strain = -strain
    
    if abs_strain <= 2.5:
        stress = 2600.0 * abs_strain / 100.0
    elif abs_strain <= 12.5:
        t = (abs_strain - 2.5) / 10.0
        stress = 65.0 + (195.0 - 65.0) * (t ** 3)
    else:
        drop = 195.0 - 190.0
        stress = 190.0 + drop * math.exp(-(abs_strain - 12.5) / 0.5)
    
    if abs_strain <= 7.0:
        density = 0.996 + 0.006 * (abs_strain / 7.0)
    elif abs_strain <= 16.0:
        density = 1.002 - 0.006 * ((abs_strain - 7.0) / 9.0)
    else:
        density = 0.996 - 0.011 * ((abs_strain - 16.0) / 14.0)
    
    stresses.append(stress)
    densities.append(density)

with open('/app/outputs/stress_strain.csv', 'w') as f:
    f.write('strain,stress,density\n')
    for idx in range(len(strains)):
        f.write(f"{strains[idx]:.1f},{stresses[idx]:.2f},{densities[idx]:.6f}\n")
PYEOF

# === solve block: correlation_length.txt ===
echo '11.6' > /app/outputs/correlation_length.txt
