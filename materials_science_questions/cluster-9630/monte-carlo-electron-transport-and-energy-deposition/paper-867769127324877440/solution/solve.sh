#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_deposition_Ni63_spectrum.csv ===
python3 << 'EOF'
import math
L = 175.0
step = 8.0
with open('/app/outputs/energy_deposition_Ni63_spectrum.csv', 'w') as f:
    f.write('depth_nm,energy_deposition_eV_per_electron\n')
    for i in range(101):
        z = i * step
        val = 0.0 if z == 0.0 else (z / (L * L)) * math.exp(-z / L)
        f.write(f'{z:.1f},{val:.6e}\n')
EOF

# === solve block: energy_deposition_17keV_beam.csv ===
python3 /solution/generate_profile.py 200 2 14500 /app/outputs/energy_deposition_17keV_beam.csv
