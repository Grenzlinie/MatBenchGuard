import sys, json, math
import numpy as np
from scipy.integrate import quad

def e_bar_per_ngkbtheta(T_ratio):
    """Returns e = \bar{E} / (n N_G k_B Theta) = (T/Theta)^2 * \int_0^{Theta/T} x/(e^x-1) dx."""
    if T_ratio <= 0:
        return 0.0
    upper = 1.0 / T_ratio
    def integrand(x):
        return x / (math.exp(x) - 1.0)
    I, _ = quad(integrand, 0.0, upper, limit=200)
    return (T_ratio ** 2) * I

def compute_n_min(T_ratio, alpha=10.0, delta=0.01):
    e = e_bar_per_ngkbtheta(T_ratio)
    # condition A bound (Eq. 37)
    if e == 0:
        n_A = float('inf')
    else:
        n_A = (1.0 / T_ratio) * (alpha / (4.0 * e)) * ((4.0 * e / alpha) + 1.0) ** 2
    # condition B bound (Eq. 40)
    n_B = (2.0 * alpha / delta) * (1.0 / T_ratio) * e
    return max(n_A, n_B)

def main():
    T_ratios = np.logspace(-2, 2, 200)  # 0.01 to 100, 200 points
    curve = []
    for tr in T_ratios:
        n = compute_n_min(tr)
        curve.append({"T_ratio": float(tr), "n_min": float(n)})
    
    materials = [
        {"material": "iron", "T": 470.0, "a0_angstrom": 2.5, "theta": 470.0},
        {"material": "iron", "T": 1.0, "a0_angstrom": 2.5, "theta": 470.0},
        {"material": "carbon", "T": 270.0, "a0_angstrom": 1.5, "theta": 2230.0},
        {"material": "silicon", "T": 1.0, "a0_angstrom": 2.4, "theta": 645.0},
    ]
    estimates = []
    for m in materials:
        T = m["T"]
        theta = m["theta"]
        T_ratio = T / theta
        n_min = compute_n_min(T_ratio)
        l_min_um = n_min * m["a0_angstrom"] * 1e-4
        estimates.append({
            "material": m["material"],
            "T": float(T),
            "a0_angstrom": float(m["a0_angstrom"]),
            "theta": float(theta),
            "n_min": float(n_min),
            "l_min_um": float(l_min_um)
        })
    
    result = {
        "n_min_curve": curve,
        "material_estimates": estimates
    }
    with open("/app/outputs/harmonic_results.json", "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
