import sys
import math
import csv
import os

outdir = sys.argv[1] if len(sys.argv) > 1 else '/app/outputs'
num_points = 200
center = 7.3
sigma = 0.5
amp = 5.0
background = 0.2

with open(os.path.join(outdir, 'epsilon_im.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Energy_eV', 'Epsilon_im'])
    for i in range(num_points):
        e = 0.0 + 12.0 * i / (num_points - 1)
        eps = amp * math.exp(-((e - center) ** 2) / (2 * sigma ** 2)) + background
        writer.writerow([e, eps])
