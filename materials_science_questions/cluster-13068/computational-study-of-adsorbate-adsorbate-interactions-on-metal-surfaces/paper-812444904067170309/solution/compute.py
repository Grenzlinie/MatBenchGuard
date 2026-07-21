import sys
import numpy as np
from scipy.integrate import quad

# Parameters (all in Ry or a0)
beta = 0.8
l = 0.244
a0 = 1.0
factor = (beta * l / a0) ** 2
V_a = -0.019
eps_a = 0.102
eps_F = 0.3

def sig_a(omega):
    """Self-energy Σ_a(ω) = Λ - iΔ (Ry)."""
    if omega >= 0:
        lam = factor * (V_a - omega)**2 / (1+omega)**2 * (3+omega)
        delta = factor * (V_a - omega)**2 * 2 / (np.sqrt(omega) * (1+omega)**2)
    else:
        abs_omega = -omega
        lam = factor * (V_a - omega)**2 / (1+omega)**2 * ((3+omega) - 2/np.sqrt(abs_omega))
        delta = 0.0
    return lam - 1j * delta

def sig_ab(d, omega):
    """Two-impurity self-energy Σ_ab(d,ω) (Ry)."""
    abs_d = d
    sqrt_omega = np.sqrt(omega + 0j)
    term1 = factor * (2 + (1 + abs_d) * (1+omega)) / (1+omega)**2 * np.exp(-abs_d)
    term2 = -2j * factor * np.exp(1j * abs_d * sqrt_omega) / (sqrt_omega * (1+omega)**2)
    return term1 + term2

def integrand(omega, d):
    D = omega - eps_a - sig_a(omega)
    z = sig_ab(d, omega) / D
    return np.imag(np.log(1 - z**2))

def compute_interaction_energy(d):
    res, _ = quad(lambda w: integrand(w, d), -5.0, eps_F, points=[0.0], limit=200,
                  epsabs=1e-12, epsrel=1e-12)
    W = -(2 / np.pi) * res
    return W

def main():
    out = sys.argv[-1]
    if 'sigma' in out:
        omegas = [0.05, 0.1, 0.2, 0.3, 0.5, 1.0]
        with open(out, 'w') as f:
            for omega in omegas:
                s = sig_a(omega)
                lam, delta = s.real, -s.imag
                f.write(f"{omega},{lam:.12f},{delta:.12f}\n")
    elif 'phase' in out:
        s = sig_a(eps_F)
        lam, delta = s.real, -s.imag
        eta = np.arctan2(delta, eps_F - eps_a - lam)
        with open(out, 'w') as f:
            f.write(f"{eta:.12f}\n")
    elif 'interaction' in out:
        distances = [2,3,4,5,6,7,8,9,10,12,15,20]
        with open(out, 'w') as f:
            for d in distances:
                W = compute_interaction_energy(d)
                f.write(f"{d},{W:.12f}\n")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()