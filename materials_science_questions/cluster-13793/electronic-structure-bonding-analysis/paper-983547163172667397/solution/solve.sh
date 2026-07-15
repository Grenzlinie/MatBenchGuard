#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json, sys
sys.path.insert(0, '/solution')
from elasticity import compute_all

systems = [
    ('Cu3P', 200, 90, 85, 225, 45),
    ('CuPIn', 190, 80, 75, 205, 60),
    ('CuPSi', 195, 85, 80, 210, 55),
    ('CuPSc', 185, 80, 75, 200, 35),
    ('CuPTa', 190, 85, 80, 210, 30)
]
results = []
for name, c11, c12, c13, c33, c44 in systems:
    props = compute_all(c11, c12, c13, c33, c44)
    results.append({
        'name': name,
        'bulk_modulus_GPa': round(props['B'], 2),
        'shear_modulus_GPa': round(props['G'], 2),
        'youngs_modulus_GPa': round(props['E'], 2),
        'poisson_ratio': round(props['v'], 3),
        'hardness_GPa': round(props['Hv'], 2)
    })

with open('/app/outputs/results.json', 'w') as f:
    json.dump({'systems': results}, f, indent=2)
"
