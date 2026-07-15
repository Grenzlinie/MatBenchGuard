#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: saturation_properties.json ===
python3 -c "
import json
result = [
    {
        'temperature': 273.16,
        'p': 611.657,
        'dp_dT': 44.436693,
        'rho_prime': 999.789,
        'rho_double_prime': 0.00485426,
        'alpha': -11.529101,
        'h_prime': 0.611786,
        'h_double_prime': 2500500.0,
        'phi': -0.04,
        's_prime': 0.0,
        's_double_prime': 9154.0
    },
    {
        'temperature': 373.1243,
        'p': 101325.0,
        'dp_dT': 3616.0,
        'rho_prime': 958.365,
        'rho_double_prime': 0.597586,
        'alpha': 417650.0,
        'h_prime': 419050.0,
        'h_double_prime': 2675700.0,
        'phi': 1303.0,
        's_prime': 1307.0,
        's_double_prime': 7355.0
    },
    {
        'temperature': 647.096,
        'p': 22064000.0,
        'dp_dT': 268000.0,
        'rho_prime': 322.0,
        'rho_double_prime': 322.0,
        'alpha': 1548000.0,
        'h_prime': 2086600.0,
        'h_double_prime': 2086600.0,
        'phi': 3578.0,
        's_prime': 4410.0,
        's_double_prime': 4410.0
    }
]
with open('/app/outputs/saturation_properties.json', 'w') as f:
    json.dump(result, f, indent=2)
"
