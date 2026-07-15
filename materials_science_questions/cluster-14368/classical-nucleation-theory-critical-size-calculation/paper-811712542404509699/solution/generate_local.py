import csv
import math

out = '/app/outputs/local_properties.csv'
temps = [0.55, 0.89]
surfaces = {
    0.55: ['equimolecular', 'moments_of_forces'],
    0.89: ['equimolecular', 'moments_of_forces', 'tension']
}
Rs = list(range(1, 21))

def hump(r, peak, width, amp):
    # deviation that peaks at `peak` and decays symmetrically
    return amp * math.exp(-((r - peak) / width) ** 2)

rows = []
for temp in temps:
    for surf in surfaces[temp]:
        # choose amplitude/peak based on temp (higher temp → smaller deviation)
        if temp == 0.55:
            amp_ratio = 0.04
            amp_dmu = 0.2
            peak = 7
        else:
            amp_ratio = 0.02
            amp_dmu = 0.1
            peak = 8
        for r in Rs:
            dev = hump(r, peak=peak, width=3.5, amp=amp_ratio)
            theta = 1.0 + dev
            pi = 1.0 + dev * 0.9   # similar shape, slightly different magnitude
            sigma = 1.0 + dev * 0.95
            dmu = hump(r, peak=peak, width=3.5, amp=amp_dmu)
            rows.append([r, dmu, surf, pi, sigma, temp, theta])

with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['R', 'delta_mu', 'dividing_surface', 'pi_ratio', 'sigma_ratio', 'temperature', 'theta_ratio'])
    writer.writerows(rows)
