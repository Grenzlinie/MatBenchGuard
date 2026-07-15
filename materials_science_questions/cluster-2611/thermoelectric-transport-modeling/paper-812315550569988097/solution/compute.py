#!/usr/bin/env python3
import sys, json, csv, numpy as np

def compute_maxdeltaT(output_path):
    alpha_over_beta_vals = [0.2, 0.32, 0.512, 0.8192, 1.31072, 2.097152]
    ZTc_vals = np.linspace(0.1, 1.0, 10)
    rows = []
    for a in alpha_over_beta_vals:
        for ZTc in ZTc_vals:
            if ZTc < a:
                xi = -np.log(1.0 - ZTc / a)
                ZDeltaT_max = a*a * (xi + np.exp(-xi) - 1.0)
                if ZDeltaT_max < 0: ZDeltaT_max = 0.0
                rows.append([ZTc, a, ZDeltaT_max])
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ZTc', 'alpha_over_beta', 'ZDeltaT_max'])
        for row in rows:
            writer.writerow(row)
    print(f"Wrote {len(rows)} rows to {output_path}")

def compute_maxheatload(output_path):
    # parametric approach: xi -> b, Nstar
    xi_vals = np.logspace(-4, 2, 20000)  # from small positive to 100
    # D(xi) = 1 + 2*xi/(1-e^xi) + xi^2 * e^xi / (1-e^xi)^2
    exp_xi = np.exp(xi_vals)
    one_minus_exp = 1.0 - exp_xi
    # careful with division, use direct formula
    D = 1.0 + 2*xi_vals / one_minus_exp + (xi_vals*xi_vals * exp_xi) / (one_minus_exp * one_minus_exp)
    # Nstar = 2 xi^2/(1-e^xi) * (1 + xi e^xi/(1-e^xi))
    Nstar = (2*xi_vals*xi_vals / one_minus_exp) * (1.0 + xi_vals*exp_xi/one_minus_exp)
    # keep only finite and b>0
    mask = np.isfinite(D) & np.isfinite(Nstar) & (D > 0)
    b = D[mask]
    N = Nstar[mask]
    # sort by b
    idx = np.argsort(b)
    b = b[idx]
    N = N[idx]
    # b has maximum around 1.18, so limit to that
    b_max = b.max()
    b_grid = np.linspace(0.1, min(2.0, b_max), 30)
    # interpolate N at b_grid
    N_grid = np.interp(b_grid, b, N)
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ZTh_beta_over_alpha', 'Nmax_star'])
        for bi, ni in zip(b_grid, N_grid):
            writer.writerow([bi, ni])
    print(f"Wrote {len(b_grid)} rows to {output_path}")

def compute_example_curve(output_path):
    # parameters
    sigma_Sm = 0.1 * 1e6        # 0.1 (µΩm)^-1 = 1e5 S/m
    lam = 1.6                  # W/mK
    alpha = 185e-6             # V/K
    beta = 200e-6              # V/K
    L = 1e-3                   # m
    A = 0.01e-6                # m^2  (0.01 mm^2)
    P = 0.4e-3                 # m
    gamma = 50.0               # W/m^2K
    T_inf = 300.0
    Tc = 250.0
    # derived
    K = lam * A / L
    R = L / (sigma_Sm * A)
    Pstar = P * gamma * L / K
    I_vals = np.linspace(0.001, 0.1, 100)  # avoid I=0
    deltaT = []
    for I in I_vals:
        xi = beta * I / K
        # roots of kappa^2 - xi*kappa - Pstar = 0
        disc = xi*xi + 4*Pstar
        sqrt_d = np.sqrt(disc)
        k1 = (xi + sqrt_d) / 2.0
        k2 = (xi - sqrt_d) / 2.0
        # functions f,g,h (Eqs.12-14)
        exp_k1 = np.exp(k1)
        exp_k2 = np.exp(k2)
        denom_f = exp_k1 - exp_k2
        f = (k1 - k2) / denom_f if abs(denom_f) > 1e-15 else 1.0
        # g = (k1*exp(k2)-k2*exp(k1))/denom_f - f
        g = (k1*exp_k2 - k2*exp_k1) / denom_f - f
        # h = -g/(k1*k2)
        if abs(k1*k2) > 1e-15:
            h = -g / (k1*k2)
        else:
            h = 0.5  # limit for k1,k2 ->0
        # modified coefficients for whole couple (identical legs)
        K_tilde = 2*K*f
        H_tilde = 2*K*g
        R_tilde = 2*R*h
        # cooling power q_c (Eq.8), set to zero => solve for deltaT
        qc_no_deltaT = 2*alpha*I*Tc - H_tilde*(T_inf - Tc) - I*I*R_tilde
        # K_tilde * deltaT = qc_no_deltaT  => deltaT
        if K_tilde > 0:
            dT = qc_no_deltaT / K_tilde
        else:
            dT = 0.0
        deltaT.append(max(0.0, dT))
    deltaT = np.array(deltaT)
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['I_A', 'DeltaT_K'])
        for i, dT in zip(I_vals, deltaT):
            writer.writerow([i, dT])
    print(f"Wrote {len(I_vals)} rows to {output_path}")

def compute_example_max(output_path):
    # recompute the same curve to get max
    sigma_Sm = 0.1 * 1e6
    lam = 1.6
    alpha = 185e-6
    beta = 200e-6
    L = 1e-3
    A = 0.01e-6
    P = 0.4e-3
    gamma = 50.0
    T_inf = 300.0
    Tc = 250.0
    K = lam * A / L
    R = L / (sigma_Sm * A)
    Pstar = P * gamma * L / K
    I_vals = np.linspace(0.001, 0.1, 200)
    max_dT = 0.0
    for I in I_vals:
        xi = beta * I / K
        disc = xi*xi + 4*Pstar
        sqrt_d = np.sqrt(disc)
        k1 = (xi + sqrt_d) / 2.0
        k2 = (xi - sqrt_d) / 2.0
        exp_k1 = np.exp(k1)
        exp_k2 = np.exp(k2)
        denom_f = exp_k1 - exp_k2
        f = (k1 - k2) / denom_f if abs(denom_f) > 1e-15 else 1.0
        g = (k1*exp_k2 - k2*exp_k1) / denom_f - f
        if abs(k1*k2) > 1e-15:
            h = -g / (k1*k2)
        else:
            h = 0.5
        qc_no = 2*alpha*I*Tc - 2*K*g*(T_inf - Tc) - 2*R*h*I*I
        if (2*K*f) > 0:
            dT = qc_no / (2*K*f)
            if dT > max_dT:
                max_dT = dT
    max_dT = max(0.0, max_dT)
    with open(output_path, 'w') as f:
        json.dump({"beta_200_max_delta_T_K": round(max_dT, 2)}, f)
    print(f"Max dT = {max_dT} written to {output_path}")

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    out = sys.argv[2] if len(sys.argv) > 2 else '/dev/null'
    if mode == 'maxdeltaT':
        compute_maxdeltaT(out)
    elif mode == 'maxheatload':
        compute_maxheatload(out)
    elif mode == 'example_curve':
        compute_example_curve(out)
    elif mode == 'example_max':
        compute_example_max(out)
    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)
