import numpy as np
from scipy.special import binom
from scipy.optimize import fsolve, bisect

# ========== Physical constants ==========
Jz = 1.0  # energy unit

# ========== Helper: function f(x,y,H1,H2) ==========
def f_func(x, y, H1, H2, T, Jx, Jy):
    beta = 1.0 / T
    dx = Jx - Jy
    sx = Jx + Jy
    sum_xy = x + y + H1 + H2
    diff_xy = x - y + H1 - H2
    X0 = np.sqrt(dx*dx + sum_xy*sum_xy)
    Y0 = np.sqrt(sx*sx + diff_xy*diff_xy)
    if X0 == 0.0:
        # limit: f -> (H1+H2) * ? Actually when X0->0, sum_xy=0 and Jx=Jy (dx=0).
        # The expression becomes (0)*...? We'll return 0.0 as it's odd.
        return 0.0
    num = sum_xy * np.sinh(beta * X0)
    denom = np.cosh(beta * X0) + np.exp(-2.0 * beta * Jz) * np.cosh(beta * Y0)
    return num / (X0 * denom)

# ========== Compute F(x,y) for given distribution parameters ==========
def compute_F(x, y, w, H0, T, Jx, Jy):
    # Two-site independent distribution: P(H1,H2) = product of single-site distribution
    # Evaluate f for all 9 combos (or 4 if w=0) with appropriate weights
    if w == 0.0:
        # bimodal: H_i ∈ {+H0, -H0} each prob 0.5
        vals = [H0, -H0]
        probs = [0.5, 0.5]
        result = 0.0
        for H1, p1 in zip(vals, probs):
            for H2, p2 in zip(vals, probs):
                result += p1 * p2 * f_func(x, y, H1, H2, T, Jx, Jy)
        return result
    else:
        # trimodal: single-site distribution: P(H) = w δ(H) + (1-w)/2 [δ(H-H0)+δ(H+H0)]
        vals = [0.0, H0, -H0]
        probs = [w, (1-w)/2, (1-w)/2]
        result = 0.0
        for H1, p1 in zip(vals, probs):
            for H2, p2 in zip(vals, probs):
                result += p1 * p2 * f_func(x, y, H1, H2, T, Jx, Jy)
        return result

# ========== Precompute operator shift coefficients ==========
def get_shift_coeffs(a, b):
    # Computes coefficients K[k] such that A_x^a B_x^b = sum_k K[k] * exp(k * Jz * ∇_x)
    # k ranges from -(a+b) to (a+b) in steps of 2? Actually k takes all integer values
    # but many are zero. We compute by expanding (cosh)^a (sinh)^b.
    # Representation: cosh(∇) = (exp(∇)+exp(-∇))/2, sinh(∇) = (exp(∇)-exp(-∇))/2
    # Use convolution

    # Initialize array with a single 1 at position 0 (exp(0*∇))
    coeffs = np.zeros(1)
    coeffs[0] = 1.0
    center = 0

    # Apply cosh a times
    factor_cosh = np.array([0.5, 0.0, 0.5])  # exp(-1*∇), exp(0*∇), exp(+1*∇) weighted
    for _ in range(a):
        new_len = len(coeffs) + 2
        new_coeffs = np.zeros(new_len)
        for i in range(len(coeffs)):
            new_coeffs[i] += coeffs[i] * factor_cosh[1]   # exp(0)
            new_coeffs[i+1] += coeffs[i] * factor_cosh[2]  # exp(+1)
            new_coeffs[i] += coeffs[i] * factor_cosh[0]    # exp(-1)
        coeffs = new_coeffs
        center += 1  # shift center because exp(-1) displaced left

    # Apply sinh b times
    factor_sinh = np.array([-0.5, 0.0, 0.5])  # exp(-1*∇), exp(0*∇), exp(+1*∇) with signs
    for _ in range(b):
        new_len = len(coeffs) + 2
        new_coeffs = np.zeros(new_len)
        for i in range(len(coeffs)):
            new_coeffs[i] += coeffs[i] * factor_sinh[1]   # exp(0)
            new_coeffs[i+1] += coeffs[i] * factor_sinh[2]  # exp(+1)
            new_coeffs[i] += coeffs[i] * factor_sinh[0]    # exp(-1)
        coeffs = new_coeffs
        center += 1

    # Now the array index i corresponds to shift k = (i - center) * Jz
    # We'll return dict mapping k->coeff for non-zero coeffs
    idx = np.nonzero(np.abs(coeffs) > 1e-15)[0]
    res = {}
    for i in idx:
        k = i - center
        res[k] = coeffs[i]
    return res

# ========== Build C_k coefficients ==========
def compute_Ck(z0, w, H0, T, Jx, Jy, max_k=None):
    # Prepare F grid for integer x,y in [-z0, z0]
    x_vals = np.arange(-z0, z0+1, dtype=float) * Jz
    y_vals = np.arange(-z0, z0+1, dtype=float) * Jz
    F_grid = np.zeros((len(x_vals), len(y_vals)))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            F_grid[i, j] = compute_F(x, y, w, H0, T, Jx, Jy)

    # Precompute operator coeffs for all (a,b) combinations with a=z0-p, b=p
    coeff_x = {}
    coeff_y = {}
    for p in range(z0+1):
        a = z0 - p
        b = p
        coeff_x[(a,b)] = get_shift_coeffs(a, b)
        coeff_y[(a,b)] = get_shift_coeffs(a, b)  # same formula

    # Compute C_k
    if max_k is None:
        max_k = 2*z0
    C = np.zeros(max_k+1)

    for p in range(z0+1):
        for q in range(z0+1):
            a, b = z0-p, p
            c, d = z0-q, q
            k = p + q
            # C'_{pq} = binom(z0,p)*binom(z0,q) * O_{pq}
            bin_coeff = binom(z0, p) * binom(z0, q)
            # O_{pq}
            O = 0.0
            for kx, wx in coeff_x[(a,b)].items():
                for ky, wy in coeff_y[(c,d)].items():
                    # index in grid: x = kx * Jz, y = ky * Jz
                    ix = kx + z0  # because x_vals[0] = -z0*Jz
                    iy = ky + z0
                    if 0 <= ix < len(x_vals) and 0 <= iy < len(y_vals):
                        O += wx * wy * F_grid[ix, iy]
            C[k] += bin_coeff * O

    return C

# ========== Tricritical point finder (bimodal w=0) ==========
def compute_tricritical_bimodal(z0, rx, ry):
    Jx = rx * Jz
    Jy = ry * Jz
    w = 0.0

    def eqs(vars):
        H0, T = vars
        if T <= 0 or H0 <= 0:
            return [1e6, 1e6]
        C = compute_Ck(z0, w, H0, T, Jx, Jy, max_k=3)
        C1 = C[1]
        C3 = C[3]
        return [C1 - 1.0, C3]

    # initial guess: scaled from isotropic reference
    H0_guess = 2.274 * (rx / 1.0) * (1.0 / ry)  # rough
    T_guess = 2.748 * (rx / 1.0) * (1.0 / ry)  # rough
    # limit to positive
    H0_guess = max(H0_guess, 0.1)
    T_guess = max(T_guess, 0.1)

    sol = fsolve(eqs, [H0_guess, T_guess], maxfev=2000, xtol=1e-12)
    H0_sol, T_sol = sol
    # verify that C3 < 0 (should be close to 0, but we are at tricritical where C3=0, okay)
    return H0_sol, T_sol

# ========== w* finder ==========
def compute_w_star(z0, rx, ry):
    Jx = rx * Jz
    Jy = ry * Jz
    T_min = 1e-6  # approximate zero temperature

    def has_zero_T_solution(w):
        # Check if there exists H0 such that C1=1 at T_min
        # Solve for H0: C1(H0, T_min) - 1 = 0
        def f(H0):
            C = compute_Ck(z0, w, H0, T_min, Jx, Jy, max_k=1)
            return C[1] - 1.0

        # First check at H0=0: C1(0) at T_min? Typically C1 is less than 1?
        # We'll scan a range
        H0_vals = np.linspace(0.1, 10.0, 100)
        signs = []
        for H0 in H0_vals:
            val = f(H0)
            signs.append(val)
        # Look for sign change
        for i in range(len(signs)-1):
            if signs[i] * signs[i+1] <= 0:
                return True
        return False

    # Binary search for maximum w where solution exists
    lo = 0.0
    hi = 1.0
    for _ in range(30):
        mid = (lo + hi) / 2
        if has_zero_T_solution(mid):
            lo = mid
        else:
            hi = mid
    return lo
