import math
import csv

hbar_e = 6.582119569e-16   # T·m^2 (ℏ/e)
a = 2.46e-10               # m
Lz = 3.5e-10              # m
E = 340.0                  # N/m
nu = 0.165
beta = 3.0
sqrt3 = math.sqrt(3.0)

forces_nN = [0.01, 0.05, 0.1, 0.2]
x_range_angstrom = list(range(-100, 101, 2))   # -100 .. 100 Å step 2

outfile = "/app/outputs/step_02_pseudomag_field.csv"

with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["F_nN", "x_A", "B_z_T"])
    for F_nN in forces_nN:
        F_N = F_nN * 1e-9
        # common factor (hbar/e) * (F0/(E Lz^2)) * (√3 β/(2a)) * (2+ν)
        factor = (hbar_e / (E * Lz**2)) * (sqrt3 * beta / (2.0 * a)) * (2.0 + nu) * F_N
        for x_A in x_range_angstrom:
            # scaled dimensionless coordinate x → x/Lz  (Lz = 3.5 Å)
            x_scaled = x_A / 3.5
            if x_A == 0:
                B_z = 0.0
            else:
                abs_x = abs(x_scaled)
                term1 = 2.0 * math.log(1.0 + abs_x) / abs_x
                term2 = (2.0 + 3.0 * abs_x) / (1.0 + abs_x)**2
                bracket = term1 - term2
                # Eq. (21) with the minus sign for the K1,+ valley
                B_z = -factor * (1.0 / x_scaled) * bracket
            writer.writerow([F_nN, x_A, B_z])
