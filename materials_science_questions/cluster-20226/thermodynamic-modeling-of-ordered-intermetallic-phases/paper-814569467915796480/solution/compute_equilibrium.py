import math
import sys

def alpha(omega):
    """Asymptotic form Eq. (14): α(ω) ≈ 6/5 - √π ω^{1/3}"""
    if omega <= 0.0:
        return 1.2
    return 1.2 - math.sqrt(math.pi) * (omega ** (1.0/3.0))

def compute_C(xi, omega):
    """Left-hand side of Eq. (13): C = (ξ/3) α(ω)^{1/3} / (1-ω)"""
    a = alpha(omega)
    if a <= 0.0:
        return float('inf')
    return (xi / 3.0) * (a ** (1.0/3.0)) / (1.0 - omega)

def f_x(x):
    """Right-hand side of Eq. (13): x^{1/3} (1-x)"""
    return (x ** (1.0/3.0)) * (1.0 - x)

def solve_x2(omega, xi=0.5):
    """Find the x ≥ 0.25 solution of Eq. (13). Returns None if no solution."""
    C = compute_C(xi, omega)
    max_val = f_x(0.25)   # β_c ≈ 0.47247
    if C > max_val:
        return None
    # Bisection on [0.25, 1-eps]
    lo, hi = 0.25, 0.9999999
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        fm = f_x(mid) - C
        if abs(fm) < 1e-12 or (hi - lo) < 1e-12:
            return mid
        if fm > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def reduced_free_energy(omega, x, omega0):
    """Eq. (17): f(ω) = F / (V m Δc₀²)"""
    term1 = 1.5 * x * (1.0 - x) * omega * (1.0 - omega)
    term2 = 0.5 * omega * ((1.0 - omega0) - (1.0 - omega) * x) ** 2
    term3 = 0.5 * (1.0 - omega) * (omega0 - omega * x) ** 2
    return term1 + term2 + term3

def compute_equilibrium_for_omega0(omega0, xi=0.5):
    # homogeneous state at ω=0
    f0 = 0.5 * omega0 * omega0
    best_omega = 0.0
    best_x = 0.0
    min_f = f0

    # fine grid of ω from 0.0001 to 0.5
    step = 0.0002
    omega = step
    while omega <= 0.5:
        x2 = solve_x2(omega, xi)
        if x2 is not None:
            f_val = reduced_free_energy(omega, x2, omega0)
            if f_val < min_f:
                min_f = f_val
                best_omega = omega
                best_x = x2
        omega += step

    # If best_omega is still 0, no precipitate
    if best_omega <= 0.0:
        return 0.0, 0.0, 0.0

    # Recompute x at best_omega precisely
    x_eq = solve_x2(best_omega, xi)
    if x_eq is None:
        x_eq = best_x

    # Reduced radius Eq. (19): R_eq/R00 = x^{-2/3} α(ω)^{-1/3}
    a = alpha(best_omega)
    if a <= 0.0 or x_eq <= 0.0:
        R_norm = 0.0
    else:
        R_norm = (x_eq ** (-2.0/3.0)) * (a ** (-1.0/3.0))

    return best_omega, x_eq, R_norm

def main():
    output_path = "/app/outputs/equilibrium_curves.csv"
    with open(output_path, 'w') as f:
        f.write("omega0,omega_eq,x_eq,R_eq_norm\n")
        omega0 = 0.0
        while omega0 <= 0.5001:
            omega_eq, x_eq, R_norm = compute_equilibrium_for_omega0(omega0)
            # Round to avoid tiny numerical artifacts
            omega_eq = round(omega_eq, 6)
            x_eq = round(x_eq, 6)
            R_norm = round(R_norm, 6)
            f.write(f"{omega0:.6f},{omega_eq:.6f},{x_eq:.6f},{R_norm:.6f}\n")
            omega0 = round(omega0 + 0.01, 6)

if __name__ == "__main__":
    main()