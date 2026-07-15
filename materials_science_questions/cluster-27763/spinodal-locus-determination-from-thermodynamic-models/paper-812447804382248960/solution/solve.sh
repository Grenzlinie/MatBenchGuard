#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: percolation_functions.csv ===
cat <<'PYEOF' > /tmp/gen_percolation.py
import csv, math, sys

q = 3
sigma = 5

# critical temperature for q>2
num = (q-1)**((sigma-1)/(sigma+1)) - 1.0
denom = q - 2
theta_c = num / denom

print(f"theta_c = {theta_c}", file=sys.stderr)

def potts_probs(theta):
    if theta <= 0.0:
        return 1.0, 1.0
    if theta >= theta_c:
        p1 = 1.0 / q
        p11 = 1.0 / (1.0 + (q-1)*theta)
        return p1, p11
    a = 1.0 / theta
    def g(r):
        f = (a*r + q - 1) / (r + a + q - 2)
        return r - f**sigma
    low = 1.000001
    high = max(2.0, a**sigma * 2)
    while g(high) <= 0:
        high *= 2
    for _ in range(200):
        mid = (low + high) / 2
        if g(mid) <= 0:
            low = mid
        else:
            high = mid
    r = (low + high) / 2
    p1 = r / (r + q - 1)
    p11 = a * r / (a * r + q - 1)
    return p1, p11

def percolation(theta):
    p1, p11 = potts_probs(theta)
    p_b = 1.0 - theta
    c = p_b * p11
    sigma_c = sigma * c
    if sigma_c <= 1.0:
        Q = 1.0
        thresh = 'critical' if abs(sigma_c - 1.0) < 1e-12 else 'subcritical'
    else:
        def h(Q):
            return Q - (1 - c) - c * (Q**sigma)
        points = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
        vals = [h(p) for p in points]
        a_, b_ = None, None
        for i in range(len(points)-1):
            if vals[i] * vals[i+1] < 0:
                a_ = points[i]
                b_ = points[i+1]
                break
        if a_ is None:
            # fallback – simple iteration from 0.5
            Q_est = 0.5
            for _ in range(200):
                f_val = Q_est - (1-c) - c * Q_est**sigma
                df = 1 - sigma * c * Q_est**(sigma-1)
                Q_new = Q_est - f_val/df
                if abs(Q_new - Q_est) < 1e-14:
                    Q_est = Q_new
                    break
                Q_est = Q_new
            Q = Q_est
        else:
            lo, hi = a_, b_
            for _ in range(200):
                mid = (lo + hi) / 2
                if h(mid) * h(lo) > 0:
                    lo = mid
                else:
                    hi = mid
            Q = (lo + hi) / 2
        thresh = 'supercritical'
    # percolative observables
    N = p1 * Q**(sigma+1) - (sigma+1)/2 * p1 * p_b * p11 * Q**(2*sigma)
    P = 1.0 - Q**(sigma+1)
    denom = 1.0 - sigma * p_b * p11 * Q**(sigma-1)
    if abs(denom) < 1e-15:
        S = float('inf')
    else:
        S = (1.0 + p_b * p11 * Q**(sigma-1)) / denom
    return p1, p11, p_b, Q, N, P, S, thresh

# ---- build theta grid ----
theta_vals = [0.0]
# main grid from 0 to 1
theta_vals.extend([round(i/200.0, 12) for i in range(1, 200)])   # 0.005 .. 0.995
# dense near theta_c
margin = 0.02
theta_vals.extend([round(theta_c - margin + i*0.001, 12) for i in range(int(2*margin/0.001))])
theta_vals.extend([theta_c, theta_c + 1e-12, theta_c + 0.0001])
theta_vals.append(1.0)

theta_vals = sorted(set(round(t, 12) for t in theta_vals))

# ---- write CSV ----
with open('/app/outputs/percolation_functions.csv', 'w', newline='') as f:
    fieldnames = ['theta', 'p1', 'p11', 'p_b', 'Q', 'N', 'P', 'S', 'threshold_flag']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for theta in theta_vals:
        p1, p11, p_b, Q, N, P, S, thresh = percolation(theta)
        row = {
            'theta': theta,
            'p1': p1,
            'p11': p11,
            'p_b': p_b,
            'Q': Q,
            'N': N,
            'P': P,
            'S': S,
            'threshold_flag': thresh
        }
        writer.writerow(row)
PYEOF
python3 /tmp/gen_percolation.py
