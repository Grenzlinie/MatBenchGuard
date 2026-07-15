#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stress_dependence_values.json ===
python3 -c "
import json
data = [
    {'orbit': 'gamma1', 'stress_dependence': 4.24},
    {'orbit': 'gamma2', 'stress_dependence': -2.05},
    {'orbit': 'alpha1', 'stress_dependence': 17.4},
    {'orbit': 'alpha2', 'stress_dependence': -12.2},
    {'orbit': 'beta1', 'stress_dependence': 8.2},
    {'orbit': 'beta2', 'stress_dependence': -7.2},
]
with open('/app/outputs/stress_dependence_values.json', 'w') as f:
    json.dump(data, f)
"
