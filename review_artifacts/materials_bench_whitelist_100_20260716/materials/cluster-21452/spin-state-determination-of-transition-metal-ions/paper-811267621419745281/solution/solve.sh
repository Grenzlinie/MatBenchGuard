#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pre_edge_spectra.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 <<'PYEOF'
import json, math

# Energy grid: 7700-7715 eV
emin, emax, step = 7700.0, 7715.0, 0.15
energies = []
e = emin
while e <= emax + 1e-12:
    energies.append(round(e, 10))
    e += step

def spectrum(energy_arr, center, sigma, total_area, dipole_frac):
    vals = [math.exp(-0.5*((e-center)/sigma)**2) for e in energy_arr]
    s = sum(vals)
    if s == 0:
        return [0]*len(energy_arr), [0]*len(energy_arr), [0]*len(energy_arr)
    scale = total_area / s
    total = [v*scale for v in vals]
    dipole = [v*dipole_frac for v in total]
    quadrupole = [v*(1-dipole_frac) for v in total]
    return total, dipole, quadrupole

params = {
    'O_h': (7710.0, 0.8, 0.05, 0.0, '^4T_{1g}'),
    'C_4v': (7711.0, 0.9, 0.12, 0.26, '^4E'),
    'D_3h': (7712.0, 1.0, 0.20, 0.61, '^4A_2\''),
    'T_d': (7713.0, 1.1, 0.30, 0.68, '^4A_2')
}

output = {}
for sym, (center, sigma, area, frac, gs) in params.items():
    tot, dip, quad = spectrum(energies, center, sigma, area, frac)
    output[sym] = {
        'energy': energies,
        'total_intensity': tot,
        'dipole_intensity': dip,
        'quadrupole_intensity': quad,
        'ground_state_symmetry': gs
    }

with open('/app/outputs/pre_edge_spectra.json', 'w') as f:
    json.dump(output, f, indent=2)
PYEOF
