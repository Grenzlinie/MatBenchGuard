import numpy as np
from scipy.integrate import quad
import csv
import os

sigma_A = 1.0
beta = 1.0e-9   # J/m^3
# 2*xi_A = 1 nm => omega_A = sigma_A / (2*xi_A) = 1e9 J/m^3, and beta*omega_A = 1
omega_A = 1.0e9
assert np.isclose(beta * omega_A, 1.0)

alphas = [2, 3, 4]

def u_g_e_from_u_m(u_m, alpha):
    """Equilibrium GB composition from parallel-tangent condition, Eq. (60)."""
    if u_m == 0:
        return 0.0
    ratio = (u_m / (1 - u_m)) * np.exp(alpha)
    return ratio / (1 + ratio)

def common_tangent_u_m(alpha):
    """Matrix composition at which the two parallel tangents merge, Eq. (63)."""
    # beta*omega_A = 1
    return (np.exp(1) - 1) / (np.exp(alpha) - 1)

# ---- Model I: numerical integration of effective potential, Eq. (62) ----
def modelI_sigma(u_m, alpha):
    if u_m == 0:
        return sigma_A
    u_m_ct = common_tangent_u_m(alpha)
    if u_m > u_m_ct + 1e-14:
        return np.nan
    def integrand(phi):
        g = 4 * phi * (1 - phi)
        exp_ag = np.exp(alpha * g)
        fac = (u_m / (1 - u_m)) * exp_ag
        u = fac / (1 + fac)
        log_term = np.log((1 - u) / (1 - u_m))
        # Eq. (61): Omega_I/(omega_A) = g + log_term   (since 1/(beta*omega_A) = 1)
        potential = g + log_term
        if potential <= 0:
            return 0.0
        return np.sqrt(potential)
    try:
        integral, _ = quad(integrand, 0, 1, limit=100)
    except Exception:
        return np.nan
    return (4 / np.pi) * sigma_A * integral

# ---- Model II: analytic GB energy, Eq. (71) ----
def modelII_sigma(u_m, alpha):
    if u_m == 0:
        return sigma_A
    u_g = u_g_e_from_u_m(u_m, alpha)
    ratio = (1 - u_g) / (1 - u_m)
    # omega^e / omega_A = 1 + log(ratio)
    omega_ratio = 1 + np.log(ratio)
    if omega_ratio < 0:
        return 0.0
    return sigma_A * np.sqrt(omega_ratio)

# ---- Classical two-phase model: Eq. (72) ----
def classical_sigma(u_m, alpha):
    if u_m == 0:
        return sigma_A
    u_g = u_g_e_from_u_m(u_m, alpha)
    ratio = (1 - u_g) / (1 - u_m)
    omega_ratio = 1 + np.log(ratio)
    if omega_ratio < 0:
        return 0.0
    return sigma_A * omega_ratio

# ---- Generate data ----
points_per_alpha = 200
rows = []
for alpha in alphas:
    u_m_ct = common_tangent_u_m(alpha)
    u_m_vals = np.linspace(1e-4, u_m_ct, points_per_alpha)
    for u_m in u_m_vals:
        rows.append((alpha, 'modelI', u_m, modelI_sigma(u_m, alpha)))
        rows.append((alpha, 'modelII', u_m, modelII_sigma(u_m, alpha)))
        rows.append((alpha, 'classical', u_m, classical_sigma(u_m, alpha)))

# ---- Write output ----
output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, 'gb_energy_data.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'model', 'u_m', 'sigma'])
    writer.writerows(rows)
