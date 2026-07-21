import csv
import math

# Coupled vibration model constants for PZT-4
gamma = 0.58
norm_k_eff = 0.59   # tall-rod effective coupling coefficient for PZT-4

# PZT-4 material constants (Berlincourt et al., 1964)
c33E  = 115e9          # Pa
k33   = 0.70            # longitudinal coupling coefficient
e33   = 15.1            # C/m^2
e31   = -5.2
eps0  = 8.854187817e-12
eps33S= 635 * eps0      # F/m, epsilon^S_33/epsilon_0 = 635

# Compute c33' (Eq. (25) context)
c33_prime = c33E * (1 + (1 - 8/math.pi**2) * k33**2 / (1 - k33**2))

# Factor A = (8/pi^2) * (e33^2 / (c33_prime * eps33S))
A = (8 / math.pi**2) * (e33**2 / (c33_prime * eps33S))

# Constant part inside parentheses of Eq. 46: 1 - 1.1 * gamma * (e31/e33)
B = 1 - 1.1 * gamma * (e31 / e33)

# Range of aspect ratios
step = 0.01
start = 0.50
end = 1.50
n_points = int((end - start) / step) + 1

rows = []
for i in range(n_points):
    ar = round(start + i * step, 10)
    beta = 1.4 * ar
    # Frequency equation (41): Omega^2 - (1 + 1/beta^2)*Omega + (1-gamma^2)/beta^2 = 0
    b = -(1 + 1 / beta**2)
    c = (1 - gamma**2) / (beta**2)
    disc = b**2 - 4 * c
    sqrt_disc = math.sqrt(disc)
    omega1 = (-b - sqrt_disc) / 2.0   # smaller root
    omega2 = (-b + sqrt_disc) / 2.0   # larger root

    # Effective coupling coefficient for branch 1 (omega1)
    val1 = B - omega1
    denom1 = gamma**2 * (2*omega1 - 1) + (1 - omega1)**2
    if denom1 == 0:
        k_eff1 = 0.0
    else:
        tmp1 = A * val1**2 / denom1
        k_eff1 = math.sqrt(tmp1 / (1 + tmp1)) if tmp1 >= 0 else 0.0
    keff1_norm = k_eff1 / norm_k_eff

    # Effective coupling coefficient for branch 2 (omega2)
    val2 = B - omega2
    denom2 = gamma**2 * (2*omega2 - 1) + (1 - omega2)**2
    if denom2 == 0:
        k_eff2 = 0.0
    else:
        tmp2 = A * val2**2 / denom2
        k_eff2 = math.sqrt(tmp2 / (1 + tmp2)) if tmp2 >= 0 else 0.0
    keff2_norm = k_eff2 / norm_k_eff

    rows.append([ar, omega1, omega2, keff1_norm, keff2_norm])

# Write CSV
with open('/app/outputs/coupled_vibration_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['aspect_ratio', 'omega_1', 'omega_2', 'keff_1_norm', 'keff_2_norm'])
    writer.writerows(rows)
