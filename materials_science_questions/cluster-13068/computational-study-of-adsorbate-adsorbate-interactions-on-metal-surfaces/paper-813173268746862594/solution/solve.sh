#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: interaction_energies.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import brentq
import itertools, csv, os

T = 0.5
Us = [1.0, 2.5, 4.0]
Vs = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5]

# ---------- exact diagonalization via direct bitmask ----------
def exact_deltaW(U, V):
    if V == 0:
        return 0.0
    N = 4
    # basis for 2 electrons out of 4 sites (spin up/down sectors)
    combs = list(itertools.combinations(range(N), 2))
    basis = [sum(1<<i for i in c) for c in combs]
    n_states = len(basis)  # 6
    idx_map = {s:i for i,s in enumerate(basis)}
    # single-particle Hamiltonian for one spin
    Ea0 = -U/2
    H_spin = np.zeros((n_states, n_states))
    # site energies
    for s,mask in enumerate(basis):
        if mask & 1:  # site 0 occupied
            H_spin[s,s] += Ea0
    # hopping terms: pairs (i,j) with amplitude t
    hops = [(0,1,-V), (1,2,-T), (2,3,-T)]
    for i,j,t in hops:
        for s,mask in enumerate(basis):
            # hop from j to i (i empty, j occupied)
            if (mask & (1<<j)) and not (mask & (1<<i)):
                new_mask = (mask & ~(1<<j)) | (1<<i)
                s2 = idx_map[new_mask]
                # fermion sign: count occupied sites between i and j
                lo, hi = (i,j) if i<j else (j,i)
                mid_mask = mask & ~((1<<lo) | (1<<hi))
                count = bin(mid_mask >> (lo+1)).count('1')
                sign = 1 if count%2==0 else -1
                H_spin[s2,s] += t * sign
    # make symmetric
    H_spin = H_spin + H_spin.T - np.diag(H_spin.diagonal())
    I = np.eye(n_states)
    H_total = np.kron(H_spin, I) + np.kron(I, H_spin)
    # add U term: diagonal for states where adatom (site 0) doubly occupied
    for i_up in range(n_states):
        occ0_up = 1 if basis[i_up] & 1 else 0
        for i_down in range(n_states):
            occ0_down = 1 if basis[i_down] & 1 else 0
            if occ0_up and occ0_down:
                idx = i_up * n_states + i_down
                H_total[idx,idx] += U
    eigvals = np.linalg.eigvalsh(H_total)
    E0 = -U/2 - 2*np.sqrt(2)*T
    return eigvals[0] - E0

# ---------- approximations ----------
def weak_deltaW(U, V):
    return -V**2/(U + 2*np.sqrt(2)*T) - 4*V**2/U

def RSC_deltaW(U, V):
    V_eff = max(V, 1e-12)
    E_SC = -U/4 - 0.5*np.sqrt((U/2)**2 + 16*V_eff**2)
    E_3_2 = 2*(np.sqrt(2)-1)*T
    deltaW_SC = E_SC + E_3_2
    E_minus = 0.25*(-U - np.sqrt(U**2 + 16*V_eff**2))
    E_plus  = 0.25*(-U + np.sqrt(U**2 + 16*V_eff**2))
    num1 = (E_SC * E_minus + 2*V_eff**2)**2
    denom1 = (2*E_minus + T - E_SC) * (E_SC**2 + 4*V_eff**2) * (E_minus**2 + V_eff**2)
    term1 = num1 / denom1 if denom1 != 0 else 0.0
    num2 = (E_SC * E_plus + 2*V_eff**2)**2
    denom2 = (2*E_plus + T - E_SC) * (E_SC**2 + 4*V_eff**2) * (E_plus**2 + V_eff**2)
    term2 = num2 / denom2 if denom2 != 0 else 0.0
    deltaW_R = -T**2 * (term1 + term2) * 2.0
    return deltaW_SC + deltaW_R

def RHF_deltaW(U, V):
    T2 = T**2
    V2 = V**2
    term = np.sqrt(V2*V2 + 4*T2*T2)
    outer1 = V2 + 2*T2 + term
    outer2 = max(0, V2 + 2*T2 - term)
    return -np.sqrt(2) * (np.sqrt(outer1) + np.sqrt(outer2) - 2*T)

def URHF_deltaW(U, V):
    def occ_diff(x):
        H_up = np.zeros((4,4))
        H_up[0,0] = -U*x
        H_up[0,1] = H_up[1,0] = -V
        H_up[1,2] = H_up[2,1] = H_up[2,3] = H_up[3,2] = -T
        evals_up, evecs_up = np.linalg.eigh(H_up)
        H_down = np.zeros((4,4))
        H_down[0,0] = U*x
        H_down[0,1] = H_down[1,0] = -V
        H_down[1,2] = H_down[2,1] = H_down[2,3] = H_down[3,2] = -T
        evals_down, evecs_down = np.linalg.eigh(H_down)
        occ_up = sum(np.abs(evecs_up[:, i][0])**2 for i in range(2))
        occ_down = sum(np.abs(evecs_down[:, i][0])**2 for i in range(2))
        return (occ_up - occ_down)/2 - x
    try:
        x_sol = brentq(occ_diff, 0, 0.5)
    except ValueError:
        x_sol = 0.0
    H_up = np.zeros((4,4))
    H_up[0,0] = -U*x_sol
    H_up[0,1] = H_up[1,0] = -V
    H_up[1,2] = H_up[2,1] = H_up[2,3] = H_up[3,2] = -T
    evals_up = np.linalg.eigvalsh(H_up)
    H_down = np.zeros((4,4))
    H_down[0,0] = U*x_sol
    H_down[0,1] = H_down[1,0] = -V
    H_down[1,2] = H_down[2,1] = H_down[2,3] = H_down[3,2] = -T
    evals_down = np.linalg.eigvalsh(H_down)
    E_occ = evals_up[0] + evals_up[1] + evals_down[0] + evals_down[1]
    E_HF = E_occ - U*(0.25 - x_sol**2)
    E0 = -U/2 - 2*np.sqrt(2)*T
    return E_HF - E0

# ---------- write CSV ----------
out_dir = os.environ.get('OUTDIR', '/app/outputs')
out_path = os.path.join(out_dir, 'interaction_energies.csv')
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['U','V','exact_deltaW','weak_deltaW','RSC_deltaW','RHF_deltaW','URHF_deltaW'])
    for U in Us:
        for V in Vs:
            exact = exact_deltaW(U, V)
            weak = weak_deltaW(U, V)
            rsc = RSC_deltaW(U, V)
            rhf = RHF_deltaW(U, V)
            urhf = URHF_deltaW(U, V)
            writer.writerow([U, V, exact, weak, rsc, rhf, urhf])
PYEOF

# === solve block: weak_limits.csv ===
python3 /solution/compute.py weak_limits /app/outputs/weak_limits.csv
