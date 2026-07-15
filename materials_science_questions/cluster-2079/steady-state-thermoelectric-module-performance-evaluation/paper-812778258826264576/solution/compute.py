import csv
import math
import sys

# Constants
L = 4e-3           # m
A0 = 16e-6          # m^2
mu_n = 0.5
mu_p = 0.5
T_low = 300.0

# material property functions (T in K)
def k_n1(T):
    return 0.6586 + 329.63/T + 22145/T**2

def alpha_n1(T):  # returns V/K
    val = 173.26 - 3.8229*T + 0.011679*T**2 - 1.5584e-5*T**3 + 7.6695e-9*T**4
    return val * 1e-6

def sigma_n1(T):
    return 1462 - 10.419*T + 0.031315*T**2 - 4.029e-5*T**3 + 1.9034e-8*T**4

def k_p1(T):
    return 0.56959 + 550.66/T - 47483/T**2

def alpha_p1(T):
    val = 1450 - 10.36*T + 0.03123*T**2 - 4.038e-5*T**3 + 1.903e-8*T**4
    return val * 1e-6

def sigma_p1(T):
    return 179.02 + 12.336*T - 0.042167*T**2 + 5.129e-5*T**3 - 2.1435e-8*T**4

def k_n2(T):
    return -4.6205 + 9.9277e-3*T + 833.7/T + 235636/T**2

def alpha_n2(T):
    val = 443.49 - 4.5121*T + 9.4424e-3*T**2 - 5.8362e-6*T**3
    return val * 1e-6

def sigma_n2(T):
    return -2139.4 + 2.5778*T + math.exp(12.795 - 0.89098*math.log(T))

def k_p2(T):
    return -1.8067 + 5.729e-3*T - 64.639/T + 1.3395e5/T**2

def alpha_p2(T):
    val = -188.2 + 2.2411*T - 3.0075e-3*T**2 + 2.4914e-7*T**3
    return val * 1e-6

def sigma_p2(T):
    return -473.1 + 0.86507*T + math.exp(16.637 - 1.6942*math.log(T))

# reference constants
T_ref = 273.0
sigma_ref = sigma_n1(T_ref)
k_ref = k_n1(T_ref)
R0 = L / (sigma_ref * A0)
K0 = k_ref * A0 / L

def material_set_segmented():
    return {
        'k_n1': k_n1, 'k_n2': k_n2, 'k_p1': k_p1, 'k_p2': k_p2,
        'alpha_n1': alpha_n1, 'alpha_n2': alpha_n2, 'alpha_p1': alpha_p1, 'alpha_p2': alpha_p2,
        'sigma_n1': sigma_n1, 'sigma_n2': sigma_n2, 'sigma_p1': sigma_p1, 'sigma_p2': sigma_p2
    }

def material_set_unsegmented(mat):
    if mat == 'mat1':
        return {
            'k_n1': k_n1, 'k_n2': k_n1, 'k_p1': k_p1, 'k_p2': k_p1,
            'alpha_n1': alpha_n1, 'alpha_n2': alpha_n1, 'alpha_p1': alpha_p1, 'alpha_p2': alpha_p1,
            'sigma_n1': sigma_n1, 'sigma_n2': sigma_n1, 'sigma_p1': sigma_p1, 'sigma_p2': sigma_p1
        }
    else:
        return {
            'k_n1': k_n2, 'k_n2': k_n2, 'k_p1': k_p2, 'k_p2': k_p2,
            'alpha_n1': alpha_n2, 'alpha_n2': alpha_n2, 'alpha_p1': alpha_p2, 'alpha_p2': alpha_p2,
            'sigma_n1': sigma_n2, 'sigma_n2': sigma_n2, 'sigma_p1': sigma_p2, 'sigma_p2': sigma_p2
        }

def compute_segmented(theta, a, R_L_R0, mat_set):
    T_high = T_low / theta
    T_int_n = (T_high + T_low) / 2
    T_int_p = (T_high + T_low) / 2
    tol = 1e-6
    max_iter = 50
    for _ in range(max_iter):
        T_n1_avg = (T_high + T_int_n) / 2
        T_n2_avg = (T_int_n + T_low) / 2
        T_p1_avg = (T_high + T_int_p) / 2
        T_p2_avg = (T_int_p + T_low) / 2
        kn1 = mat_set['k_n1'](T_n1_avg)
        kn2 = mat_set['k_n2'](T_n2_avg)
        kp1 = mat_set['k_p1'](T_p1_avg)
        kp2 = mat_set['k_p2'](T_p2_avg)
        # effective n-leg conductivity
        if abs(a) < 1e-12:
            k_n_eff = 1.0 / (mu_n/kn1 + (1-mu_n)/kn2)
        else:
            ea = math.exp(a)
            eam = math.exp(a*mu_n)
            denom = (1 - math.exp(-a)) * ((eam - 1)/kn1 + (ea - eam)/kn2)
            k_n_eff = a**2 / denom
        # p-leg effective conductivity (flat)
        k_p_eff = 1.0 / (mu_p/kp1 + (1-mu_p)/kp2)
        DT = T_high - T_low
        if abs(a) < 1e-12:
            DT_n1 = (k_n_eff / kn1) * mu_n * DT
            DT_n2 = (k_n_eff / kn2) * (1 - mu_n) * DT
        else:
            f1 = (1 - math.exp(-a)) * (math.exp(a*mu_n) - 1) / a**2
            f2 = (1 - math.exp(-a)) * (math.exp(a) - math.exp(a*mu_n)) / a**2
            DT_n1 = (k_n_eff / kn1) * f1 * DT
            DT_n2 = (k_n_eff / kn2) * f2 * DT
        DT_p1 = (k_p_eff / kp1) * mu_p * DT
        DT_p2 = (k_p_eff / kp2) * (1 - mu_p) * DT
        T_int_n_new = T_high - DT_n1
        T_int_p_new = T_high - DT_p1
        if max(abs(T_int_n_new - T_int_n), abs(T_int_p_new - T_int_p)) < tol:
            T_int_n = T_int_n_new
            T_int_p = T_int_p_new
            break
        T_int_n = T_int_n_new
        T_int_p = T_int_p_new
    # after convergence
    ap1 = mat_set['alpha_p1'](T_p1_avg)
    ap2 = mat_set['alpha_p2'](T_p2_avg)
    an1 = mat_set['alpha_n1'](T_n1_avg)
    an2 = mat_set['alpha_n2'](T_n2_avg)
    alpha_p_eff = ap1 * (k_p_eff/kp1) * mu_p + ap2 * (k_p_eff/kp2) * (1 - mu_p)
    if abs(a) < 1e-12:
        alpha_n_eff = an1 * (k_n_eff/kn1) * mu_n + an2 * (k_n_eff/kn2) * (1 - mu_n)
    else:
        f1 = (1 - math.exp(-a)) * (math.exp(a*mu_n) - 1) / a**2
        f2 = (1 - math.exp(-a)) * (math.exp(a) - math.exp(a*mu_n)) / a**2
        alpha_n_eff = an1 * (k_n_eff/kn1) * f1 + an2 * (k_n_eff/kn2) * f2
    alpha_eff = alpha_p_eff - alpha_n_eff
    alpha_eff1 = ap1 - an1
    # resistances
    sp1 = mat_set['sigma_p1'](T_p1_avg)
    sp2 = mat_set['sigma_p2'](T_p2_avg)
    sn1 = mat_set['sigma_n1'](T_n1_avg)
    sn2 = mat_set['sigma_n2'](T_n2_avg)
    if abs(a) < 1e-12:
        Rn = L/(sn1*A0)*mu_n + L/(sn2*A0)*(1-mu_n)
    else:
        Rn = ((1 - math.exp(-a)) * L / (a**2 * A0)) * ((math.exp(a*mu_n)-1)/sn1 + (math.exp(a)-math.exp(a*mu_n))/sn2)
    Rp = (1/A0) * (L*mu_p/sp1 + L*(1-mu_p)/sp2)
    R_TEG = Rn + Rp
    # R_{n,1}+R_{p,1}
    if abs(a) < 1e-12:
        Rn1 = L*mu_n/(sn1*A0)
    else:
        Rn1 = ((1 - math.exp(-a)) * L / (a**2 * A0)) * ((math.exp(a*mu_n)-1)/sn1)
    Rp1 = (L*mu_p)/(sp1*A0)
    Rn1_Rp1_ratio = (Rn1 + Rp1) / R0
    K_eff = (k_n_eff + k_p_eff) * A0 / L
    ZT_avg = (alpha_eff**2 * T_high * (1+theta)) / (2 * R_TEG * K_eff)
    R_L = R_L_R0 * R0
    R_TEG_R0 = R_TEG / R0
    num_eta = 2 * ZT_avg * (1 - theta) * R_L_R0 * R_TEG_R0
    denom_eta = (2 * (alpha_eff1/alpha_eff) * (R_TEG_R0 + R_L_R0) * R_TEG_R0 +
                 (1+theta) * (R_TEG_R0 + R_L_R0)**2 -
                 2 * ZT_avg * (1 - theta) +
                 R_TEG_R0 * Rn1_Rp1_ratio)
    eta = num_eta / denom_eta if denom_eta != 0 else 0.0
    I = alpha_eff * (T_high - T_low) / (R_TEG + R_L)
    W = I**2 * R_L
    return eta, W, I

def compute_unsegmented(theta, a, R_L_R0, mat):
    mat_set = material_set_unsegmented(mat)
    eta, W, I = compute_segmented(theta, a, R_L_R0, mat_set)
    return W, I

# Main
outdir = sys.argv[1]
a_vals = [round(-3.0 + i*0.5, 2) for i in range(13)]  # -3 to 3 step 0.5
thetas = [0.45, 0.55]
RL_R0_list = [2, 4, 6, 8]

eff_rows = []
pow_rows = []
cur_rows = []
wr_rows = []

for theta in thetas:
    for a in a_vals:
        seg_data = {}
        for rl in RL_R0_list:
            eta, W, I = compute_segmented(theta, a, rl, material_set_segmented())
            seg_data[rl] = (eta, W, I)
            eff_rows.append((theta, rl, a, eta*100))
            pow_rows.append((theta, rl, a, W))
            cur_rows.append((theta, rl, a, I))
        W_max = max(seg_data[rl][1] for rl in RL_R0_list)
        for rl in RL_R0_list:
            W1, _ = compute_unsegmented(theta, a, rl, 'mat1')
            W2, _ = compute_unsegmented(theta, a, rl, 'mat2')
            xi1 = W1 / W_max if W_max > 0 else 0.0
            xi2 = W2 / W_max if W_max > 0 else 0.0
            wr_rows.append((theta, rl, a, xi1, xi2))

with open(f"{outdir}/efficiency_vs_a.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["theta", "RL_R0", "a", "efficiency_percent"])
    w.writerows(eff_rows)

with open(f"{outdir}/power_vs_a.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["theta", "RL_R0", "a", "power_W"])
    w.writerows(pow_rows)

with open(f"{outdir}/current_vs_a.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["theta", "RL_R0", "a", "current_A"])
    w.writerows(cur_rows)

with open(f"{outdir}/work_ratio_vs_a.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["theta", "RL_R0", "a", "xi1", "xi2"])
    w.writerows(wr_rows)
