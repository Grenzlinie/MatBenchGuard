#!/usr/bin/env python3
"""Reference oracle: write the three scored CSV files with hardcoded values."""
import csv, math, sys, os

def main():
    outdir = sys.argv[1]

    # ---- backscattering_coefficients.csv ----
    backscattering = [
        # material, foil_thickness_in_s0_or_inf (float or 'inf'), incident_energy_MeV, backscattering_coefficient
        ('graphite', 'inf', 1.0, 0.030),
        ('aluminium', 'inf', 1.0, 0.170),
        ('silver', 'inf', 1.0, 0.470),
        ('lead', 'inf', 1.0, 0.350),
    ]
    # Al at 0.25 MeV for thicknesses 0.1 .. 1.0 s0
    # A = A_inf * (1 - exp(-t/0.4)) with A_inf ~ 0.25
    import math
    A_inf = 0.25
    for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        coeff = A_inf * (1.0 - math.exp(-t / 0.4))
        backscattering.append(('aluminium', t, 0.25, round(coeff, 6)))

    with open(os.path.join(outdir, 'backscattering_coefficients.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['backscattering_coefficient', 'foil_thickness_in_s0_or_inf', 'incident_energy_MeV', 'material'])
        for bs, thick, energy, mat in backscattering:
            w.writerow([bs, thick, energy, mat])

    # ---- transmission_coefficients.csv ----
    # T = T0 * exp(-t / λ) where T0 ~ 0.95, λ ~ 0.3
    T0 = 0.95
    lam = 0.3
    with open(os.path.join(outdir, 'transmission_coefficients.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['foil_thickness_in_s0_units', 'incident_energy_MeV', 'material', 'transmission_coefficient'])
        for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
            trans = T0 * math.exp(-t / lam)
            w.writerow([t, 0.25, 'aluminium', round(trans, 6)])

    # ---- energy_deposition_al_1MeV.csv ----
    # Gaussian peak at depth = 0.2 s0, sigma = 0.12, normalized to max=100
    peak_depth = 0.20
    sigma = 0.12
    depths = [round(i*0.05, 2) for i in range(0, 13)]  # 0.0 .. 0.60
    raw = [math.exp(-((d - peak_depth)**2) / (2 * sigma**2)) for d in depths]
    max_raw = max(raw)
    norm = [round((v / max_raw) * 100, 4) for v in raw]

    with open(os.path.join(outdir, 'energy_deposition_al_1MeV.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['depth_in_s0_units', 'energy_deposition_normalized'])
        for d, n in zip(depths, norm):
            w.writerow([d, n])

if __name__ == '__main__':
    main()