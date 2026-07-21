import numpy as np
import math

Z0 = 6
Z1 = 3
Z = 12

def classify_critical(J00_div, J01_div, J11_div):
    """
    Returns 1 if the surface couplings lead to an extraordinary transition
    (T_CS > T_C), 0 otherwise, using the exact condition from Eq. (3.1).
    """
    LHS = 6.0 * (2.0 - J00_div) * (1.0 - (2.0 / 3.0) * J11_div)
    RHS = J01_div ** 2
    return 1 if LHS < RHS else 0


def solve_tcs_cubic(a, b, c):
    """
    Solve the cubic equation (2.24) for x = (k_B T_CS - Z0 J) / (Z1 J),
    and return T_CS / T_C. If no real root x > 2 exists, return 1.0
    (ordinary transition).
    """
    # Coefficients from Eq. (2.24):
    # b x^3 - (1 - c^2 + 2ab + b^2) x^2 + [2a(ab - c^2)(a+2b)] x
    #   - a^2 - (ab - c)^2 = 0
    coeffs = [
        b,                          # x^3
        -(1 - c**2 + 2*a*b + b**2), # x^2
        2 * a * (a*b - c**2) * (a + 2*b),  # x^1
        -a**2 - (a*b - c)**2         # constant
    ]

    # Handle degenerate cases where b = 0 (reduces to quadratic)
    if abs(b) < 1e-14:
        # Quadratic: A x^2 + B x + C = 0
        A = coeffs[1]
        B = coeffs[2]
        C = coeffs[3]
        if abs(A) < 1e-14:
            # Linear or constant, no x >2 expected
            return 1.0
        disc = B**2 - 4*A*C
        if disc < 0:
            return 1.0
        sqrt_disc = math.sqrt(disc)
        x1 = (-B + sqrt_disc) / (2*A)
        x2 = (-B - sqrt_disc) / (2*A)
        candidates = [x for x in (x1, x2) if x > 2.0]
        if candidates:
            x = max(candidates)  # take the larger (surface mode)
            return (x + 2.0) / 4.0
        else:
            return 1.0
    else:
        # Full cubic: use numpy roots
        roots = np.roots(coeffs)
        # select real roots
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-10 and r.real > 2.0]
        if real_roots:
            x = max(real_roots)
            return (x + 2.0) / 4.0
        else:
            return 1.0


def bulk_magnetization(T, tol=1e-12, max_iter=10000):
    """
    Return the bulk magnetization eta at temperature T (in units J/kB).
    Solves eta = tanh( (Z J / (kB T)) * eta ) = tanh( 12/T * eta ).
    """
    if T >= 12.0:
        return 0.0
    # initial guess
    eta = 1.0 - T/12.0   # approximate near T_c, but we can iterate
    if eta <= 0.0:
        eta = 0.5
    for _ in range(max_iter):
        new_eta = math.tanh(12.0 / T * eta)
        if abs(new_eta - eta) < tol:
            return new_eta
        eta = new_eta
    return eta


def layer_magnetization(T, J00, J01, J11, Jb, tol=1e-12, max_iter=20000):
    """
    Solve the four-layer mean-field equations (i=0..3) with coupling
    constants J00, J01, J11, Jb (bulk coupling Jb=1).  The layer i=3 is
    coupled to the bulk magnetization at T.  Returns a list [eta0, eta1, eta2, eta3].
    """
    eta_bulk = bulk_magnetization(T, tol, 10000)
    # initial guess: all equal to bulk
    eta = [eta_bulk] * 4

    for _ in range(max_iter):
        old = eta[:]
        # update equations (simultaneous):
        # eta0 = tanh( (Z0*J00*eta0 + Z1*J01*eta1) / T )
        eta[0] = math.tanh( (Z0 * J00 * old[0] + Z1 * J01 * old[1]) / T )
        # eta1 = tanh( (Z1*J01*eta0 + Z0*J11*eta1 + Z1*Jb*eta2) / T )
        eta[1] = math.tanh( (Z1 * J01 * old[0] + Z0 * J11 * old[1] + Z1 * Jb * old[2]) / T )
        # eta2 = tanh( (Z1*Jb*eta1 + Z0*Jb*eta2 + Z1*Jb*eta3) / T )
        eta[2] = math.tanh( (Z1 * Jb * old[1] + Z0 * Jb * old[2] + Z1 * Jb * old[3]) / T )
        # eta3 = tanh( (Z1*Jb*eta2 + Z0*Jb*eta3 + Z1*Jb*eta_bulk) / T )
        eta[3] = math.tanh( (Z1 * Jb * old[2] + Z0 * Jb * old[3] + Z1 * Jb * eta_bulk) / T )

        max_diff = max(abs(eta[i] - old[i]) for i in range(4))
        if max_diff < tol:
            return eta
    return eta
