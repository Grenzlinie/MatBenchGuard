#!/usr/bin/env python3
import math, csv, sys

# Energy range: 0 to 8 eV, step 0.05 eV (161 points)
energies = [round(i*0.05, 5) for i in range(161)]

# Lorentz oscillator parameters per strain (S, omega0, gamma)
# S in eV^2, omega0 in eV, gamma in eV.
# Oscillators are designed to roughly match the described spectral features:
#  - equilibrium (0%): main peaks near 4 eV and 6 eV, broad low-energy absorption
#  - -8% compression: additional sharp peak near 4.5 eV
#  - +8% tension: similar to equilibrium with slight blue shift of peaks

oscillators = {
    -8: [
        # low-energy broad
        (10.0, 3.0, 1.0),
        # primary peak around 4 eV (slightly shifted)
        (15.0, 3.9, 0.5),
        # compression-induced strong peak at 4.5 eV
        (20.0, 4.5, 0.3),
        # main high-energy peak
        (20.0, 6.0, 0.5),
        # high-energy shoulder
        (10.0, 7.5, 0.5),
    ],
    0: [
        (10.0, 3.0, 1.0),
        (15.0, 4.0, 0.5),
        # no extra peak at 4.5
        (20.0, 6.0, 0.5),
        (10.0, 7.5, 0.5),
    ],
    8: [
        (10.0, 3.2, 1.0),
        (15.0, 4.2, 0.5),
        (20.0, 6.2, 0.5),
        (10.0, 7.7, 0.5),
    ],
}

writer = csv.writer(sys.stdout)
writer.writerow(["strain_percent", "energy_eV", "epsilon1", "epsilon2"])

for strain in sorted(oscillators.keys()):
    params = oscillators[strain]
    for omega in energies:
        e1 = 1.0
        e2 = 0.0
        for S, w0, g in params:
            w2 = w0**2
            denom = (w2 - omega**2)**2 + (g*omega)**2
            if denom == 0.0:
                continue  # avoid division by zero (should not happen)
            e2 += S * g * omega / denom
            e1 += S * (w2 - omega**2) / denom
        # guarantee physically reasonable values
        if e1 < 1.0:
            e1 = 1.0
        if e2 < 0.0:
            e2 = 0.0
        writer.writerow([strain, omega, round(e1, 6), round(e2, 6)])
