import csv
import math

# Constants (cgs units)
c11 = 1.68e12
c12 = 1.21e12
c44 = 0.75e12
rho = 8.96
a_cm = 3.61e-8  # 3.61 Å -> cm
epsilon = c11 - c12 - 2*c44

# k_max in 1/Å (as given in the public instruction)
k_max_per_angstrom = {
    "100": math.sqrt(2) * math.pi / (a_cm * 1e8),
    "110": math.sqrt(5) * math.pi / (a_cm * 1e8),
    "111": math.sqrt(1.5) * math.pi / (a_cm * 1e8)
}

num_points = 21

with open("/app/outputs/dispersion_curves.csv", mode='w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["direction", "mode", "k", "frequency"])

    for direction, kmax in k_max_per_angstrom.items():
        for i in range(num_points):
            k_per_A = i * kmax / (num_points - 1)
            k_cm = k_per_A * 1e8

            if direction == "100":
                sin_arg = a_cm * k_cm / (2 * math.sqrt(2))
                sin2 = math.sin(sin_arg)**2
                factor = 8.0 / (rho * a_cm**2)
                omega2_L = factor * sin2 * c11
                omega2_T = factor * sin2 * c44
                w.writerow([direction, "L", k_per_A, math.sqrt(max(0, omega2_L)) / 1e13])
                w.writerow([direction, "T1", k_per_A, math.sqrt(max(0, omega2_T)) / 1e13])
                w.writerow([direction, "T2", k_per_A, math.sqrt(max(0, omega2_T)) / 1e13])

            elif direction == "110":
                sin_arg = a_cm * k_cm / 4.0
                sin2 = math.sin(sin_arg)**2
                factor = 8.0 / (rho * a_cm**2)
                # L mode
                omega2_L = factor * sin2 * (2*c11 - epsilon - (2*c11 - c44 - epsilon) * sin2)
                # T1 mode
                omega2_T1 = factor * sin2 * (epsilon + 2*c44 - (c44 + epsilon) * sin2)
                # T2 mode
                omega2_T2 = factor * sin2 * (2*c44 - (2*c44 - c11) * sin2)
                w.writerow([direction, "L", k_per_A, math.sqrt(max(0, omega2_L)) / 1e13])
                w.writerow([direction, "T1", k_per_A, math.sqrt(max(0, omega2_T1)) / 1e13])
                w.writerow([direction, "T2", k_per_A, math.sqrt(max(0, omega2_T2)) / 1e13])

            elif direction == "111":
                sin_arg = a_cm * k_cm / math.sqrt(6)
                sin2 = math.sin(sin_arg)**2
                factor = 2.0 / (rho * a_cm**2)
                omega2_L = factor * (3*c11 - 2*epsilon) * sin2
                omega2_T = factor * (3*c44 + epsilon) * sin2
                w.writerow([direction, "L", k_per_A, math.sqrt(max(0, omega2_L)) / 1e13])
                w.writerow([direction, "T1", k_per_A, math.sqrt(max(0, omega2_T)) / 1e13])
                w.writerow([direction, "T2", k_per_A, math.sqrt(max(0, omega2_T)) / 1e13])
