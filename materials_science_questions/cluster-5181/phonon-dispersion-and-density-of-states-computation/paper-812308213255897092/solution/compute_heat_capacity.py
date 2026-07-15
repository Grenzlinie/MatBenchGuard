import numpy as np
from scipy.integrate import quad
import csv

# Physical constants
h = 6.62607015e-34  # Planck constant, J·s
k_B = 1.380649e-23   # Boltzmann constant, J/K
nu_max = 2.5e11       # Hz

# Density of states g(nu)
def g(nu):
    return 1.45e-13 * nu**2 - 2.75e-37 * nu**4

# Integrand for heat capacity per 3R
def integrand(nu, T):
    x = h * nu / (k_B * T)
    if x == 0:
        return 0.0
    factor = (x**2) * np.exp(x) / (np.exp(x) - 1)**2
    return g(nu) * factor

# Temperatures
temperatures = [0.2, 0.4, 0.6, 0.8, 1.0]

output_path = '/app/outputs/heat_capacity.csv'
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'C_v_over_3R'])
    for T in temperatures:
        integral, error = quad(integrand, 0, nu_max, args=(T,), limit=200, epsabs=1e-14, epsrel=1e-12)
        Cv_over_3R = integral / 3.0  # C_v/3R
        writer.writerow([T, Cv_over_3R])
