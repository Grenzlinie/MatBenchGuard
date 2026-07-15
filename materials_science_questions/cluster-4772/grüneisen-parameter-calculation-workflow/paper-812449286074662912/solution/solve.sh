#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: TOECs.json ===
python3 -c "
import json

# TOECs
toecs = {
    'nu1': -95,
    'nu2': -70,
    'nu3': -22,
    'C111': -692,
    'C112': -234,
    'C123': -95,
    'C144': -70,
    'C155': -115,
    'C456': -23
}
with open('$OUTDIR/TOECs.json', 'w') as f:
    json.dump(toecs, f)

# temperature_pressure_derivatives
deriv = {
    'dS_dT_GPa_K': -0.0087,
    'dB_dT_GPa_K': -0.00775,
    'dS_dP_none': 0.92,
    'dB_dP_none': 5.30,
    'gamma_11': 1.89,
    'gamma_44': 0.83
}
with open('$OUTDIR/temperature_pressure_derivatives.json', 'w') as f:
    json.dump(deriv, f)
"

# === solve block: temperature_pressure_derivatives.json ===
cat > /app/outputs/temperature_pressure_derivatives.json <<'FFEOF'
{
  "dS_dT_GPa_K": -0.0087,
  "dB_dT_GPa_K": -0.00775,
  "dS_dP_none": 0.92,
  "dB_dP_none": 5.30,
  "gamma_11": 1.89,
  "gamma_44": 0.83
}
FFEOF
