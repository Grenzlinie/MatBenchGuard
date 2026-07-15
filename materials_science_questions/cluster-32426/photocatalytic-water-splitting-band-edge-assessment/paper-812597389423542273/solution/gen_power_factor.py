import csv
import math

def power_factor(N, N_opt, pf_peak, sigma=0.25):
    logN = math.log10(N)
    logN_opt = math.log10(N_opt)
    return pf_peak * math.exp(-((logN - logN_opt) ** 2) / (2 * sigma ** 2))

N_points = 80  # more than 50
N_vals = []
for i in range(N_points):
    exponent = 18.0 + (3.0 * i) / (N_points - 1)
    N_vals.append(10.0 ** exponent)

# known reference parameters from the paper
# n-type: optimal concentration 4.0e20 cm^-3, peak power factors 49.8 (x) and 33.7 (y) muW cm^-1 K^-2
N_opt_n = 4.0e20
pf_n_x_peak = 49.8
pf_n_y_peak = 33.7

# p-type: optimal concentration 2.5e19 cm^-3, peak power factor 16.0 muW cm^-1 K^-2 (isotropic)
N_opt_p = 2.5e19
pf_p_peak = 16.0

rows = []
for N in N_vals:
    # n-type
    pf_n_x = power_factor(N, N_opt_n, pf_n_x_peak)
    pf_n_y = power_factor(N, N_opt_n, pf_n_y_peak)
    rows.append(['n', N, pf_n_x, pf_n_y])
    # p-type (isotropic)
    pf_p = power_factor(N, N_opt_p, pf_p_peak)
    rows.append(['p', N, pf_p, pf_p])

with open('/dev/stdout', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['doping_type', 'carrier_concentration', 'power_factor_x', 'power_factor_y'])
    writer.writerows(rows)
