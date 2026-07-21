import json
import csv
import math
import sys

def cubic_root(beta):
    """Solve the cubic equation for w0 using bisection."""
    c3 = 1.0 - 9.0 * beta * beta
    c2 = 54.0 * beta * (1.0 + beta)
    c1 = -4.0 * (1.0 + 21.0 * beta + 36.0 * beta * beta)
    c0 = 24.0 * beta * (2.0 + 3.0 * beta)

    def f(w):
        return ((c3 * w + c2) * w + c1) * w + c0

    if beta < 1.0 / 3.0:
        lo, hi = 1.0, 2.0
    else:
        lo, hi = 0.0, 1.0

    # ensure valid bracket
    f_lo = f(lo)
    f_hi = f(hi)
    # if signs are same, extend bracket (should not happen for our β range)
    if f_lo * f_hi > 0.0:
        if beta < 1.0/3.0:
            hi = 5.0
            f_hi = f(hi)
        else:
            lo = -1.0
            f_lo = f(lo)

    for _ in range(200):
        mid = (lo + hi) / 2.0
        f_mid = f(mid)
        if f_mid == 0.0 or (hi - lo) < 1e-12:
            return mid
        if f_lo * f_mid < 0.0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def compute_w0_values():
    """Return dict with w0 for β=0.1 and β=1.0."""
    vals = {}
    for beta in [0.1, 1.0]:
        w0 = cubic_root(beta)
        key = f"beta_{beta}"
        vals[key] = round(w0, 5)
    return vals


def compute_free_energy():
    """Return list of (beta, delta_F) for β=0.01..0.20 step 0.01."""
    L = 35.0
    rows = []
    # step 0.01 to 0.20 inclusive
    betas = [round(0.01 * i, 2) for i in range(1, 21)]
    for beta in betas:
        w0 = cubic_root(beta)
        # compute matching parameters
        # s1, r1
        s1 = math.sqrt((1.0 + 15.0 * beta) / (4.0 * beta * (2.0 + 3.0 * beta)))
        r1 = 2.0 / (3.0 * s1)
        # w2
        w2 = (w0 / 4.0) * ( (1.0 + 3.0 * beta) / 6.0 * w0 * w0 + beta * w0 - 2.0 / 3.0 )
        # s2 (valid for β<1/3, which holds here)
        if beta < 1.0 / 3.0:
            denom = 2.0 * beta * (2.0 + 3.0 * beta) * (w0 - 1.0)
            s2 = math.sqrt((1.0 - 3.0 * beta) / denom)
        else:
            s2 = s1  # not used

        # asymptotic coefficients
        A = (1.0 + 15.0 * beta) / (12.0 * beta * (2.0 + 3.0 * beta))
        B = (1.0 - 3.0 * beta) / (4.0 * beta * (2.0 + 3.0 * beta))

        # piecewise definitions
        def R(s):
            if s <= s1:
                return r1 * s
            else:
                return 1.0 - A / (s * s)

        def S(s):
            if s <= s2:
                return w0 + w2 * s * s
            else:
                return 1.0 + B / (s * s)

        def R_prime(s):
            if s <= s1:
                return r1
            else:
                return 2.0 * A / (s * s * s)

        def S_prime(s):
            if s <= s2:
                return 2.0 * w2 * s
            else:
                return -2.0 * B / (s * s * s)

        # integrand of the reduced free energy: G(s) such that
        # F(s) = a η0^2 * G(s), with G(s) = (9/8) * ( ... )
        def integrand(s):
            if s == 0.0:
                # handle limit analytically: R~r1*s, S~w0, S'~0, etc.
                Rv = 0.0
                Sv = w0
                Rp = r1
                Sp = 0.0
                # term2 at s=0: limit 3 r1^2
                term1 = Sp * Sp + 3.0 * Rp * Rp
                term2 = 3.0 * r1 * r1
                term3 = -2.0 / 3.0 * Sv * Sv - 2.0 * Rv * Rv
                term4 = -6.0 * beta * Sv * (Rv * Rv - 1.0 / 9.0 * Sv * Sv)
                term5 = (1.0 / 12.0) * (1.0 + 3.0 * beta) * ((Sv * Sv + 3.0 * Rv * Rv) ** 2)
                return (9.0 / 8.0) * (term1 + term2 + term3 + term4 + term5)
            else:
                Rv = R(s)
                Sv = S(s)
                Rp = R_prime(s)
                Sp = S_prime(s)
                term1 = Sp * Sp + 3.0 * Rp * Rp
                term2 = (3.0 / (s * s)) * Rv * Rv
                term3 = -2.0 / 3.0 * Sv * Sv - 2.0 * Rv * Rv
                term4 = -6.0 * beta * Sv * (Rv * Rv - 1.0 / 9.0 * Sv * Sv)
                term5 = (1.0 / 12.0) * (1.0 + 3.0 * beta) * ((Sv * Sv + 3.0 * Rv * Rv) ** 2)
                return (9.0 / 8.0) * (term1 + term2 + term3 + term4 + term5)

        # Numerically integrate ∫₀ᴸ s * G(s) ds using Simpson's rule
        N = 10000  # number of intervals (even)
        ds = L / N
        sum_s = 0.0
        for i in range(N + 1):
            s = i * ds
            if s == 0.0:
                s = 1e-12  # tiny offset for safety; handled inside integrand
            g = integrand(s)
            coeff = 2.0
            if i == 0 or i == N:
                coeff = 1.0
            else:
                coeff = 4.0 if i % 2 == 1 else 2.0
            sum_s += coeff * s * g
        integral_Fb = ds / 3.0 * sum_s

        # smooth free energy per unit length in dimensionless units
        F_b_unit = (8.0 / 9.0) * integral_Fb

        # singular core free energy (dimensionless)
        R_c = 3.0 / (2.0 * math.sqrt(1.0 + beta))
        F_c_unit = (8.0 / 9.0) * (
            -0.75 * (1.0 + beta) * (L * L - R_c * R_c)
            + (27.0 / 8.0) * math.log(L / R_c)
        )

        delta_F = F_b_unit - F_c_unit
        rows.append((beta, delta_F))
    return rows


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("w0", "all"):
        w0_vals = compute_w0_values()
        with open("/app/outputs/w0_values.json", "w") as f:
            json.dump(w0_vals, f, indent=2)
    if mode in ("energy", "all"):
        fe_data = compute_free_energy()
        with open("/app/outputs/free_energy_difference.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["beta", "delta_F"])
            for beta, df in fe_data:
                writer.writerow([beta, df])

if __name__ == "__main__":
    main()