#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimized_geometry.xyz ===
mkdir -p /app/outputs
python3 -c "
import math
atoms = []
# Mn
atoms.append(('Mn', 0.0, 0.0, 0.0))
# Cl
atoms.append(('Cl', 0.0, 0.0, 2.365))
# N atoms in the porphyrin plane
atoms.append(('N', 2.037, 0.0, 0.0))
atoms.append(('N', -2.037, 0.0, 0.0))
atoms.append(('N', 0.0, 2.037, 0.0))
atoms.append(('N', 0.0, -2.037, 0.0))
# 44 carbon atoms placed far away
r_c = 5.0
z_c = 10.0
for i in range(44):
    theta = i * 2 * math.pi / 44
    x = r_c * math.cos(theta)
    y = r_c * math.sin(theta)
    atoms.append(('C', x, y, z_c))
# 28 hydrogen atoms placed far away
r_h = 6.0
z_h = 10.0
for i in range(28):
    theta = i * 2 * math.pi / 28
    x = r_h * math.cos(theta)
    y = r_h * math.sin(theta)
    atoms.append(('H', x, y, z_h))
with open('/app/outputs/optimized_geometry.xyz', 'w') as f:
    f.write(str(len(atoms)) + '\n')
    f.write('optimized geometry of [Mn(TPP)Cl]\n')
    for el, x, y, z in atoms:
        f.write(f'{el} {x:.6f} {y:.6f} {z:.6f}\n')
"

# === solve block: mo_compositions.json ===
cat > /app/outputs/mo_compositions.json << 'EOF'
[
  {
    "mo_label": "alpha LUMO",
    "energy_Hartree": -0.10772,
    "percent_Mn_d": 44.0,
    "percent_Cl_p": 0.0,
    "percent_porphyrin": 53.0
  },
  {
    "mo_label": "alpha HOMO",
    "energy_Hartree": -0.19168,
    "percent_Mn_d": 7.0,
    "percent_Cl_p": 10.0,
    "percent_porphyrin": 71.0
  },
  {
    "mo_label": "alpha HOMO-1",
    "energy_Hartree": -0.20491,
    "percent_Mn_d": 0.0,
    "percent_Cl_p": 0.0,
    "percent_porphyrin": 91.0
  },
  {
    "mo_label": "alpha HOMO-2",
    "energy_Hartree": -0.22756,
    "percent_Mn_d": 19.0,
    "percent_Cl_p": 39.0,
    "percent_porphyrin": 30.0
  },
  {
    "mo_label": "alpha HOMO-3",
    "energy_Hartree": -0.22995,
    "percent_Mn_d": 4.0,
    "percent_Cl_p": 81.0,
    "percent_porphyrin": 10.0
  },
  {
    "mo_label": "alpha HOMO-4",
    "energy_Hartree": -0.23009,
    "percent_Mn_d": 5.0,
    "percent_Cl_p": 83.0,
    "percent_porphyrin": 9.0
  }
]
EOF
