#!/usr/bin/env python3
import sys, csv, math, os

system = sys.argv[1]
out = f"/app/outputs/{system}_thermo.csv"

params = {
    'si': {
        'B2Dstar0': 2.50,
        'deltaB2D': 0.06,
        'sl_star': 1.89e-5,   # eV/Å^2/K, from a* dB2D*/da * alpha
        'sl_b2d': -2.5e-5,    # negative slope, B2D decreases
        'alpha_300': -3.0e-6,
        'C_max': 49.88,       # J/(mol·K), 6R for Si2
        'Tc': 150.0,
    },
    'hsi': {
        'B2Dstar0': 1.75,
        'deltaB2D': 0.05,
        'sl_star': 3.99e-5,  # a*dB2D*/da = -13.3, alpha -3e-6
        'sl_b2d': 2.5e-5,    # increased by 5.0e-5 relative to Si
        'alpha_300': -3.0e-6,
        'C_max': 70.0,       # larger due to H modes
        'Tc': 150.0,
    },
    'ge': {
        'B2Dstar0': 2.20,
        'deltaB2D': 0.04,
        'sl_star': 1.488e-4, # a*dB2D*/da = -18.6, alpha -8e-6
        'sl_b2d': -1.0e-4,
        'alpha_300': -8.0e-6,
        'C_max': 49.88,
        'Tc': 100.0,
    },
    'hge': {
        'B2Dstar0': 1.50,
        'deltaB2D': 0.03,
        'sl_star': 5.52e-5,  # a*dB2D*/da = -13.8, alpha -4e-6
        'sl_b2d': -6.9e-5,   # increased by 3.1e-5
        'alpha_300': -4.0e-6,
        'C_max': 70.0,
        'Tc': 100.0,
    },
}

p = params[system]
Bstar0 = p['B2Dstar0']
delta = p['deltaB2D']
sl_star = p['sl_star']
sl_b2d = p['sl_b2d']
a300 = p['alpha_300']
Cmax = p['C_max']
Tc = p['Tc']

Tmax = 600
Tstep = 20
temps = [i*Tstep for i in range(0, (Tmax//Tstep)+1)]

with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'alpha', 'C_V', 'B2D', 'B2D_star'])
    for T in temps:
        alpha = a300 * (T/300.0) if T > 0 else 0.0
        Cv = Cmax * (1.0 - math.exp(-(T/Tc)**1.5))
        Bstar = Bstar0 + sl_star * T
        B2d = Bstar0 + delta + sl_b2d * T
        writer.writerow([f"{T:.2f}", f"{alpha:.6e}", f"{Cv:.4f}", f"{B2d:.6f}", f"{Bstar:.6f}"])
