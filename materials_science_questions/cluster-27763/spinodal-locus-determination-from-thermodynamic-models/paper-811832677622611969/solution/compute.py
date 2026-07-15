import sys, os, csv
import numpy as np
from scipy.optimize import fsolve, bisect, minimize_scalar

outdir = sys.argv[1] if len(sys.argv) > 1 else '/tmp'

# Parameter sets
param_sets = [
    {"name": "Λ=350, η_c=-0.05, η_cc=0.04", "Lambda": 350, "eta_c": -0.05, "eta_cc": 0.04},
    {"name": "Λ=100, η_c=-0.05, η_cc=0.04", "Lambda": 100, "eta_c": -0.05, "eta_cc": 0.04},
    {"name": "Λ=100, η_c=-0.03, η_cc=0",    "Lambda": 100, "eta_c": -0.03, "eta_cc": 0.0},
    {"name": "Λ=100, η_c=-0.01, η_cc=-0.04","Lambda": 100, "eta_c": -0.01, "eta_cc": -0.04},
]

def eps(c, eta_c, eta_cc):
    return eta_c * c + 0.5 * eta_cc * c**2

def eps_prime(c, eta_c, eta_cc):
    return eta_c + eta_cc * c

def phi(t, c, Pi, Lambda, eta_c, eta_cc):
    if c <= 0 or c >= 1:
        return np.inf
    ent = c * np.log(c) + (1-c) * np.log(1-c)
    return t * ent + 2 * c * (1-c) - 4.5 * Pi**2 + 3 * np.sqrt(Lambda) * eps(c, eta_c, eta_cc) * Pi

def dphi_dc(t, c, Pi, Lambda, eta_c, eta_cc):
    if c <= 0 or c >= 1:
        return np.inf
    ent_d = np.log(c) - np.log(1-c)
    return t * ent_d + 2 * (1 - 2*c) + 3 * np.sqrt(Lambda) * eps_prime(c, eta_c, eta_cc) * Pi

def dphi_dPi(t, c, Pi, Lambda, eta_c, eta_cc):
    return -9 * Pi + 3 * np.sqrt(Lambda) * eps(c, eta_c, eta_cc)

def omega(t, c, Pi, Lambda, eta_c, eta_cc):
    return phi(t,c,Pi, Lambda, eta_c, eta_cc) - c * dphi_dc(t,c,Pi, Lambda, eta_c, eta_cc) - Pi * dphi_dPi(t,c,Pi, Lambda, eta_c, eta_cc)

def spinodal_t(c, Pi, Lambda, eta_c, eta_cc):
    # returns t from spinodal condition Eq.22
    A = 4 - Lambda * (eta_c + eta_cc*c)**2
    B = 3 * eta_cc * np.sqrt(Lambda) * Pi
    return c * (1-c) * (A - B)

def spinodal_c_root_for_t(t, Pi, Lambda, eta_c, eta_cc):
    # find two c solutions for given t, Pi
    # use bisection
    f = lambda c: spinodal_t(c, Pi, Lambda, eta_c, eta_cc) - t
    roots = []
    # scan n points
    cs = np.linspace(0, 1, 200)
    vals = f(cs)
    for i in range(len(cs)-1):
        if np.sign(vals[i]) != np.sign(vals[i+1]):
            try:
                root = bisect(f, cs[i], cs[i+1], xtol=1e-12)
                roots.append(root)
            except:
                pass
    return sorted(roots)

def critical_point(params):
    Lambda = params['Lambda']; eta_c = params['eta_c']; eta_cc = params['eta_cc']
    if eta_cc == 0:
        t_c = 1 - Lambda * eta_c**2 / 4
        c_c = 0.5
        P_o_c = 0.0
        return t_c, c_c, P_o_c
    # solve for c such that t_sp(c,0) = t_crit(c)
    def t_sp0(c):
        return c*(1-c)*(4 - Lambda*(eta_c+eta_cc*c)**2)
    def t_crit(c):
        if c == 0.5:
            # handle singularity? limit finite
            return 0.0
        return (c*(1-c))**2 / (1-2*c) * 3 * Lambda * eta_cc * (eta_c + eta_cc*c)
    # find root of t_sp0 - t_crit = 0
    def F(c):
        return t_sp0(c) - t_crit(c)
    # find intervals where F changes sign
    # The consolute critical point is often near c ~ 0.5, search [0.1,0.5] and [0.5,0.9]
    for a,b in [(0.1,0.5-1e-6), (0.5+1e-6,0.9)]:
        try:
            fa, fb = F(a), F(b)
            if fa*fb < 0:
                c_root = bisect(F, a, b, xtol=1e-12)
                t_c = t_sp0(c_root)
                return t_c, c_root, 0.0
        except:
            continue
    raise RuntimeError("Critical point not found")

def spinodal_c_for_P(t, c, Lambda, eta_c, eta_cc):
    # compute Pi from spinodal Eq.22 given t and c
    if eta_cc == 0:
        return None
    A = 4 - Lambda * (eta_c + eta_cc*c)**2
    B = 3 * eta_cc * np.sqrt(Lambda)
    if abs(B) < 1e-15:
        return None
    return (A - t/(c*(1-c))) / B

def solve_pair_for_alpha(t, Pi_o, params, c_alpha_guess, c_sp2):
    # For alpha branch: Pi_alpha = Pi_o, solve for c_beta, Pi_beta from dphi_dc, dphi_dPi equalities
    Lambda = params['Lambda']; eta_c = params['eta_c']; eta_cc = params['eta_cc']
    def eqs2(vars, c_alpha):
        c_beta, Pi_beta = vars
        d1 = dphi_dc(t, c_alpha, Pi_o, Lambda, eta_c, eta_cc) - dphi_dc(t, c_beta, Pi_beta, Lambda, eta_c, eta_cc)
        d2 = dphi_dPi(t, c_alpha, Pi_o, Lambda, eta_c, eta_cc) - dphi_dPi(t, c_beta, Pi_beta, Lambda, eta_c, eta_cc)
        return [d1, d2]
    def omega_diff(c_alpha):
        sol = fsolve(lambda v: eqs2(v, c_alpha), [c_sp2, Pi_o], xtol=1e-12, maxfev=1000)
        c_b, Pi_b = sol
        return omega(t, c_alpha, Pi_o, Lambda, eta_c, eta_cc) - omega(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
    # find root of omega_diff in interval [1e-6, c_alpha_guess]
    try:
        c_a_root = bisect(omega_diff, 1e-6, c_alpha_guess, xtol=1e-12, maxiter=100)
    except:
        return None
    # final solve for other phase
    sol = fsolve(lambda v: eqs2(v, c_a_root), [c_sp2, Pi_o], xtol=1e-12)
    return c_a_root, Pi_o, sol[0], sol[1]

def solve_pair_for_beta(t, Pi_o, params, c_beta_guess, c_sp1):
    Lambda = params['Lambda']; eta_c = params['eta_c']; eta_cc = params['eta_cc']
    def eqs2(vars, c_beta):
        c_alpha, Pi_alpha = vars
        d1 = dphi_dc(t, c_alpha, Pi_alpha, Lambda, eta_c, eta_cc) - dphi_dc(t, c_beta, Pi_o, Lambda, eta_c, eta_cc)
        d2 = dphi_dPi(t, c_alpha, Pi_alpha, Lambda, eta_c, eta_cc) - dphi_dPi(t, c_beta, Pi_o, Lambda, eta_c, eta_cc)
        return [d1, d2]
    def omega_diff(c_beta):
        sol = fsolve(lambda v: eqs2(v, c_beta), [c_sp1, Pi_o], xtol=1e-12, maxfev=1000)
        c_a, Pi_a = sol
        return omega(t, c_a, Pi_a, Lambda, eta_c, eta_cc) - omega(t, c_beta, Pi_o, Lambda, eta_c, eta_cc)
    try:
        c_b_root = bisect(omega_diff, c_beta_guess, 1-1e-6, xtol=1e-12, maxiter=100)
    except:
        return None
    sol = fsolve(lambda v: eqs2(v, c_b_root), [c_sp1, Pi_o], xtol=1e-12)
    return sol[0], sol[1], c_b_root, Pi_o

def compute_tc_binodal_slice(Pi_o, params):
    Lambda = params['Lambda']; eta_c = params['eta_c']; eta_cc = params['eta_cc']
    # find critical t on this slice: maximum of spinodal t over c
    def neg_t(c):
        return -spinodal_t(c, Pi_o, Lambda, eta_c, eta_cc)
    res = minimize_scalar(neg_t, bounds=(0.001, 0.999), method='bounded')
    c_c_slice = res.x
    t_c_slice = -res.fun
    # generate binodal points for t from t_c_slice down to 0.05
    rows = []
    ts = np.linspace(t_c_slice - 0.005, 0.05, 50)  # adapt count
    # initial guesses
    prev_alpha = None; prev_beta = None
    # compute spinodal compositions for first t
    c_sp = spinodal_c_root_for_t(t_c_slice, Pi_o, Lambda, eta_c, eta_cc)
    if len(c_sp) < 2:
        return rows
    for t_val in ts:
        if t_val <= 0:
            continue
        c_sp = spinodal_c_root_for_t(t_val, Pi_o, Lambda, eta_c, eta_cc)
        if len(c_sp) < 2:
            continue
        c_sp1, c_sp2 = c_sp[0], c_sp[1]
        # alpha branch (z=0)
        if prev_alpha is None:
            guess_ca = c_c_slice
            guess_cb = c_c_slice
        else:
            guess_ca = prev_alpha[0]
            guess_cb = prev_alpha[2] if prev_alpha else c_sp2
        res_a = solve_pair_for_alpha(t_val, Pi_o, params, guess_ca, c_sp2)
        if res_a:
            rows.append((params['name'], 't_c', t_val, Pi_o, res_a[0], res_a[2], res_a[1], res_a[3], 0.0))
            prev_alpha = res_a
        # beta branch (z=1)
        if prev_beta is None:
            guess_cb = c_c_slice
            guess_ca = c_c_slice
        else:
            guess_cb = prev_beta[2]
            guess_ca = prev_beta[0] if prev_beta else c_sp1
        res_b = solve_pair_for_beta(t_val, Pi_o, params, guess_cb, c_sp1)
        if res_b:
            rows.append((params['name'], 't_c', t_val, Pi_o, res_b[0], res_b[2], res_b[1], res_b[3], 1.0))
            prev_beta = res_b
    return rows

def compute_cP_binodal_slice(t_val, params):
    Lambda = params['Lambda']; eta_c = params['eta_c']; eta_cc = params['eta_cc']
    # For c-P slice, we need to find binodal for varying Pi_o at fixed t=0.8
    # Determine range of Pi_o where two-phase region exists.
    # We can use spinodal to estimate: compute Pi for each c, find region where spinodal Pi exists.
    # Then solve binodal for a grid of Pi_o.
    rows = []
    # approximate range of Pi
    if eta_cc != 0:
        # compute spinodal Pi min and max
        cs = np.linspace(0.01, 0.99, 100)
        Pis = [spinodal_c_for_P(t_val, c, Lambda, eta_c, eta_cc) for c in cs]
        Pis = [p for p in Pis if p is not None and not np.isnan(p) and not np.isinf(p)]
        if len(Pis) < 4:
            return rows
        Pi_min, Pi_max = np.min(Pis), np.max(Pis)
        Pi_range = np.linspace(Pi_min, Pi_max, 40)
    else:
        # eta_cc=0: Pi independent; choose range -0.5 to 0.5
        Pi_range = np.linspace(-0.5, 0.5, 40)

    prev_alpha = None; prev_beta = None
    for Pi_o in Pi_range:
        # compute spinodal c for this Pi_o
        c_sp = spinodal_c_root_for_t(t_val, Pi_o, Lambda, eta_c, eta_cc)
        if len(c_sp) < 2:
            continue
        c_sp1, c_sp2 = c_sp[0], c_sp[1]
        # alpha branch
        if prev_alpha is None:
            guess_ca = c_sp1
        else:
            guess_ca = prev_alpha[0]
        res_a = solve_pair_for_alpha(t_val, Pi_o, params, guess_ca, c_sp2)
        if res_a:
            rows.append((params['name'], 'c_P', t_val, Pi_o, res_a[0], res_a[2], res_a[1], res_a[3], 0.0))
            prev_alpha = res_a
        # beta branch
        if prev_beta is None:
            guess_cb = c_sp2
        else:
            guess_cb = prev_beta[2]
        res_b = solve_pair_for_beta(t_val, Pi_o, params, guess_cb, c_sp1)
        if res_b:
            rows.append((params['name'], 'c_P', t_val, Pi_o, res_b[0], res_b[2], res_b[1], res_b[3], 1.0))
            prev_beta = res_b
    return rows

# Generate CSVs
phase_rows = []
spinodal_rows = []
critical_rows = []

for p in param_sets:
    # critical point
    t_c, c_c, P_c = critical_point(p)
    critical_rows.append((p['name'], t_c, c_c, P_c))

    # spinodal t_c slice at Pi_o=0.1
    Pi_slice = 0.1
    if p['eta_cc'] != 0:
        cs_sp = np.linspace(0.01, 0.99, 200)
        for c in cs_sp:
            t_sp = spinodal_t(c, Pi_slice, p['Lambda'], p['eta_c'], p['eta_cc'])
            if t_sp > 0:
                spinodal_rows.append((p['name'], 't_c', t_sp, Pi_slice, c))
    else:
        # solve spinodal eq for c at Pi_o irrelevant
        # use t = c(1-c)*(4 - Lambda*eta_c^2)
        A = 4 - p['Lambda'] * p['eta_c']**2
        cs_sp = np.linspace(0.01, 0.99, 200)
        for c in cs_sp:
            t_sp = c*(1-c)*A
            if t_sp > 0:
                spinodal_rows.append((p['name'], 't_c', t_sp, Pi_slice, c))

    # spinodal c_P slice at t=0.8
    if p['eta_cc'] != 0:
        cs = np.linspace(0.01, 0.99, 200)
        for c in cs:
            Pi = spinodal_c_for_P(0.8, c, p['Lambda'], p['eta_c'], p['eta_cc'])
            if Pi is not None and not np.isnan(Pi) and not np.isinf(Pi):
                spinodal_rows.append((p['name'], 'c_P', 0.8, Pi, c))
    else:
        # eta_cc=0, solve for c such that t=0.8 = c(1-c)*(4 - Lambda*eta_c^2)
        A = 4 - p['Lambda'] * p['eta_c']**2
        # quadratic c^2 - c + 0.8/A = 0, only if discriminant >=0
        disc = 1 - 4*0.8/A if A>0 else -1
        if disc >= 0:
            c1 = (1 - np.sqrt(disc))/2
            c2 = (1 + np.sqrt(disc))/2
            spinodal_rows.append((p['name'], 'c_P', 0.8, 0.0, c1))
            spinodal_rows.append((p['name'], 'c_P', 0.8, 0.0, c2))

    # binodal t_c slice at Pi_o=0.1
    phase_rows.extend(compute_tc_binodal_slice(0.1, p))

    # binodal c_P slice at t=0.8
    phase_rows.extend(compute_cP_binodal_slice(0.8, p))

# Write CSV files
with open(os.path.join(outdir, 'phase_boundary_data.csv'), 'w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['param_set','slice_type','t','P_o','c_alpha','c_beta','P_alpha','P_beta','z'])
    for row in phase_rows:
        out.writerow([row[0], row[1], '{:.8g}'.format(row[2]), '{:.8g}'.format(row[3]),
                      '{:.8g}'.format(row[4]), '{:.8g}'.format(row[5]), '{:.8g}'.format(row[6]),
                      '{:.8g}'.format(row[7]), row[8]])

with open(os.path.join(outdir, 'spinodal_data.csv'), 'w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['param_set','slice_type','t','P_o','c_spinodal'])
    for row in spinodal_rows:
        out.writerow([row[0], row[1], '{:.8g}'.format(row[2]), '{:.8g}'.format(row[3]),
                      '{:.8g}'.format(row[4])])

with open(os.path.join(outdir, 'critical_points.csv'), 'w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['param_set','t_c','c_c','P_o_c'])
    for row in critical_rows:
        out.writerow([row[0], '{:.8g}'.format(row[1]), '{:.8g}'.format(row[2]), '{:.8g}'.format(row[3])])

print("Oracle data generated.")
