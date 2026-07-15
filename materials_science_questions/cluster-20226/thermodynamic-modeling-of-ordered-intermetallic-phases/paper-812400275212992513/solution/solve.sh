#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: equilibrium_data.csv ===
python3 << 'PYEOF'
import csv
import json
import math

with open('/solution/input_spec.json') as f:
    spec = json.load(f)
pairs = spec['equilibrium_pairs']

rows = []
for A, w in pairs:
    if A < 4 and (-1 + A/4) <= w <= (1 - A/4):
        # two-phase equilibrium
        denom = 4 - A
        x = 1.0 - (A * w) / denom
        y = -1.0 - (A * w) / denom
        z = 0.5 + 2.0 * w / denom
        phi = (A / 4.0) - (A * w * w) / denom
    else:
        if (A < 4 and w < -1 + A/4) or (A >= 4 and w < 0):
            # single-phase beta
            z = 0.0
            y = w
            x = w
            phi = (1.0 + w)**2
        else:
            # single-phase alpha
            z = 1.0
            x = w
            y = w
            phi = (1.0 - w)**2
    rows.append([A, w, x, y, z, phi])

with open('/app/outputs/equilibrium_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['A','w','x','y','z','phi'])
    for r in rows:
        writer.writerow(r)
PYEOF

# === solve block: field_boundaries.csv ===
python3 << 'PYEOF'
import csv
import json

with open('/solution/input_spec.json') as f:
    spec = json.load(f)
A_vals = spec['field_A_values']

rows = []
for A in A_vals:
    if A < 4:
        w_lower = -1.0 + A/4.0
        w_upper = 1.0 - A/4.0
    else:
        w_lower = 0.0
        w_upper = 0.0
    rows.append([A, w_lower, w_upper])

with open('/app/outputs/field_boundaries.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['A','w_lower','w_upper'])
    for r in rows:
        writer.writerow(r)
PYEOF
