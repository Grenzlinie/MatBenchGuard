import math, csv, os

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)

def A_func(Delta, D, t):
    """A(alpha) from Eq. (20) with Handrich-Kaneyoshi distribution."""
    denom_plus = 5*t + 1 + Delta + D
    denom_minus = 5*t + 1 + Delta - D
    term_plus = (1 + Delta + D) / denom_plus
    term_minus = (1 + Delta - D) / denom_minus
    return 0.5 * (term_plus + term_minus)

def a_func(t):
    """Transfer function a from the bulk recursion, Eq. (18).
    The formula a = -3/2 + (5/2)t - 1/2 sqrt(5(t-1)(t-1/5)) is extended to
yield a real, continuous, |a|<=1 function for all t by using the physically
correct root of the quadratic a^2 - (5t-3)a + 1 = 0."""
    d = (5*t - 3)**2 - 4
    if t <= 0.2:
        # take the root with |a| < 1 (the plus sign when 5t-3 < 0)
        a = 0.5 * ((5*t - 3) + math.sqrt(d))
    elif t < 1.0:
        # discriminant < 0 -> complex roots with real part (5t-3)/2
        a = (5*t - 3) / 2
    else:
        # t >= 1, discriminant >= 0, take the root with |a| < 1 (minus sign)
        a = 0.5 * ((5*t - 3) - math.sqrt(d))
    return a

def secular_residual(t, Delta_S, D_S, Delta_1, D_1):
    """Value of the secular equation (19) at reduced temperature t."""
    A_S = A_func(Delta_S, D_S, t)
    A_1 = A_func(Delta_1, D_1, t)
    a = a_func(t)
    return (4*A_S - 1) * ((4 + a) / (5*t + 1) - 1) - A_1**2

def solve_t(Delta_S, D_S, Delta_1, D_1, t_min=0.001, t_max=10.0, tol=1e-12):
    """Find the root t of the secular equation by bisection."""
    f_min = secular_residual(t_min, Delta_S, D_S, Delta_1, D_1)
    f_max = secular_residual(t_max, Delta_S, D_S, Delta_1, D_1)
    if f_min * f_max > 0:
        return float('nan')
    for _ in range(200):
        t_mid = (t_min + t_max) / 2
        f_mid = secular_residual(t_mid, Delta_S, D_S, Delta_1, D_1)
        if abs(f_mid) < tol:
            return t_mid
        if f_min * f_mid < 0:
            t_max = t_mid
        else:
            t_min = t_mid
            f_min = f_mid
    return (t_min + t_max) / 2

# ---------------------------------------------------------------------------
# 1. phase_diagram.csv
# ---------------------------------------------------------------------------
with open(os.path.join(OUTDIR, "phase_diagram.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Delta_S", "t_c", "param_label"])
    for i in range(-10, 51):
        Delta_S = i * 0.1
        t_pure = solve_t(Delta_S, 0.0, 0.0, 0.0)
        writer.writerow([Delta_S, t_pure, "pure"])
        t_amor = solve_t(Delta_S, 2.0, 0.0, 0.0)
        writer.writerow([Delta_S, t_amor, "amorphized"])

# ---------------------------------------------------------------------------
# 2. critical_values.csv
# ---------------------------------------------------------------------------
with open(os.path.join(OUTDIR, "critical_values.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["D_S", "Delta_c_S"])
    for j in range(0, 11):
        D_S = j * 0.5
        # For t=1 we need A_S = 5/24 (derived analytically).
        # Solve A_S(Delta_S, D_S, t=1) = 5/24
        lo, hi = -0.99, 20.0
        f_lo = A_func(lo, D_S, 1.0) - 5.0/24.0
        f_hi = A_func(hi, D_S, 1.0) - 5.0/24.0
        if f_lo * f_hi > 0:
            Delta_c = float('nan')
        else:
            for _ in range(200):
                mid = (lo + hi) / 2
                f_mid = A_func(mid, D_S, 1.0) - 5.0/24.0
                if abs(f_mid) < 1e-12:
                    Delta_c = mid
                    break
                if f_lo * f_mid < 0:
                    hi = mid
                else:
                    lo = mid
                    f_lo = f_mid
            else:
                Delta_c = mid
        writer.writerow([D_S, Delta_c])

# ---------------------------------------------------------------------------
# 3. reentrant_curve.csv
# ---------------------------------------------------------------------------
with open(os.path.join(OUTDIR, "reentrant_curve.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["delta_S", "t_c"])
    Delta_S = 7.0
    Delta_1 = -0.9
    D_1 = 0.0
    for k in range(0, 21):
        delta_S = k * 0.05
        D_S = delta_S * (1 + Delta_S)
        t_c = solve_t(Delta_S, D_S, Delta_1, D_1)
        writer.writerow([delta_S, t_c])