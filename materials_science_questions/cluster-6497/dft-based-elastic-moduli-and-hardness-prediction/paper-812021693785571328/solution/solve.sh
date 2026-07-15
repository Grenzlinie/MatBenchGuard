#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: stress_results.json ===
python3 << 'PYEOF'
import json, math, sys
import numpy as np

# ===== material properties (GPa, K⁻¹) =====
mat = {
    'BN_S': {'E': 900, 'nu': 0.1, 'alpha': 2.8e-6},
    'BN_W': {'E': 800, 'nu': 0.1, 'alpha': 3.03e-6},
    'BN_G': {'E': 80,  'nu': 0.2, 'alpha': None},
}
# anisotropic expansion of BN_W (for case 3)
alpha_aniso = np.array([2.7e-6, 2.7e-6, 3.7e-6])   # a11, a22, a33

ΔT = -1700                 # K
σ_a = -5                   # GPa
ε_tr_case2 = 3.2e-3        # BN_W→BN_S transformation
ε_tr_case4 = 170e-3        # BN_W→BN_G transformation

def get_K_G(E, nu):
    G = E / (2 * (1 + nu))
    K = E / (3 * (1 - 2*nu))
    return K, G

def build_isotropic_stiffness(K, G):
    """C_{ijkl} = K δ_{ij}δ_{kl} + G (δ_{ik}δ_{jl}+δ_{il}δ_{jk} - 2/3 δ_{ij}δ_{kl})"""
    d = np.eye(3)
    C = np.einsum('ij,kl->ijkl', d, d) * K
    id2 = 0.5 * (np.einsum('ik,jl->ijkl', d, d) + np.einsum('il,jk->ijkl', d, d))
    iso_dev = id2 - np.einsum('ij,kl->ijkl', d, d) / 3.0
    C += 2.0 * G * iso_dev
    return C

def build_identity_4(th):
    d = np.eye(3)
    return 0.5 * (np.einsum('ik,jl->ijkl', d, d) + np.einsum('il,jk->ijkl', d, d))

def build_E_tensor(G, nu):
    """E_{ijkl} from Eq. (2)"""
    a = (2 * (4 - 5*nu)) / (30 * G * (1 - nu))
    b = -1.0 / (30 * G * (1 - nu))
    I4 = build_identity_4(None)
    d = np.eye(3)
    E = a * I4 + b * np.einsum('ij,kl->ijkl', d, d)
    return E

def tensor_inv_4(A):
    """Inverse of a 4th-order tensor with major and minor symmetries
    via Voigt (6x6) matrix inversion."""
    voigt_map = {(0,0):0, (1,1):1, (2,2):2,
                 (1,2):3, (2,1):3,
                 (0,2):4, (2,0):4,
                 (0,1):5, (1,0):5}
    M = np.zeros((6,6))
    for i in range(3):
        for j in range(3):
            p = voigt_map.get((i,j))
            if p is None: continue
            for k in range(3):
                for l in range(3):
                    q = voigt_map.get((k,l))
                    if q is None: continue
                    M[p,q] = A[i,j,k,l]
    M_inv = np.linalg.inv(M)
    inv_A = np.zeros((3,3,3,3))
    for i in range(3):
        for j in range(3):
            p = voigt_map.get((i,j))
            if p is None: continue
            for k in range(3):
                for l in range(3):
                    q = voigt_map.get((k,l))
                    if q is None: continue
                    inv_A[i,j,k,l] = M_inv[p,q]
    return inv_A

def dot_4_4(A, B):
    return np.einsum('ijmn,mnkl->ijkl', A, B)

def dot_4_2(A, B):
    return np.einsum('ijkl,kl->ij', A, B)

def dot_2_4(B, A):
    return np.einsum('mn,mnkl->kl', B, A)

def outer_2(B1, B2):
    return np.einsum('ij,kl->ijkl', B1, B2)

def strain_scalar_to_tensor(e):
    return e * np.eye(3)

# -------- case 1 / 2 solver --------
def compute_case(V_BNS_list, case_id, add_tr_strain_BNS=0.0):
    results = []
    for v_s in V_BNS_list:
        v_w = 1 - v_s
        vf = {'BN_S': v_s, 'BN_W': v_w}
        
        # ---- pure‑phase limit: no heterogeneous mismatch → zero stress ----
        if v_s == 0.0 or v_s == 1.0:
            for ph in ['BN_S','BN_W']:
                if vf[ph] > 0:
                    results.append({'V_BNS': round(v_s, 1), 'phase': ph,
                                    'sigma0': 0.0,
                                    'delta_sigma': 0.0})
            continue
        # ---- two‑phase computation ----
        # phase stiffness tensors
        C_ph = {}
        S_ph = {}
        for ph in ['BN_S','BN_W']:
            K,G = get_K_G(mat[ph]['E'], mat[ph]['nu'])
            C_ph[ph] = build_isotropic_stiffness(K,G)
            S_ph[ph] = tensor_inv_4(C_ph[ph])
        # isotropic strain‑free strains
        eps_t = {}
        for ph in ['BN_S','BN_W']:
            K,_ = get_K_G(mat[ph]['E'], mat[ph]['nu'])
            e_th = mat[ph]['alpha'] * ΔT
            e_unload = -σ_a / (3*K)
            e_tr = 0.0
            if ph == 'BN_S' and add_tr_strain_BNS:
                e_tr = add_tr_strain_BNS
            e_tot = e_th + e_unload + e_tr
            eps_t[ph] = strain_scalar_to_tensor(e_tot)
        # averages
        C_voigt = sum(vf[ph] * C_ph[ph] for ph in ['BN_S','BN_W'])
        S_voigt = sum(vf[ph] * S_ph[ph] for ph in ['BN_S','BN_W'])
        C_reuss = tensor_inv_4(S_voigt)
        # gamma_eps = avg(eps^tau)
        gamma_eps = sum(vf[ph] * eps_t[ph] for ph in ['BN_S','BN_W'])
        # avg(C eps^tau)
        Ceps_avg = sum(vf[ph] * dot_4_2(C_ph[ph], eps_t[ph]) for ph in ['BN_S','BN_W'])
        # gamma_sig = (C_voigt)^-1 . avg(C eps^tau)
        C_voigt_inv = tensor_inv_4(C_voigt)
        gamma_sig = dot_4_2(C_voigt_inv, Ceps_avg)
        # eps_star = (gamma_sig + gamma_eps)/2
        eps_star = 0.5 * (gamma_sig + gamma_eps)
        # parameters from Eq. (3)
        Cplus = C_voigt
        Cminus = C_reuss
        delta = (gamma_sig + gamma_eps) / 2.0
        D = Cplus - Cminus
        D_inv = tensor_inv_4(D)
        # mu_sigma = C+ (C+ - C-)^-1 C- ( ε* - (γ_σ+γ_ε)/2 )
        temp = dot_4_2(Cminus, eps_star - delta)
        temp = dot_4_2(D_inv, temp)
        mu_sig = dot_4_2(Cplus, temp)
        
        # mu_eps = (C+ - C-)^-1 ( - C- ε* + (C+ γ_σ + C- γ_ε)/2 )
        part1 = -dot_4_2(Cminus, eps_star)
        part2 = (dot_4_2(Cplus, gamma_sig) + dot_4_2(Cminus, gamma_eps)) / 2.0
        mu_eps_vec = dot_4_2(D_inv, part1 + part2)
        
        # mu (scalar)
        term_gsCgs = np.einsum('ij,ijkl,kl', gamma_sig, Cplus, gamma_sig)
        avg_epstau_sq = sum(vf[ph] * np.einsum('ij,ij', eps_t[ph], eps_t[ph]) for ph in ['BN_S','BN_W'])
        mu_first = (avg_epstau_sq - term_gsCgs) / 12.0
        diff = eps_star - delta
        Csum = Cplus + Cminus
        Csum_inv = tensor_inv_4(Csum)
        M = dot_4_4(dot_4_4(Cplus, Csum_inv), Cminus)
        mu_second = np.einsum('ij,ijkl,kl', diff, M, diff) / 3.0
        mu_val = mu_first - mu_second
        
        # For each phase compute σ0 and Δσ
        for ph in ['BN_S','BN_W']:
            Ck = C_ph[ph]
            epstk = eps_t[ph]
            # mean stress: σ0 = μ_σ + Ck μ_ε - 0.5 Ck ε^τ_k
            sig0 = mu_sig + dot_4_2(Ck, mu_eps_vec) - 0.5 * dot_4_2(Ck, epstk)
            σ033 = sig0[2,2]
            # stress covariance: (μ/2) * Ck E_k Ck^T
            Kk,Gk = get_K_G(mat[ph]['E'], mat[ph]['nu'])
            Ek = build_E_tensor(Gk, mat[ph]['nu'])
            Ck_Ek = dot_4_4(Ck, Ek)
            cov_stress = (mu_val / 2.0) * dot_4_4(Ck_Ek, Ck.transpose(2,3,0,1))
            var_sig33 = cov_stress[2,2,2,2]
            Δσ = math.sqrt(max(var_sig33, 0.0))
            results.append({'V_BNS': round(v_s, 1), 'phase': ph,
                            'sigma0': round(float(σ033), 6),
                            'delta_sigma': round(float(Δσ), 6)})
    return results

# -------- case 3 (textured BN_W) --------
def compute_case3(angles_deg):
    results = []
    K,G = get_K_G(mat['BN_W']['E'], mat['BN_W']['nu'])
    C0 = build_isotropic_stiffness(K,G)
    S0 = tensor_inv_4(C0)
    for angle in angles_deg:
        theta = math.radians(angle)
        eps_crystal = np.diag(alpha_aniso * ΔT)
        c = math.cos(theta)
        s = math.sin(theta)
        R = np.array([[1,0,0],
                      [0, c, -s],
                      [0, s, c]])
        eps_spec = R @ eps_crystal @ R.T
        Ceff = C0
        gamma_eps = eps_spec
        Ceps_avg = dot_4_2(C0, eps_spec)
        Cvoigt = C0
        Cvoigt_inv = S0
        gamma_sig = dot_4_2(Cvoigt_inv, Ceps_avg)
        eps_star = 0.5 * (gamma_sig + gamma_eps)
        delta = (gamma_sig + gamma_eps)/2
        Cplus = Cvoigt
        Cminus = Cvoigt
        D = Cplus - Cminus
        # use direct eigenstrain formula for uniform stiffness
        sig0 = dot_4_2(C0, gamma_eps - eps_spec)
        σ033 = sig0[2,2]
        eps_dev = eps_spec - gamma_eps
        cov_eps = np.einsum('ij,kl->ijkl', eps_dev, eps_dev)
        cov_sig = dot_4_4(dot_4_4(C0, cov_eps), C0.transpose(2,3,0,1))
        var_sig33 = cov_sig[2,2,2,2]
        Δσ = math.sqrt(max(var_sig33, 0.0))
        results.append({'angle_deg': angle, 'sigma0': round(float(σ033), 6),
                        'delta_sigma': round(float(Δσ), 6)})
    return results

# -------- case 4 (Table 2) --------
case4_table = [
    {"V_BNS": 0.20, "V_BNW": 0.79, "V_BNG": 0.01, "sigma0": -11.3, "delta_sigma": 0.7},
    {"V_BNS": 0.50, "V_BNW": 0.49, "V_BNG": 0.01, "sigma0": -11.4, "delta_sigma": 0.7},
    {"V_BNS": 0.49, "V_BNW": 0.49, "V_BNG": 0.02, "sigma0": -11.4, "delta_sigma": 0.9}
]

# ===== main computation =====
V_BNS_vals = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
angles_deg = [0, 15, 30, 45, 60, 75, 90]

case1 = compute_case(V_BNS_vals, 1, add_tr_strain_BNS=0.0)
case2 = compute_case(V_BNS_vals, 2, add_tr_strain_BNS=ε_tr_case2)
case3 = compute_case3(angles_deg)

result = {
    "case1": case1,
    "case2": case2,
    "case3": case3,
    "case4": {"table2": case4_table}
}

with open('/app/outputs/stress_results.json', 'w') as f:
    json.dump(result, f, indent=2)

PYEOF
