#!/usr/bin/env python3
import sys
import csv
import math

def debye_d(x):
    """Debye integral D(x) = (3/x^3) integral_0^x t^3/(e^t-1) dt."""
    if x <= 0:
        return 1.0
    if x > 20:
        # asymptotic for large x
        pi4_5 = math.pi**4 / 5.0
        return pi4_5 / (x**3)
    # series expansion (accurate for small to moderate x)
    term = 1.0
    d = term
    n = 1
    # known expansion coefficients: D(x) = 1 - 3x/8 + x^2/20 - x^4/1680 + x^6/60480 - ...
    # General term: a_n = (-1)^n * 3 * B_{2n} / ((2n)! (2n+3))? Using explicit terms for up to good accuracy.
    # We'll compute using a few terms.
    x2 = x * x
    x4 = x2 * x2
    x6 = x4 * x2
    x8 = x6 * x2
    term1 = 3.0 * x / 8.0
    term2 = x2 / 20.0
    term3 = x4 / 1680.0
    term4 = x6 / 60480.0
    term5 = x8 / 2395008.0
    d = 1.0 - term1 + term2 - term3 + term4 - term5
    # clamp between 0 and 1
    if d < 0.0:
        d = 0.0
    elif d > 1.0:
        d = 1.0
    return d

def heat_capacity_cv(theta, T):
    """Molar heat capacity at constant volume (J/molK) for Debye model, n_atoms=3."""
    if T <= 0:
        return 0.0
    x = theta / T
    D = debye_d(x)
    R = 8.314462618
    n = 3  # atoms per formula unit
    factor = 3.0 * n * R
    # C_V = 3 n R [4 D(x) - 3 x/(exp(x)-1)]
    exp_term = math.exp(x)
    return factor * (4.0 * D - 3.0 * x / (exp_term - 1.0))

def main():
    if len(sys.argv) != 2:
        print("Usage: generate_csv.py <output_file>")
        sys.exit(1)
    outpath = sys.argv[1]

    compounds = [
        ("RuMnTe", 124.485, 4.89),  # static B0, alpha0
        ("CoMnTe", 118.869, 5.71)
    ]
    # Anchor data from Table 3 (T, P) -> (Theta, gamma)
    anchor = {
        "RuMnTe": {
            (300, 0): (363.91, 2.79),
            (300, 15): (461.66, 2.14),
            (300, 30): (525.79, 1.82),
            (300, 45): (574.97, 1.63),
            (600, 0): (347.22, 2.93),
            (600, 15): (454.15, 2.18),
            (600, 30): (520.93, 1.84),
            (600, 45): (571.43, 1.64),
            (900, 0): (326.05, 3.12),
            (900, 15): (445.82, 2.22),
            (900, 30): (515.80, 1.87),
            (900, 45): (567.68, 1.65),
            (1200, 0): (297.80, 3.39),
            (1200, 15): (436.65, 2.28),
            (1200, 30): (510.09, 1.89),
            (1200, 45): (563.78, 1.67)
        },
        "CoMnTe": {
            (300, 0): (365.83, 2.71),
            (300, 15): (477.93, 2.41),
            (300, 30): (558.28, 2.20),
            (300, 45): (622.18, 2.04),
            (600, 0): (347.66, 2.76),
            (600, 15): (466.32, 2.44),
            (600, 30): (549.94, 2.22),
            (600, 45): (615.63, 2.06),
            (900, 0): (327.58, 2.80),
            (900, 15): (453.80, 2.48),
            (900, 30): (540.85, 2.24),
            (900, 45): (608.51, 2.08),
            (1200, 0): (305.63, 2.86),
            (1200, 15): (440.27, 2.51),
            (1200, 30): (531.38, 2.27),
            (1200, 45): (601.06, 2.09)
        }
    }

    Ts = list(range(0, 1300, 100))  # 0..1200
    Ps = list(range(0, 46, 5))      # 0..45

    rows = []
    for compound, B0, alpha0 in compounds:
        # Build linear models per P for Theta and gamma from anchor points
        # For each P in [0,15,30,45], collect (T, theta) and (T, gamma) from anchor
        anchor_p = {0: [], 15: [], 30: [], 45: []}
        for (T, P), (th, ga) in anchor[compound].items():
            anchor_p[P].append((T, th, ga))
        # compute linear fit for each P
        theta_fits = {}
        gamma_fits = {}
        for P in [0, 15, 30, 45]:
            pts = anchor_p[P]
            N = len(pts)
            sum_t = 0.0
            sum_t2 = 0.0
            sum_th = 0.0
            sum_ga = 0.0
            sum_t_th = 0.0
            sum_t_ga = 0.0
            for T, th, ga in pts:
                sum_t += T
                sum_t2 += T * T
                sum_th += th
                sum_ga += ga
                sum_t_th += T * th
                sum_t_ga += T * ga
            denom = N * sum_t2 - sum_t * sum_t
            if abs(denom) < 1e-6:
                # fallback
                theta_slope = 0.0
                theta_intercept = sum_th / N
                gamma_slope = 0.0
                gamma_intercept = sum_ga / N
            else:
                theta_slope = (N * sum_t_th - sum_t * sum_th) / denom
                theta_intercept = (sum_th - theta_slope * sum_t) / N
                gamma_slope = (N * sum_t_ga - sum_t * sum_ga) / denom
                gamma_intercept = (sum_ga - gamma_slope * sum_t) / N
            theta_fits[P] = (theta_intercept, theta_slope)
            gamma_fits[P] = (gamma_intercept, gamma_slope)

        # For P not exactly 0,15,30,45 we can interpolate linearly in P from the fits.
        # We'll use fits at P=0,15,30,45 and linearly interpolate the coefficients.
        def get_theta(T, P):
            if P <= 0:
                inter, slope = theta_fits[0]
            elif P >= 45:
                inter, slope = theta_fits[45]
            else:
                # find bracketing Ps
                ps_sorted = [0, 15, 30, 45]
                for i in range(1, len(ps_sorted)):
                    if P <= ps_sorted[i]:
                        p_left = ps_sorted[i-1]
                        p_right = ps_sorted[i]
                        frac = (P - p_left) / (p_right - p_left)
                        inter_left, slope_left = theta_fits[p_left]
                        inter_right, slope_right = theta_fits[p_right]
                        inter = inter_left + (inter_right - inter_left) * frac
                        slope = slope_left + (slope_right - slope_left) * frac
                        break
            return inter + slope * T

        def get_gamma(T, P):
            if P <= 0:
                inter, slope = gamma_fits[0]
            elif P >= 45:
                inter, slope = gamma_fits[45]
            else:
                ps_sorted = [0, 15, 30, 45]
                for i in range(1, len(ps_sorted)):
                    if P <= ps_sorted[i]:
                        p_left = ps_sorted[i-1]
                        p_right = ps_sorted[i]
                        frac = (P - p_left) / (p_right - p_left)
                        inter_left, slope_left = gamma_fits[p_left]
                        inter_right, slope_right = gamma_fits[p_right]
                        inter = inter_left + (inter_right - inter_left) * frac
                        slope = slope_left + (slope_right - slope_left) * frac
                        break
            return inter + slope * T

        # Bulk modulus model: B_T(T,P) = B0 + dP*P - dT*T
        dP = 2.0   # GPa / GPa
        dT = 0.01  # GPa / K
        def get_BT(T, P):
            return B0 + dP * P - dT * T

        # Thermal expansion coefficient model: alpha(T,P) = alpha0 * f_T(T) * f_P(P)
        # alpha0 given in 10^-5 K^-1 units
        def get_alpha(T, P, alpha0):
            if T <= 0:
                return 0.0
            if T <= 300:
                fT = math.sqrt(T / 300.0)
            else:
                fT = 1.0 + (T - 300.0) / 900.0
            fP = 1.0 / (1.0 + 0.015 * P)
            return alpha0 * fT * fP

        for T in Ts:
            for P in Ps:
                theta = get_theta(T, P)
                gamma = get_gamma(T, P)
                B_T = get_BT(T, P)
                alpha_val = get_alpha(T, P, alpha0)  # units of 1e-5 K^-1
                C_V = heat_capacity_cv(theta, T)      # J/(mol K)
                # C_P = C_V * (1 + alpha * gamma * T), alpha in K^-1 = alpha_val * 1e-5
                alpha_true = alpha_val * 1e-5
                if T <= 0:
                    C_P = 0.0
                else:
                    C_P = C_V * (1.0 + alpha_true * gamma * T)
                rows.append([compound, T, P, round(B_T, 4), round(C_V, 4), round(C_P, 4),
                             round(theta, 4), round(gamma, 4), round(alpha_val, 4)])

    # Write CSV
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['compound', 'T_K', 'P_GPa', 'B_T_GPa', 'C_V_JmolK', 'C_P_JmolK',
                         'Theta_K', 'gamma', 'alpha_1e5_perK'])
        writer.writerows(rows)

if __name__ == '__main__':
    main()