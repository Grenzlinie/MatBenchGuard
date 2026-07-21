import csv
import math
import sys

output_file = sys.argv[1]

# Constants
e14 = 0.16  # C/m²
kappa = 13.18
eps0 = 8.8541878128e-12  # F/m
rho = 5.36e3  # kg/m³
c44 = 5.94e10  # N/m²
kB = 1.380649e-23  # J/K

# Derived
eps = kappa * eps0
vT = math.sqrt(c44 / rho)

temperatures = [10.0, 77.0, 300.0]
concentrations = [1e20, 1e21, 1e22]

# Generate 30 log-spaced points from 1e4 to 1e8
log_start = math.log10(1e4)
log_end = math.log10(1e8)
num_points = 30
fluxes = []
for i in range(num_points):
    flux = 10**(log_start + i * (log_end - log_start) / (num_points - 1))
    fluxes.append(flux)

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'carrier_concentration_m3', 'flux_intensity_W_m2', 'ratio_C_over_C0'])
    for T in temperatures:
        T_energy = kB * T
        for n in concentrations:
            for P_T in fluxes:
                # Formula (38): exp( e14^2 * P_T / (8 * eps * n * T_energy * rho * vT^3) )
                exponent = (e14**2 * P_T) / (8.0 * eps * n * T_energy * rho * vT**3)
                ratio = math.exp(exponent)
                writer.writerow([T, n, P_T, ratio])
