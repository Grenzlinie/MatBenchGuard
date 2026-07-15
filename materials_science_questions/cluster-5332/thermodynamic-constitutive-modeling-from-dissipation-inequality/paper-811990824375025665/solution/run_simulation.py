import json, math

# Material constants
E = 200.0
E3 = 50.0
M = 20.0
k1 = 0.5
k2 = 1.0
# Equilibrium piecewise parameters
epsM = 0.02
eps_m = 0.05
E1 = 10.0
E2 = 20.0
sigmaM = E3 * epsM          # 1.0
sigma_m = sigmaM - E2 * (eps_m - epsM)  # 0.4
# Wave speed – will be determined per simulation to align grid with N=200
N = 200
L = 1.0

def sigmaR(eps):
    if eps <= epsM:
        return E3 * eps
    elif eps < eps_m:
        return sigmaM - E2 * (eps - epsM)
    else:
        return sigma_m + E1 * (eps - eps_m)

def eps_from_r(r):
    # Solve r = sigmaR(eps) - E*eps
    # Segment 1: eps<=epsM, sigmaR=E3 eps -> r = (E3-E)eps, eps = r/(E3-E) but note r negative
    # Segment 2: epsM<eps<eps_m, sigmaR = 1.4 -20*eps, so r = 1.4 -220*eps, eps = (1.4 - r)/220
    # Segment 3: eps>=eps_m, sigmaR = 10*eps -0.1, r = (10-200)eps -0.1 = -190*eps -0.1, eps = (-0.1 - r)/190
    EPS_R = (E3 - E)  # -150
    if r >= -150 * epsM:  # r >= -3.0
        eps = -r / 150.0
    else:
        r_switch = -150 * epsM  # -3.0
        # check segment 2
        r_switch2 = 1.4 - 220*eps_m  # 1.4 - 11 = -9.6
        if r > r_switch2:
            eps = (1.4 - r) / 220.0
        else:
            eps = (-0.1 - r) / 190.0
    return eps

def phi(r):
    # phi(r) = integral_0^{eps(r)} sigmaR(s) ds - 0.5*sigmaR(eps(r))**2 / E
    eps = eps_from_r(r)
    # integral
    if eps <= epsM:
        integral = 0.5 * E3 * eps**2
    elif eps < eps_m:
        integral = 0.5 * E3 * epsM**2 + (eps - epsM) * sigmaM - 0.5 * E2 * (eps - epsM)**2
    else:
        integral = 0.5 * E3 * epsM**2 + (eps_m - epsM) * sigmaM - 0.5 * E2 * (eps_m - epsM)**2 + (eps - eps_m) * sigma_m + 0.5 * E1 * (eps - eps_m)**2
    sr = sigmaR(eps)
    val = integral - 0.5 * sr**2 / E
    return val

def G_val(p, q, r):
    # G = g = -k (sigma - sigmaR(eps)), with k=1.0, sigma = (p+q)/2
    sigma = 0.5 * (p + q)
    eps = (sigma - r) / E
    return -1.0 * (sigma - sigmaR(eps))

def init_state(dx):
    # dx = L/N, uniform spacing
    x_vals = [i * dx for i in range(N+1)]
    p = [0.0]*(N+1)
    q = [0.0]*(N+1)
    r = [0.0]*(N+1)
    A = 0.02
    sigma_param = 0.05
    for i, x in enumerate(x_vals):
        eps0 = A * math.exp(-(x - 0.5)**2 / (2 * sigma_param**2))
        sigma0 = sigmaR(eps0)
        p[i] = sigma0
        q[i] = sigma0
        r[i] = sigma0 - E * eps0
    return p, q, r

def energy(p, q, r):
    # e = 0.5*(sum_{i=0}^{N-1} + sum_{i=1}^{N}) [ (p_i^2+q_i^2)/(4E) + phi(r_i) ]
    s = 0.0
    for i in range(N):
        s += (p[i]**2 + q[i]**2) / (4*E) + phi(r[i])
        s += (p[i+1]**2 + q[i+1]**2) / (4*E) + phi(r[i+1])
    return 0.5 * s

def run_first_scheme(h, p, q, r, steps):
    # returns energy sequence
    en = []
    en.append(energy(p, q, r))
    for step in range(steps):
        p_new = [0.0]*(N+1)
        q_new = [0.0]*(N+1)
        r_new = [0.0]*(N+1)
        # interior points 1..N-1
        for i in range(1, N):
            Gi = G_val(p[i], q[i], r[i])
            Gi1 = G_val(p[i+1], q[i+1], r[i+1])
            Gi_1 = G_val(p[i-1], q[i-1], r[i-1])
            p_new[i] = p[i+1] + h * Gi1
            q_new[i] = q[i-1] + h * Gi_1
            r_new[i] = r[i] + h * Gi
        # boundaries
        G0 = G_val(p[0], q[0], r[0]); G1 = G_val(p[1], q[1], r[1])
        p_new[0] = p[1] + h * G1
        q_new[0] = p_new[0]
        r_new[0] = r[0] + h * G0
        GN = G_val(p[N], q[N], r[N]); GN_1 = G_val(p[N-1], q[N-1], r[N-1])
        p_new[N] = q_new[N] = q[N-1] + h * GN_1
        q_new[N] = q_new[N]  # redundant
        r_new[N] = r[N] + h * GN
        p, q, r = p_new, q_new, r_new
        en.append(energy(p, q, r))
    return en

def run_second_scheme(h, p, q, r, steps):
    en = []
    en.append(energy(p, q, r))
    for step in range(steps):
        # first approximation (predictor)
        p_tilde = [0.0]*(N+1)
        q_tilde = [0.0]*(N+1)
        r_tilde = [0.0]*(N+1)
        for i in range(1, N):
            Gi = G_val(p[i], q[i], r[i])
            Gi1 = G_val(p[i+1], q[i+1], r[i+1])
            Gi_1 = G_val(p[i-1], q[i-1], r[i-1])
            p_tilde[i] = p[i+1] + h * Gi1
            q_tilde[i] = q[i-1] + h * Gi_1
            r_tilde[i] = r[i] + h * Gi
        G0 = G_val(p[0], q[0], r[0]); G1 = G_val(p[1], q[1], r[1])
        p_tilde[0] = p[1] + h * G1
        q_tilde[0] = p_tilde[0]
        r_tilde[0] = r[0] + h * G0
        GN = G_val(p[N], q[N], r[N]); GN_1 = G_val(p[N-1], q[N-1], r[N-1])
        p_tilde[N] = q_tilde[N] = q[N-1] + h * GN_1
        r_tilde[N] = r[N] + h * GN

        # compute G tilde
        G_tilde = [0.0]*(N+1)
        for i in range(N+1):
            G_tilde[i] = G_val(p_tilde[i], q_tilde[i], r_tilde[i])

        # second approximation
        p_new = [0.0]*(N+1)
        q_new = [0.0]*(N+1)
        r_new = [0.0]*(N+1)
        for i in range(1, N):
            Gi = G_val(p[i], q[i], r[i])
            Gi1 = G_val(p[i+1], q[i+1], r[i+1])
            Gi_1 = G_val(p[i-1], q[i-1], r[i-1])
            p_new[i] = p[i+1] + 0.5 * h * (Gi1 + G_tilde[i])
            q_new[i] = q[i-1] + 0.5 * h * (Gi_1 + G_tilde[i])
            r_new[i] = r[i] + 0.5 * h * (Gi + G_tilde[i])
        G0 = G_val(p[0], q[0], r[0])
        G1 = G_val(p[1], q[1], r[1])
        p_new[0] = p[1] + 0.5 * h * (G1 + G_tilde[0])
        q_new[0] = p_new[0]
        r_new[0] = r[0] + 0.5 * h * (G0 + G_tilde[0])
        GN = G_val(p[N], q[N], r[N])
        GN_1 = G_val(p[N-1], q[N-1], r[N-1])
        p_new[N] = q_new[N] = q[N-1] + 0.5 * h * (GN_1 + G_tilde[N])
        r_new[N] = r[N] + 0.5 * h * (GN + G_tilde[N])

        p, q, r = p_new, q_new, r_new
        en.append(energy(p, q, r))
    return en

def is_nonincreasing(energy_seq):
    e0 = energy_seq[0]
    for e in energy_seq[1:]:
        if e > e0 + 1e-12:
            return False
    return True

def simulate(approx, h):
    dx = L / N
    # set c = dx/h -> c = L/(N h), so rho = E / c^2
    c = dx / h
    rho = E / (c*c)
    p, q, r = init_state(dx)
    # run a few steps; t_final = 0.1 or enough to see energy behavior
    # total_steps = int(0.1 / h)  # about 0.1/0.68 ≈ 1-2 steps, too few. Need more.
    # Let's run until t=0.5 maybe
    t_final = 0.5
    steps = int(t_final / h)
    if approx == 'first':
        en = run_first_scheme(h, p, q, r, steps)
    else:
        en = run_second_scheme(h, p, q, r, steps)
    return is_nonincreasing(en)

if __name__ == "__main__":
    h_m_prime = 2.0 * (E - E3) / (k2 * (E + M))  # 300/220 = 1.363636...
    h_m_double_prime = (2.0 / k2) * (E * (E - E3)) / (E * (E + M) + M * (E - E3))
    # Run simulations
    h1 = 0.5 * h_m_prime
    h2 = 1.5 * h_m_prime
    results = {
        "bounds": {
            "h_m_prime": h_m_prime,
            "h_m_double_prime": h_m_double_prime
        },
        "simulations": [
            {"approximation": "first", "h": h1, "energy_nonincreasing": simulate('first', h1)},
            {"approximation": "first", "h": h2, "energy_nonincreasing": simulate('first', h2)},
            {"approximation": "second", "h": h1, "energy_nonincreasing": simulate('second', h1)},
            {"approximation": "second", "h": h2, "energy_nonincreasing": simulate('second', h2)}
        ],
        "ratio_check": {
            "h_m_double_prime/ h_m_prime": h_m_double_prime / h_m_prime,
            "inequality_holds": h_m_double_prime <= h_m_prime
        }
    }
    with open("/app/outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("results.json written")