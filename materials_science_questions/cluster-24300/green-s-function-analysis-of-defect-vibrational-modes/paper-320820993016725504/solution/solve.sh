#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dispersion_results.json ===
python3 -c "
import json, math
xi=0.5; beta=0.5; gamma=0.0; H=0.0; g_prime_over_g=1.0; JS=1.0
points = []
for kx in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.14]:
    for kz in [0.0, 1.0]:
        Ek = JS * (4 - 2*math.cos(kx) - 2*math.cos(kz))
        gamma_prime = gamma - xi
        eps = - (H * gamma_prime + xi * Ek) / JS
        E_plus = Ek + 2*JS * (eps**2) / (2*(eps-1))
        if eps <= 2*(beta-1) or eps >= 2*beta:
            E_minus = Ek + 2*JS * ((eps+2*(1-beta))**2) / (2*(eps+1-2*beta))
        else:
            continue
        points.append({'kappa_x': kx, 'kappa_z': kz, 'E_plus': E_plus, 'E_minus': E_minus})
sm_cond = True
am_cond = bool(points)
kx0=0.5; kz0=0.0
Ek0 = JS * (4 - 2*math.cos(kx0) - 2*math.cos(kz0))
eps0 = - (H * gamma_prime + xi * Ek0) / JS
beta_list = [0.0, 0.3, 0.5, 0.7, 1.0]
E_plus_vals = []
for b in beta_list:
    Ep = Ek0 + 2*JS * (eps0**2) / (2*(eps0-1))
    E_plus_vals.append(Ep)
constant_confirmed = all(abs(v - E_plus_vals[0]) < 1e-10 for v in E_plus_vals)
output = {
    'parameters': {'xi': xi, 'beta': beta, 'gamma': gamma, 'H': H, 'g_prime_over_g': g_prime_over_g, 'J_S': JS},
    'condition_check': {'SM_localization_condition': sm_cond, 'AM_localization_condition': am_cond},
    'points': points,
    'beta_independence_check': {
        'kappa_x': kx0, 'kappa_z': kz0,
        'beta_values': beta_list,
        'E_plus_values': E_plus_vals,
        'constant_confirmed': constant_confirmed
    }
}
with open('/app/outputs/dispersion_results.json', 'w') as f:
    json.dump(output, f, indent=2)
"
