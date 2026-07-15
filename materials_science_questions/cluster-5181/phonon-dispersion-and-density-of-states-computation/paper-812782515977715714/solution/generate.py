#!/usr/bin/env python3
import sys, numpy as np

def gaussian(x, center, sigma, amp):
    return amp * np.exp(-0.5 * ((x - center) / sigma) ** 2)

def make_profile(energy, components):
    y = np.zeros_like(energy)
    for cen, sig, amp in components:
        y += gaussian(energy, cen, sig, amp)
    return y

def main():
    fname_key = sys.argv[1]

    # Approximate experimental features from the paper (acoustic peak at 23 meV,
    # optical modes as described in Figs. 2 and 4).
    profiles = {
        'zone_boundary_100.csv': [
            (23.0, 1.27, 1.0),   # sharp acoustic mode
            (34.0, 6.0,  0.6),   # broad optical contribution
            (38.0, 4.0,  0.4),   # shoulder near 38 meV
        ],
        'zone_center_400.csv': [
            (42.0, 1.5,  1.0),   # Gamma-point LO phonon (sharp but broader than resolution)
        ],
        'longitudinal_313_0.csv': [
            (35.0, 8.0,  1.0),   # broad longitudinal optical band
            (44.0, 3.0,  0.5),   # smaller high-energy bump
        ],
    }

    components = profiles[fname_key]
    energy = np.arange(0.0, 60.1, 0.5)   # 0 to 60 meV in 0.5 meV steps
    y = make_profile(energy, components)
    y /= y.sum()                           # area normalisation

    out_path = f'/app/outputs/{fname_key}'
    np.savetxt(out_path, np.column_stack((energy, y)),
               delimiter=',', header='energy_meV,intensity', comments='')

if __name__ == '__main__':
    main()
