#!/usr/bin/env python3
import math, csv, sys

# Constants
c1 = 0.28
gamma = 1.5
cE = 1.622e3  # J/(kg·K)
T0 = 303.0    # K

materials = {
    'A': {'c3': 0.8683e-3, 'beta2': -0.0288},
    'B': {'c3': 1.0829e-3, 'beta2': 0.0689}
}

lambda_values = [0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2]
p_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

def volume_heat(l):
    return -cE * T0 * math.log(1.0 + c1 * (l**(-6.0*gamma) - 1.0))

def shear_heat(p, c3):
    return -cE * T0 * math.log(1.0 + (c3 / 3.0) * p * p)

def shape_heat(l, c3, beta2):
    term = ((0.5 + beta2) * (l*l + 2.0/l) + (0.5 - beta2) * (2.0*l + 1.0/(l*l)) - 3.0)
    return -cE * T0 * math.log(1.0 + (c3 / 3.0) * term)

writer = csv.writer(sys.stdout)
writer.writerow(['deformation', 'material', 'parameter', 'W'])

# Volume for both materials (same result)
for lam in lambda_values:
    w = volume_heat(lam)
    writer.writerow(['volume', 'A', lam, f'{w:.6f}'])
    writer.writerow(['volume', 'B', lam, f'{w:.6f}'])

# Shear
for mat, props in materials.items():
    c3 = props['c3']
    for p in p_values:
        w = shear_heat(p, c3)
        writer.writerow(['shear', mat, p, f'{w:.6f}'])

# Shape
for mat, props in materials.items():
    c3 = props['c3']
    beta2 = props['beta2']
    for lam in lambda_values:
        w = shape_heat(lam, c3, beta2)
        writer.writerow(['shape', mat, lam, f'{w:.6f}'])