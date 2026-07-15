#!/usr/bin/env python3
import sys, argparse, numpy as np
from scipy.optimize import minimize

# ---------- Free energy ----------
def free_energy(M, e3, t, H, r, a, g, p, q, t_c, t_m, t_m1):
    term_M = 0.5 * (t - t_c) * M**2 + 0.25 * M**4
    mart_base = 0.5/t_m1 * (t - t_m) * e3**2 + (2.0/3.0)*a*e3**3 + 0.25*e3**4
    term_e3 = r * mart_base
    coupling = 0.5*g*e3**2*M**2 + (1.0/3.0)*p*e3**3*M**2 + 0.5*q*e3**2*M**4
    zeeman = - M * H
    return term_M + term_e3 + coupling + zeeman

# ---------- Global minimum search ----------
def find_global_min(t, H, params, n_grid=7):
    M_grid = np.linspace(0.05, 2.0, n_grid)
    e3_grid = np.linspace(-1.5, 1.5, n_grid)
    best = None
    solutions = []
    for M0 in M_grid:
        for e30 in e3_grid:
            bounds = [(0.0, 3.0), (-2.0, 2.0)]
            res = minimize(lambda x: free_energy(x[0], x[1], t, H, params['r'], params['a'], params['g'], params['p'], params['q'], params['t_c'], params['t_m'], params['t_m1']),
                           [M0, e30], method='L-BFGS-B', bounds=bounds, options={'maxiter':500, 'ftol':1e-12})
            if res.success:
                M_opt, e3_opt = res.x
                F_val = res.fun
                solutions.append((M_opt, e3_opt, F_val))
    if not solutions:
        raise RuntimeError(f"No solution found at t={t}")
    arr = np.array(solutions)
    rounded = np.round(arr[:,:2], decimals=6)
    _, idx = np.unique(rounded, axis=0, return_index=True)
    unique = arr[idx]
    order = np.argsort(unique[:,2])
    sorted_sol = unique[order]
    global_min = sorted_sol[0]
    second_min = sorted_sol[1] if len(sorted_sol)>1 and np.linalg.norm(sorted_sol[1,:2]-sorted_sol[0,:2]) > 0.01 else None
    return global_min, second_min

# ---------- Find first-order transition temperature from scan ----------
def find_FOT(t_vals, M_vals, threshold=0.2):
    diff_M = np.abs(np.diff(M_vals))
    idx = np.argmax(diff_M)
    if diff_M[idx] > threshold:
        t_trans = 0.5 * (t_vals[idx] + t_vals[idx+1])
        return t_trans
    else:
        return None

# ---------- Alloy parameter sets ----------
def get_CuGa_params(x):
    r = 0.324
    a = -0.706
    g = -0.547
    p = 0.572
    q = 0.0
    t_m1 = 3.46 / (1 + (8.0/9.0)*a**2)
    t_m0 = -3.68 + t_m1
    t_c = 1.0 + (0.11 - 1.0) * x
    t_m = t_m0 + (t_m1 - t_m0) * x
    return {'r':r, 'a':a, 'g':g, 'p':p, 'q':q, 't_c':t_c, 't_m':t_m, 't_m1':t_m1}

def get_In_params(x):
    r = 1.36
    a = -0.51
    g = 0.40
    p = 0.0
    q = 0.10
    t_m1 = 3.18 / (1 + (8.0/9.0)*a**2)
    t_m0 = -3.70 + t_m1
    t_c = 1.0 + (0.906 - 1.0) * x
    t_m = t_m0 + (t_m1 - t_m0) * x
    return {'r':r, 'a':a, 'g':g, 'p':p, 'q':q, 't_c':t_c, 't_m':t_m, 't_m1':t_m1}

# ---------- Compute ΔS curve ----------
def compute_delta_S_curve(x, alloy_getter, H_val, t_range):
    params = alloy_getter(x)
    t_vals = np.arange(t_range[0], t_range[1], 0.001)
    M0 = np.empty_like(t_vals)
    e30 = np.empty_like(t_vals)
    MH = np.empty_like(t_vals)
    e3H = np.empty_like(t_vals)
    for i, t in enumerate(t_vals):
        gmin0, _ = find_global_min(t, 0.0, params)
        M0[i], e30[i] = gmin0[0], gmin0[1]
        gminH, _ = find_global_min(t, H_val, params)
        MH[i], e3H[i] = gminH[0], gminH[1]
    dS = -0.5*(MH**2 - M0**2) - (params['r']/(2*params['t_m1']))*(e3H**2 - e30**2)
    return t_vals, dS

# ---------- Compute RC for a composition ----------
def compute_RC(x, alloy_getter, H_val):
    params = alloy_getter(x)
    t_vals = np.arange(0.4, 1.5, 0.002)
    M0_arr = np.empty_like(t_vals)
    e30_arr = np.empty_like(t_vals)
    MH_arr = np.empty_like(t_vals)
    e3H_arr = np.empty_like(t_vals)
    for i, t in enumerate(t_vals):
        gmin0, _ = find_global_min(t, 0.0, params)
        M0_arr[i], e30_arr[i] = gmin0[0], gmin0[1]
        gminH, _ = find_global_min(t, H_val, params)
        MH_arr[i], e3H_arr[i] = gminH[0], gminH[1]
    TA = find_FOT(t_vals, M0_arr)
    TB = find_FOT(t_vals, MH_arr)
    if TA is None or TB is None:
        return 0.0
    # compute ΔS on the same grid
    dS = -0.5*(MH_arr**2 - M0_arr**2) - (params['r']/(2*params['t_m1']))*(e3H_arr**2 - e30_arr**2)
    # integrate between TA and TB (absolute area)
    # find indices within [min(TA,TB), max(TA,TB)]
    t_low = min(TA, TB)
    t_high = max(TA, TB)
    mask = (t_vals >= t_low) & (t_vals <= t_high)
    if np.sum(mask) < 2:
        return 0.0
    t_sel = t_vals[mask]
    dS_sel = dS[mask]
    integral = np.trapz(dS_sel, t_sel)
    RC = abs(integral)   # paper reports positive RC
    return RC

# ---------- Main handler ----------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['delta_CuGa','delta_In','RC_CuGa','RC_In'])
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    if args.mode == 'delta_CuGa':
        t, dS = compute_delta_S_curve(0.26, get_CuGa_params, 0.005, (0.8, 1.3))
        with open(args.out, 'w') as f:
            f.write("reduced_temperature,delta_S\n")
            for ti, si in zip(t, dS):
                f.write(f"{ti:.6f},{si:.8f}\n")

    elif args.mode == 'delta_In':
        t, dS = compute_delta_S_curve(0.37, get_In_params, 0.005, (0.7, 1.2))
        with open(args.out, 'w') as f:
            f.write("reduced_temperature,delta_S\n")
            for ti, si in zip(t, dS):
                f.write(f"{ti:.6f},{si:.8f}\n")

    elif args.mode == 'RC_CuGa':
        xs = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
        with open(args.out, 'w') as f:
            f.write("x,RC_bar\n")
            for x in xs:
                rc = compute_RC(x, get_CuGa_params, 0.005)
                f.write(f"{x:.2f},{rc:.6f}\n")

    elif args.mode == 'RC_In':
        xs = [0.34, 0.36, 0.37, 0.38, 0.40, 0.42]
        with open(args.out, 'w') as f:
            f.write("x,RC_bar\n")
            for x in xs:
                rc = compute_RC(x, get_In_params, 0.005)
                f.write(f"{x:.2f},{rc:.6f}\n")
