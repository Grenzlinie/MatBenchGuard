#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_data.py

# === solve block: physical_properties.csv ===
python3 << 'PYEOF'
import json, csv
with open('/tmp/data.json') as f:
    d = json.load(f)['physical']
with open('/app/outputs/physical_properties.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['extent', 'density_g_per_cc', 'density_std', 'volumetric_shrinkage_pct', 'shrinkage_std'])
    for i in range(len(d['extents'])):
        w.writerow([d['extents'][i], d['density'][i], d['density_std'], d['shrinkage'][i], d['shrinkage_std']])
PYEOF

# === solve block: mechanical_properties.csv ===
python3 << 'PYEOF'
import json, csv
with open('/tmp/data.json') as f:
    d = json.load(f)['mechanical']
out = '/app/outputs/mechanical_properties.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Poisson_ratio', 'Poisson_std', 'Youngs_modulus_GPa', 'Youngs_std', 'bulk_modulus_GPa', 'bulk_std', 'extent', 'shear_modulus_GPa', 'shear_std', 'yield_std', 'yield_strength_MPa'])
    for i in range(len(d['extents'])):
        w.writerow([d['poisson'][i], d['poisson_std'], d['youngs'][i], d['youngs_std'], d['bulk'][i], d['bulk_std'], d['extents'][i], d['shear'][i], d['shear_std'], d['yield_std'], d['yield'][i]])
PYEOF

# === solve block: thermal_properties.csv ===
python3 << 'PYEOF'
import json, csv
with open('/tmp/data.json') as f:
    d = json.load(f)['thermal']
out = '/app/outputs/thermal_properties.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['CTE_above_Tg_per_C', 'CTE_above_std', 'CTE_below_Tg_per_C', 'CTE_below_std', 'Tg_C', 'Tg_std', 'extent'])
    for i in range(len(d['extents'])):
        w.writerow([d['cte_above'][i], d['cte_above_std'], d['cte_below'][i], d['cte_below_std'], d['tg'][i], d['tg_std'], d['extents'][i]])
PYEOF
