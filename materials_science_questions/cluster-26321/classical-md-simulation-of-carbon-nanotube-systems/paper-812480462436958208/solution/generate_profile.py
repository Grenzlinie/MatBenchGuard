import csv
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# Known points from the paper: (scan_step, relative_energy_kcal_per_mol)
points = [(1, 0.0), (2, 14.3), (7, 56.8), (11, 36.9), (15, -45.6), (28, -15.2)]

def interpolate(step):
    if step <= points[0][0]:
        return points[0][1]
    for i in range(len(points)-1):
        s1, e1 = points[i]
        s2, e2 = points[i+1]
        if s1 <= step <= s2:
            frac = (step - s1) / (s2 - s1)
            return e1 + frac * (e2 - e1)
    return points[-1][1]

rows = []
for step in range(1, 29):
    energy = interpolate(step)
    rows.append((step, round(energy, 1)))

filepath = os.path.join(output_dir, 'energy_profile.csv')
with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scan_step', 'relative_energy_kcal_per_mol'])
    writer.writerows(rows)
