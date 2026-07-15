import numpy as np
import scipy.special as sp
import math
import csv

# Physical parameters
lambda_val = 0.22
epsilon0 = 4.0       # meV
kF = 2.06            # nm^-1
omega_D = 100.0      # meV
epsilon_F = 60.0     # meV

# Coherence length
xi = 2.0 * epsilon_F / (kF * epsilon0)   # nm

# Bulk gap from Eq. (13)
arg = (1.0 / lambda_val + 1.5) * epsilon0 / omega_D
Delta0 = epsilon0 / np.sinh(arg)         # meV

# Prefactor appearing in f_{1/2} and f_1
prefactor = 1.0 - 3.0 * Delta0 / (2.0 * omega_D)

# Aspect ratios
alphas = [1.2, 1.4]

# Output CSV
with open('/app/outputs/delta_vs_area.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['area_nm2', 'aspect_ratio', 'gap_meV'])

    for area_nm2 in range(25, 401):
        L_len = math.sqrt(area_nm2)      # L
        for alpha in alphas:
            Lx = alpha * L_len
            Ly = L_len / alpha
            L2 = area_nm2

            # ---- Leading correction f_{1/2} ----
            fhalf_sum = 0.0
            max_nm = 60   # enough for area <= 400 nm^2, xi ~ 14.6 nm
            for n in range(0, max_nm + 1):
                for m in range(0, max_nm + 1):
                    if n == 0 and m == 0:
                        continue
                    Ln = 2.0 * math.sqrt((Lx * n) ** 2 + (Ly * m) ** 2)
                    arg_xi = Ln / xi
                    # prune if contribution is extremely small
                    if arg_xi > 50.0:
                        continue
                    j0 = sp.j0(kF * Ln)
                    sinc_val = math.sin(arg_xi) / arg_xi
                    fhalf_sum += j0 * sinc_val

            fhalf = prefactor * fhalf_sum

            # ---- Next-to-leading correction f_1 ----
            # Weyl term (Dirichlet: minus sign)
            weyl = (Lx + Ly) / (kF * L2)

            # One-dimensional periodic orbit sums
            sum_cos = 0.0
            for Li in [Lx, Ly]:
                sum_i = 0.0
                n = 1
                while True:
                    Ln_i = 2.0 * n * Li
                    arg_xi_i = Ln_i / xi
                    if arg_xi_i > 50.0:
                        break
                    cos_val = math.cos(kF * Ln_i)
                    sinc_val_i = math.sin(arg_xi_i) / arg_xi_i
                    sum_i += cos_val * sinc_val_i
                    n += 1
                sum_cos += (2.0 * Li / (kF * L2)) * sum_i

            bracket = weyl + sum_cos
            f1 = - prefactor * bracket - (3.0 * Delta0 / (2.0 * omega_D)) * (fhalf ** 2)

            # Total gap
            gap = Delta0 * (1.0 + fhalf + f1)

            writer.writerow([float(area_nm2), alpha, gap])
