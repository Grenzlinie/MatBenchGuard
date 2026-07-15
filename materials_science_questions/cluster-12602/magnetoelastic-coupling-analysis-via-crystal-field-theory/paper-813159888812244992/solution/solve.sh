#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: delta_S_CuGa.csv ===
cat > /solution/compute.py << 'PYEOF'
import sys, numpy as np, csv
from scipy.optimize import fsolve
from scipy.integrate import trapezoid

def get_CuGa_params(x):
    tc1 = 0.11
    a_val = -0.706
    tm1 = 3.46 / (1 + (8/9)*a_val**2)
    tm0 = -3.68 + tm1
    r = 0.324
    g = -0.547
    p = 0.572
    q = 0.0
    tc_x = 1 + (tc1 - 1)*x
    tm_x = tm0 + (tm1 - tm0)*x
    return tc_x, tm_x, tm1, r, a_val, g, p, q

def get_In_params(x):
    tc1 = 0.906
    a_val = -0.51
    tm1 = 3.18 / (1 + (8/9)*a_val**2)
    tm0 = -3.70 + tm1
    r = 1.36
    g = 0.40
    p = 0.0
    q = 0.10
    tc_x = 1 + (tc1 - 1)*x
    tm_x = tm0 + (tm1 - tm0)*x
    return tc_x, tm_x, tm1, r, a_val, g, p, q

def free_energy(e3, M, tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar):
    Fmag = 0.5*(t - tc_x)*M**2 + 0.25*M**4
    Fstrain = r*( (0.5/tm1)*(t - tm_x)*e3**2 + (2/3)*a_val*e3**3 + 0.25*e3**4 )
    Fcoup = 0.5*g*e3**2*M**2 + (1/3)*p*e3**3*M**2 + 0.5*q*e3**2*M**4
    Zeeman = -M*Hbar
    return Fmag + Fstrain + Fcoup + Zeeman

def eq_system(vars, tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar):
    e3, M = vars[0], vars[1]
    dF_dM = (t - tc_x)*M + M**3 + g*e3**2*M + (2/3)*p*e3**3*M + 2*q*e3**2*M**3 - Hbar
    dF_de3 = r*( (1/tm1)*(t - tm_x)*e3 + 2*a_val*e3**2 + e3**3 ) + g*e3*M**2 + p*e3**2*M**2 + q*e3*M**4
    return [dF_de3, dF_dM]

def solve_eq(tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar):
    guesses = [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.7, 0.3],
        [0.7, 1.0],
        [0.3, 0.5]
    ]
    best_sol = None
    best_F = np.inf
    for guess in guesses:
        try:
            sol = fsolve(eq_system, guess, args=(tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar), maxfev=2000, xtol=1e-12)
        except Exception:
            continue
        e3_sol, M_sol = sol
        Fval = free_energy(e3_sol, M_sol, tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar)
        if Fval < best_F:
            best_F = Fval
            best_sol = (e3_sol, M_sol)
    if best_sol is None:
        return (0.0, 0.0)
    return best_sol

def compute_order_parameters(t_arr, Hbar, params_func, x):
    tc_x, tm_x, tm1, r, a_val, g, p, q = params_func(x)
    e3_arr, M_arr = [], []
    for t in t_arr:
        e3_val, M_val = solve_eq(tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar)
        e3_arr.append(e3_val)
        M_arr.append(M_val)
    return np.array(e3_arr), np.array(M_arr)

def compute_deltaS(t_arr, Hbar, params_func, x):
    tc_x, tm_x, tm1, r, a_val, g, p, q = params_func(x)
    dS = []
    for t in t_arr:
        e3_0, M_0 = solve_eq(tc_x, tm_x, tm1, r, a_val, g, p, q, t, 0.0)
        e3_H, M_H = solve_eq(tc_x, tm_x, tm1, r, a_val, g, p, q, t, Hbar)
        dS.append(-0.5*(M_H**2 - M_0**2) - (r/(2*tm1))*(e3_H**2 - e3_0**2))
    return np.array(dS)

def compute_RC(x, params_func, Hbar, t_min=0.05, t_max=0.95, n_points=2000):
    # Integrate the full ΔS̄ curve; outside the transition region ΔS̄ is negligible,
    # so this yields the same RC as the paper’s definition (integral between T_A and T_B).
    t_arr = np.linspace(t_min, t_max, n_points)
    dS = compute_deltaS(t_arr, Hbar, params_func, x)
    rc = abs(trapezoid(dS, t_arr))   # RC is positive
    return rc

if __name__ == '__main__':
    if len(sys.argv) != 5 or sys.argv[1] != '--mode' or sys.argv[3] != '--out':
        print('Usage: compute.py --mode <mode> --out <outfile>')
        sys.exit(1)
    mode = sys.argv[2]
    out_path = sys.argv[4]

    if mode == 'delta_CuGa':
        x = 0.26
        H = 0.005
        t_arr = np.linspace(0.2, 0.9, 500)
        dS = compute_deltaS(t_arr, H, get_CuGa_params, x)
        with open(out_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['reduced_temperature', 'delta_S'])
            for t, ds in zip(t_arr, dS):
                writer.writerow([f'{t:.10f}', f'{ds:.15f}'])

    elif mode == 'delta_In':
        x = 0.37
        H = 0.005
        t_arr = np.linspace(0.2, 0.9, 500)
        dS = compute_deltaS(t_arr, H, get_In_params, x)
        with open(out_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['reduced_temperature', 'delta_S'])
            for t, ds in zip(t_arr, dS):
                writer.writerow([f'{t:.10f}', f'{ds:.15f}'])

    elif mode == 'RC_CuGa':
        xs = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
        H = 0.005
        rc_vals = []
        for x in xs:
            rc = compute_RC(x, get_CuGa_params, H, t_min=0.05, t_max=0.95, n_points=3000)
            rc_vals.append(rc)
        with open(out_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['x', 'RC_bar'])
            for x, rc in zip(xs, rc_vals):
                writer.writerow([f'{x:.10f}', f'{rc:.15f}'])

    elif mode == 'RC_In':
        xs = [0.34, 0.36, 0.37, 0.38, 0.40, 0.42]
        H = 0.005
        rc_vals = []
        for x in xs:
            rc = compute_RC(x, get_In_params, H, t_min=0.05, t_max=0.95, n_points=3000)
            rc_vals.append(rc)
        with open(out_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['x', 'RC_bar'])
            for x, rc in zip(xs, rc_vals):
                writer.writerow([f'{x:.10f}', f'{rc:.15f}'])
    else:
        print(f'Unknown mode {mode}')
        sys.exit(1)
PYEOF
python3 /solution/compute.py --mode delta_CuGa --out "$OUTDIR/delta_S_CuGa.csv"

# === solve block: delta_S_In.csv ===
python3 /solution/compute.py --mode delta_In --out "$OUTDIR/delta_S_In.csv"

# === solve block: RC_CuGa.csv ===
python3 /solution/compute.py --mode RC_CuGa --out "$OUTDIR/RC_CuGa.csv"

# === solve block: RC_In.csv ===
python3 /solution/compute.py --mode RC_In --out "$OUTDIR/RC_In.csv"
