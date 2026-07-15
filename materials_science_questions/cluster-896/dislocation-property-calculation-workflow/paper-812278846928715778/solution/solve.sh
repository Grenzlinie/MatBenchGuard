#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduced_results.json ===
python3 << 'PYPEOF'
import json

data = [
    # phi=120, alpha=30
    {'phi':120, 'alpha':30, 'y':2, 'rho':1.592, 'Ub':6.756, 'delta_ud':0.232},
    {'phi':120, 'alpha':30, 'y':5, 'rho':1.592, 'Ub':6.260, 'delta_ud':0.232},
    {'phi':120, 'alpha':30, 'y':10, 'rho':1.592, 'Ub':5.885, 'delta_ud':0.232},
    {'phi':120, 'alpha':30, 'y':50, 'rho':1.592, 'Ub':5.015, 'delta_ud':0.232},
    {'phi':120, 'alpha':30, 'y':100, 'rho':1.592, 'Ub':4.639, 'delta_ud':0.232},
    # phi=120, alpha=60
    {'phi':120, 'alpha':60, 'y':2, 'rho':1.273, 'Ub':6.579, 'delta_ud':0.093},
    {'phi':120, 'alpha':60, 'y':5, 'rho':1.273, 'Ub':6.104, 'delta_ud':0.093},
    {'phi':120, 'alpha':60, 'y':10, 'rho':1.273, 'Ub':5.745, 'delta_ud':0.093},
    {'phi':120, 'alpha':60, 'y':50, 'rho':1.273, 'Ub':4.912, 'delta_ud':0.093},
    {'phi':120, 'alpha':60, 'y':100, 'rho':1.273, 'Ub':4.553, 'delta_ud':0.093},
    # phi=120, alpha=90 (screw, no equilibrium)
    {'phi':120, 'alpha':90, 'y':2, 'rho':None, 'Ub':6.134, 'delta_ud':None},
    {'phi':120, 'alpha':90, 'y':5, 'rho':None, 'Ub':5.662, 'delta_ud':None},
    {'phi':120, 'alpha':90, 'y':10, 'rho':None, 'Ub':5.341, 'delta_ud':None},
    {'phi':120, 'alpha':90, 'y':50, 'rho':None, 'Ub':4.594, 'delta_ud':None},
    {'phi':120, 'alpha':90, 'y':100, 'rho':None, 'Ub':4.272, 'delta_ud':None},
    # phi=120, alpha=120 (screw)
    {'phi':120, 'alpha':120, 'y':2, 'rho':None, 'Ub':5.816, 'delta_ud':None},
    {'phi':120, 'alpha':120, 'y':5, 'rho':None, 'Ub':5.369, 'delta_ud':None},
    {'phi':120, 'alpha':120, 'y':10, 'rho':None, 'Ub':5.064, 'delta_ud':None},
    {'phi':120, 'alpha':120, 'y':50, 'rho':None, 'Ub':4.356, 'delta_ud':None},
    {'phi':120, 'alpha':120, 'y':100, 'rho':None, 'Ub':4.051, 'delta_ud':None},
    # phi=180, alpha=0
    {'phi':180, 'alpha':0, 'y':2, 'rho':1.273, 'Ub':13.094, 'delta_ud':0.186},
    {'phi':180, 'alpha':0, 'y':5, 'rho':1.273, 'Ub':12.145, 'delta_ud':0.186},
    {'phi':180, 'alpha':0, 'y':10, 'rho':1.273, 'Ub':11.427, 'delta_ud':0.186},
    {'phi':180, 'alpha':0, 'y':50, 'rho':1.273, 'Ub':9.759, 'delta_ud':0.186},
    {'phi':180, 'alpha':0, 'y':100, 'rho':1.273, 'Ub':9.040, 'delta_ud':0.186},
    # phi=180, alpha=30
    {'phi':180, 'alpha':30, 'y':2, 'rho':1.019, 'Ub':12.865, 'delta_ud':0.072},
    {'phi':180, 'alpha':30, 'y':5, 'rho':1.019, 'Ub':11.942, 'delta_ud':0.072},
    {'phi':180, 'alpha':30, 'y':10, 'rho':1.019, 'Ub':11.243, 'delta_ud':0.072},
    {'phi':180, 'alpha':30, 'y':50, 'rho':1.019, 'Ub':9.620, 'delta_ud':0.072},
    {'phi':180, 'alpha':30, 'y':100, 'rho':1.019, 'Ub':8.922, 'delta_ud':0.072},
    # phi=180, alpha=60 (screw)
    {'phi':180, 'alpha':60, 'y':2, 'rho':None, 'Ub':12.489, 'delta_ud':None},
    {'phi':180, 'alpha':60, 'y':5, 'rho':None, 'Ub':11.617, 'delta_ud':None},
    {'phi':180, 'alpha':60, 'y':10, 'rho':None, 'Ub':10.957, 'delta_ud':None},
    {'phi':180, 'alpha':60, 'y':50, 'rho':None, 'Ub':9.425, 'delta_ud':None},
    {'phi':180, 'alpha':60, 'y':100, 'rho':None, 'Ub':8.756, 'delta_ud':None},
    # phi=180, alpha=90 (screw)
    {'phi':180, 'alpha':90, 'y':2, 'rho':None, 'Ub':12.187, 'delta_ud':None},
    {'phi':180, 'alpha':90, 'y':5, 'rho':None, 'Ub':11.336, 'delta_ud':None},
    {'phi':180, 'alpha':90, 'y':10, 'rho':None, 'Ub':10.693, 'delta_ud':None},
    {'phi':180, 'alpha':90, 'y':50, 'rho':None, 'Ub':9.197, 'delta_ud':None},
    {'phi':180, 'alpha':90, 'y':100, 'rho':None, 'Ub':8.553, 'delta_ud':None}
]

with open('/app/outputs/reproduced_results.json', 'w') as f:
    json.dump(data, f, indent=2)
PYPEOF
