#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: surface_tensions.json ===
python3 -c "
import json, math

# Constants
sigma = 1.0
eps = 1.0
z = {111: 3, 110: 5, 100: 4}
area = {111: math.sqrt(3)/2, 110: math.sqrt(2), 100: 1.0}

# Surface tensions
tensions = {}
for plane in (111, 110, 100):
    gamma = (z[plane]*eps/2) / area[plane]
    tensions[str(plane)] = gamma

# gamma_111/T_coll for delta sequence
deltas = [0.1, 0.01, 0.001]
ratio_list = []
gamma_111 = tensions['111']
for d in deltas:
    T_coll = 2*eps / math.log(1/d)
    ratio = gamma_111 / T_coll
    ratio_list.append({'delta': d, 'ratio': ratio})

output = {
    '111': tensions['111'],
    '110': tensions['110'],
    '100': tensions['100'],
    'gamma_over_T_coll': ratio_list
}

with open('/app/outputs/surface_tensions.json', 'w') as f:
    json.dump(output, f, indent=2)
    f.write('\n')
"
