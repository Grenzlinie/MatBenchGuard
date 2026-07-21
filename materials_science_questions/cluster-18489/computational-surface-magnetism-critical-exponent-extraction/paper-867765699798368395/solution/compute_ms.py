#!/usr/bin/env python3
import sys, math, csv, json

R = 2.0

# Critical couplings
lc_tm = R**(-0.5)          # r^{-1/2}
lc_pd = R**(-2/3)          # r^{-2/3}

# λ/λ_c values to evaluate
ratios = [0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1]

def sigma_tm(x):
    """Thue-Morse series Σ(x) via recursion (3.9). x in (0,1)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return float('inf')
    # Use recursion with a depth guard; for small enough x the σ(x²) term is negligible.
    def rec(xx, depth):
        if depth > 50:
            return xx * xx / (1 - xx * xx)
        if xx < 1e-12:
            return xx * xx / (1 - xx * xx)
        x2 = xx * xx
        sig_x2 = rec(x2, depth + 1)
        return xx * xx / (1 - xx * xx) + (1.0 / xx - 1.0) * sig_x2
    return rec(x, 0)

def ms_tm(u):
    """Compute surface magnetization for Thue-Morse. u = λ_c/λ."""
    if u >= 1:
        return 0.0
    u2 = u * u
    u4 = u2 * u2
    x = u4
    # Eq. (3.8) S = [1 + r u²] / (1 - u⁴) + (r⁻¹ - r) λ²/λ_c² Σ(x)
    S = (1.0 + R * u2) / (1.0 - u4) + (1.0/R - R) * (1.0 / u2) * sigma_tm(x)
    return 1.0 / math.sqrt(S)

def S_pd(u, lam_c):
    """Infinite product (4.7) for period-doubling."""
    prod = 1.0
    inv_lc = 1.0 / lam_c
    k = 1
    while True:
        exp1 = 2 ** (2 * k - 1)
        exp2 = 2 ** (2 * k)
        term1 = lam_c * (u ** exp1)
        term2 = inv_lc * (u ** exp2)
        if term1 < 1e-15 and term2 < 1e-15:
            break
        prod *= (1.0 + term1) * (1.0 + term2)
        k += 1
        if k > 100:
            break
    return prod

def ms_pd(u, lam_c):
    """Surface magnetization for period-doubling."""
    if u >= 1:
        return 0.0
    S = S_pd(u, lam_c)
    return 1.0 / math.sqrt(S)

def compute_ms():
    rows = []
    for ratio in ratios:
        lam_tm = lc_tm * ratio
        lam_pd = lc_pd * ratio
        u_tm = 1.0 / ratio   # λ_c / λ
        u_pd = u_tm
        ms_val_tm = ms_tm(u_tm)
        ms_val_pd = ms_pd(u_pd, lc_pd)
        rows.append(('thue_morse', R, ratio, ms_val_tm))
        rows.append(('period_doubling', R, ratio, ms_val_pd))
    return rows

def fit_beta(rows, seq_name):
    """Fit m_s = A * t^{β_s} on the three smallest positive t."""
    # t = 1 - (λ_c/λ)² = 1 - u², where u = 1/ratio
    data = []
    for row in rows:
        if row[0] == seq_name and row[2] > 1.0:
            ratio = row[2]
            ms = row[3]
            u = 1.0 / ratio
            t = 1.0 - u * u
            if t > 0 and ms > 0:
                data.append((math.log(t), math.log(ms)))
    # Sort by t ascending
    data.sort(key=lambda xy: xy[0])
    # Use three smallest
    if len(data) < 3:
        raise ValueError(f"Not enough points for fit for {seq_name}")
    data = data[:3]
    n = len(data)
    sum_x = sum(x for x, y in data)
    sum_y = sum(y for x, y in data)
    sum_xy = sum(x * y for x, y in data)
    sum_x2 = sum(x * x for x, y in data)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    return slope  # β_s

def output_csv():
    rows = compute_ms()
    with open('/app/outputs/surface_magnetization_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sequence', 'r', 'lambda_over_lambda_c', 'ms'])
        writer.writerows(rows)

def output_json():
    rows = compute_ms()
    beta_tm_fitted = fit_beta(rows, 'thue_morse')
    beta_pd_fitted = fit_beta(rows, 'period_doubling')
    # Also theoretical values (used only for reference, but output fitted)
    res = {
        'thue_morse_beta_s': beta_tm_fitted,
        'period_doubling_beta_s': beta_pd_fitted
    }
    with open('/app/outputs/critical_exponents.json', 'w') as f:
        json.dump(res, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: compute_ms.py [csv|json]')
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'csv':
        output_csv()
    elif cmd == 'json':
        output_json()
    else:
        print('Invalid command')
        sys.exit(1)
