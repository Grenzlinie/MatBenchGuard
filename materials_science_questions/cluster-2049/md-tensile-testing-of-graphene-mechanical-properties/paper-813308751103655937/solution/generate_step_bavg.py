import csv
import math

# Domain
x_min = -9.5
x_max = 9.5
nbins = 60
dx = (x_max - x_min) / nbins
x_vals = [x_min + (i + 0.5) * dx for i in range(nbins)]

# Model: two Gaussians with opposite sign, peaks near ±1 nm
sigma = 0.7   # nm
amp_pos = 42.0   # T
amp_neg = -40.0  # T
mu_pos = 1.0
mu_neg = -1.0

def B_avg(x):
    return amp_pos * math.exp(-((x - mu_pos) ** 2) / (2 * sigma ** 2)) + \
           amp_neg * math.exp(-((x - mu_neg) ** 2) / (2 * sigma ** 2))

B_vals = [B_avg(x) for x in x_vals]

with open('/app/outputs/step_Bavg.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x (nm)', 'B_avg (T)'])
    for x, b in zip(x_vals, B_vals):
        writer.writerow([f'{x:.6f}', f'{b:.6f}'])
