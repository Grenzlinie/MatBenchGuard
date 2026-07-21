import sys
import numpy as np
from scipy.optimize import fsolve

# Energy parameters in reduced units (scaled by |J_s|)
vAA = 0.4
vBB = 0.8
vAA_s = 0.7
vBB_s = 0.9
vAA_p = 0.8   # v'_AA
vBB_p = 1.0   # v'_BB
w = 1.0
ws = 1.2
wp = 1.6

# Precomputed constants from the algebraic simplification of Eq.(15)
# Equation (15) simplifies to:
#   tau * ln( c_sA*(1-c_A) / ((1-c_sA)*c_A) ) = 1.0 + 4.8*c_A - 4.8*c_sA
# (derived from the given v and w values)
RHS_c = 1.0
RHS_cA_coeff = 4.8
RHS_csA_coeff = -4.8

def ln_term(c_sA, cA):
    if c_sA <= 0.0 or c_sA >= 1.0 or cA <= 0.0 or cA >= 1.0:
        return 0.0
    return np.log(c_sA * (1.0 - cA) / ((1.0 - c_sA) * cA))

def eq_mu0(vars, cA):
    c_sA = vars[0]
    tau = 2.0 * c_sA**2
    eq2 = tau * ln_term(c_sA, cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * c_sA)
    return [eq2]

def eq_mu05(vars, cA):
    c_sA, tau = vars[0], vars[1]
    mu = 0.5
    eq1 = tau * np.log((1.0 + mu) / (1.0 - mu)) - 4.0 * c_sA**2 * mu
    eq2 = tau * ln_term(c_sA, cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * c_sA)
    return [eq1, eq2]

def solve_mu0(cA):
    sol = fsolve(lambda v: eq_mu0(v, cA), 0.3, maxfev=1000)
    return sol[0]

def solve_mu05(cA):
    sol = fsolve(lambda v: eq_mu05(v, cA), [0.3, 0.1], maxfev=1000)
    return sol[0]

def generate_fig1():
    cA_arr = np.linspace(0.001, 0.20, 100)
    mu0_vals = []
    mu05_vals = []
    mu1_vals = []
    for cA in cA_arr:
        c0 = solve_mu0(cA)
        c05 = solve_mu05(cA)
        # mu=1 limit: tau=0, RHS leads to linear relation
        c1 = (RHS_c + RHS_cA_coeff * cA) / (-RHS_csA_coeff)   # = (1+4.8cA)/4.8
        mu0_vals.append(c0)
        mu05_vals.append(c05)
        mu1_vals.append(c1)
    with open('/app/outputs/fig1_csA_vs_cA.csv', 'w') as f:
        f.write('cA,csA_mu0,csA_mu0p5,csA_mu1\n')
        for i, cA in enumerate(cA_arr):
            f.write(f"{cA},{mu0_vals[i]},{mu05_vals[i]},{mu1_vals[i]}\n")
    print("Fig1 CSV written.")

def eq_full(vars, cA, mu_val):
    c_sA, tau = vars[0], vars[1]
    eq1 = tau * np.log((1.0 + mu_val) / (1.0 - mu_val)) - 4.0 * c_sA**2 * mu_val
    eq2 = tau * ln_term(c_sA, cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * c_sA)
    return [eq1, eq2]

def solve_csA_for_mu(cA, mu):
    """Return c_sA and tau for a given cA and mu."""
    if mu <= 0.0:
        c_sA = solve_mu0(cA)
        tau = 2.0 * c_sA**2
        return c_sA, tau
    if mu >= 1.0 - 1e-12:
        c_sA = (1.0 + 4.8 * cA) / 4.8
        tau = 1e-6  # not used, just a placeholder
        return c_sA, tau
    sol = fsolve(lambda v: eq_full(v, cA, mu), [0.3, 0.1], maxfev=1000)
    return sol[0], sol[1]

def generate_fig2():
    cA_list = [0.001, 0.01, 0.05, 0.1]
    mu_vals = np.linspace(0.0, 1.0, 100)
    # store csA for each mu and cA
    data = {cA: [] for cA in cA_list}
    for mu in mu_vals:
        for cA in cA_list:
            c_sA, _ = solve_csA_for_mu(cA, mu)
            data[cA].append(c_sA)
    with open('/app/outputs/fig2_csA_vs_mu.csv', 'w') as f:
        f.write('mu,csA_cA0p001,csA_cA0p01,csA_cA0p05,csA_cA0p1\n')
        for i, mu in enumerate(mu_vals):
            line = f"{mu}"
            for cA in cA_list:
                line += f",{data[cA][i]}"
            f.write(line + '\n')
    print("Fig2 CSV written.")

def generate_fig3():
    cA_list = [0.01, 0.05, 0.1]
    tau_arr = np.linspace(0.0, 2.0, 200)
    results = {cA: [] for cA in cA_list}
    for cA in cA_list:
        mu_prev = 1.0     # T=0 saturation
        c_sA_prev = (1.0 + 4.8 * cA) / 4.8   # tau=0 limit
        for tau in tau_arr:
            if tau == 0.0:
                mu = 1.0
                c_sA = c_sA_prev
            elif mu_prev < 1e-5:
                # already in paramagnetic phase, solve only segregation eq
                def eq2_only(vars):
                    cs = vars[0]
                    return [tau * ln_term(cs, cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * cs)]
                sol = fsolve(eq2_only, c_sA_prev, maxfev=1000)
                c_sA = sol[0]
                mu = 0.0
            else:
                # solve coupled equations with previous solution as guess
                def eqs(vars):
                    mu_s, cs = vars[0], vars[1]
                    eq1 = tau * np.log((1.0 + mu_s) / (1.0 - mu_s)) - 4.0 * cs**2 * mu_s
                    eq2 = tau * ln_term(cs, cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * cs)
                    return [eq1, eq2]
                try:
                    sol = fsolve(eqs, [mu_prev, c_sA_prev], maxfev=1000)
                    mu, c_sA = sol[0], sol[1]
                    if mu < 1e-5 or np.isnan(mu):
                        mu = 0.0
                        # re-solve eq2 only
                        def eq2_only(v):
                            return [tau * ln_term(v[0], cA) - (RHS_c + RHS_cA_coeff * cA + RHS_csA_coeff * v[0])]
                        sol2 = fsolve(eq2_only, c_sA_prev, maxfev=1000)
                        c_sA = sol2[0]
                except Exception:
                    mu = 0.0
                    c_sA = c_sA_prev
            results[cA].append(mu)
            mu_prev = mu
            c_sA_prev = c_sA
    with open('/app/outputs/fig3_mu_vs_T.csv', 'w') as f:
        f.write('tau,mu_cA0p01,mu_cA0p05,mu_cA0p1\n')
        for i, tau in enumerate(tau_arr):
            line = f"{tau}"
            for cA in cA_list:
                line += f",{results[cA][i]}"
            f.write(line + '\n')
    print("Fig3 CSV written.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: generate_ref.py {fig1|fig2|fig3}")
        sys.exit(1)
    arg = sys.argv[1]
    if arg == 'fig1':
        generate_fig1()
    elif arg == 'fig2':
        generate_fig2()
    elif arg == 'fig3':
        generate_fig3()
    else:
        print(f"Unknown command: {arg}")
        sys.exit(1)
