#!/usr/bin/env python3
import math
import csv
import sys
import os

# ========== CuMnPt6 model ==========
A_CuMnPt6 = -6053.0
W_CuMn = -395.0

def U_over_k_CuMnPt6(S1, S3):
    return (3.0/32.0) * (A_CuMnPt6 * S1*S1 + 4.0 * W_CuMn * S3*S3)

def safe_log(x):
    if x <= 0.0:
        return -float('inf')
    return math.log(x)

def phi_over_k_CuMnPt6(S1, S3):
    # formula from the paper, Eq. (3)
    t1 = (1.0 + 3.0*S1 + 4.0*S3) * safe_log(1.0 + 3.0*S1 + 4.0*S3)
    t2 = (1.0 + 3.0*S1 - 4.0*S3) * safe_log(1.0 + 3.0*S1 - 4.0*S3)
    t3 = 12.0 * (1.0 - S1) * safe_log(1.0 - S1)
    t4 = 6.0 * (3.0 + S1) * safe_log(3.0 + S1)
    phi = -(1.0/32.0) * (t1 + t2 + t3 + t4) - (1.0/4.0) * (3.0*math.log(3.0) - math.log(8.0) - 3.0*math.log(4.0))
    return phi

def free_over_k_CuMnPt6(S1, S3, T):
    # F/k = U/k - T * phi/k
    U = U_over_k_CuMnPt6(S1, S3)
    phi = phi_over_k_CuMnPt6(S1, S3)
    return U - T * phi

# ========== MnPt7 model ==========
V_MnPt = -1517.0
W_MnPt = -318.0

def probs_from_S1_S3_MnPt7(S1, S3):
    # x = 1/8 = 0.125
    # S1 = 4*(x - P_C)  => P_C = x - S1/4
    # P_A = (1/4 + 3*S1/2 + S3)/2
    # P_B = (1/4 + 3*S1/2 - S3)/2
    x = 0.125
    PC = x - S1/4.0
    PA = (0.25 + 1.5*S1 + S3) / 2.0
    PB = (0.25 + 1.5*S1 - S3) / 2.0
    return PA, PB, PC

def U_over_k_MnPt7(S1, S3):
    # U/k = (3/32)[ (4 V_MnPt/k - 6 W_MnPt/k) S1**2 + 4 (W_MnPt/k) S3**2 ]
    coeff_S1 = 4.0*V_MnPt - 6.0*W_MnPt
    coeff_S3 = 4.0*W_MnPt
    return (3.0/32.0) * (coeff_S1 * S1*S1 + coeff_S3 * S3*S3)

def phi_over_k_MnPt7(S1, S3):
    PA, PB, PC = probs_from_S1_S3_MnPt7(S1, S3)
    # check probability bounds
    if PA <= 0.0 or PA >= 1.0 or PB <= 0.0 or PB >= 1.0 or PC <= 0.0 or PC >= 1.0:
        return -float('inf')  # invalid, make F large positive
    def ent(p):
        if p <= 0.0 or p >= 1.0:
            return 0.0
        return p * math.log(p) + (1.0 - p) * math.log(1.0 - p)
    # phi/k = -(1/32)[ 4*(ent(PA)+ent(1-PA)? Actually the text: 4 (P_A ln P_A + (1-P_A) ln(1-P_A)) ... for A and B sites, 24 for C sites
    # So: 4 * (P_A ln P_A + (1-P_A) ln(1-P_A)) + 4 * (P_B ln P_B + (1-P_B) ln(1-P_B)) + 24 * (P_C ln P_C + (1-P_C) ln(1-P_C))
    term = 4.0 * (PA * math.log(PA) + (1.0-PA) * math.log(1.0-PA)) + \
           4.0 * (PB * math.log(PB) + (1.0-PB) * math.log(1.0-PB)) + \
           24.0 * (PC * math.log(PC) + (1.0-PC) * math.log(1.0-PC))
    phi = -(1.0/32.0) * term
    return phi

def free_over_k_MnPt7(S1, S3, T):
    U = U_over_k_MnPt7(S1, S3)
    phi = phi_over_k_MnPt7(S1, S3)
    return U - T * phi

# ========== Minimisation via grid search ==========
def grid_search(f, S1_lim, S3_lim, step):
    """
    f(S1, S3) -> float (F/k).  Returns (best_S1, best_S3, best_val).
    S1_lim = (min, max), S3_lim = (min, max).
    """
    best_val = float('inf')
    best = (0.0, 0.0)
    S1_min, S1_max = S1_lim
    S3_min, S3_max = S3_lim
    S1 = S1_min
    while S1 <= S1_max + 1e-12:
        S3 = S3_min
        while S3 <= S3_max + 1e-12:
            val = f(S1, S3)
            if val < best_val:
                best_val = val
                best = (S1, S3)
            S3 += step
        S1 += step
    return best[0], best[1]

def compute_alloy(name, f, T_range, S1_lim, S3_lim, grid_step, out_dir):
    out_path = os.path.join(out_dir, f"{name}_order.csv")
    with open(out_path, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['T', 'S1', 'S3'])
        for T in T_range:
            # for each T do grid search
            S1, S3 = grid_search(lambda s1,s3: f(s1,s3,T), S1_lim, S3_lim, grid_step)
            writer.writerow([T, S1, S3])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python compute_order.py <output_dir>', file=sys.stderr)
        sys.exit(1)
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)

    T_start = 800
    T_end = 1300
    T_step = 10
    T_range = range(T_start, T_end + 1, T_step)

    grid_step = 0.005   # 0.005 gives ~200×200 points per T, fine enough

    # CuMnPt6: S1 in [0, 1], S3 in [0, 1]
    print('Computing CuMnPt6...')
    compute_alloy('CuMnPt6',
                  lambda s1,s3,T: free_over_k_CuMnPt6(s1,s3,T),
                  T_range,
                  (0.0, 1.0),  # S1 limits
                  (0.0, 1.0),  # S3 limits
                  grid_step,
                  out_dir)

    # MnPt7: S1 ∈ [0, 0.5], S3 ∈ [0, 1] (will be clipped by probability constraints)
    print('Computing MnPt7...')
    compute_alloy('MnPt7',
                  lambda s1,s3,T: free_over_k_MnPt7(s1,s3,T),
                  T_range,
                  (0.0, 0.5),  # S1 limits
                  (0.0, 1.0),  # S3 limits
                  grid_step,
                  out_dir)

    print('Done.')
