#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

mkdir -p /app/outputs

# === solve block: hot_spot_results.json ===
python3 << 'PYEOF' > "$OUTDIR/hot_spot_results.json"
import json
import numpy as np

L = 1e-2          # m
w = 5e-4          # m
t1 = 2.5e-4       # m
t2_base = 5e-4    # m
k1 = 163.0
kz = 5.0
q_flux = 1.4e7    # W/m2 (1.4 kW/cm2)
Q = q_flux * w**2
h_conv = 1e4
N_series = 200

def make_eigen(N):
    m = np.arange(1, N+1)
    lam = m * np.pi / L
    beta = np.sqrt(lam[:, None]**2 + lam[None, :]**2)
    return lam, beta

def phi_stable(zeta, k2, t2):
    # stable formula using negative exponentials to avoid overflow
    exp_m2zt2 = np.exp(-2 * zeta * t2)
    exp_m4zt1 = np.exp(-4 * zeta * t1)
    exp_m2zt1 = np.exp(-2 * zeta * t1)
    alpha = (1 - k2/k1) / (1 + k2/k1)
    psi = (zeta + h_conv/k2) / (zeta - h_conv/k2)
    num = alpha * exp_m2zt2 - exp_m4zt1 + psi * (1 - alpha * exp_m2zt1)
    den = alpha * exp_m2zt2 + exp_m4zt1 + psi * (1 + alpha * exp_m2zt1)
    return num / den

def peak_excess_temp(kxy):
    k2_eq = np.sqrt(kxy * kz)
    t2_eq = t2_base / np.sqrt(kz / kxy)
    A0 = Q / L**2 * (t1/k1 + t2_base/kz + 1/h_conv)
    lam, beta = make_eigen(N_series)
    sin_term = np.sin((L+w)/2 * lam) - np.sin((L-w)/2 * lam)
    phi_lam = phi_stable(lam, k2_eq, t2_eq)
    A_m = 2 * Q * sin_term / (L**2 * w * k1 * lam**2 * phi_lam)
    S1 = np.sum(A_m)
    cos_lam_L2 = np.cos(lam * L / 2)
    sin_lam_w2 = np.sin(lam * w / 2)
    factor_m = cos_lam_L2 * sin_lam_w2
    num_mn = 16 * Q * (factor_m[:, None] * factor_m[None, :])
    lam_mn = lam[:, None] * lam[None, :]
    phi_beta = phi_stable(beta, k2_eq, t2_eq)
    denom_mn = L**2 * w**2 * k1 * beta * lam_mn * phi_beta
    A_mn = num_mn / denom_mn
    S2 = np.sum(A_mn)
    return A0 + 2*S1 + S2

def total_resistance(t2_val, kxy, N=200):
    k2_eq = np.sqrt(kxy * kz)
    t2_eq = t2_val / np.sqrt(kz / kxy)
    R1D = t1/(k1*L**2) + t2_val/(kz*L**2) + 1/(h_conv*L**2)
    lam, beta = make_eigen(N)
    sin2 = np.sin(lam * w / 2)**2
    phi_lam = phi_stable(lam, k2_eq, t2_eq)
    S_single = np.sum(sin2 / (lam**3 * phi_lam))
    Rsp1 = (1 / ((w/2)**2 * (L/2)**2 * k1)) * S_single
    sin2_m = sin2[:, None]
    sin2_n = sin2[None, :]
    lam_m2 = lam[:, None]**2
    lam_n2 = lam[None, :]**2
    phi_beta = phi_stable(beta, k2_eq, t2_eq)
    S_double = np.sum(sin2_m * sin2_n / (lam_m2 * lam_n2 * beta * phi_beta))
    Rsp2 = (1 / ((w/2)**4 * (L/2)**2 * k1)) * S_double
    return R1D + Rsp1 + Rsp2

def find_opt_thickness(kxy):
    t_vals = np.linspace(1e-5, 2e-3, 200)
    R_vals = np.array([total_resistance(t, kxy, N=200) for t in t_vals])
    idx_min = np.argmin(R_vals)
    from scipy.optimize import minimize_scalar
    res = minimize_scalar(lambda t: total_resistance(t, kxy, N=200),
                          bounds=(t_vals[max(idx_min-2,0)], t_vals[min(idx_min+2,len(t_vals)-1)]),
                          method='bounded')
    if res.success:
        opt_t = res.x
        opt_R = res.fun
    else:
        opt_t = t_vals[idx_min]
        opt_R = R_vals[idx_min]
    return opt_t * 1e6, opt_R

T5 = peak_excess_temp(5.0)
T350 = peak_excess_temp(350.0)
T1800 = peak_excess_temp(1800.0)
opt_t_um, opt_R = find_opt_thickness(350.0)

result = {
    'kxy5_excess_temp': round(float(T5), 4),
    'kxy350_excess_temp': round(float(T350), 4),
    'kxy1800_excess_temp': round(float(T1800), 4),
    'kxy350_opt_thickness': round(float(opt_t_um), 4),
    'kxy350_total_thermal_resistance': round(float(opt_R), 6)
}
print(json.dumps(result))
PYEOF
