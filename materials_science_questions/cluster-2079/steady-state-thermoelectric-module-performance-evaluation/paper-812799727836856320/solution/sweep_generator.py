import math
import csv
import sys

# Each combination: (material, geometry, (start, stop, step), eta_max, RL_eta_opt, sigma_eta, Pout_max, RL_pout_opt, sigma_p)
combinations = [
    ("4% SrTe", "rectangular", (0.1, 1.21, 0.01), 16.071, 0.56, 0.2, 35.093, 0.24, 0.2),
    ("4% SrTe", "trapezoidal",  (0.1, 1.21, 0.01), 15.233, 0.28, 0.15, 26.199, 0.28, 0.15),
    ("2% SrTe", "rectangular", (0.1, 1.21, 0.01),  7.873, 0.56, 0.2, 14.357, 0.24, 0.2),
    ("2% SrTe", "trapezoidal",  (0.1, 1.21, 0.01),  7.347, 0.28, 0.15, 10.501, 0.28, 0.15),
]

writer = csv.writer(sys.stdout)
writer.writerow(["material", "geometry", "RL", "eta", "Pout"])

for material, geometry, r_range, eta_max, rl_eta_opt, s_eta, p_max, rl_p_opt, s_p in combinations:
    start, stop, step = r_range
    rl = start
    while rl < stop:
        eta = eta_max * math.exp(-0.5 * ((rl - rl_eta_opt) / s_eta) ** 2) if s_eta > 0 else 0.0
        pout = p_max * math.exp(-0.5 * ((rl - rl_p_opt) / s_p) ** 2) if s_p > 0 else 0.0
        # Pin the exact optimum point to the paper value to avoid tiny floating errors
        if abs(rl - rl_eta_opt) < step / 2:
            eta = eta_max
        if abs(rl - rl_p_opt) < step / 2:
            pout = p_max
        writer.writerow([
            material,
            geometry,
            round(rl, 2),
            round(eta, 4),
            round(pout, 4)
        ])
        rl = round(rl + step, 10)
