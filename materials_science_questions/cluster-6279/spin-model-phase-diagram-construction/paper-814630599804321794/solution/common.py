import numpy as np
from scipy.optimize import fsolve

J0 = 1.0
K0 = 1.25
D = 1.2

def energies(sigma, lam, zeta):
    tilde_alpha1 = 0.5 * D - 2 * sigma * K0 - 0.5 * K0 * (zeta - 1.0) * (sigma + lam)
    tilde_alpha2 = -D / 6.0 - (2.0 / 3.0) * lam * K0 - 0.5 * K0 * (zeta - 1.0) * (sigma + lam)
    E1 = tilde_alpha1 + tilde_alpha2
    E0 = -2.0 * tilde_alpha2
    Eminus1 = -tilde_alpha1 + tilde_alpha2
    return E1, E0, Eminus1

def solve_self(T, zeta, guess=(0.1, -1.5)):
    def eq(vars):
        s, l = vars
        E1, E0, Em1 = energies(s, l, zeta)
        e1 = np.exp(-E1 / T)
        e0 = np.exp(-E0 / T)
        em1 = np.exp(-Em1 / T)
        Z = e1 + e0 + em1
        return [s - (e1 - em1) / Z, l - (e1 - 2*e0 + em1) / Z]
    sol = fsolve(eq, guess, maxfev=2000, xtol=1e-12)
    return sol[0], sol[1]
