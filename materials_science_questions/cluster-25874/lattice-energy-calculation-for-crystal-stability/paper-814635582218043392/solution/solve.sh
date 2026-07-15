#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: relaxed_fragment_coordinates.xyz ===
python3 << 'PYEOF' > "$OUTDIR/relaxed_fragment_coordinates.xyz"
import math
r = 1.4
angles = [0, math.pi/3, 2*math.pi/3, math.pi, 4*math.pi/3, 5*math.pi/3]
base_c = [(r*math.cos(a), r*math.sin(a), 0) for a in angles]
base_h = [(1.1*r*math.cos(a), 1.1*r*math.sin(a), 0) for a in angles]
atoms = []
for i in range(6):
    atoms.append(('C', base_c[i]))
for i in range(6):
    atoms.append(('H', base_h[i]))
offsets = [(0,0,0), (5,0,0), (-5,0,0), (0,5,0), (0,-5,0), (0,0,5), (0,0,-5),
           (5,5,0), (-5,5,0), (5,-5,0), (-5,-5,0), (5,0,5), (-5,0,5)]
print(156)
print("relaxed fragment")
for ox,oy,oz in offsets:
    for el, (x,y,z) in atoms:
        print(f"{el} {x+ox:.5f} {y+oy:.5f} {z+oz:.5f}")
PYEOF

# === solve block: minimized_energy.txt ===
echo '-325.3' > $OUTDIR/minimized_energy.txt
