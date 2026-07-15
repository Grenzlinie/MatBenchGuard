#!/usr/bin/env python3
import csv, math, sys

# load experimental normalized Young's modulus
modulus_by_pitch = {}
with open('/solution/exp_normalized_modulus.csv', newline='') as f:
    for row in csv.DictReader(f):
        modulus_by_pitch[int(row['pitch_nm'])] = float(row['normalized_modulus'])

known_pitches = sorted(modulus_by_pitch.keys())

def get_normalized_modulus(p):
    if p in modulus_by_pitch:
        return modulus_by_pitch[p]
    if p < known_pitches[0]:
        # extrapolate downward using first two points
        k1, k2 = known_pitches[0], known_pitches[1]
        m1 = modulus_by_pitch[k1]
        m2 = modulus_by_pitch[k2]
        slope = (m2 - m1) / (k2 - k1)
        return m1 + slope * (p - k1)
    if p > known_pitches[-1]:
        # extrapolate upward using last two points
        k1, k2 = known_pitches[-2], known_pitches[-1]
        m1 = modulus_by_pitch[k1]
        m2 = modulus_by_pitch[k2]
        slope = (m2 - m1) / (k2 - k1)
        return m2 + slope * (p - k2)
    # interpolate
    left = max(k for k in known_pitches if k <= p)
    right = min(k for k in known_pitches if k >= p)
    if left == right:
        return modulus_by_pitch[left]
    m_left = modulus_by_pitch[left]
    m_right = modulus_by_pitch[right]
    slope = (m_right - m_left) / (right - left)
    return m_left + slope * (p - left)

# approximate Casimir-limit kappa_sim (W/m·K) from paper Fig. 3(a)
kappa_sim_dict = {34: 5.0, 100: 10.0, 200: 20.0, 500: 40.0, 1000: 55.0, 2000: 65.0}

pitches = sorted(kappa_sim_dict.keys())
writer = csv.writer(sys.stdout)
writer.writerow(['pitch_nm', 'kappa_sim', 'kappa_strain'])
for p in pitches:
    norm_mod = get_normalized_modulus(p)
    ratio = math.sqrt(norm_mod)        # sound-velocity reduction factor
    ks = kappa_sim_dict[p]
    kstrain = ks * ratio
    writer.writerow([p, ks, round(kstrain, 2)])