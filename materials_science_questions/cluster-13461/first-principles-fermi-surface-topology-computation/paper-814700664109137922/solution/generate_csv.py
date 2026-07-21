import csv, sys, cmath, math

# Representative parameters (SI)
e = 1.602e-19          # C
n0 = 1.0e24            # m^-3  (1e18 cm^-3)
mu_e = 1.0             # m^2/Vs (electron mobility)
mu_h = 2.0             # m^2/Vs (hole mobility)

# Magnetic fields (T)
B_vals = [1.0, 2.0, 4.0, 8.0, 12.0]
# p/n ratios
ratios = [i/100 for i in range(95, 106)]  # 0.95 to 1.05 inclusive step 0.01

writer = csv.writer(sys.stdout)
writer.writerow(['B', 'p_over_n', 'value'])

for B in B_vals:
    for r in ratios:
        n = n0
        p = r * n0
        # Complex resistivity formula (Eq. 1)
        numerator = 1.0 + mu_e*mu_h*B*B + 1j*(mu_e - mu_h)*B
        denominator = e * (n*mu_e + p*mu_h + 1j*(p - n)*mu_e*mu_h*B)
        rho = numerator / denominator
        rho_xx = rho.real

        # Zero-field resistivity for this carrier ratio
        rho_0_num = 1.0 + 0j
        rho_0_den = e * (n*mu_e + p*mu_h + 0j)
        rho_0 = (rho_0_num / rho_0_den).real

        MR = (rho_xx - rho_0) / rho_0
        writer.writerow([B, r, MR])
