import csv, math, sys

mu_eq = 1.86
mu_ov = 10.24
zeta = 421.0
tau = 1.0
alpha = 0.449
beta_val = 0.494
b = 51078
epsilon0 = -0.11
lambda0 = 1.0 / (1.0 - epsilon0)

frequencies = [10, 20, 30, 40, 50, 60]
amplitudes = [0.001, 0.0025, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05]

rows = []
pi = math.pi
for f in frequencies:
    omega = 2 * pi * f
    omega_tau = omega * tau
    for amp in amplitudes:
        a = 1.0 + (2 * b / pi) * amp * (omega_tau ** alpha)
        term = (omega * zeta / a) ** beta_val
        cos_term = math.cos(beta_val * pi / 2)
        sin_term = math.sin(beta_val * pi / 2)
        denom = 1.0 + 2 * term * cos_term + term * term
        G_prime = (
            mu_eq * (lambda0**2 + 2 / lambda0)
            + 3 * mu_ov * (term**2 + term * cos_term) / denom
        )
        G_double_prime = 3 * mu_ov * (term * sin_term) / denom
        rows.append([f, amp, G_prime, G_double_prime])

with open(sys.argv[1], 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['frequency_Hz', 'strain_amplitude', 'G_prime_MPa', 'G_double_prime_MPa'])
    writer.writerows(rows)
