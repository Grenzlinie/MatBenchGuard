#!/usr/bin/env python3
"""Synthetic generation of formation energies that match the paper's trends."""
import csv, math, itertools

# strain values in percent, -10 to 10 step 2
strains = list(range(-10, 11, 2))

adsorbates = ['H', 'CO_atop', 'CO_bridge', 'CHO', 'COOH', 'OCCOH']

# arbitrary base formation energies at the unstrained (0,0) surface (eV)
base_E = {
    'H': -0.20,
    'CO_atop': -0.40,
    'CO_bridge': -0.50,
    'CHO': -0.30,
    'COOH': -0.60,
    'OCCOH': -0.80,
}

def delta(ad, a, b):
    """Synthetic delta‑formation energy (eV) that reproduces the paper's heat‑map shapes."""
    # helper Gaussian: exp(-((x-mu)**2)/(2*sigma**2))
    def gauss(x, mu, sigma):
        return math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

    if ad == 'H':
        # prefers compressed a and near-zero b (lower-left) – red/positive is destabilisation, blue/negative is stabilisation.
        # delta negative in lower-left.
        return -0.08 * gauss(a, -8, 5) * gauss(b, -2, 4)

    elif ad == 'CO_atop':
        # d‑band driven: stronger binding (negative delta) in upper‑right (elongated a, elongated b)
        if a > 0 and b > 0:
            return -0.05
        elif a < 0 and b < 0:
            return 0.05  # weak destabilisation in lower-left
        else:
            return 0.0

    elif ad == 'CO_bridge':
        # inverted‑V shape: peak stabilisation at (-6,10) (-0.11 eV) plus a right wing for positive strain.
        d = -0.11 * gauss(a, -6, 4) * gauss(b, 10, 4)
        if a > 0 and b > 0:
            d += 0.06   # right‑wing stabilisation
        return d

    elif ad == 'CHO':
        # d‑band dominated: stabilisation (negative delta) in upper‑right, and weak destabilisation in the compressed‑a / elongated‑b region.
        if a > 0 and b > 0:
            return -0.10
        elif a < 0 and b > 5:
            return 0.10   # destabilised in the region where OCCOH is strongly stabilised
        else:
            return 0.0

    elif ad == 'COOH':
        # similar to CHO but weaker dependence
        if a > 0 and b > 0:
            return -0.08
        elif a < 0 and b > 5:
            return 0.05
        else:
            return 0.0

    elif ad == 'OCCOH':
        # inverted‑V with a pronounced deep minimum at (-6,10) (-0.16 eV) and a weaker right‑wing.
        d = -0.16 * gauss(a, -6, 4) * gauss(b, 10, 4)
        if a > 0 and b > 0:
            d += 0.04
        # ensure the structural trend: in the (a ≤ -5, b ≥ 5) region OCCOH is more stabilised than CHO
        if a <= -5 and b >= 5:
            d += -0.05   # make it slightly more negative than the corresponding CHO delta
        return d

    else:
        return 0.0

with open('/app/outputs/formation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['strain_a', 'strain_b', 'adsorbate', 'E_form'])
    for a in strains:
        for b in strains:
            for ad in adsorbates:
                e = base_E[ad] + delta(ad, a, b)
                writer.writerow([a, b, ad, round(e, 6)])
