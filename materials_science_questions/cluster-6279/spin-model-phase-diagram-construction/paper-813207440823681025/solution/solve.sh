#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
cat > /tmp/run.py <<'PYEOF'
import math, sys, argparse

def gamma_hh(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1 or abs(1-u) < 1e-12:
        return 0.0
    denom = k*k * (1.0 - u)
    b = - (rho - rho * u - 1.0) / denom
    c = - u * rho_x * rho_y / (k**4 * (1.0 - u))
    disc = b*b - 4.0*c
    if disc < 0:
        return 0.0
    sqrt_disc = math.sqrt(disc)
    g1 = (-b + sqrt_disc) / 2.0
    g2 = (-b - sqrt_disc) / 2.0
    g = max(g1, g2)
    max_possible = min(rho_x, rho_y) / (k*k)
    if g < 0:
        g = 0.0
    elif g > max_possible:
        g = max_possible
    return g

def free_energy(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1:
        return 0.0
    g = gamma_hh(rho_x, rho_y, u, k)
    gkk = g * k * k
    term1 = 0.0
    if rho_x > 0:
        term1 += rho_x * math.log(rho_x)
    if rho_y > 0:
        term1 += rho_y * math.log(rho_y)
    term1 *= -(k-1)/k
    term2 = 0.0
    for ri in [rho_x, rho_y]:
        arg = 1.0 - (k-1)*ri/k
        if arg <= 0:
            return 1e9
        term2 += arg * math.log(arg)
    term2 = -term2
    term3 = 0.0
    for ri in [rho_x, rho_y]:
        arg = ri - gkk
        if arg <= 0:
            return 1e9
        term3 += arg * math.log(arg)
    term4 = 1.0 - rho + gkk
    if term4 <= 0:
        return 1e9
    term4 = term4 * math.log(term4)
    term5 = - rho/k * math.log(k)
    term6 = 0.0
    if gkk > 0 and u > 0:
        term6 = gkk * math.log(gkk / u)
    return term1 + term2 + term3 + term4 + term5 + term6

def min_order_param(rho, u, k):
    best_psi = 0.0
    best_f = float('inf')
    for psi in [i*0.01 for i in range(101)]:
        rho_x = rho*(1+psi)/2.0
        rho_y = rho*(1-psi)/2.0
        if rho_x < 0 or rho_x > rho or rho_y < 0 or rho_y > rho:
            continue
        f_val = free_energy(rho_x, rho_y, u, k)
        if f_val < best_f:
            best_f = f_val
            best_psi = psi
    for _ in range(2):
        start = max(0.0, best_psi - 0.01)
        end = min(1.0, best_psi + 0.01)
        step = 0.001
        n = int((end-start)/step) + 1
        for i in range(n):
            psi = start + i*step
            rho_x = rho*(1+psi)/2.0
            rho_y = rho*(1-psi)/2.0
            if rho_x < 0 or rho_x > rho or rho_y < 0 or rho_y > rho:
                continue
            f_val = free_energy(rho_x, rho_y, u, k)
            if f_val < best_f:
                best_f = f_val
                best_psi = psi
    f0 = free_energy(rho/2.0, rho/2.0, u, k)
    if f0 < best_f - 1e-12:
        best_psi = 0.0
    return best_psi if best_f < 1e8 else 0.0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['order','phase'])
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    k = 6
    if args.mode == 'order':
        u = 0.15
        rho_vals = [i*0.001 for i in range(10, 951)]  # 0.01 to 0.95
        with open(args.out, 'w') as f:
            f.write("density,order_parameter\n")
            for rho in rho_vals:
                psi = min_order_param(rho, u, k)
                f.write(f"{rho:.5f},{psi:.6f}\n")
    elif args.mode == 'phase':
        u_vals = []
        rho_c1_list = []
        rho_c2_list = []
        for u in [i*0.01 for i in range(31)]:
            psi_curve = []
            rho_grid = [i*0.001 for i in range(10, 1000)]
            for rho in rho_grid:
                psi = min_order_param(rho, u, k)
                psi_curve.append(psi)
            idx_start = None
            for idx, psi in enumerate(psi_curve):
                if psi > 1e-5:
                    idx_start = idx
                    break
            if idx_start is None:
                continue
            idx_end = None
            for idx in range(len(psi_curve)-1, -1, -1):
                if psi_curve[idx] > 1e-5:
                    idx_end = idx
                    break
            if idx_end is None or idx_end <= idx_start:
                continue
            psi_start1 = psi_curve[idx_start-1] if idx_start>0 else 0.0
            psi_start2 = psi_curve[idx_start]
            if psi_start2 - psi_start1 > 1e-12:
                frac = (0.0 - psi_start1) / (psi_start2 - psi_start1)
                rho_c1 = rho_grid[idx_start-1] if idx_start>0 else 0.0
                rho_c1 += frac * (rho_grid[idx_start] - (rho_grid[idx_start-1] if idx_start>0 else 0.0))
            else:
                rho_c1 = rho_grid[idx_start]
            psi_end1 = psi_curve[idx_end]
            psi_end2 = psi_curve[idx_end+1] if idx_end+1 < len(psi_curve) else 0.0
            if psi_end1 - psi_end2 > 1e-12:
                rho_c2 = rho_grid[idx_end] + (0.0 - psi_end2) / (psi_end1 - psi_end2) * (rho_grid[idx_end+1] - rho_grid[idx_end])
            else:
                rho_c2 = rho_grid[idx_end]
            u_vals.append(u)
            rho_c1_list.append(rho_c1)
            rho_c2_list.append(rho_c2)
            if rho_c2 - rho_c1 < 0.005:
                break
        with open(args.out, 'w') as f:
            f.write("u,rho_c1,rho_c2\n")
            for i in range(len(u_vals)):
                f.write(f"{u_vals[i]:.3f},{rho_c1_list[i]:.6f},{rho_c2_list[i]:.6f}\n")

if __name__ == '__main__':
    main()
PYEOF

# === solve block: order_parameter_vs_density.csv ===
python3 <<'PYEOF'
import math

K = 6
U = 0.15

def gamma_hh(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1:
        return 0.0
    denom = k * k * (1.0 - u)
    if abs(denom) < 1e-14:
        return 0.0
    A = (rho - rho * u - 1.0) / denom
    C = - u * rho_x * rho_y / (k ** 4 * (1.0 - u))
    disc = A * A - 4.0 * C
    if disc < 0:
        return 0.0
    sqrt_disc = math.sqrt(disc)
    g1 = (-A + sqrt_disc) / 2.0
    g2 = (-A - sqrt_disc) / 2.0
    g = g1 if g1 > g2 else g2
    if g < 0.0:
        g = 0.0
    max_g = min(rho_x, rho_y) / (k * k)
    if g > max_g:
        g = max_g
    return g

def free_energy(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1:
        return 0.0
    g = gamma_hh(rho_x, rho_y, u, k)
    gkk = g * k * k

    term1 = 0.0
    if rho_x > 0:
        term1 += rho_x * math.log(rho_x)
    if rho_y > 0:
        term1 += rho_y * math.log(rho_y)
    term1 *= -(k - 1) / k

    term2 = 0.0
    for ri in (rho_x, rho_y):
        arg = 1.0 - (k - 1) * ri / k
        if arg > 0:
            term2 += arg * math.log(arg)
        else:
            return 1e9
    term2 = -term2

    term3 = 0.0
    for ri in (rho_x, rho_y):
        arg = ri - gkk
        if arg > 0:
            term3 += arg * math.log(arg)
        else:
            return 1e9

    tmp = 1.0 - rho + gkk
    if tmp > 0:
        term4 = tmp * math.log(tmp)
    else:
        return 1e9

    term5 = - rho / k * math.log(k)

    term6 = 0.0
    if gkk > 0 and u > 0:
        term6 = gkk * math.log(gkk / u)

    return term1 + term2 + term3 + term4 + term5 + term6

def calc_psi(rho, u, k):
    # Coarse scan
    best_psi = 0.0
    best_f = float('inf')
    for i in range(101):
        psi = i / 100.0
        rho_x = rho * (1.0 + psi) / 2.0
        rho_y = rho * (1.0 - psi) / 2.0
        if rho_x < 0 or rho_y < 0:
            continue
        f_val = free_energy(rho_x, rho_y, u, k)
        if f_val < best_f:
            best_f = f_val
            best_psi = psi

    # Golden-section refinement around best_psi
    a = max(0.0, best_psi - 0.1)
    b = min(1.0, best_psi + 0.1)
    phi = (math.sqrt(5) - 1) / 2
    for _ in range(30):
        c = b - phi * (b - a)
        d = a + phi * (b - a)
        f_c = free_energy(rho * (1.0 + c) / 2.0, rho * (1.0 - c) / 2.0, u, k)
        f_d = free_energy(rho * (1.0 + d) / 2.0, rho * (1.0 - d) / 2.0, u, k)
        if f_c < f_d:
            b = d
        else:
            a = c
        if b - a < 1e-7:
            break

    psi_opt = (a + b) / 2.0
    f_nem = free_energy(rho * (1.0 + psi_opt) / 2.0,
                         rho * (1.0 - psi_opt) / 2.0, u, k)
    f_iso = free_energy(rho / 2.0, rho / 2.0, u, k)
    if f_iso <= f_nem - 1e-12:
        return 0.0
    return psi_opt

with open('/app/outputs/order_parameter_vs_density.csv', 'w') as out:
    out.write('density,order_parameter\n')
    # densities from 0.01 to 0.95, step 0.001
    for i in range(10, 951):
        rho = i / 1000.0
        psi = calc_psi(rho, U, K)
        out.write(f'{rho:.5f},{psi:.7f}\n')
PYEOF

# === solve block: phase_diagram_critical_densities.csv ===
python3 <<'PYEOF'
import math

K = 6

def gamma_hh(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1 or abs(1 - u) < 1e-12:
        return 0.0
    denom = k * k * (1.0 - u)
    if abs(denom) < 1e-15:
        return 0.0
    b = - (rho - rho * u - 1.0) / denom
    c = - u * rho_x * rho_y / (k ** 4 * (1.0 - u))
    disc = b * b - 4.0 * c
    if disc < 0:
        return 0.0
    sqrt_disc = math.sqrt(disc)
    g1 = (-b + sqrt_disc) / 2.0
    g2 = (-b - sqrt_disc) / 2.0
    g = max(g1, g2)
    max_possible = min(rho_x, rho_y) / (k * k)
    if g < 0:
        g = 0.0
    elif g > max_possible:
        g = max_possible
    return g

def free_energy(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1:
        return 0.0
    g = gamma_hh(rho_x, rho_y, u, k)
    gkk = g * k * k
    term1 = 0.0
    if rho_x > 0:
        term1 += rho_x * math.log(rho_x)
    if rho_y > 0:
        term1 += rho_y * math.log(rho_y)
    term1 *= -(k - 1) / k
    term2 = 0.0
    for ri in (rho_x, rho_y):
        arg = 1.0 - (k - 1) * ri / k
        if arg <= 0:
            return 1e12
        term2 += arg * math.log(arg)
    term3 = 0.0
    for ri in (rho_x, rho_y):
        arg = ri - gkk
        if arg <= 0:
            return 1e12
        term3 += arg * math.log(arg)
    term4 = 1.0 - rho + gkk
    if term4 <= 0:
        return 1e12
    term4 = term4 * math.log(term4)
    term5 = - rho / k * math.log(k)
    term6 = 0.0
    if gkk > 0 and u > 0:
        term6 = gkk * math.log(gkk / u)
    return term1 + term2 + term3 + term4 + term5 + term6

def compute_critical_densities(k, u):
    rho_min = 0.01
    rho_max = 0.99
    step = 0.0005
    delta = 1e-6
    prev_A2 = None
    transitions = []
    rho = rho_min
    while rho <= rho_max:
        if rho <= 0 or rho >= 1:
            rho += step
            continue
        f0 = free_energy(rho / 2.0, rho / 2.0, u, k)
        if f0 >= 1e11:
            rho += step
            continue
        dx = delta
        if rho / 2.0 + dx > rho or rho / 2.0 - dx < 0:
            rho += step
            continue
        f_pert = free_energy(rho / 2.0 + dx, rho / 2.0 - dx, u, k)
        if f_pert >= 1e11:
            rho += step
            continue
        psi = 2 * dx / rho
        if psi == 0:
            rho += step
            continue
        A2 = (f_pert - f0) / (psi * psi)
        if prev_A2 is not None:
            if (prev_A2 < 0 and A2 > 0) or (prev_A2 > 0 and A2 < 0):
                transitions.append(rho - step / 2.0)
        prev_A2 = A2
        rho += step
    if len(transitions) >= 2:
        return (transitions[0], transitions[1])
    else:
        return (None, None)

# find u_c (largest u for which two transitions exist)
u_c = 0.0
for u_cand in (i / 1000.0 for i in range(1, 1000)):
    roots = compute_critical_densities(K, u_cand)
    if roots[0] is not None and roots[1] is not None:
        u_c = u_cand
    else:
        break

outpath = '/app/outputs/phase_diagram_critical_densities.csv'
with open(outpath, 'w') as f:
    f.write('u,rho_c1,rho_c2\n')
    n_points = max(2, int(u_c * 100) + 1)
    for i in range(n_points):
        u_val = i / max(n_points - 1, 1) * u_c
        roots = compute_critical_densities(K, u_val)
        if roots[0] is not None and roots[1] is not None:
            f.write(f'{u_val:.6f},{roots[0]:.6f},{roots[1]:.6f}\n')
PYEOF
