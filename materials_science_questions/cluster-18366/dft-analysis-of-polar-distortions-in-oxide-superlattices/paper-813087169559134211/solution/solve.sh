#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_diagram.csv ===
python3 << 'PYEOF'
import csv
rows = []
for i in range(0, 101):
    r = i / 100.0
    if r < 0.2:
        dt = 'A'
    elif r < 0.4:
        dt = 'T'
    elif r < 0.7:
        dt = 'H'
    else:
        dt = 'V'
    rows.append((r, dt))
with open('/app/outputs/phase_diagram.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['r', 'domain_type'])
    w.writerows(rows)
PYEOF

# === solve block: transition_points.json ===
python3 << 'PYEOF'
import json
data = {'T_to_H': 0.4, 'H_to_V': 0.7}
with open('/app/outputs/transition_points.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
