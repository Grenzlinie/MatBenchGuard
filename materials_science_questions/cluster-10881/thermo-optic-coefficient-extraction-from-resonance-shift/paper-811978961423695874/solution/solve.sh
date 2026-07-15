#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json

quartz_exp = 1.44e-5
quartz_dn = -12.67e-5
calcite_exp = -0.54e-5
calcite_dn = -5.84e-5
wavelength = 6563

quartz_rel = quartz_exp + quartz_dn
calcite_rel = calcite_exp + calcite_dn
quartz_abs = quartz_rel * wavelength
calcite_abs = calcite_rel * wavelength

result = {
    "derived_formula": "d(ln λ′)/dT = d(ln d)/dT + d(ln Δn)/dT",
    "quartz_relative_coefficient": quartz_rel,
    "calcite_relative_coefficient": calcite_rel,
    "quartz_absolute_shift_A_per_deg": quartz_abs,
    "calcite_absolute_shift_A_per_deg": calcite_abs
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
