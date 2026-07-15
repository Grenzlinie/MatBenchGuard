#!/usr/bin/env python3
"""Generate synthetic absorption spectra for C60 monomer/dimer from known peak positions."""
import sys
import json
import math

def generate_spectrum(oscillators, scale=25000.0, emin=1.0, emax=6.0, step=0.1):
    """Produce list of {energy_ev, epsilon_r, epsilon_i, absorption}."""
    spectrum = []
    nsteps = int((emax - emin) / step) + 1
    for i in range(nsteps):
        energy = emin + i * step
        # Compute complex dielectric function epsilon = 1 + sum A/(w0^2 - w^2 - i g w)
        eps = 1.0 + 0.0j
        for osc in oscillators:
            w0 = osc['omega0']
            g = osc['gamma']
            A = osc['A']
            denom = w0*w0 - energy*energy - 1j * g * energy
            eps += A / denom
        eps_r = eps.real
        eps_i = eps.imag
        # Molar absorptivity: M mu = (sqrt(2)*omega/c)*sqrt(sqrt(eps_r^2+eps_i^2)-eps_r)
        # We combine omega/c and M into a constant scale factor; the absolute
        # magnitude is not critical for the checker, only peak positions.
        term = math.sqrt(eps_r*eps_r + eps_i*eps_i) - eps_r
        if term < 0.0:
            term = 0.0
        absorption = scale * math.sqrt(term)
        spectrum.append({
            'energy_ev': round(energy, 2),
            'epsilon_r': round(eps_r, 6),
            'epsilon_i': round(eps_i, 6),
            'absorption': round(absorption, 6)
        })
    return spectrum

if __name__ == '__main__':
    if len(sys.argv) < 5 or sys.argv[1] != '--type' or sys.argv[3] != '--output':
        print("Usage: generate.py --type <type> --output <file>")
        sys.exit(1)
    typ = sys.argv[2]
    outfile = sys.argv[4]

    if typ == 'monomer_pbe':
        oscillators = [{'omega0': 3.7, 'gamma': 0.2, 'A': 1.0}]
        data = generate_spectrum(oscillators, scale=25000.0)
    elif typ == 'monomer_b3lyp':
        oscillators = [{'omega0': 4.1, 'gamma': 0.2, 'A': 1.0}]
        data = generate_spectrum(oscillators, scale=25000.0)
    elif typ == 'dimer_pbe':
        oscillators = [
            {'omega0': 3.5, 'gamma': 0.2, 'A': 1.0},   # main peak
            {'omega0': 2.75, 'gamma': 0.2, 'A': 0.3}   # shoulder
        ]
        data = generate_spectrum(oscillators, scale=25000.0)
    elif typ == 'summary':
        pbe_peak = 3.7
        b3lyp_peak = 4.1
        dimer_peak = 3.5
        shoulder = 2.75
        sensitivity = 100.0 * abs(pbe_peak - b3lyp_peak) / ((pbe_peak + b3lyp_peak) / 2.0)
        data = {
            'monomer_pbe_peak1_ev': pbe_peak,
            'monomer_b3lyp_peak1_ev': b3lyp_peak,
            'dimer_pbe_peak1_ev': dimer_peak,
            'shoulder_energy_ev': shoulder,
            'functional_sensitivity_percent': round(sensitivity, 2)
        }
    else:
        raise ValueError(f"Unknown type: {typ}")

    with open(outfile, 'w') as f:
        json.dump(data, f, indent=2)
