#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: vacancy_defect_results.json ===
python3 -c "
import json, math
Tm = 1473.0
C = 2.14e-3
eV_J = 1.602176634e-19
kB = 1.380649e-23
NA = 6.02214076e23

delta_H_s_eV = C * Tm
energy_per_defect_J = delta_H_s_eV * eV_J
arg = - (delta_H_s_eV * eV_J) / (2 * kB * Tm)
X_Si_v = math.exp(arg)
excess = X_Si_v * NA * energy_per_defect_J

result = {
    'delta_H_s_eV': delta_H_s_eV,
    'X_Si_v_per_mol': X_Si_v,
    'energy_per_defect_J': energy_per_defect_J,
    'excess_molar_energy_J_per_mol': excess
}
with open('/app/outputs/vacancy_defect_results.json', 'w') as f:
    json.dump(result, f)
"
