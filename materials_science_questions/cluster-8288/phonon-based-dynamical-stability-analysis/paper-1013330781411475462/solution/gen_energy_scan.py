#!/usr/bin/env python3
"""Generate dummy energy-vs-amplitude scan data with minima at paper-reported displacements."""
import json
import math

# Paper-reported energy-minimizing displacements (Å)
gamma_disp = {"Ta": 0.025, "Re": 0.101, "Si": 0.046}
S_disp = {"Ta": 0.061, "Re": 0.153, "Si": 0.098}

def total_energy(d, d0, base_curvature=50.0):
    """Simple parabolic well: E = c*(d - d0)^2 + E0"""
    return base_curvature * (d - d0)**2 - 0.3  # E0 = -0.3 eV/f.u. for both modes at minima

# Generate amplitude ranges around the minima
amplitudes = [0.001 * i for i in range(0, 300)]  # 0 to 0.3 Å
scan = {
    "gamma_mode": {
        "displacements": amplitudes,
        "energies": [total_energy(a, gamma_disp["Ta"]) for a in amplitudes]  # using Ta displacement as scalar amplitude
    },
    "S_mode": {
        "displacements": amplitudes,
        "energies": [total_energy(a, S_disp["Ta"]) for a in amplitudes]
    }
}
print(json.dumps(scan, indent=2))
