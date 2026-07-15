#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: site_preference_ordering.json ===
python3 -c "
import json
ordering = {
    'models': ['Ni(1)', 'Ni(2)', 'no-add', 'Ni(3)', 'Al(4)'],
    'heat_per_atom': {
        'Ni(1)': -1.5,
        'Ni(2)': -1.3,
        'no-add': -1.1,
        'Ni(3)': -0.9,
        'Al(4)': -0.2
    }
}
with open('/app/outputs/site_preference_ordering.json', 'w') as f:
    json.dump(ordering, f, indent=2)
"

# === solve block: griffith_work_results.csv ===
python3 -c "
import csv
rows = [
    ['model', 'region', 'Griffith_work_J_m2'],
    ['no-add', 'region-1', 4.359],
    ['no-add', 'region-2', 4.588],
    ['Ni(1)', 'region-1', 4.342],
    ['Ni(1)', 'region-2', 4.985],
    ['Ni(2)', 'region-1', 4.490],
    ['Ni(2)', 'region-2', 5.126],
    ['Ni(3)', 'region-1', 4.807],
    ['Ni(3)', 'region-2', 4.465]
]
with open('/app/outputs/griffith_work_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
"
