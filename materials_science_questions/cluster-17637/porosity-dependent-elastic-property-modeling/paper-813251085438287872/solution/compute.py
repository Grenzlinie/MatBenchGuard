import math
import csv

nu0 = 0.33
gamma = 0.7

# g for prolate spheroid
sqrt1m2 = math.sqrt(1 - gamma*gamma)
g = (gamma*gamma) / (2 * sqrt1m2) * math.log((1 + sqrt1m2) / (1 - sqrt1m2))

# f0, f1
one_m_g2 = 1 - gamma*gamma
f0 = (1 - g) / (2 * one_m_g2)
f1 = ((2 + gamma*gamma) * g - 3 * gamma*gamma) / (4 * one_m_g2 * one_m_g2)

kappa = 1.0 / (2 * (1 - nu0))

# common denominator for h1, h3, h6
denom_cte = 2 * (4*kappa - 1) * (2*kappa*(f0 - f1) - (4*kappa - 1)*f0*f0)

h1 = kappa*(f0 - f1) / denom_cte
h2 = 1.0 / (2 * (1 - (2 - kappa)*f0 - kappa*f1))
h3 = -(2*kappa*f0 - f0 + 2*kappa*f1) / (2 * denom_cte)
h5 = 1.0 / (f0 + 4 * kappa * f1)
h6 = (4*kappa - 1 - 6*kappa*f0 + 2*f0 - 2*kappa*f1) / (2 * denom_cte)

# B and C for isotropic average (Eq. 4.5)
B = (2 * (1 + nu0) / (1 - 2*nu0)) * (38*h1 - h2 + 44*h3 + 2*h5 + 8*h6) / 30.0
C = (2*h1 + 11*h2 - 4*h3 + 8*h5 + 2*h6) / 15.0

# shape factors for spherical RVE (Eq. 4.3)
phi_K = (2.0/3.0) * (1 - 2*nu0) / (1 - nu0)
phi_G = (1.0/15.0) * (7 - 5*nu0) / (1 - nu0)

# generate porosity points (0 to 0.8 inclusive, 21 points)
num_points = 21
p_values = [i * 0.04 for i in range(num_points)]

rows = []
for p in p_values:
    denom_B = 1 - p * B * phi_K
    denom_C = 1 - p * C * phi_G
    A_K = ((1 - 2*nu0) / 3.0) * (p * B / denom_B)
    A_G = (2 * (1 + nu0) / 3.0) * (p * C / denom_C)
    E_eff_over_E0 = 1.0 / (1 + A_K + A_G)
    rows.append([p, E_eff_over_E0])

output_path = "/app/outputs/step_01_E_eff_normalized.csv"
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["porosity", "E_eff_over_E0"])
    writer.writerows(rows)
