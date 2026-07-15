import math
import csv

# Copperlike material constants from Tables I and II (public)
G = 51e9              # Pa
nu = 0.3              # dimensionless
rho = 9830            # kg/m^3
sigma0 = 200e6        # Pa
rho_d_m = 1e15        # 1/m^2
N = 4
l_c = 1e-6            # m
dt_c = 2e-10          # s
psi_inc_s = 1e-3      # dimensionless
psi_fluc_coeff = 0.033  # ψ1 = ψ2 = 0.033 * ψ_inc_s
psi_amp = psi_fluc_coeff * psi_inc_s

# Critical dislocation velocity
c_s = math.sqrt(G / rho)
v_cr = (math.sqrt(2) * c_s / N) * math.sqrt((1 - nu) / (1 - 2 * nu))

with open('/app/outputs/critical_velocity.txt', 'w') as f:
    f.write(f"{v_cr}\n")

# Time instances for evaluation
times = [5e-9, 1e-8, 2e-8]   # seconds
t_ns_list = [5, 10, 20]       # nanoseconds

U0f = l_c**2 * rho_d_m * sigma0 * psi_inc_s / 12.0

rows = []
for vratio in [x / 10.0 for x in range(0, 10)]:
    v_d = vratio * v_cr
    zeta_c = l_c - N * v_d * dt_c
    if zeta_c <= 0:
        zeta_c = 1e-12   # safety guard, not reached for vratio ≤ 0.9

    # dynamic hardening theta_psi
    if vratio == 0.0:
        theta_psi = 0.0
    else:
        fac = (c_s / v_cr) ** 2 * vratio ** 2
        theta_psi = (G * rho_d_m * zeta_c**2) / (3 * N**2) * fac / (1 - vratio**2)

    for t, t_ns in zip(times, t_ns_list):
        # position along the path at a fixed material point (x=0)
        zeta = -N * v_d * t
        # dimensionless coordinate for the incompatibility modulation
        s = math.sqrt(24) * zeta / zeta_c if zeta_c != 0 else 0.0
        psi_inc = psi_inc_s + psi_amp * math.sin(s) + psi_amp * math.cos(s)

        Uzf = U0f - (zeta_c**2 * rho_d_m / 12.0) * (sigma0 * psi_inc + 0.5 * theta_psi * psi_inc**2)
        k_s = Uzf / U0f
        rows.append([vratio, t_ns, k_s])

# Write CSV with required columns
with open('/app/outputs/k_s_vs_velocity.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['vd_over_vcr', 't_ns', 'k_s'])
    writer.writerows(rows)