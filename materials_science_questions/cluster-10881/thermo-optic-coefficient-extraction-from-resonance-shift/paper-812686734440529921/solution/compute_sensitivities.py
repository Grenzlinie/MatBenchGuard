import math
import csv

lam = 0.6328  # µm
k = 2.0 * math.pi / lam
n_s = 1.605
delta_ns = 0.08875
n_0 = 1.0
const_exp = 1.02e4
d1_coeff = 8.243e3

temperatures_C = [217, 250, 310]

# Grid of effective indices covering the single-mode range (just above substrate to near surface)
n_e_start = 1.517
n_e_end = 1.600
n_points = 84  # yields step 0.001
n_e_list = [n_e_start + i * (n_e_end - n_e_start) / (n_points - 1) for i in range(n_points)]

with open('/app/outputs/step_01_sensitivities.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ne', 'temperature_C', 'delta_ne_delta_t', 'delta_ne_delta_T'])
    for T_C in temperatures_C:
        T_K = T_C + 273.15
        for n_e in n_e_list:
            ne_sq = n_e ** 2
            k_s = k * (n_s ** 2 - ne_sq) ** 0.5
            k0 = k * (ne_sq - n_0 ** 2) ** 0.5
            # eigenvalue equation (12) solved for d1
            d1 = (3.0 * k ** 2 * n_s * delta_ns * (math.pi / 4.0 + math.atan(k0 / k_s))) / (k_s ** 3)
            # effective depth model (10) gives t in minutes
            exp_factor = math.exp(-const_exp / (2.0 * T_K))
            t = (d1 / (d1_coeff * exp_factor)) ** 2
            # alpha from equation (16) simplified for TE0 (ξ=1)
            bracket = n_e / k0 + 3.0 / k_s
            alpha = (k_s ** 4 * d1) / (6.0 * k ** 4 * n_s * delta_ns * bracket)
            # sensitivities (14)-(15)
            delta_ne_delta_t = alpha / t  # 1/min
            delta_ne_delta_T = const_exp * alpha / (T_K ** 2)  # 1/K ≡ 1/°C
            writer.writerow([n_e, T_C, delta_ne_delta_t, delta_ne_delta_T])
