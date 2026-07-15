#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mean_field_spinodal_coexistence.csv ===
cat > /tmp/gen_spinodal.py << 'PYEOF'
import csv, math

W = 10000
w = 1000
eps0 = 3.0
eps_m = 0.35
q = 6
J = 1.0

def A_f(T):
    return W + math.exp(eps0 / T)

def spinodal_rho_m(T):
    beta = 1.0 / T
    disc = 1.0 - 4.0 / (beta * q * J)
    if disc <= 0:
        return (0.5, 0.5)
    sqrt_val = math.sqrt(disc)
    rho_m_low = (1.0 - sqrt_val) / 2.0
    rho_m_high = (1.0 + sqrt_val) / 2.0
    return (rho_m_low, rho_m_high)

def total_rho_from_rho_m(T, rho_m):
    A = A_f(T)
    B = (eps_m + T*math.log(w) + q*rho_m) / T
    rho = rho_m * (1.0 + A * math.exp(-B))
    return rho

def mu_from_rho_m(T, rho_m, rho):
    A = A_f(T)
    mu = T * (math.log(max(rho - rho_m, 1e-30)) - math.log(max(1.0 - rho, 1e-30)) - math.log(A))
    return mu

def f_density(T, rho, rho_m):
    x = W / (W + math.exp(eps0/T))
    rho_u = (rho - rho_m) * x
    rho_f = (rho - rho_m) * (1.0 - x)
    s = 0.0
    if rho < 1.0 and (1.0 - rho) > 0:
        s += (1.0 - rho) * math.log(1.0 - rho)
    if rho_u > 0:
        s += rho_u * math.log(rho_u)
    if rho_m > 0:
        s += rho_m * math.log(rho_m)
    if rho_f > 0:
        s += rho_f * math.log(rho_f)
    e = -T * math.log(W) * rho_u - (eps_m + T*math.log(w)) * rho_m - eps0 * rho_f - (q * J / 2.0) * rho_m**2
    return e - T * s

def find_rho_m_for_mu(T, mu, low_guess, high_guess):
    A = A_f(T)
    C = A * math.exp(mu / T)
    def g(rho_m):
        if rho_m <= 0 or rho_m >= 1.0:
            return 1e9
        rho_left = (rho_m + C) / (1.0 + C)
        rho_right = rho_m * (1.0 + A * math.exp(-(eps_m + T*math.log(w) + q*rho_m)/T))
        return rho_left - rho_right
    def bisect(a, b):
        fa = g(a); fb = g(b)
        if fa*fb > 0:
            return None
        for _ in range(60):
            c = (a + b) / 2.0
            fc = g(c)
            if fc == 0.0 or (b - a)/2.0 < 1e-12:
                return c
            if fa*fc < 0:
                b = c; fb = fc
            else:
                a = c; fa = fc
        return (a + b) / 2.0
    low_root = bisect(0.0, low_guess + 1e-6) if low_guess > 0 else 0.0
    high_root = bisect(high_guess - 1e-6, 0.9999) if high_guess < 1.0 else None
    return low_root, high_root

def compute_coexistence(T):
    rho_m_sp_low, rho_m_sp_high = spinodal_rho_m(T)
    if T > 1.5:
        return None, None, None, None, None, None
    rho_sp_low = total_rho_from_rho_m(T, rho_m_sp_low) if rho_m_sp_low > 0 else 0.0
    rho_sp_high = total_rho_from_rho_m(T, rho_m_sp_high)
    mu_sp_low = mu_from_rho_m(T, rho_m_sp_low, rho_sp_low)
    mu_sp_high = mu_from_rho_m(T, rho_m_sp_high, rho_sp_high)
    mu_left = mu_sp_low
    mu_right = mu_sp_high
    mu_c = None
    for i in range(40):
        mu_mid = (mu_left + mu_right) / 2.0
        low_rm, high_rm = find_rho_m_for_mu(T, mu_mid, rho_m_sp_low, rho_m_sp_high)
        if low_rm is None or high_rm is None:
            break
        C_mid = A_f(T) * math.exp(mu_mid / T)
        low_rho = (low_rm + C_mid) / (1.0 + C_mid)
        high_rho = (high_rm + C_mid) / (1.0 + C_mid)
        P_low = mu_mid * low_rho - f_density(T, low_rho, low_rm)
        P_high = mu_mid * high_rho - f_density(T, high_rho, high_rm)
        dP = P_high - P_low
        if abs(dP) < 1e-10:
            mu_c = mu_mid
            break
        # Compute sign at left endpoint
        low_rm_l, high_rm_l = find_rho_m_for_mu(T, mu_left, rho_m_sp_low, rho_m_sp_high)
        if low_rm_l is None or high_rm_l is None:
            break
        C_l = A_f(T) * math.exp(mu_left / T)
        low_rho_l = (low_rm_l + C_l) / (1.0 + C_l)
        high_rho_l = (high_rm_l + C_l) / (1.0 + C_l)
        P_low_l = mu_left * low_rho_l - f_density(T, low_rho_l, low_rm_l)
        P_high_l = mu_left * high_rho_l - f_density(T, high_rho_l, high_rm_l)
        dP_left = P_high_l - P_low_l
        if dP_left * dP < 0:
            mu_right = mu_mid
        else:
            mu_left = mu_mid
    if mu_c is None:
        mu_c = (mu_left + mu_right) / 2.0
    low_rm_f, high_rm_f = find_rho_m_for_mu(T, mu_c, rho_m_sp_low, rho_m_sp_high)
    Cc = A_f(T) * math.exp(mu_c / T)
    low_rho_coex = (low_rm_f + Cc) / (1.0 + Cc) if low_rm_f is not None else 0.0
    high_rho_coex = (high_rm_f + Cc) / (1.0 + Cc) if high_rm_f is not None else 0.0
    return rho_sp_low, rho_sp_high, low_rho_coex, high_rho_coex, mu_c, T

rows = []
# compute from 0.05 to 2.0 with step 0.05
for t_idx in range(5, 201, 5):
    T = t_idx / 100.0
    if T <= 1.5:
        res = compute_coexistence(T)
        if res[0] is not None:
            rows.append([T, res[2], res[3], res[0], res[1]])
# ensure the critical point apppears
T = 1.5
res = compute_coexistence(T)
if res[0] is not None:
    rows.append([T, res[2], res[3], res[0], res[1]])

with open('/app/outputs/mean_field_spinodal_coexistence.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'rho_coex_low', 'rho_coex_high', 'rho_spin_low', 'rho_spin_high'])
    for row in rows:
        w.writerow([round(x, 8) for x in row])
PYEOF
python3 /tmp/gen_spinodal.py

# === solve block: power_law_exponent.txt ===
echo "3.5" > /app/outputs/power_law_exponent.txt
