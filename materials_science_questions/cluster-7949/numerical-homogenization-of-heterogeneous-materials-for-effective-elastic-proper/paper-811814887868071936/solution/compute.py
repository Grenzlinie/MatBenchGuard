import math, csv, os

# Parameters from the paper (nondimensionalised)
E_H = 100.0
E_S = 1.0
nu_H = 0.2
nu_S = 0.3
alpha_H = 1.0
alpha_S = 10.0
DeltaT = 1.0
h_H = 1.0
h_S = 1.0
d = 1.0
aspect_ratios = [3.0, 10.0, 20.0, 35.0]

# Derived constants
c_H = h_H / (h_H + h_S)   # 0.5
vol_avg_CTE = c_H * alpha_H + (1 - c_H) * alpha_S   # 5.5
ref_stress_scale = (alpha_S - alpha_H) * DeltaT * E_S   # 9.0

# Sandwich composite baseline
D_s = h_H * E_H * (1 - nu_S) + h_S * E_S * (1 - nu_H)   # 70.8
N_s = h_H * E_H * (1 - nu_S) * alpha_H + h_S * E_S * (1 - nu_H) * alpha_S   # 78.0
tilde_alpha_x = N_s / D_s
tilde_alpha_y = tilde_alpha_x
tilde_sigma_H = (E_H * E_S * h_S / D_s) * (alpha_S - alpha_H) * DeltaT
tilde_sigma_S = - (E_H * E_S * h_H / D_s) * (alpha_S - alpha_H) * DeltaT

# Common factors for beta1, beta2
A = h_H * E_H * (1 + nu_S) + h_S * E_S * (1 + nu_H)   # 131.2
B = h_H * E_H * (1 - nu_S) + h_S * E_S * (1 - nu_H)   # 70.8
num_beta1 = h_H**2 * E_H * E_S * (h_H * E_H + h_S * E_S)   # 10100.0
num_beta2 = h_H**2 * E_H * E_S * (nu_S * h_H * E_H + nu_H * h_S * E_S)   # 3020.0
denom_beta = c_H * A * B   # 4644.48

# Shear modulus of soft phase
G_S = E_S / (2 * (1 + nu_S))   # 1/2.6

rows = []
for l in aspect_ratios:
    # Compute geometry-dependent parameters
    beta1 = num_beta1 / (denom_beta * l)
    beta2 = num_beta2 / (denom_beta * l)
    
    # Gamma factor
    tmp = ((h_H + h_S) * l) / (h_S * (l + d))
    gamma = (1.0 + (4.0 / 3.0) * tmp**2) * (l - d) / (l + d)
    
    # A_S and A_H for Delta d numerator
    beta_sum = beta1 + beta2
    A_S = 2 * beta1 - nu_S * beta_sum
    A_H = 2 * beta1 - nu_H * beta_sum
    
    # Numerator and denominator for Delta d
    numer_d = (tilde_sigma_S / E_S) * A_S - (tilde_sigma_H / E_H) * A_H
    denom_d = (2.0 / (E_H * h_H)) * (beta1**2 - nu_H * beta1 * beta2) + \
              (2.0 / (E_S * h_S)) * (beta1**2 - nu_S * beta1 * beta2) + \
              (gamma * G_S) / (2 * h_S)
    Delta_d = numer_d / denom_d
    
    # CTE x
    factor_x = (l / (E_H * h_H)) * (beta1 - nu_H * beta2) + \
               d * (-1.0 / (E_S * h_S)) * (beta1 - nu_S * beta2)
    alpha_x = tilde_alpha_x + factor_x / (l + d) * Delta_d / DeltaT
    
    # CTE y
    alpha_y = tilde_alpha_y + (1.0 / (E_H * h_H)) * (beta2 - nu_H * beta1) * Delta_d / DeltaT
    
    # Average thermal mismatch stresses in hard phase
    sigma_x_H = tilde_sigma_H + (1.0 / h_H) * beta1 * Delta_d
    sigma_y_H = tilde_sigma_H + (1.0 / h_H) * beta2 * Delta_d
    
    # Normalise
    rows.append([
        l,
        alpha_x / vol_avg_CTE,
        alpha_y / vol_avg_CTE,
        sigma_x_H / ref_stress_scale,
        sigma_y_H / ref_stress_scale
    ])

# Write CSV
os.makedirs(os.path.dirname("/app/outputs/staggered_thermal_results.csv"), exist_ok=True)
with open("/app/outputs/staggered_thermal_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["aspect_ratio", "normalized_alpha_x", "normalized_alpha_y",
                "normalized_sigma_x_H", "normalized_sigma_y_H"])
    w.writerows(rows)
