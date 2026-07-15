#!/usr/bin/env python3
import sys, csv

params = {
    ('X', 'tension'): {'E': 116, 'strain_peak': 0.155, 'strain_fail': 0.175, 'drop_factor': 0.7},
    ('Y', 'tension'): {'E': 117, 'strain_peak': 0.170, 'strain_fail': 0.190, 'drop_factor': 0.7},
    ('Z', 'tension'): {'E': 160, 'strain_peak': 0.085, 'strain_fail': 0.100, 'drop_factor': 0.7},
    ('X', 'compression'): {'E': 143, 'strain_peak': 0.135},
    ('Y', 'compression'): {'E': 150, 'strain_peak': 0.145},
    ('Z', 'compression'): {'E': 175, 'strain_peak': 0.220},
}

mode = sys.argv[2]
dir = sys.argv[1]
p = params[(dir, mode)]

writer = csv.writer(sys.stdout)
writer.writerow(['strain', 'stress'])

strain_linear = 0.005
dt = 0.0002

def next_strain(s):
    s += dt
    return round(s, 10)

if mode == 'tension':
    E = p['E']
    strain_peak = p['strain_peak']
    strain_fail = p['strain_fail']
    drop_factor = p['drop_factor']
    # peak stress: bridge from linear end with a concave quadratic
    peak_stress = E * strain_linear + E * (strain_peak - strain_linear) * 0.4
    strain = 0.0
    while strain <= strain_peak:
        if strain <= strain_linear:
            stress = E * strain
        else:
            t = (strain - strain_linear) / (strain_peak - strain_linear)
            stress = E * strain_linear + (peak_stress - E * strain_linear) * (1 - (1 - t)**2)
        writer.writerow([f'{strain:.6f}', f'{stress:.6f}'])
        strain = next_strain(strain)
    while strain <= strain_fail:
        t = (strain - strain_peak) / (strain_fail - strain_peak)
        stress = peak_stress * (1 - (1 - drop_factor) * t)
        writer.writerow([f'{strain:.6f}', f'{stress:.6f}'])
        strain = next_strain(strain)
    final_strain = strain_fail + 0.02
    while strain <= final_strain:
        t = (strain - strain_fail) / (final_strain - strain_fail)
        stress = drop_factor * peak_stress * (1 - t)
        writer.writerow([f'{strain:.6f}', f'{stress:.6f}'])
        strain = next_strain(strain)
else:  # compression
    E = p['E']
    strain_peak = p['strain_peak']
    peak_stress = E * strain_linear + E * (strain_peak - strain_linear) * 0.5
    strain = 0.0
    while strain <= strain_peak:
        if strain <= strain_linear:
            stress = E * strain
        else:
            t = (strain - strain_linear) / (strain_peak - strain_linear)
            stress = E * strain_linear + (peak_stress - E * strain_linear) * (1 - (1 - t)**3)
        writer.writerow([f'{strain:.6f}', f'{stress:.6f}'])
        strain = next_strain(strain)
    final_strain = strain_peak + 0.02
    while strain <= final_strain:
        t = (strain - strain_peak) / (final_strain - strain_peak)
        stress = peak_stress * (1 - 0.02 * t)
        writer.writerow([f'{strain:.6f}', f'{stress:.6f}'])
        strain = next_strain(strain)
