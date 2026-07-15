#!/usr/bin/env python3
"""Oracle helper: compute COP curves and strain reduction factors for the
ZnBVI-rich CdxZn1-xOyBVI1-y thermodynamic clustering model.
"""
import sys
import csv
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint

# Gas constant in J/(mol·K)
R = 8.314

# Matrix-specific parameters -------------------------------------------------
# (composition y, x_ratio, Δu_B (kJ/mol), deformation energies: u_Cd, u_O,
#  u_104Cd, u_4O10Cd (all kJ/mol))
PARAMS = {
    "ZnS": {
        "y": 5e-4,
        "x_ratio": 2.5,
        "delta_u_B": -16.0,      # kJ/mol
        "u_Cd": 24.983,
        "u_O": 58.911,
        "u_104Cd": 58.6102,
        "u_4O10Cd": 57.243,
    },
    "ZnSe": {
        "y": 3e-4,
        "x_ratio": 2.5,
        "delta_u_B": -25.0,
        "u_Cd": 6.225,
        "u_O": 77.721,
        "u_104Cd": 97.604,
        "u_4O10Cd": 101.656,
    },
    "ZnTe": {
        "y": 2e-3,
        "x_ratio": 2.5,
        "delta_u_B": +37.0,
        "u_Cd": 6.063,
        "u_O": 162.03,
        "u_104Cd": 137.02,
        "u_4O10Cd": 389.95,
    },
}


def entropy_expr(alpha, beta, x, y):
    """Return the dimensionless expression S_expr = ( -T s ) / (R T).
    From Eq. (4) of the paper, with the same notation.
    """
    # Helper: safe x*log(x/y) returning 0 when x==0
    def safe_xlogx_over_y(v, w):
        # v * ln(v / w) = 0 when v==0
        out = np.where(v > 0, v * np.log(np.maximum(v, 1e-300) / np.maximum(w, 1e-300)), 0.0)
        return out

    # Terms that appear in Eq. (4)
    # 1. (1-α)y ln( (1-α)y / (1-αy) )
    term1 = safe_xlogx_over_y((1 - alpha) * y, 1 - alpha * y)

    # 2. (1-y) ln( (1-y) / (1-αy) )
    term2 = safe_xlogx_over_y(1 - y, 1 - alpha * y)

    # 3. [x - (10/4)α y - 4β y] ln( [x - (10/4)α y - 4β y] / [1 - (10/4)α y - 4β y] )
    c = x - 2.5 * alpha * y - 4 * beta * y    # note 10/4 = 2.5
    d = 1 - 2.5 * alpha * y - 4 * beta * y
    term3 = safe_xlogx_over_y(c, d)

    # 4. (1-x) ln( (1-x) / d )
    term4 = safe_xlogx_over_y(1 - x, d)

    # 5. (1-α-β)y ln( (1-α-β) / (1-α) )
    e = (1 - alpha - beta) * y
    f = 1 - alpha
    term5 = safe_xlogx_over_y(e, f)

    # 6. β y ln( β / (1-α) )
    term6 = safe_xlogx_over_y(beta * y, 1 - alpha)

    # 7. (1/10) α y ln( 27 α y / 20 )
    term7 = safe_xlogx_over_y(0.1 * alpha * y, 20.0 / 27.0)  # 27 α y / 20 -> invert? Actually ln(27 α y /20) = - ln(20/(27 α y)). Use safe_xlogx_over_y directly: (0.1 α y) * ln(27 α y /20). Write as safe_xlogx_over_y(0.1*α*y, 20/(27*α*y)? That's messy. Simpler: compute directly.
    # term7 = 0.1 * alpha * y * np.log(np.maximum(27 * alpha * y / 20, 1e-300))
    # But safe: v = 0.1*α*y, and the ratio inside log is (27 α y /20). Since we want v * ln(v / w) form, we can set w = (20/27)* (v / (α*y))? Not needed; just compute directly.
    term7 = np.where(alpha * y > 0, 0.1 * alpha * y * np.log(np.maximum(27 * alpha * y / 20.0, 1e-300)), 0.0)

    # 8. (2/27) ln( (20 - 27 α y) / 20 )
    term8 = safe_xlogx_over_y(2.0/27.0, 20.0 / (20 - 27 * alpha * y + 1e-12))  # tricky
    # term8 = (2/27) * ln( (20 - 27 α y)/20 ). We can use safe_xlogx_over_y with v = 2/27? Actually it's (2/27) * ln(...). That's not v*ln(v/w) form. Compute directly:
    term8 = np.where(27 * alpha * y < 20, (2.0/27.0) * np.log(np.maximum((20 - 27 * alpha * y)/20.0, 1e-300)), 0.0)

    S = term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8
    return S


def free_energy(ab, T, x, y, delta_u_B, u_Cd, u_O, u_104Cd, u_4O10Cd):
    """Free energy f(α,β) in kJ/mol."""
    alpha, beta = ab[0], ab[1]

    # Bond energy (α,β-dependent part)
    bond = delta_u_B * (alpha + beta) * (1 - x) * y   # kJ/mol

    # Internal strain energy Eq. (3)
    uIS = (
        (1 - alpha - beta) * y * u_O
        + (x - 2.5 * alpha * y - 4 * beta * y) * u_Cd
        + 0.25 * alpha * y * u_4O10Cd
        + beta * y * u_104Cd
    )

    # Entropy term: -T s = R T * S_expr (J/mol) -> kJ/mol
    s_expr = entropy_expr(alpha, beta, x, y)
    entropy_kJ = R * T * s_expr / 1000.0

    f = bond + uIS + entropy_kJ
    return f


def compute_cop_curve(matrix, outpath):
    """Write T, alpha, beta CSV for the given matrix."""
    p = PARAMS[matrix]
    y = p["y"]
    x = p["x_ratio"] * y
    delta_u_B = p["delta_u_B"]
    u_Cd = p["u_Cd"]
    u_O = p["u_O"]
    u_104Cd = p["u_104Cd"]
    u_4O10Cd = p["u_4O10Cd"]

    T_range = np.arange(273, 1074, 10)  # 273,283,...1073 K
    results = []

    # Constraints for the optimizer
    # 0 <= α,β <= 1 and α+β <= 1 and x - 2.5 α y - 4 β y >= 0
    bounds = Bounds([0, 0], [1, 1])
    # Linear constraints: A @ [α,β] <= ub
    A = np.array([[1, 1],          # α+β
                  [2.5 * y, 4 * y]])  # 2.5 y α + 4 y β
    ub = np.array([1, x])          # α+β <= 1,  2.5 y α + 4 y β <= x
    linear_constraint = LinearConstraint(A, -np.inf, ub)

    for T in T_range:
        # Use several starting points to avoid local minima
        init_guesses = [
            (0.01, 0.01),
            (0.5, 0.1),
            (0.9, 0.05),
            (0.95, 0.02),
            (0.99, 0.0),
        ]
        best_ab = None
        best_f = np.inf
        for guess in init_guesses:
            res = minimize(
                fun=lambda ab: free_energy(ab, T, x, y, delta_u_B,
                                           u_Cd, u_O, u_104Cd, u_4O10Cd),
                x0=guess,
                bounds=bounds,
                constraints=linear_constraint,
                method='SLSQP',
                options={'maxiter': 200, 'ftol': 1e-12},
            )
            if res.success and res.fun < best_f:
                best_f = res.fun
                best_ab = res.x
        # If the optimizer failed completely (should not happen), fall back to the best initial guess
        if best_ab is None:
            # brute-force scan tiny grid
            best_ab = (0.5, 0.1)
            best_f = free_energy(best_ab, T, x, y, delta_u_B,
                                 u_Cd, u_O, u_104Cd, u_4O10Cd)
            for ai in np.linspace(0, 1, 21):
                for bi in np.linspace(0, 1 - ai, 21):
                    fv = free_energy([ai, bi], T, x, y, delta_u_B,
                                     u_Cd, u_O, u_104Cd, u_4O10Cd)
                    if fv < best_f:
                        best_f = fv
                        best_ab = [ai, bi]
        # Round to reasonable precision
        alpha_val = round(float(best_ab[0]), 6)
        beta_val = round(float(best_ab[1]), 6)
        results.append((T, alpha_val, beta_val))

    # Write CSV
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["T (K)", "alpha", "beta"])
        writer.writerows(results)
    print(f"Wrote {len(results)} rows to {outpath}")


def compute_strain_reduction(outpath):
    """Write strain reduction factors for all three matrices."""
    rows = []
    for matrix, p in PARAMS.items():
        y = p["y"]
        x = p["x_ratio"] * y
        u_Cd = p["u_Cd"]
        u_O = p["u_O"]
        u_104Cd = p["u_104Cd"]
        u_4O10Cd = p["u_4O10Cd"]

        # internal strain energy: Eq. (3)
        def uIS(alpha, beta):
            return (
                (1 - alpha - beta) * y * u_O
                + (x - 2.5 * alpha * y - 4 * beta * y) * u_Cd
                + 0.25 * alpha * y * u_4O10Cd
                + beta * y * u_104Cd
            )

        # Fully isolated: α=β=0
        iso = uIS(0.0, 0.0)
        # Fully clustered (all O in 4O10Cd): α=1, β=0
        # Check: with x=2.5y, the isolated Cd term becomes (2.5y - 2.5y - 0)*u_Cd = 0
        clus = uIS(1.0, 0.0)

        factor = iso / clus if clus != 0 else 0.0
        rows.append((matrix, round(factor, 6)))

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["matrix", "reduction_factor"])
        writer.writerows(rows)
    print(f"Wrote strain reduction factors to {outpath}")


if __name__ == "__main__":
    if len(sys.argv) != 4 and not (len(sys.argv) == 3 and sys.argv[1] == "strain_reduction"):
        print("Usage: compute.py cop <Matrix> <outpath>  OR  compute.py strain_reduction <outpath>")
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "cop":
        matrix = sys.argv[2]
        outpath = sys.argv[3]
        compute_cop_curve(matrix, outpath)
    elif mode == "strain_reduction":
        outpath = sys.argv[2]
        compute_strain_reduction(outpath)
    else:
        print("Unknown mode")
        sys.exit(1)
