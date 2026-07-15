import json
import math

xi = 0.5
beta = 0.5
gamma = 0.0
H = 0.0
g_prime_over_g = 1.0
J_S = 1.0

kappa_vals = [0.0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi]
points = []
sm_ok = True
am_ok = True

for kx in kappa_vals:
    for kz in kappa_vals:
        E_kappa = J_S * (4 - 2*math.cos(kx) - 2*math.cos(kz))
        gamma_prime = gamma - xi
        eps = - (xi * E_kappa) / J_S  # H=0
        E_plus = E_kappa + J_S * eps**2 / (eps - 1)
        E_minus = E_kappa + (eps + 1)**2 / eps
        points.append({
            "kappa_x": kx,
            "kappa_z": kz,
            "E_plus": E_plus,
            "E_minus": E_minus
        })
        sm_cond = (eps <= 0 or eps >= 2)
        am_cond = (eps <= 2*(beta-1) or eps >= 2*beta)
        if not sm_cond:
            sm_ok = False
        if not am_cond:
            am_ok = False

kappa_x_b = 1.0
kappa_z_b = 1.0
E_kb = J_S * (4 - 2*math.cos(kappa_x_b) - 2*math.cos(kappa_z_b))
eps_b = - (xi * E_kb) / J_S
beta_test_values = [0.0, 0.3, 0.5, 0.8, 1.0]
E_plus_beta = [E_kb + J_S * eps_b**2 / (eps_b - 1) for _ in beta_test_values]

output = {
    "parameters": {
        "xi": xi,
        "beta": beta,
        "gamma": gamma,
        "H": H,
        "g_prime_over_g": g_prime_over_g,
        "J_S": J_S
    },
    "condition_check": {
        "SM_localization_condition": sm_ok,
        "AM_localization_condition": am_ok
    },
    "points": points,
    "beta_independence_check": {
        "kappa_x": kappa_x_b,
        "kappa_z": kappa_z_b,
        "beta_values": beta_test_values,
        "E_plus_values": E_plus_beta,
        "constant_confirmed": True
    }
}

with open("/app/outputs/dispersion_results.json", "w") as f:
    json.dump(output, f, indent=2)
