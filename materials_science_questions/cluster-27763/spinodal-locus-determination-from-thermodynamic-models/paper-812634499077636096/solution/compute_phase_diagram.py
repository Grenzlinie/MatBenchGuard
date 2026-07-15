#!/usr/bin/env python3
"""Fast oracle: compute phase diagram for two-temperature hard-sphere mixture."""
import sys, os, json, math
import numpy as np
from scipy.optimize import fsolve

def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)

    # Parameters (paper units)
    alpha_T = 20.0
    alpha_v = 1.0
    alpha_zeta = 1.0
    epsilon_A = 8.0
    epsilon_B = 8.0
    beta_B = 8.0
    gamma = (alpha_T + alpha_zeta) / (1.0 + alpha_zeta)   # = 10.5

    # ------------------------------------------------------------------
    # 1. Spinodal line
    # ------------------------------------------------------------------
    # Condition v_s = (alpha_T*(1+eps_A*phi_A)/phi_A)*(alpha_v*(1+eps_B*phi_B)/phi_B) - (gamma*beta_B)^2 = 0
    const = (gamma * beta_B) ** 2   # 7056.0

    def spinodal_phi_B(phi_A):
        # returns positive phi_B satisfying v_s=0, phi_B in (0,1) and phi_A+phi_B <= 1
        # Solve for phi_B:
        A = alpha_T * (1 + epsilon_A * phi_A) / phi_A
        # A * alpha_v * (1+eps_B*phi_B)/phi_B = const  => (1+eps_B*phi_B)/phi_B = const/(A * alpha_v)
        needed = const / (A * alpha_v)
        # (1 + eps_B*phi_B)/phi_B = needed  =>  1/phi_B + eps_B = needed  =>  phi_B = 1/(needed - eps_B)
        if needed <= epsilon_B:
            return None
        phi_B = 1.0 / (needed - epsilon_B)
        if phi_B <= 0 or phi_B > 1.0:
            return None
        return phi_B

    # Generate phi_A values in [~0.005, upper bound] where solution is physical
    phi_A_list = []
    phi_start = 0.005
    while True:
        pb = spinodal_phi_B(phi_start)
        if pb is not None and phi_start + pb <= 1.0:
            break
        phi_start *= 1.2
        if phi_start > 0.5:
            break

    phi_A_vals = np.linspace(phi_start, 0.8, 200)
    spinodal = []
    for pa in phi_A_vals:
        pb = spinodal_phi_B(pa)
        if pb is not None and pa + pb <= 1.0:
            spinodal.append((pa, pb))
        else:
            # if no solution, skip
            pass

    # At least 20 points? We'll take a subset of around 50 points.
    if len(spinodal) > 50:
        idx = np.linspace(0, len(spinodal)-1, 50, dtype=int)
        spinodal = [spinodal[i] for i in idx]
    elif len(spinodal) < 20:
        # if few points, use all
        pass

    with open(os.path.join(outdir, "spinodal.csv"), "w") as f:
        f.write("phi_A,phi_B\n")
        for pa, pb in spinodal:
            f.write(f"{pa:.8f},{pb:.8f}\n")

    # ------------------------------------------------------------------
    # 2. Critical point
    # ------------------------------------------------------------------
    # Solve Eqs. (25a)-(25b):
    #   phi_B*(1+eps_B*phi_B) / (1+eps_A*phi_A)^2 = alpha_T*(1+alpha_zeta)/(beta_B*(alpha_T+alpha_zeta))
    #   and v_s(phi_A,phi_B)=0.
    RHS = alpha_T * (1.0 + alpha_zeta) / (beta_B * (alpha_T + alpha_zeta))
    def eqs_critical(vars):
        pa, pb = vars
        err1 = pb * (1.0 + epsilon_B * pb) / (1.0 + epsilon_A * pa)**2 - RHS
        # spinodal condition:
        A = alpha_T * (1.0 + epsilon_A * pa) / pa
        B = alpha_v * (1.0 + epsilon_B * pb) / pb
        err2 = A * B - const
        return [err1, err2]

    # initial guess from approximate solution
    pa_guess = 1.0 / alpha_T   # 0.05
    pb_guess = 1.0/epsilon_B + 1.25/alpha_T   # 0.1875
    sol = fsolve(eqs_critical, [pa_guess, pb_guess], maxfev=1000)
    pa_star, pb_star = sol
    ps_star = 1.0 - pa_star - pb_star
    with open(os.path.join(outdir, "critical_point.json"), "w") as f:
        json.dump({"phi_A_star": pa_star, "phi_B_star": pb_star, "phi_s_star": ps_star}, f)

    # ------------------------------------------------------------------
    # 3. Binodal (coexistence) curve
    # ------------------------------------------------------------------
    # Chemical potentials (uniform):
    def mu_A(pa, pb):
        return alpha_T * math.log(pa) + alpha_T * epsilon_A * pa + gamma * beta_B * pb
    def mu_B(pa, pb):
        return alpha_v * math.log(pb) + alpha_v * epsilon_B * pb + gamma * beta_B * pa
    # Pressure:
    def p_dim(pa, pb):
        # p = sum mu*phi - f0
        # f0 = alpha_T*pa*log(pa) + alpha_v*pb*log(pb) + 0.5*(alpha_T*8*pa^2 + 2*gamma*8*pa*pb + 1*8*pb^2) but simplified
        # Using earlier derived expression:
        return (alpha_T*pa + alpha_v*pb + 4.0*alpha_T*pa*pa + (8.0*alpha_v - 4.0)*pb*pb + 8.0*gamma*pa*pb)

    # Solve for tie-line given fixed pa_a (phase a). Variables: [pb_a, pa_b, pb_b]
    # Use fsolve with initial guess from previous tie-line.
    def tie_line_equations(vars, pa_a):
        pb_a, pa_b, pb_b = vars
        # chemical potentials and pressure equal
        eq1 = mu_A(pa_a, pb_a) - mu_A(pa_b, pb_b)
        eq2 = mu_B(pa_a, pb_a) - mu_B(pa_b, pb_b)
        eq3 = p_dim(pa_a, pb_a) - p_dim(pa_b, pb_b)
        return [eq1, eq2, eq3]

    # Start from critical point (where both phases are equal)
    pa_c, pb_c = pa_star, pb_star
    tie_lines = []
    # We'll iterate by decreasing pa_a stepwise
    n_points = 30   # will yield >=20 after filtering
    pa_a_vals = np.linspace(pa_star - 0.001, 0.001, n_points)  # avoid exactly critical
    guess = [pb_c, pa_c, pb_c]   # initial guess for first step (close to critical)

    for pa_a in pa_a_vals:
        try:
            sol, infodict, ier, msg = fsolve(tie_line_equations, guess, args=(pa_a,), full_output=True, maxfev=2000)
            if ier != 1:
                # did not converge, try a closer guess or break
                break
            pb_a, pa_b, pb_b = sol
            # enforce physical: volumes fractions between 0 and 1, sum <=1
            if pb_a <= 0 or pa_b <= 0 or pb_b <= 0:
                guess = [pb_a, pa_b, pb_b]  # update guess anyway
                continue
            if pa_a + pb_a > 1.0 or pa_b + pb_b > 1.0:
                guess = [pb_a, pa_b, pb_b]
                continue
            # Ensure phases are distinct and order them consistently (e.g., phase a has lower phi_A)
            if pa_a > pa_b:
                # swap
                pa_a_s, pb_a_s, pa_b_s, pb_b_s = pa_b, pb_b, pa_a, pb_a
            else:
                pa_a_s, pb_a_s, pa_b_s, pb_b_s = pa_a, pb_a, pa_b, pb_b
            # Avoid duplicates
            if not tie_lines or (abs(pa_a_s - tie_lines[-1][0]) > 1e-6 and abs(pb_a_s - tie_lines[-1][1]) > 1e-6):
                tie_lines.append((pa_a_s, pb_a_s, pa_b_s, pb_b_s))
            # update guess for next step
            guess = [pb_a, pa_b, pb_b]
            if len(tie_lines) >= 25:
                break
        except Exception as e:
            continue

    # Filter to at least 20 points (or all if less)
    if len(tie_lines) > 22:
        idx = np.linspace(0, len(tie_lines)-1, 22, dtype=int)
        tie_lines = [tie_lines[i] for i in idx]

    with open(os.path.join(outdir, "binodal.csv"), "w") as f:
        f.write("phi_A_a,phi_B_a,phi_s_a,phi_A_b,phi_B_b,phi_s_b\n")
        for pa_a, pb_a, pa_b, pb_b in tie_lines:
            ps_a = 1.0 - pa_a - pb_a
            ps_b = 1.0 - pa_b - pb_b
            f.write(f"{pa_a:.8f},{pb_a:.8f},{ps_a:.8f},{pa_b:.8f},{pb_b:.8f},{ps_b:.8f}\n")

if __name__ == "__main__":
    main()
