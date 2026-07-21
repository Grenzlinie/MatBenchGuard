#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: epi_predictions.csv ===
cat > /tmp/compute_epi.py << 'PYEOF'
import numpy as np
from scipy.integrate import quad
import csv, os

# ---------- Isotropic stiffness helpers ----------
def iso_C(E, nu):
    lam = E * nu / ((1+nu)*(1-2*nu))
    mu = E / (2*(1+nu))
    C = np.zeros((6,6))
    C[0,0] = C[1,1] = C[2,2] = lam + 2*mu
    C[0,1] = C[0,2] = C[1,0] = C[1,2] = C[2,0] = C[2,1] = lam
    C[3,3] = C[4,4] = C[5,5] = mu
    return C, lam, mu

def iso_KG(E, nu):
    K = E / (3*(1-2*nu))
    G = E / (2*(1+nu))
    return K, G

def KG_to_E(K, G):
    return 9*K*G / (3*K + G) if (3*K + G) > 0 else 0.0

# ---------- I-integrals for spheroid (a1=a2=a, a3=c) using finite-interval substitution ----------
def I_integrals_spheroid(a, c):
    a2 = a*a
    c2 = c*c
    vol = a2 * c

    def delta(s):
        return np.sqrt((a2 + s)**2 * (c2 + s))

    def integrate(func_of_s):
        # substitution s = a2 * (1-t)/t   ->   t in [0,1], sa = 0..inf
        def integrand(t):
            s = a2 * (1.0 - t) / t
            ds_dt = -a2 / (t*t)
            # ds positive because s decreases as t increases, but we integrate from t=0 to 1, so ds = -a2/t^2 dt
            return func_of_s(s) * a2 / (t*t)
        res, _ = quad(integrand, 0.0, 1.0, epsabs=1e-14, limit=1000)
        return res

    I = np.zeros(3)
    # I1 = I2
    I[0] = 2.0 * np.pi * vol * integrate(lambda s: 1.0 / ((a2 + s) * delta(s)))
    I[2] = 2.0 * np.pi * vol * integrate(lambda s: 1.0 / ((c2 + s) * delta(s)))
    I[1] = I[0]

    II = np.zeros((3,3))
    II[0,0] = 2.0 * np.pi * vol * integrate(lambda s: 1.0 / ((a2 + s)**2 * delta(s)))
    II[2,2] = 2.0 * np.pi * vol * integrate(lambda s: 1.0 / ((c2 + s)**2 * delta(s)))
    II[0,1] = II[1,0] = II[0,0]  # a1=a2
    II[1,1] = II[0,0]
    II[0,2] = II[2,0] = 2.0 * np.pi * vol * integrate(lambda s: 1.0 / ((a2 + s)*(c2 + s) * delta(s)))
    II[1,2] = II[2,1] = II[0,2]

    return I, II

# ---------- Eshelby tensor 6x6 Voigt (spheroid with a1=a2=a, a3=c) ----------
def eshelby_tensor_voigt(a1, a2, a3, nu):
    a = a1
    c = a3
    a_sq = np.array([a*a, a*a, c*c])
    I, II = I_integrals_spheroid(a, c)
    den = 8.0 * np.pi * (1.0 - nu)
    S = np.zeros((6,6))
    for i in range(3):
        S[i,i] = (3.0 * a_sq[i] * II[i,i] + (1-2*nu) * I[i]) / den
    for i in range(3):
        for j in range(3):
            if i != j:
                S[i,j] = (a_sq[j] * II[i,j] - (1-2*nu) * I[i]) / den
    for idx, (i,j) in enumerate([(1,2),(0,2),(0,1)]):
        S[3+idx,3+idx] = ((a_sq[i]+a_sq[j]) * II[i,j] + (1-2*nu) * (I[i]+I[j])) / (2.0 * den)
    return S

# ---------- EPI bi-phasic ----------
def effective_biphasic(E_m, nu_m, E_f, nu_f, a1, a2, a3, alpha):
    if alpha <= 0.0:
        return E_m, E_m/(2*(1+nu_m))
    C_m, lam_m, mu_m = iso_C(E_m, nu_m)
    if E_f <= 0.0:
        C_f = np.zeros((6,6))
    else:
        C_f, _, _ = iso_C(E_f, nu_f)
    S = eshelby_tensor_voigt(a1, a2, a3, nu_m)
    I6 = np.eye(6)
    Cinv = np.linalg.inv(C_m)
    DeltaC = C_f - C_m
    M = I6 + (1.0 - alpha) * S @ Cinv @ DeltaC
    T = np.linalg.inv(M)
    D = DeltaC @ T
    # Isotropic projection of D (exact orientational average)
    D_ppqq = (D[0,0] + D[1,1] + D[2,2] +
              D[0,1] + D[0,2] + D[1,0] + D[1,2] + D[2,0] + D[2,1])
    D_pqpq = (D[0,0] + D[1,1] + D[2,2] +
              2.0 * (D[3,3] + D[4,4] + D[5,5]))
    K_D = D_ppqq / 9.0
    G_D = (D_pqpq - D_ppqq / 3.0) / 10.0
    K_m, G_m = iso_KG(E_m, nu_m)
    K_eff = K_m + alpha * K_D
    G_eff = G_m + alpha * G_D
    E_eff = KG_to_E(K_eff, G_eff)
    return E_eff, G_eff

# ---------- Three-phase ----------
def three_phase_effective(E_m, nu_m, alpha_p, pore_shape, alpha_s, particle_shape, E_f, nu_f):
    E1, G1 = effective_biphasic(E_m, nu_m, 0.0, 0.0, *pore_shape, alpha_p)
    nu1 = (E1/(2*G1) - 1.0) if G1 > 0 else 0.0
    E2, G2 = effective_biphasic(E1, nu1, E_f, nu_f, *particle_shape, alpha_s)
    return E2, G2

# ---------- Main ----------
OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
output_path = os.path.join(OUTDIR, 'epi_predictions.csv')

# Material constants (Table 1)
E_PPF = 2.0
G_PPF = 0.77
nu_PPF = (E_PPF/(2*G_PPF) - 1)
E_Si = 164.0
G_Si = 67.0
nu_Si = (E_Si/(2*G_Si) - 1)

def anisotropy_A(k1, k2):
    if k1 <= 0 or k2 <= 0:
        return 0.0
    return (1+k1+k2)*(1+1/k1+1/k2)/3 - 3

rows = []

# (a) porous PPF with spherical pores
for ap in [0.1,0.2,0.3,0.4,0.5,0.6,0.7]:
    k1 = k2 = 1.0
    E,G = effective_biphasic(E_PPF, nu_PPF, 0, 0, 1.0, 1.0, 1.0, ap)
    rows.append([f"porous_spherical_{ap}", ap, 0.0, k1, k2, anisotropy_A(k1,k2), E, G])

# (b) dense PPF with spherical Si particles
for als in [0.00,0.05,0.10,0.15,0.20]:
    k1 = k2 = 1.0
    E,G = effective_biphasic(E_PPF, nu_PPF, E_Si, nu_Si, 1.0,1.0,1.0, als)
    rows.append([f"dense_si_spherical_{als:.2f}", 0.0, als, k1, k2, anisotropy_A(k1,k2), E, G])

# (c) three-phase: spherical pores (α_p=0.6) + spherical Si particles
for als in [0.00,0.05,0.10,0.15,0.20]:
    k1 = k2 = 1.0
    E,G = three_phase_effective(E_PPF, nu_PPF, 0.6, (1.0,1.0,1.0),
                                als, (1.0,1.0,1.0), E_Si, nu_Si)
    rows.append([f"three_phase_spheres_0p6_{als:.2f}", 0.6, als, k1, k2, anisotropy_A(k1,k2), E, G])

# (d) three-phase: spherical pores (α_p=0.6) + highly oblate Si (k1=k2=1000) at α_s=0.10
k1 = k2 = 1000.0
al_s = 0.10
E,G = three_phase_effective(E_PPF, nu_PPF, 0.6, (1.0,1.0,1.0),
                            al_s, (k1,k2,1.0), E_Si, nu_Si)
rows.append(["three_phase_oblate_0p6_0.10", 0.6, al_s, k1, k2, anisotropy_A(k1,k2), E, G])

# (e) shape-anisotropy sweeps
# Porous PPF with various pore shapes
for ap in [0.1,0.3,0.5,0.7]:
    for k in [0.1, 1.0, 10.0, 100.0, 1000.0]:
        shape_str = "prolate" if k<1 else ("oblate" if k>1 else "spherical")
        E,G = effective_biphasic(E_PPF, nu_PPF, 0, 0, k, k, 1.0, ap)
        rows.append([f"porous_{shape_str}_{ap}_{k}", ap, 0.0, k, k, anisotropy_A(k,k), E, G])

# Dense PPF with various Si particle shapes
for als in [0.1, 0.2]:
    for k in [0.1, 1.0, 10.0, 100.0, 1000.0]:
        shape_str = "prolate" if k<1 else ("oblate" if k>1 else "spherical")
        E,G = effective_biphasic(E_PPF, nu_PPF, E_Si, nu_Si, k, k, 1.0, als)
        rows.append([f"dense_si_{shape_str}_{als}_{k}", 0.0, als, k, k, anisotropy_A(k,k), E, G])

# Three-phase with α_p=0.6, various Si particle shapes and concentrations
for als in [0.1, 0.2]:
    for k in [0.1, 1.0, 10.0, 100.0, 1000.0]:
        shape_str = "prolate" if k<1 else ("oblate" if k>1 else "spherical")
        E,G = three_phase_effective(E_PPF, nu_PPF, 0.6, (1.0,1.0,1.0),
                                    als, (k, k, 1.0), E_Si, nu_Si)
        rows.append([f"three_phase_{shape_str}_{als}_{k}", 0.6, als, k, k, anisotropy_A(k,k), E, G])

# Write CSV
header = ["case_id", "porosity_alpha_p", "particle_alpha_s", "k1", "k2", "A", "E_GPa", "G_GPa"]
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
print(f"Written {len(rows)} rows to {output_path}")
PYEOF
python3 /tmp/compute_epi.py
