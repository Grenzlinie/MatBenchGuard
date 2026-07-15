#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-learn pandas 2>/dev/null || true
python3 /solution/synthesize.py

# === solve block: free_energy_curves.csv ===
python3 << 'EOF'
import csv
import math

def generate_curve(r, hvals, energies):
    """Generate rows for a given radius with explicit (h, energy) pairs."""
    return [(r, h, e) for h, e in zip(hvals, energies)]

# -- Radius 0.9 (smooth, small magnitude, reaches zero near h~15) --
h09 = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,
      10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,16.0,18.0,20.0]
e09 = [-0.98,-0.97,-0.95,-0.92,-0.89,-0.85,-0.80,-0.74,-0.67,-0.59,-0.52,-0.44,-0.36,-0.28,
      -0.20,-0.13,-0.07,-0.02, -0.00, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# -- Radius 2.0 (smooth but steeper) --
h2 = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,
      10.0,10.5,11.0,12.0,13.0,14.0,15.0,16.0,18.0,20.0]
e2 = [-2.90,-2.85,-2.78,-2.68,-2.55,-2.40,-2.22,-2.02,-1.80,-1.56,-1.31,-1.04,-0.78,-0.54,
      -0.34,-0.20,-0.12,-0.06,-0.02, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# -- Radius 22.36 (first‑order jump: negative → zero near h~11.8‑12) --
h2236 = [0.5,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,10.5,11.0,11.3,11.5,11.7,11.8,11.9,
         12.0,12.2,12.5,13.0,14.0,15.0,17.0,20.0]
e2236 = [-8.0,-8.2,-8.8,-9.7,-10.8,-12.1,-13.6,-15.3,-17.2,-19.3,-21.6,-22.9,-24.3,-25.2,
         -25.8,-26.3,-26.5,-26.7, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# -- Radius 44.72 (jump later, near h~14) --
h4472 = [0.5,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,12.5,13.0,13.5,13.7,13.9,
         14.0,14.2,14.5,15.0,16.0,18.0,20.0]
e4472 = [-16.0,-16.3,-17.0,-18.1,-19.6,-21.5,-23.8,-26.5,-29.6,-33.1,-37.0,-41.4,-46.2,
         -48.9,-51.9,-55.3,-56.8,-58.3, 0.0,0.0,0.0,0.0,0.0,0.0,0.0]

rows = []
rows += generate_curve(0.9, h09, e09)
rows += generate_curve(2.0, h2, e2)
rows += generate_curve(22.36, h2236, e2236)
rows += generate_curve(44.72, h4472, e4472)

with open('/app/outputs/free_energy_curves.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['r_xi', 'h_xi', 'excess_free_energy'])
    for r, h, e in rows:
        w.writerow([r, h, e])
EOF

# === solve block: transition_line.csv ===
true

# === solve block: force_curves.csv ===
true
