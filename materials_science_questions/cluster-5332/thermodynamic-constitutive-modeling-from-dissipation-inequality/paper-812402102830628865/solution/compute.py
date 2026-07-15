import math
import csv

# Constants
l0_star = 1.0e-9
Delta0_l = 1.0e-8
T_g = 300.0
T_m = 373.0
T0 = (T_m + T_g) / 2.0
alpha = 4.0 / (T_m - T_g)
k = 1.380649e-23

# Grid
nF = 11
nT = 11
forces = [i * 5.0e-11 / (nF - 1) for i in range(nF)]
temperatures = [T_g + i * (T_m - T_g) / (nT - 1) for i in range(nT)]

output_path = '/app/outputs/computed_quantities.csv'

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_T', 'force_f', 'a', 'U_f', 'S_f', 'f_S', 'f_U'])
    for T in temperatures:
        for ff in forces:
            a = l0_star * ff / (k * T)
            if a == 0.0:
                La = 0.0
                dLa = 1.0 / 3.0
                ln_part = 0.0
            else:
                coth_a = 1.0 / math.tanh(a)
                La = coth_a - 1.0 / a
                dLa = -1.0 / (math.sinh(a) ** 2) + 1.0 / (a ** 2)
                arg = (math.exp(a) - math.exp(-a)) / (2.0 * a)
                ln_part = math.log(arg)
            Delta_l = Delta0_l * math.exp(alpha * (T - T0))
            l_minus_l0 = Delta_l * La
            kappa = l0_star / (k * T)
            # U_f
            U_f = alpha * Delta_l * (k * T**2 / l0_star) * ln_part
            # S_f
            term1 = - (l_minus_l0 / (kappa * T)) * (a * La - ln_part)
            term2 = alpha * Delta_l * (k * T / l0_star) * ln_part
            S_f = term1 + term2
            # f_S, f_U
            if a == 0.0:
                f_S = 0.0
                f_U = 0.0
            else:
                f_S = (1.0 - (alpha * T * La) / (a * dLa)) * ff
                f_U = (alpha * T * La) / (a * dLa) * ff
            writer.writerow(
                [repr(T), repr(ff), repr(a), repr(U_f), repr(S_f), repr(f_S), repr(f_U)]
            )
