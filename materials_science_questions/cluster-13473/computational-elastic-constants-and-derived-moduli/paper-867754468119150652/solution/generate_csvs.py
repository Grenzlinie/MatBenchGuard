import csv
import math

delta_zs = [0.05, 0.2, 0.8]
sigma = 0.2
A_plateau = 1.0
spike = 0.5
r_min = 0.05
r_max = 15.0
step = 0.02

with open('/app/outputs/step_01_C_r_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r', 'delta_z', 'C_r'])
    for dz in delta_zs:
        ell_c = 0.22 / math.sqrt(dz)
        r = r_min
        while r <= r_max:
            val = A_plateau + spike * math.exp(-((r - ell_c) / sigma) ** 2)
            C_r = val / (r ** 4)
            # round to reasonable precision
            writer.writerow([round(r, 6), dz, round(C_r, 12)])
            r += step
