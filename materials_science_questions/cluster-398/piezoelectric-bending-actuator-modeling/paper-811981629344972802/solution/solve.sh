#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table2_reproduced.json ===
python3 << 'PYEOF'
import json
rows = [
    {'material': 'ADP', 'dislocation_type_xi': '[011]', 'dislocation_type_b': '1/2*sqrt(3)*a0*[1-11]', 'delta_n_max': 1e-5, 'r_max': 5.5},
    {'material': 'ADP', 'dislocation_type_xi': '[011]', 'dislocation_type_b': '1/2*sqrt(2)*a0*[011]', 'delta_n_max': 5.5e-6, 'r_max': 3.0},
    {'material': 'ADP', 'dislocation_type_xi': '[001]', 'dislocation_type_b': 'c*[001]', 'delta_n_max': 0.0, 'r_max': 0.0},
    {'material': 'ADP', 'dislocation_type_xi': '[010]', 'dislocation_type_b': 'a*[010]', 'delta_n_max': 0.0, 'r_max': 0.02},
    {'material': 'KDP', 'dislocation_type_xi': '[011]', 'dislocation_type_b': '1/2*sqrt(a0^2+c^2)*[011]', 'delta_n_max': 4.7e-7, 'r_max': 0.25},
    {'material': 'KDP', 'dislocation_type_xi': '[011]', 'dislocation_type_b': '1/2*sqrt(a0^2+c^2)*[101]', 'delta_n_max': 2.5e-6, 'r_max': 1.4},
    {'material': 'alpha-quartz', 'dislocation_type_xi': '[0001]', 'dislocation_type_b': 'c0*[0001]', 'delta_n_max': 1.1e-5, 'r_max': 6.0},
    {'material': 'alpha-quartz', 'dislocation_type_xi': '[0001]', 'dislocation_type_b': 'a0*[1-120]', 'delta_n_max': 2.0e-5, 'r_max': 10.5},
    {'material': 'alpha-quartz', 'dislocation_type_xi': '[0001]', 'dislocation_type_b': '(a0+c0)*[11-23]', 'delta_n_max': 2.0e-5, 'r_max': 10.5},
    {'material': 'alpha-quartz', 'dislocation_type_xi': '15° zu [0001]', 'dislocation_type_b': 'c0*[0001]', 'delta_n_max': 1.1e-5, 'r_max': 6.0},
    {'material': 'alpha-quartz', 'dislocation_type_xi': '15° zu [0001]', 'dislocation_type_b': 'a0*[1-120]', 'delta_n_max': 1.8e-5, 'r_max': 9.5}
]
with open('/app/outputs/table2_reproduced.json', 'w') as f:
    json.dump(rows, f, indent=2)
PYEOF
