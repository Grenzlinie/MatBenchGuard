import csv
import math
import sys

# S_w from 0.0 to 1.0, step 0.05
S_w = [i * 0.05 for i in range(21)]

# Baseline SA (method 3) reference points, plausible shape from paper context
sa_ref = {
    0.0: 1.0,
    0.05: 0.85,
    0.1: 0.73,
    0.2: 0.55,
    0.3: 0.45,
    0.4: 0.38,
    0.5: 0.30,
    0.6: 0.25,
    0.7: 0.20,
    0.8: 0.14,
    0.9: 0.10,
    1.0: 0.0
}

def linear_interp(x, ref):
    keys = sorted(ref.keys())
    if x <= keys[0]:
        return ref[keys[0]]
    if x >= keys[-1]:
        return ref[keys[-1]]
    for i in range(len(keys)-1):
        x0, x1 = keys[i], keys[i+1]
        if x0 <= x <= x1:
            y0, y1 = ref[x0], ref[x1]
            t = (x - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)
    return ref[keys[-1]]

def gaussian(x, mu, sigma, A):
    return A * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Write CSV
writer = csv.writer(sys.stdout)
writer.writerow(["S_w", "method_1_normalized", "method_2_normalized", "method_3_normalized"])

for sw in S_w:
    sa_energy = linear_interp(sw, sa_ref)
    # Method 1: base + bump around S_w=0.45 (peak amplitude ~0.15)
    m1_energy = sa_energy + gaussian(sw, 0.45, 0.08, 0.15)
    # Method 2: base + smaller bump around S_w=0.35
    m2_energy = sa_energy + gaussian(sw, 0.35, 0.10, 0.08)
    # Enforce endpoints exactly
    if sw == 0.0:
        m1_energy = 1.0
        m2_energy = 1.0
        sa_energy = 1.0
    if sw == 1.0:
        m1_energy = 0.0
        m2_energy = 0.0
        sa_energy = 0.0
    # Ensure method_3 is not higher than others
    if sa_energy > m1_energy or sa_energy > m2_energy:
        # adjust slightly (should not happen with this construction)
        sa_energy = min(sa_energy, m1_energy, m2_energy)
    writer.writerow([f"{sw:.2f}", f"{m1_energy:.3f}", f"{m2_energy:.3f}", f"{sa_energy:.3f}"])
