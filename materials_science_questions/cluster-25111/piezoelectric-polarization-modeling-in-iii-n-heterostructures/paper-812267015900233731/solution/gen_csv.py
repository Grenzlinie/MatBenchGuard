import csv
import math

# Parameters
dE_screened = 34.0  # meV/GPa
dE_unscreened = {
    0: 12.0,
    1e16: 18.0,
    1e17: 26.0,
    1e18: 34.0
}
J_mid = {
    0: 50.0,
    1e16: 10.0,
    1e17: 0.1,
    1e18: 1e-6
}
p = 2.0  # sigmoid steepness

J_start = 1e-6
J_end = 1e3
num_points = 30
J_values = [J_start * (J_end/J_start) ** (i/(num_points-1)) for i in range(num_points)]

output_path = "/app/outputs/simulation_dE_E_dp.csv"

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["N_D", "current_density", "dE_E_dp"])
    for N_D in [0, 1e16, 1e17, 1e18]:
        dE0 = dE_unscreened[N_D]
        j0 = J_mid[N_D]
        for J in J_values:
            if dE0 == dE_screened:
                dE = dE_screened
            else:
                x = J / j0
                factor = (x ** p) / (1.0 + x ** p)
                dE = dE0 + (dE_screened - dE0) * factor
            writer.writerow([N_D, J, dE])
