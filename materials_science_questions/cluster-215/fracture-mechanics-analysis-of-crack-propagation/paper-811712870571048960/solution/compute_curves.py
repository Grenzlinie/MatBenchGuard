import numpy as np
from scipy.optimize import bisect

def A_func(alpha):
    return 0.378770*alpha + 0.111251*np.sin(2*alpha) - 0.004847*np.sin(4*alpha) + 0.000241*np.sin(6*alpha)

def B_func(alpha):
    sin_a = np.sin(alpha)
    cos_a = np.cos(alpha)
    part = 0.779825*alpha + 0.190716*np.sin(2*alpha) - 0.008309*np.sin(4*alpha) + 0.000474*np.sin(6*alpha)
    poly = 0.047833 + 0.018857*sin_a**2 + 0.009834*sin_a**4 + 0.005564*sin_a**6 + 0.003158*sin_a**8 + 0.001664*sin_a**10
    return part - sin_a*cos_a*poly

def f_func(alpha):
    sin_a = np.sin(alpha)
    cos_a = np.cos(alpha)
    t = np.sqrt(1 - (11/12)*sin_a**2)
    term1 = 1 - cos_a * t
    term2 = (1 / np.sqrt(132)) * np.log((1 + np.sqrt(11/12)) / (np.sqrt(11/12)*cos_a + t))
    return (term1 + term2) / sin_a**2

def criterion(alpha, Rf_R0, beta, m):
    sin_a = np.sin(alpha)
    cos_a = np.cos(alpha)
    t = np.sqrt(1 - (11/12)*sin_a**2)
    R0_Rf = 1.0 / Rf_R0
    Ln = np.log(Rf_R0)  # negative when Rf<R0
    Ln2 = Ln**2
    
    # non‑strain‑hardening part
    part1 = np.sqrt(3) * sin_a * f_func(alpha) * (1 - Rf_R0 + 2*Ln)
    part2 = 2*np.sqrt(3) * ((Rf_R0 - 1)*A_func(alpha) - B_func(alpha)*Ln)
    part3 = R0_Rf + 1 + Ln - 2*alpha / sin_a
    part4 = m * cos_a * (1 - Rf_R0 + Ln)
    non_beta = part1 + part2 + part3 + part4
    
    # β‑dependent part
    rt3 = np.sqrt(3)
    rt12 = np.sqrt(12)
    beta_t1 = (1/rt3) * (1/sin_a) * (5/np.sqrt(11)) * np.arcsin(np.sqrt(11/12)*sin_a) * (2*Ln + 1 - Rf_R0)
    beta_t2 = (1/11) * t * (2*Ln + 3*(1 - Rf_R0))
    beta_t3 = -13/12 * Ln2
    beta_t4 = (1/rt3) * sin_a * Ln2
    beta_t5 = -rt3/2 * sin_a * (Rf_R0 - 1) * Ln
    beta_t6 = 38/33 * Ln
    beta_t7 = 0.5 * 73/33
    beta_t8 = -35/33 * Rf_R0
    beta_t9 = 0.5 * 13/3 * R0_Rf
    beta_t10 = 0.5 * 7/3 * Rf_R0 * Ln
    beta_t11 = (1/rt3) * np.log((t - 1/rt12) / (1 - 1/rt12)) * Ln
    beta_t12 = -0.5 * (1/rt3) * np.log(cos_a) * (2*Ln + Ln2)
    beta_t13 = 0.5 * (1/rt3) * np.log(sin_a + 1) * Ln2
    beta_t14 = (1/rt3) * (1/sin_a) * np.log(t + (1/rt12)*sin_a) * (2*Ln + 1 - Rf_R0)
    beta_t15 = (1/rt3) * (1/sin_a) * np.log(cos_a) * (Ln2 - Rf_R0*Ln - Ln + Rf_R0 - 1)
    beta_t16 = 2*m / t * ( -0.5 * 11/12 * Ln2 - (1 - 5/12 * Rf_R0)*Ln - 7/12*(1 - Rf_R0) )
    beta_t17 = 5/12 * sin_a**2 * Ln2
    beta_t18 = sin_a**2 * ( (11/12 - 1/3*Rf_R0)*Ln - 7/12*(1 - Rf_R0) )
    beta_part = beta_t1 + beta_t2 + beta_t3 + beta_t4 + beta_t5 + beta_t6 + beta_t7 + beta_t8 + beta_t9 + beta_t10 + beta_t11 + beta_t12 + beta_t13 + beta_t14 + beta_t15 + beta_t16 + beta_t17 + beta_t18
    
    return non_beta + beta * beta_part

def find_r(alpha_rad, beta, m):
    def f(r):
        if r <= 0 or r >= 99.9:
            return np.inf
        Rf_R0 = np.sqrt(1 - r/100.0)
        return criterion(alpha_rad, Rf_R0, beta, m)
    low = 0.1
    high = 90.0
    f_low = f(low)
    f_high = f(high)
    if f_low * f_high > 0:
        # try to shorten interval
        for r0 in np.linspace(0.1, 90, 100):
            if f(r0) * f_low < 0:
                high = r0
                f_high = f(r0)
                break
        else:
            return None
    try:
        return bisect(f, low, high, rtol=1e-6)
    except ValueError:
        return None

# parameter grids
betas = [0.0, 0.05, 0.10, 0.15, 0.20]
ms = [0.0, 0.05, 0.10, 0.15, 0.20]
alphas_deg = np.arange(5.0, 80.5, 0.5)

output_path = "/app/outputs/boundary_curves.csv"
with open(output_path, "w") as f:
    f.write("alpha_deg,reduction_percent,m,beta\n")
    for beta in betas:
        for m in ms:
            for alpha_deg in alphas_deg:
                alpha_rad = np.deg2rad(alpha_deg)
                r_pct = find_r(alpha_rad, beta, m)
                if r_pct is not None:
                    f.write(f"{alpha_deg},{r_pct:.6f},{m},{beta}\n")
