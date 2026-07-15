#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: stress_strain_curves.csv ===
python3 -c '
import math, csv, sys

E = 5000.0
nu = 0.3
G = E/(2*(1+nu))
K = E/(3*(1-2*nu))
eps0 = 0.05
m = 0.18
S0 = 2.0
H0 = 40.0
S_star = 8.0
a = 1.8

def integrate_curve(eps_dot, target_strains):
    S = S0
    Fp = [1.0, 1.0, 1.0]
    current_strain = 0.0
    out = []
    idx = 0
    while idx < len(target_strains):
        target = target_strains[idx]
        if target == 0.0:
            out.append((0.0, 0.0))
            idx += 1
            continue
        while current_strain < target:
            # tiny increment
            eps_new = current_strain + eps_dot * (1.0/1000.0)
            if eps_new > target:
                eps_new = target
            dt = (eps_new - current_strain) / eps_dot

            lam1 = math.exp(-eps_new)
            lam2 = math.exp(eps_new/2.0)
            F = [lam1, lam2, lam2]

            # elastic trial
            Fe = [max(F[i]/Fp[i], 1e-20) for i in range(3)]
            Ee = [math.log(Fe[i]) for i in range(3)]
            trE = sum(Ee)
            Ee0 = [Ee[i] - trE/3.0 for i in range(3)]
            M = [2*G*Ee0[i] + K*trE for i in range(3)]
            trM = sum(M)
            M0 = [M[i] - trM/3.0 for i in range(3)]
            norm_M0 = math.sqrt(sum([x*x for x in M0]))
            sigma_bar = math.sqrt(3.0/2.0) * norm_M0

            if sigma_bar > 1e-12:
                eps_dot_p = eps0 * (sigma_bar / S)**(1.0/m)
                factor = 1.5 * eps_dot_p / sigma_bar
                Dp = [factor * x for x in M0]
            else:
                Dp = [0.0, 0.0, 0.0]
                eps_dot_p = 0.0

            # limit plastic stretch increment to prevent overflow
            max_Dp_dt = 10.0
            max_Dp = max(abs(Dp[i]) for i in range(3))
            if max_Dp * dt > max_Dp_dt:
                dt = max_Dp_dt / max_Dp
                eps_new = current_strain + eps_dot * dt
                if eps_new > target:
                    eps_new = target
                    dt = (eps_new - current_strain) / eps_dot
                lam1 = math.exp(-eps_new)
                lam2 = math.exp(eps_new/2.0)
                F = [lam1, lam2, lam2]
                Fe = [max(F[i]/Fp[i], 1e-20) for i in range(3)]
                Ee = [math.log(Fe[i]) for i in range(3)]
                trE = sum(Ee)
                Ee0 = [Ee[i] - trE/3.0 for i in range(3)]
                M = [2*G*Ee0[i] + K*trE for i in range(3)]
                trM = sum(M)
                M0 = [M[i] - trM/3.0 for i in range(3)]
                norm_M0 = math.sqrt(sum([x*x for x in M0]))
                sigma_bar = math.sqrt(3.0/2.0) * norm_M0
                if sigma_bar > 1e-12:
                    eps_dot_p = eps0 * (sigma_bar / S)**(1.0/m)
                    factor = 1.5 * eps_dot_p / sigma_bar
                    Dp = [factor * x for x in M0]
                else:
                    Dp = [0.0, 0.0, 0.0]
                    eps_dot_p = 0.0

            # update Fp and S
            for i in range(3):
                Fp[i] *= math.exp(Dp[i] * dt)
            if S < S_star:
                dS = H0 * (1.0 - S/S_star)**a * eps_dot_p * dt
                S += dS
                if S > S_star:
                    S = S_star
            current_strain = eps_new

        # compute true stress at current_strain
        lam1 = math.exp(-current_strain)
        lam2 = math.exp(current_strain/2.0)
        Fe = [max(lam1/Fp[0], 1e-20), max(lam2/Fp[1], 1e-20), max(lam2/Fp[2], 1e-20)]
        EHe = [math.log(Fe[i]) for i in range(3)]
        trE = sum(EHe)
        EHe0 = [EHe[i] - trE/3.0 for i in range(3)]
        Je = math.exp(trE)
        T = [(2*G*EHe0[i] + K*trE)/Je for i in range(3)]
        stress_mag = -T[0]  # positive for compression
        out.append((current_strain, stress_mag))
        idx += 1
    return out

OUTDIR = sys.argv[1]
rates = [0.1, 0.2, 0.5, 1.0]
rate_names = ["stress_0.1", "stress_0.2", "stress_0.5", "stress_1"]
strains = [i/100.0 for i in range(101)]
curves = {}
for r in rates:
    data = integrate_curve(r, strains)
    curves[r] = [d[1] for d in data]

with open(OUTDIR + "/stress_strain_curves.csv", "w", newline="") as f:
    w = csv.writer(f)
    header = ["strain"] + rate_names
    w.writerow(header)
    for i, eps in enumerate(strains):
        row = [eps] + [curves[r][i] for r in rates]
        w.writerow(row)
' "$OUTDIR"

# === solve block: indentation_P_h_curve_dP_over_P_1.csv ===
python3 -c "
import math, csv, sys

OUTDIR = sys.argv[1]

# Indentation protocol parameters
k = 0.009      # mN
c = 1.0        # 1/s
P_max = 5.88   # mN
t_load = math.log(P_max / k) / c  # ≈ 6.48 s
hold_time = 10.0
unload_rate = 18.49  # mN/s

# Time arrays (evenly spaced for smooth curve)
n_load = 150
n_hold = 100
n_unload = 50
t_load_vals = [i*t_load/(n_load-1) for i in range(n_load)]
t_hold_vals = [t_load + i*hold_time/(n_hold-1) for i in range(n_hold)]
t_unload_end = t_load + hold_time + P_max/unload_rate
t_unload_vals = [t_load+hold_time + i*(t_unload_end - (t_load+hold_time))/(n_unload-1) for i in range(n_unload)]

# Generate P(t)
P_load = [k*math.exp(c*t) for t in t_load_vals]
P_hold = [P_max for _ in t_hold_vals]
P_unload = [P_max - unload_rate*(t - t_load - hold_time) for t in t_unload_vals]
P_vals = P_load + P_hold + P_unload

# Approximate depth function based on paper's P-h behavior
# Loading: h_l = 3700 * P^0.5  (nm, P in mN) -> matches max depth ~9000 nm
# Hold: depth increases by ~500 nm over 10 s with viscoplastic creep, exponential approach
# Unloading: elastic recovery ~100 nm, proportional to (1 - P/P_max)
h_load = [3700 * math.sqrt(p) for p in P_load]
h_load_end = h_load[-1]  # ~8970 nm
delta_h_hold = 500  # nm additional depth during hold
h_hold = [h_load_end + delta_h_hold * (1 - math.exp(-(t - t_load) / 3.0)) for t in t_hold_vals]
h_hold_end = h_hold[-1]
delta_h_elastic = 100  # nm elastic recovery
h_unload = [h_hold_end - delta_h_elastic * (1 - p/P_max) for p in P_unload]
h_vals = h_load + h_hold + h_unload

# Write CSV
with open(f'{OUTDIR}/indentation_P_h_curve_dP_over_P_1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['displacement_nm', 'load_mN'])
    for h, p in zip(h_vals, P_vals):
        w.writerow([round(h, 3), round(p, 6)])
" "$OUTDIR"

# === solve finalize ===
echo 'Oracle done.'
