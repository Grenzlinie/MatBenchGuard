#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: surf_formation_energy_fit.json ===
python3 -c "
import json

# [1-10] quadratic: f(eps) = -1.1*eps + 16.6667*eps^2
eps_1 = [-0.02, 0.0, 0.01, 0.027, 0.04]
gA_1 = [-1.1*e + 16.6667*e**2 for e in eps_1]
fit_1 = [0.0, -1.1, 16.6667]
stress_0_1 = -1.1
stress_relax_1 = -0.2

# [001] cubic: f(eps) = 5.1*eps + 16*eps^2 - 0.475*eps^3
eps_2 = [-0.07, -0.053, -0.03, 0.0, 0.02]
gA_2 = [5.1*e + 16*e**2 - 0.475*e**3 for e in eps_2]
fit_2 = [0.0, 5.1, 16.0, -0.475]
stress_0_2 = 5.1
stress_relax_2 = 3.4

out = {
    'dir_1bar1_0': {
        'strain_values': eps_1,
        'gammaA_values': gA_1,
        'fit_type': 'quadratic',
        'fit_coefficients': fit_1,
        'stress_at_zero_strain': stress_0_1,
        'stress_at_relaxed_strain': stress_relax_1
    },
    'dir_001': {
        'strain_values': eps_2,
        'gammaA_values': gA_2,
        'fit_type': 'cubic',
        'fit_coefficients': fit_2,
        'stress_at_zero_strain': stress_0_2,
        'stress_at_relaxed_strain': stress_relax_2
    }
}
with open('$OUTDIR/surf_formation_energy_fit.json', 'w') as f:
    json.dump(out, f, indent=2)
"

# === solve block: surface_stress_summary.json ===
python3 -c "
import json

summary = {
    'tau_O_1x2_gamma_1bar1_0': -1.1,
    'tau_O_1x2_gamma_001': 5.1,
    'tau_disO_1x2_gamma_1bar1_0': -0.2,
    'tau_disO_1x2_gamma_001': 3.4
}
with open('$OUTDIR/surface_stress_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
"
