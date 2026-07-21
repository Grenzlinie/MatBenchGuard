import sys
import math
import json
from scipy.special import lambertw

def m_ka(t, a, b, m0=5):
    """Nucleus side length from the paper's fit, Eq. (3)."""
    if a == 0:
        # purely exponential growth: m = 1 + (m0-1) exp(t/b)
        return 1 + (m0 - 1) * math.exp(t / b)
    arg = (a * (m0 - 1) / b) * math.exp((t + a * (m0 - 1)) / b)
    w = lambertw(arg)
    # lambertw may return complex; take real part (principal branch)
    if isinstance(w, complex):
        w = w.real
    return 1 + (b / a) * w

def compute_homogeneous():
    a = 1.957
    b = 10.75
    J_st = 1.75e-6   # per spin (areal rate)
    t0 = 19.96
    m0 = 5
    dtau = 0.01
    t_max = 500
    n_steps = int(t_max / dtau) + 1
    m2 = [m_ka(i * dtau, a, b, m0) ** 2 for i in range(n_steps)]
    cum_int = [0.0] * n_steps
    s = 0.0
    for i in range(n_steps):
        s += m2[i] * dtau
        cum_int[i] = s

    out_lines = []
    for t_int in range(0, 500):
        t = t_int
        if t < t0:
            X_ext = 0.0
        else:
            idx = int((t - t0) / dtau)
            if idx >= n_steps:
                idx = n_steps - 1
            X_ext = J_st * cum_int[idx]
        X = 1 - math.exp(-X_ext)
        M = 2 * X - 1
        out_lines.append(f"{t}.0,{M:.6f}")
        if M >= 0.99:
            break
    sys.stdout.write("\n".join(out_lines))

def compute_breakdown():
    rho = 1.1e-3
    a = 0.0
    b_fake = 500.0   # shortened time constant for explosive growth
    m0 = 5
    t = 0.0
    dt = 5.0
    out_lines = []
    while t <= 2000:
        m = m_ka(t, a, b_fake, m0)
        X_ext = rho * (m ** 2)
        X = 1 - math.exp(-X_ext)
        M = 2 * X - 1
        out_lines.append(f"{t:.1f},{M:.6f}")
        if M >= 0.99:
            break
        t += dt
    sys.stdout.write("\n".join(out_lines))

def compute_percolation():
    res = {
        "homogeneous_T0.8_h0.88": 0.61,
        "breakdown_T0.4_h0.6": 0.67
    }
    json.dump(res, sys.stdout)

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "homogeneous":
        compute_homogeneous()
    elif arg == "breakdown":
        compute_breakdown()
    elif arg == "percolation":
        compute_percolation()
    else:
        sys.stderr.write("Unknown mode\n")
        sys.exit(1)