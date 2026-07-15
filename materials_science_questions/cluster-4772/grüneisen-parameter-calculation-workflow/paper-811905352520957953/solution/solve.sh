#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: fitted_potential_params.json ===
python3 << 'EOPY'
import numpy as np, csv, json, os
out = '/app/outputs'

# Lattice and volume
a = 5.84
Vz = a**3
f2 = a**4 / Vz   # = a
f3 = 4 * a**6 / Vz  # = 4 a^3

# Experimental inputs
C11e, C12e, C44e = 142.38, 124.10, 95.24
C111e, C112e, C123e, C144e, C155e, C456e = -1.65, -0.62, -0.48, -0.60, -0.69, -0.56

# ---------- Fit potential parameters ----------
# SOEC parameters (exact from 3 eqns)
alpha = (C12e + C44e) / (8 * f2)
lam   = (C44e - C12e) / (2 * f2)
sigma = (C11e / f2 - 4*alpha - 3*lam) / 8

# TOEC parameters (least squares)
b = np.array([C456e / f3, C112e / f3, C111e / f3, C123e / f3, C144e / f3, C155e / f3])
A = np.array([
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 16],
    [1,-3, 0],
    [1,-1, 0],
    [1, 1, 0]
])
x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
beta, zeta, nu = x[0], x[1], x[2]

# Save fitted params
with open(f'{out}/fitted_potential_params.json','w') as f:
    json.dump({'alpha_GPa':alpha,'lambda_GPa':lam,'sigma_GPa':sigma,
               'beta_TPa':beta,'zeta_TPa':zeta,'nu_TPa':nu}, f, indent=2)

# ---------- SOECs and aggregates ----------
C11 = (4*alpha + 3*lam + 8*sigma) * f2
C12 = (4*alpha - lam) * f2
C44 = (4*alpha + lam) * f2
CL  = (C11 + C12 + 2*C44) / 2
Cp  = (C11 - C12) / 2
K   = (C11 + 2*C12) / 3
P   = C12 - C44
A_anis = 2*C44 / (C11 - C12)
with open(f'{out}/soecs_and_aggregates.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['property','value_GPa_or_dimensionless'])
    for prop,val in [('C11',C11),('C12',C12),('C44',C44),('C_L',CL),
                     ('C_prime',Cp),('K',K),('P',P),('A',A_anis)]:
        w.writerow([prop, f'{val:.6g}'])

# ---------- TOECs ----------
C111 = (beta + zeta + 16*nu) * f3
C112 = (beta + zeta) * f3
C123 = (beta - 3*zeta) * f3
C144 = (beta - zeta) * f3
C155 = (beta + zeta) * f3
C456 = beta * f3
with open(f'{out}/toecs.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['constant','value_TPa'])
    for const,val in [('C111',C111),('C112',C112),('C123',C123),
                      ('C144',C144),('C155',C155),('C456',C456)]:
        w.writerow([const, f'{val:.6g}'])

# ---------- Pressure derivatives ----------
# Convert TOECs to GPa for pressure derivative formulas
C111g = C111 * 1000
C112g = C112 * 1000
C123g = C123 * 1000
C144g = C144 * 1000
C155g = C155 * 1000

denom = C11 + 2*C12
dC11dp = -(C111g + 2*C112g + 2*C11 + 2*C12) / denom
dC12dp = -(C123g + 2*C112g - C11 - C12) / denom
dC44dp = -(C144g + 2*C155g + C11 + 2*C12 + C44) / denom
with open(f'{out}/pressure_derivatives.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['derivative','value'])
    w.writerow(['dC11_dp', f'{dC11dp:.6g}'])
    w.writerow(['dC12_dp', f'{dC12dp:.6g}'])
    w.writerow(['dC44_dp', f'{dC44dp:.6g}'])

# ---------- Mode Grüneisen parameters ----------
dC11_deta = C111g + 2*C112g
dC12_deta = 2*C112g + C123g
dC44_deta = C144g + 2*C155g

def christoffel(C11,C12,C44, n):
    n1,n2,n3 = n
    G = np.zeros((3,3))
    G[0,0] = C11*n1**2 + C44*(n2**2+n3**2)
    G[1,1] = C11*n2**2 + C44*(n1**2+n3**2)
    G[2,2] = C11*n3**2 + C44*(n1**2+n2**2)
    G[0,1]=G[1,0] = (C12 + C44)*n1*n2
    G[0,2]=G[2,0] = (C12 + C44)*n1*n3
    G[1,2]=G[2,1] = (C12 + C44)*n2*n3
    return G

def compute_gammas(C11,C12,C44, d11,d12,d44, n):
    G = christoffel(C11,C12,C44, n)
    dG = christoffel(d11,d12,d44, n)
    vals, vecs = np.linalg.eigh(G)
    gammas = []
    for j in range(3):
        lam = vals[j]
        w = vecs[:,j]
        dlam = w.T @ dG @ w
        gamma = -(dlam/(2*lam) + 1.5)
        gammas.append(gamma)
    return vals, vecs, gammas

def label_modes(vals, vecs, gammas, n, theta_deg):
    idx = np.argsort(vals)
    idx_T = idx[:2].tolist()
    idx_L = idx[2]
    if abs(n[1]) < 1e-12:
        pure_y = [i for i in idx_T if abs(vecs[1,i]) > 0.999]
        if len(pure_y) == 1:
            iT2 = pure_y[0]
            iT1 = [i for i in idx_T if i != iT2][0]
        else:
            iT1, iT2 = idx_T[0], idx_T[1]
    else:
        gT = [(gammas[i], i) for i in idx_T]
        gT.sort(key=lambda x: x[0])
        iT1, iT2 = gT[0][1], gT[1][1]
    return idx_L, iT1, iT2

rows = []
for dir_name, n in [('[001]',(0,0,1)), ('[110]',(1/np.sqrt(2),1/np.sqrt(2),0)),
                    ('[111]',(1/np.sqrt(3),1/np.sqrt(3),1/np.sqrt(3)))]:
    vals, vecs, gammas = compute_gammas(C11,C12,C44, dC11_deta,dC12_deta,dC44_deta, n)
    iL, iT1, iT2 = label_modes(vals, vecs, gammas, n, 0)
    rows.append([dir_name, 0, 'qL', f'{gammas[iL]:.6g}'])
    rows.append([dir_name, 0, 'qT1', f'{gammas[iT1]:.6g}'])
    rows.append([dir_name, 0, 'qT2', f'{gammas[iT2]:.6g}'])

for deg in range(0,91,5):
    th = np.deg2rad(deg)
    n = (np.sin(th), 0, np.cos(th))
    vals, vecs, gammas = compute_gammas(C11,C12,C44, dC11_deta,dC12_deta,dC44_deta, n)
    iL, iT1, iT2 = label_modes(vals, vecs, gammas, n, deg)
    rows.append(['(010)', deg, 'qL', f'{gammas[iL]:.6g}'])
    rows.append(['(010)', deg, 'qT1', f'{gammas[iT1]:.6g}'])
    rows.append(['(010)', deg, 'qT2', f'{gammas[iT2]:.6g}'])

with open(f'{out}/mode_gruneisen_params.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['direction','angle_deg','mode','gamma'])
    for row in rows:
        w.writerow(row)

# ---------- Low-temperature limit gamma_L and delta ----------
nth, nph = 360, 720
thetas = np.linspace(0, np.pi, nth)
phis   = np.linspace(0, 2*np.pi, nph)
dth = thetas[1] - thetas[0]
dph = phis[1] - phis[0]

sum_num = 0.0
sum_den = 0.0
for th in thetas:
    sinth = np.sin(th)
    for ph in phis:
        n = (sinth*np.cos(ph), sinth*np.sin(ph), np.cos(th))
        vals, vecs, gammas = compute_gammas(C11,C12,C44, dC11_deta,dC12_deta,dC44_deta, n)
        for lam, gamma in zip(vals, gammas):
            w = lam**(-1.5)
            dA = sinth * dth * dph
            sum_num += gamma * w * dA
            sum_den += w * dA

gamma_L = sum_num / sum_den

delta = -1 - (C111g + 6*C112g + 2*C123g) / (3*C11 + 2*C12)

with open(f'{out}/gamma_L_and_delta.json','w') as f:
    json.dump({'gamma_L': gamma_L, 'delta': delta}, f)
EOPY

# === solve block: soecs_and_aggregates.csv ===
# already created by fitted_potential_params.json step

# === solve block: toecs.csv ===
# already created

# === solve block: pressure_derivatives.csv ===
# already created

# === solve block: mode_gruneisen_params.csv ===
# already created

# === solve block: gamma_L_and_delta.json ===
# already created
