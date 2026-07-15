import numpy as np
from scipy.integrate import quad
import json

# Constants
R = 8.314462618  # J/(mol·K)
k = 1.380649e-23 # J/K
h = 6.62607015e-34 # J·s
pi = np.pi

def debye(x):
    if x == 0:
        return 1.0
    # Numerical integration of ∫_0^x y^3/(e^y-1) dy
    integral, _ = quad(lambda y: y**3 / (np.exp(y) - 1.0), 0, x, limit=200)
    return 3.0 * integral / x**3

def compute():
    # Solid limit parameters
    mu = 1.0
    L_solid = 0.001
    T = 1000.0
    Theta_D = 0.1  # K
    Theta_solid = Theta_D * (1 + L_solid)
    x_solid = Theta_solid / T
    D_solid = debye(x_solid)
    term1 = 4.0 * D_solid - 3.0 * x_solid / (np.exp(x_solid) - 1.0)
    factor_L_solid = 1.0 - (L_solid / (4.0 * (L_solid + 1.0))) * (3.0 - L_solid / (L_solid + 1.0))
    Cv_solid = (3.0 * R / mu) * term1 * factor_L_solid
    Cv_expected_solid = 3.0 * R / mu
    rel_err_solid = abs(Cv_solid - Cv_expected_solid) / abs(Cv_expected_solid)

    # Gas limit parameters
    L_gas = 100.0
    Theta_gas = Theta_D * (1 + L_gas)
    x_gas = Theta_gas / T
    D_gas = debye(x_gas)
    term1_gas = 4.0 * D_gas - 3.0 * x_gas / (np.exp(x_gas) - 1.0)
    factor_L_gas = 1.0 - (L_gas / (4.0 * (L_gas + 1.0))) * (3.0 - L_gas / (L_gas + 1.0))
    Cv_gas = (3.0 * R / mu) * term1_gas * factor_L_gas
    Cv_expected_gas = 3.0 * R / (2.0 * mu)
    rel_err_gas = abs(Cv_gas - Cv_expected_gas) / abs(Cv_expected_gas)

    # Entropy check parameters
    L_ent = 100.0
    T_ent = 1000.0
    Theta_D_ent = 0.1
    Theta_ent = Theta_D_ent * (1 + L_ent)
    x_ent = Theta_ent / T_ent
    D_ent = debye(x_ent)
    # Generalized Debye entropy (Eq. 14)
    term_ent1 = 4.0 * D_ent * (1.0 - 3.0 * L_ent / (8.0 * (L_ent + 1.0)))
    term_ent2 = 3.0 * np.log(1.0 - np.exp(-x_ent))
    S_computed = (R / mu) * (term_ent1 - term_ent2)
    # Ideal gas entropy (Eq. 15, Sackur-Tetrode)
    v = 0.0821   # m³/mol
    m = 1.660539e-27  # kg (approx 1 amu)
    g_a = 1.0
    arg = h**3 / ((2 * pi * m * k * T_ent)**(1.5) * g_a * m * v)
    S_ig = (R / mu) * (2.5 - np.log(arg))
    rel_err_S = abs(S_computed - S_ig) / abs(S_ig)

    result = {
        "solid_limit": {
            "mu": mu,
            "L": L_solid,
            "T": T,
            "Theta_D": Theta_D,
            "computed_Cv": Cv_solid,
            "expected_Cv": Cv_expected_solid,
            "relative_error": rel_err_solid
        },
        "gas_limit": {
            "mu": mu,
            "L": L_gas,
            "T": T,
            "Theta_D": Theta_D,
            "computed_Cv": Cv_gas,
            "expected_Cv": Cv_expected_gas,
            "relative_error": rel_err_gas
        },
        "entropy_check": {
            "L": L_ent,
            "T": T_ent,
            "v": v,
            "mu": mu,
            "m": m,
            "g_a": g_a,
            "computed_S": S_computed,
            "ideal_gas_S": S_ig,
            "relative_error": rel_err_S
        }
    }

    with open("/app/outputs/verification_results.json", "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    compute()
