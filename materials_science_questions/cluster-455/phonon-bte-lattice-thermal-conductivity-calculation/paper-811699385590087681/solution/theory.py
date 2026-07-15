import csv
import numpy as np
from scipy.integrate import quad

# parameters from instruction
kB = 1.380649e-23
hbar = 1.054571817e-34
T = 300.0

# phonon velocities (m/s)
vT1 = 3.55e3
vT2 = 1.30e3
vL1 = 4.92e3
vL2 = 2.46e3
# characteristic velocities for combined rates (average of segment values)
vC_T = (vT1 + vT2) / 2.0
vC_L = (vL1 + vL2) / 2.0

# cutoff temperatures
th1 = 90.0
th2 = 108.0
th4 = 208.0
th3 = 319.0

# dispersion factors (R_i) – extremely small, kept for completeness
R1 = 2.95e-27
R2 = 8.28e-27
R3 = 0.0
R4 = 1.13e-27

# coefficient C
C = (kB / (3.0 * np.pi**2)) * (kB * T / hbar)**3

# integrand for Dubey integrals (without tau)
def integrand(x, R):
    ex = np.exp(x)
    factor = (1.0 + R * x**2 * T**2)**2 / (1.0 + 3.0 * R * x**2 * T**2)
    return x**4 * ex / (ex - 1.0)**2 * factor

# compute the four integrals
I_T1, _ = quad(lambda x: integrand(x, R1), 0.0, th1 / T)
I_T2, _ = quad(lambda x: integrand(x, R2), th1 / T, th2 / T)
I_L1, _ = quad(lambda x: integrand(x, R3), 0.0, th4 / T)
I_L2, _ = quad(lambda x: integrand(x, R4), th4 / T, th3 / T)

# total Debye-like coefficients for the bulk conductivity formula
bulk_coeff_T = (I_T1 / vT1 + I_T2 / vT2) / vC_T
bulk_coeff_L = (I_L1 / vL1 + I_L2 / vL2) / vC_L

# bulk germanium thermal conductivity ~58 W/mK
k_bulk = 58.0
L_b = k_bulk / (C * (bulk_coeff_T + bulk_coeff_L))   # Casimir length (m)

# decrement function F(delta) from Eq. (20)
def F_dec(delta):
    if delta <= 0:
        return 1.0
    # integral from 1 to infinity
    integ, _ = quad(lambda t: (t**(-3) - t**(-5)) * np.exp(-delta * t), 1.0, np.inf)
    return 1.0 - 0.375 * delta**(-2) + 1.5 * delta**(-2) * integ

# thicknesses in nanometres -> metres
thicknesses_nm = [5.67, 10.21, 17.00, 22.67, 28.34, 34.01, 39.68, 45.35, 50.92]
results = []

for d_nm in thicknesses_nm:
    d = d_nm * 1e-9
    delta = d / L_b
    F = F_dec(delta)
    # relaxation rates
    tau_inv_T = vC_T * (1.0 / L_b + 1.0 / (d * F))
    tau_inv_L = vC_L * (1.0 / L_b + 1.0 / (d * F))
    # thermal conductivity contributions
    k_T = C * (I_T1 / vT1 + I_T2 / vT2) / tau_inv_T
    k_L = C * (I_L1 / vL1 + I_L2 / vL2) / tau_inv_L
    k_total = k_T + k_L
    results.append((d_nm, k_total))

# write CSV
with open('/app/outputs/step_02_theory_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['thickness_nm', 'k_theory_WmK'])
    for d_nm, k in results:
        w.writerow([f'{d_nm:.2f}', f'{k:.6f}'])
