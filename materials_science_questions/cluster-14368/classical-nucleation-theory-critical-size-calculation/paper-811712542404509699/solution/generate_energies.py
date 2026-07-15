import csv
import math

out = '/app/outputs/energies_and_masses.csv'
temps = [0.55, 0.89]
# dividing surfaces per temperature
surfaces = {
    0.55: ['equimolecular', 'moments_of_forces'],
    0.89: ['equimolecular', 'moments_of_forces', 'tension']
}
Rs = list(range(1, 21))

def gauss(r, peak, width, amp):
    return 1.0 + amp * math.exp(-((r - peak) / width) ** 2)

rows = []
for temp in temps:
    for surf in surfaces[temp]:
        if surf == 'tension':
            amp_e = 0.005   # up to 0.5%
            amp_m = 0.005
        else:
            amp_e = 0.0025  # ~0.25%
            amp_m = 0.0025
        for r in Rs:
            e = gauss(r, peak=5, width=3, amp=amp_e)
            m = gauss(r, peak=5, width=3, amp=amp_m)
            rows.append([e, r, surf, m, temp])

with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['E_ratio', 'R', 'dividing_surface', 'm_ratio', 'temperature'])
    writer.writerows(rows)
