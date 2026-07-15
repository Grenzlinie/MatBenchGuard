import numpy as np
from scipy.special import jn_zeros, j0, j1
from scipy.integrate import quad
import csv

# Crystal and pump parameters (SI units)
R = 0.003          # m (3 mm)
L = 0.002          # m (2 mm)
lam = 13.0          # W/(m·K)
beta = 2070.0       # m⁻¹ (20.7 cm⁻¹)
omega = 0.00032     # m (0.32 mm)
P = 20.0            # W
lambda_p = 808e-9
lambda_L = 1064e-9
eta = 1.0 - lambda_p / lambda_L   # ≈0.2406
I0 = 2.0 * P / (np.pi * omega**2)
T_amb = 5.0          # °C (relative ambient temperature)

sigma_vals = [0.0, 0.6, 100.0]
N_terms = 50         # number of Bessel terms
nr = 100
nz = 100

# Bessel zeros and derivatives
alpha = jn_zeros(0, N_terms)           # α_n, n=1..N_terms
J0prime = -j1(alpha)                   # J₀'(α_n)
J1_sq = j1(alpha)**2

# Compute radial integral I_n = ∫_0^R r J₀(α_n r/R) exp(-2r²/ω²) dr
I_n = np.empty(N_terms)
for i, a_n in enumerate(alpha):
    integrand = lambda r, a=a_n: r * j0(a * r / R) * np.exp(-2 * r**2 / omega**2)
    I_n[i] = quad(integrand, 0.0, R, limit=200)[0]

# Pre‑factor C_n where f_n(z) = C_n * exp(-β z)
C_n = (2 * eta * beta * I0 / (lam * R**2 * J1_sq)) * I_n    # (K/m³?)

a_vals = alpha / R      # a_n = α_n / R

csv_path = "/app/outputs/temperature_field.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sigma", "r_mm", "z_mm", "u_degC"])

    for sigma in sigma_vals:
        # Build modal coefficients A_n, B_n for this σ
        A_n = np.empty(N_terms)
        B_n = np.empty(N_terms)
        for i, a in enumerate(a_vals):
            aL = a * L
            shL = np.sinh(aL)
            chL = np.cosh(aL)

            # phi_n'(0) = (R / α_n) * C_n  because I'(0)=1
            phi0_prime = (R / alpha[i]) * C_n[i]

            # I(L) and I'(L) analytical formulas
            b = beta
            # I(L)
            exp_aL = np.exp(aL)
            exp_baL = np.exp(-b*L)
            exp_maL = np.exp(-aL)
            I_L = 0.5 * (
                (exp_aL - exp_baL) / (a + b) +
                (exp_baL - exp_maL) / (a - b)
            )
            Iprime_L = 0.5 * (
                (a * exp_aL + b * exp_baL) / (a + b) +
                (-b * exp_baL + a * exp_maL) / (a - b)
            )

            phi_L = (R * C_n[i] / alpha[i]) * I_L
            phi_prime_L = (R * C_n[i] / alpha[i]) * Iprime_L

            # Denominator
            D = (sigma**2 + a**2) * shL + 2.0 * sigma * a * chL

            # P_n and Q_n
            j0p = J0prime[i]  # negative
            # P_n
            term1_P = sigma * phi_prime_L
            term2_P = -(2 * sigma * T_amb) / (R * j0p) * shL
            term3_P = -(2 * sigma**2 * T_amb) / (alpha[i] * j0p) * chL
            term4_P = (2 * sigma**2 * T_amb) / (alpha[i] * j0p)
            Pn = term1_P + term2_P + term3_P + term4_P

            # Q_n
            Qn = ((2 * sigma**2 * T_amb) / (alpha[i] * j0p)) * shL \
                 + ((2 * sigma * T_amb) / (R * j0p)) * chL \
                 + ((2 * sigma * T_amb) / (R * j0p))

            # A_n
            A_num = (-sigma * phi0_prime * shL
                     - a * phi0_prime * chL
                     + a * phi_prime_L
                     + Pn)
            A_n[i] = A_num / D

            # B_n
            B_num = (a * phi0_prime * shL
                     + sigma * phi0_prime * chL
                     + sigma**2 * phi_L
                     + Qn)
            B_n[i] = B_num / D

        # Grid evaluation
        r_vals = np.linspace(0.0, R, nr)   # m
        z_vals = np.linspace(0.0, L, nz)   # m
        Rgrid, Zgrid = np.meshgrid(r_vals, z_vals, indexing='ij')  # (nr, nz)

        u = np.zeros_like(Rgrid)
        for i, a in enumerate(a_vals):
            # z‑dependent part: A cosh(az) + B sinh(az) + φ(z)
            az = a * Zgrid
            cosh_az = np.cosh(az)
            sinh_az = np.sinh(az)
            # φ(z) = (R C / α) * I(z)
            # I(z)
            exp_az = np.exp(az)
            exp_mbz = np.exp(-beta * Zgrid)
            exp_maz = np.exp(-az)
            I_z = 0.5 * (
                (exp_az - exp_mbz) / (a + beta) +
                (exp_mbz - exp_maz) / (a - beta)
            )
            phi_z = (R * C_n[i] / alpha[i]) * I_z

            axial_part = A_n[i] * cosh_az + B_n[i] * sinh_az + phi_z
            radial_part = j0(alpha[i] * Rgrid / R)
            u += axial_part * radial_part

        # Convert to mm and °C
        r_mm = Rgrid * 1000.0
        z_mm = Zgrid * 1000.0
        u_degC = u

        # Write rows
        for i_r in range(nr):
            for i_z in range(nz):
                writer.writerow([
                    sigma,
                    round(r_mm[i_r, i_z], 6),
                    round(z_mm[i_r, i_z], 6),
                    round(u_degC[i_r, i_z], 6)
                ])
