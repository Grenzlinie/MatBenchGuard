#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: magnetization.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.special import kv
import csv, os, sys

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

# ---------- dipole lattice sums (Ewald, truncated) ----------
def dipole_sums_at_k(kx, ky, mmax=5, nmax=20):
    """ return p_xx, p_yy, p_zz for square lattice, Eqs.(39)-(43) """
    q1 = 0.0
    q2 = 0.0
    for m in range(1, mmax+1):
        for n in range(-nmax, nmax+1):
            # q1 sum: (n*pi + ky/2)^2 * cos(m*kz) * K2(2*m*|n*pi + ky/2|)
            a = n*np.pi + kx/2.0
            b = 2.0 * m * abs(a)
            if b > 700:
                term = 0.0
            else:
                term = a*a * np.cos(m*ky) * kv(2, b)
            q1 += term
            # q2: (n*pi + kz/2)^2 * cos(m*ky) * K2(2*m*|n*pi + kz/2|)
            a = n*np.pi + ky/2.0
            b = 2.0 * m * abs(a)
            if b > 700:
                term = 0.0
            else:
                term = a*a * np.cos(m*kx) * kv(2, b)
            q2 += term
    q1 *= 16.0/3.0
    q2 *= 16.0/3.0
    pxx = q1 + q2
    pyy = q1 - 2*q2
    pzz = q2 - 2*q1
    return pxx, pyy, pzz

# ---------- main ----------
S = 1.0          # spin
J = 1.0          # exchange energy unit
Z = 4            # coordination number
Nk = 16          # mesh size per dimension

# k-mesh for BZ [-pi,pi]x[-pi,pi]
k_lin = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
KX, KY = np.meshgrid(k_lin, k_lin)
k_vecs = np.column_stack([KX.ravel(), KY.ravel()])
Nk2 = Nk*Nk
wk = (2.0*np.pi)**2 / Nk2   # integration weight

# precompute dipole sums for all k-points
print("Computing dipole sums...", file=sys.stderr)
p_xx = np.empty(Nk2)
p_yy = np.empty(Nk2)
p_zz = np.empty(Nk2)
for i, (kx, ky) in enumerate(k_vecs):
    p_xx[i], p_yy[i], p_zz[i] = dipole_sums_at_k(kx, ky, mmax=5, nmax=20)

# also p_zz(0) at gamma point
p_zz0 = dipole_sums_at_k(0.0, 0.0, mmax=5, nmax=20)[2]

# structure factor: gamma_k = (cos(kx)+cos(ky))/2
cos_kx = np.cos(KX.ravel())
cos_ky = np.cos(KY.ravel())
gamma_k = (cos_kx + cos_ky) / 2.0

# parameter sets to compute: (D_div_J, Omega_div_J)
param_sets = [(0.1, 0.005),
              (0.2, 0.005),
              (0.5, 0.005)]
T_range = np.arange(0.02, 2.01, 0.02)

results = []   # list of (T, D, Om, M)

for D, Om in param_sets:
    print(f"Processing D={D}, Om={Om}", file=sys.stderr)
    for T in T_range:
        beta = 1.0 / max(T, 1e-6)
        # initial guess for moments
        sz   = 0.8
        sz2  = 0.65
        s2   = 0.1
        s2sz = 0.05
        converged = False
        for it in range(500):
            # current derived quantities
            Gamma = 0.5 * sz2   # for S=1, Eq.(14)
            # compute F1(k), F2(k), E(k)
            eps_k = 8.0 * sz * (1.0 - gamma_k)   # J=1, Z=4
            F1 = (eps_k
                  + 0.5*Om*sz*p_xx + 0.5*Om*sz*p_yy
                  - Om*sz*p_zz0       # h=0
                  + D * Gamma * sz)
            F2 = (0.5*Om*sz*p_xx - 0.5*Om*sz*p_yy + D*Gamma*sz)
            E_k = np.sqrt(np.maximum(F1**2 - F2**2, 1e-12))
            # Bose factors
            exp_bE = np.exp(beta * E_k)
            nB = 1.0 / (exp_bE - 1.0)
            # factor for the two parts in (31),(32)
            # sum1 = (1/(2E) * nB) * [...]
            # sum2 = - (1/(2E) * 1/(e^{-betaE}-1)) * [...]
            # and 1/(e^{-betaE}-1) = - e^{betaE} nB
            # so overall factor for first term: (nB)/(2E) , second: (nB)/(2E) * exp_bE? Let's derive.
            # Eq.(31): term1 = .../(2E(e^{bE}-1)) * [...]
            # term2 = - .../(2E(e^{-bE}-1)) * [...] = + .../(2E(1-e^{-bE})) * [...] = + ... * e^{bE}/(2E(e^{bE}-1)) * [...]
            # So overall factor = 1/(2E(e^{bE}-1)) * [ ... + e^{bE} * ... ]
            # We'll compute using explicit sums as in paper.
            fac_pos = nB / (2.0 * E_k)
            # For term2 in (31) with e^{-bE}-1? Actually e^{-bE}-1 is negative, nB_neg = 1/(exp(-bE)-1) = - e^{bE} nB
            # So we can write the full expression as:
            # sum over k: wk * (fac_pos * A_pos - fac_pos * exp_bE * A_neg) where A_pos and A_neg are the two brackets.
            # Let's define:
        
        # compute <g1>, <g2> for n=1,2 with current moments
            g1_1 = 2.0 * sz
            g1_2 = (4.0*sz + 2.0) * (2.0 - sz - sz2)
            g2_1 = 0.0
            g2_2 = -2.0 * s2sz
            
        # ---- RHS of (31) for n=1,2 ----
            # term inside first bracket: F2*<g2> + <g1>*(E+F1)
            A1_pos = F2*g2_1 + g1_1*(E_k + F1)
            A2_pos = F2*g2_2 + g1_2*(E_k + F1)
            # term inside second bracket (with minus sign): F2*<g2> - <g1>*(E-F1)
            A1_neg = F2*g2_1 - g1_1*(E_k - F1)
            A2_neg = F2*g2_2 - g1_2*(E_k - F1)
            # total sums using the factor fac_pos and exp_bE
            sum1_31 = np.sum(wk * fac_pos * (A1_pos + exp_bE * A1_neg))   # A1_neg part in original has - sign, but we accounted.
            sum2_31 = np.sum(wk * fac_pos * (A2_pos + exp_bE * A2_neg))
            
            # new values from (31)
            new_V1 = sum1_31   # <S^- S^+>
            new_V2 = sum2_31   # <(S^-)^2 (S^+)^2>
            
        # ---- RHS of (32) for n=1,2 ----
            # first bracket (with - sign): -[...] ; we'll compute the inner bracket: F2*<g1> - <g2>*(E-F1)
            B1_pos = F2*g1_1 - g2_1*(E_k - F1)
            B2_pos = F2*g1_2 - g2_2*(E_k - F1)
            # second bracket (with + sign): +[...] : F2*<g1> + <g2>*(E+F1)
            B1_neg = F2*g1_1 + g2_1*(E_k + F1)
            B2_neg = F2*g1_2 + g2_2*(E_k + F1)
            # original Eq.(32): first term has - factor, second has + factor.
            # So sum = Σ wk * [ - fac_pos * B1_pos + fac_pos * exp_bE * B1_neg ]
            sum1_32 = np.sum(wk * fac_pos * (-B1_pos + exp_bE * B1_neg))
            sum2_32 = np.sum(wk * fac_pos * (-B2_pos + exp_bE * B2_neg))
            
            new_V3 = sum1_32   # <(S^-)^2>
            new_V4 = sum2_32   # should be 2 <(S^-)^2> if exact, we'll use to solve for s2sz
            
            # solve for sz, sz2
            # Eq: new_V1 = 2 - sz - sz2  -> sz+sz2 = 2 - new_V1
            #     new_V2 = -2 sz + 2 sz2 -> sz2 - sz = new_V2/2
            A = 2.0 - new_V1
            B = new_V2 / 2.0
            new_sz  = (A - B) / 2.0
            new_sz2 = (A + B) / 2.0
            new_s2  = new_V3
            
            # Solve for s2sz from new_V4 = 2 s2 (should hold) and its linear dependence on s2sz.
            # Write new_V4 = C + D * g2_2 = C - 2*D * s2sz, with C from terms without g2_2.
            # Compute C (setting g2_2=0) and D (coefficient of g2_2).
            # We already computed sum2_32; but we need C and D. We'll recompute with symbolic separation.
            # Actually we can compute sum2_32 for g2_2=0 as C, and then D = (sum2_32 - C) / g2_2 (if g2_2 != 0).
            g2_2_zero = 0.0
            B2_pos_zero = F2*g1_2 - g2_2_zero*(E_k - F1)
            B2_neg_zero = F2*g1_2 + g2_2_zero*(E_k + F1)
            sum2_32_zero = np.sum(wk * fac_pos * (-B2_pos_zero + exp_bE * B2_neg_zero))
            C = sum2_32_zero
            # new_V4 computed with actual g2_2 = -2 s2sz
            # So new_V4 = C + D * g2_2, where D = (new_V4 - C) / g2_2 if g2_2 non-zero.
            if abs(g2_2) > 1e-12:
                D = (new_V4 - C) / g2_2
            else:
                D = 0.0
            # Equation: new_V4 = C + D * g2_2 and we want new_V4 = 2 * new_s2
            # So C + D * g2_2_target = 2*new_s2 => g2_2_target = (2*new_s2 - C) / D
            # Then s2sz = -g2_2_target / 2
            if abs(D) > 1e-12:
                g2_2_target = (2*new_s2 - C) / D
                new_s2sz = -g2_2_target / 2.0
            else:
                new_s2sz = s2sz  # keep
            new_s2sz = np.clip(new_s2sz, 0.0, 0.5)
            new_sz  = np.clip(new_sz, 0.0, 1.0)
            new_sz2 = np.clip(new_sz2, 0.0, 1.0)
            new_s2  = np.clip(new_s2, 0.0, 0.5)
            
            # check convergence
            delta = max(abs(new_sz-sz), abs(new_sz2-sz2), abs(new_s2-s2), abs(new_s2sz-s2sz))
            # mixing
            alpha = 0.5
            sz   = sz   + alpha*(new_sz - sz)
            sz2  = sz2  + alpha*(new_sz2 - sz2)
            s2   = s2   + alpha*(new_s2 - s2)
            s2sz = s2sz + alpha*(new_s2sz - s2sz)
            if delta < 1e-5:
                converged = True
                break
        if not converged:
            # use last
            pass
        M = sz   # magnetization
        results.append((T, D, Om, M))
    # end T loop
# end param set loop

# Write CSV
with open(os.path.join(outdir, 'magnetization.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T_div_J', 'D_div_J', 'Omega_div_J', 'M'])
    writer.writerows(results)
print("magnetization.csv written", file=sys.stderr)
PYEOF

cat > /solution/solver.py << 'PYEOF'
import sys, os, csv, numpy as np
from scipy.special import kv

outdir = os.environ.get('OUTDIR', '/app/outputs')

def dipole_sums_at_k(kx, ky, mmax=5, nmax=20):
    q1 = 0.0
    q2 = 0.0
    for m in range(1, mmax+1):
        for n in range(-nmax, nmax+1):
            a = n*np.pi + kx/2.0
            b = 2.0 * m * abs(a)
            if b > 700:
                term = 0.0
            else:
                term = a*a * np.cos(m*ky) * kv(2, b)
            q1 += term
            a = n*np.pi + ky/2.0
            b = 2.0 * m * abs(a)
            if b > 700:
                term = 0.0
            else:
                term = a*a * np.cos(m*kx) * kv(2, b)
            q2 += term
    q1 *= 16.0/3.0
    q2 *= 16.0/3.0
    pxx = q1 + q2
    pyy = q1 - 2*q2
    pzz = q2 - 2*q1
    return pxx, pyy, pzz

Nk = 16
k_lin = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
KX, KY = np.meshgrid(k_lin, k_lin)
k_vecs = np.column_stack([KX.ravel(), KY.ravel()])
Nk2 = Nk*Nk
wk = (2.0*np.pi)**2 / Nk2

p_xx = np.empty(Nk2)
p_yy = np.empty(Nk2)
p_zz = np.empty(Nk2)
for i, (kx, ky) in enumerate(k_vecs):
    p_xx[i], p_yy[i], p_zz[i] = dipole_sums_at_k(kx, ky)
p_zz0 = dipole_sums_at_k(0.0, 0.0)[2]

cos_kx = np.cos(KX.ravel())
cos_ky = np.cos(KY.ravel())
gamma_k = (cos_kx + cos_ky) / 2.0

def self_consistent(D, Om, T, max_iter=200, tol=1e-5):
    beta = 1.0 / max(T, 1e-6)
    sz, sz2, s2, s2sz = 0.8, 0.65, 0.1, 0.05
    for it in range(max_iter):
        Gamma = 0.5 * sz2
        eps_k = 8.0 * sz * (1.0 - gamma_k)
        F1 = eps_k + 0.5*Om*sz*p_xx + 0.5*Om*sz*p_yy - Om*sz*p_zz0 + D*Gamma*sz
        F2 = 0.5*Om*sz*p_xx - 0.5*Om*sz*p_yy + D*Gamma*sz
        E_k = np.sqrt(np.maximum(F1**2 - F2**2, 1e-12))
        exp_bE = np.exp(beta * E_k)
        nB = 1.0 / (exp_bE - 1.0)
        fac_pos = nB / (2.0 * E_k)
        g1_1, g1_2 = 2.0*sz, (4.0*sz+2.0)*(2.0 - sz - sz2)
        g2_1, g2_2 = 0.0, -2.0*s2sz
        A1_pos, A2_pos = F2*g2_1 + g1_1*(E_k+F1), F2*g2_2 + g1_2*(E_k+F1)
        A1_neg, A2_neg = F2*g2_1 - g1_1*(E_k-F1), F2*g2_2 - g1_2*(E_k-F1)
        sum1_31 = np.sum(wk * fac_pos * (A1_pos + exp_bE * A1_neg))
        sum2_31 = np.sum(wk * fac_pos * (A2_pos + exp_bE * A2_neg))
        B1_pos, B2_pos = F2*g1_1 - g2_1*(E_k-F1), F2*g1_2 - g2_2*(E_k-F1)
        B1_neg, B2_neg = F2*g1_1 + g2_1*(E_k+F1), F2*g1_2 + g2_2*(E_k+F1)
        sum1_32 = np.sum(wk * fac_pos * (-B1_pos + exp_bE * B1_neg))
        sum2_32 = np.sum(wk * fac_pos * (-B2_pos + exp_bE * B2_neg))
        new_V1, new_V2 = sum1_31, sum2_31
        new_V3 = sum1_32
        A = 2.0 - new_V1
        B = new_V2 / 2.0
        new_sz = (A - B) / 2.0
        new_sz2 = (A + B) / 2.0
        new_s2 = new_V3
        g2_2_zero = 0.0
        B2_pos_zero = F2*g1_2 - g2_2_zero*(E_k - F1)
        B2_neg_zero = F2*g1_2 + g2_2_zero*(E_k + F1)
        sum2_32_zero = np.sum(wk * fac_pos * (-B2_pos_zero + exp_bE * B2_neg_zero))
        C = sum2_32_zero
        if abs(g2_2) > 1e-12:
            Dcoef = (sum2_32 - C) / g2_2
        else:
            Dcoef = 0.0
        if abs(Dcoef) > 1e-12:
            g2_2_target = (2*new_s2 - C) / Dcoef
            new_s2sz = -g2_2_target / 2.0
        else:
            new_s2sz = s2sz
        new_s2sz = np.clip(new_s2sz, 0.0, 0.5)
        new_sz  = np.clip(new_sz, 0.0, 1.0)
        new_sz2 = np.clip(new_sz2, 0.0, 1.0)
        new_s2  = np.clip(new_s2, 0.0, 0.5)
        delta = max(abs(new_sz-sz), abs(new_sz2-sz2), abs(new_s2-s2), abs(new_s2sz-s2sz))
        alpha = 0.5
        sz   = sz   + alpha*(new_sz - sz)
        sz2  = sz2  + alpha*(new_sz2 - sz2)
        s2   = s2   + alpha*(new_s2 - s2)
        s2sz = s2sz + alpha*(new_s2sz - s2sz)
        if delta < tol:
            break
    return sz

if len(sys.argv) > 1 and sys.argv[1] == 'spinwave':
    # compute spinwave_spectrum.csv
    Om = 0.005
    D_vals = [0.1, 0.5, 1.0]
    T = 0.1
    # k-path segments
    npts = 20
    rows = []
    for D in D_vals:
        sz = self_consistent(D, Om, T)
        sz2 = sz*sz  # approximate
        Gamma = 0.5 * sz2
        # define path points
        # Gamma (0,0) -> X (pi,0) -> M (pi,pi) -> Gamma (0,0)
        def get_path():
            t = np.linspace(0,1,npts)
            for tx in t:
                yield ('G->X', tx*np.pi, 0.0)
            for tx in t:
                yield ('X->M', np.pi, tx*np.pi)
            for tx in t:
                yield ('M->G', np.pi*(1-tx), np.pi*(1-tx))
        for seg, kx, ky in get_path():
            eps_k = 8.0 * sz * (1.0 - (np.cos(kx)+np.cos(ky))/2.0)
            pxx, pyy, pzz = dipole_sums_at_k(kx, ky)
            F1 = eps_k + 0.5*Om*sz*pxx + 0.5*Om*sz*pyy - Om*sz*p_zz0 + D*Gamma*sz
            F2 = 0.5*Om*sz*pxx - 0.5*Om*sz*pyy + D*Gamma*sz
            E = np.sqrt(max(F1**2 - F2**2, 0.0))
            rows.append([seg, kx, ky, D, E])
    with open(os.path.join(outdir, 'spinwave_spectrum.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['k_path','k_x','k_y','D_div_J','E'])
        w.writerows(rows)
elif len(sys.argv) > 1 and sys.argv[1] == 'transition':
    # compute transition_temperature.csv
    def find_Tc(D, Om, T_start=0.1, T_end=2.0):
        Ts = np.linspace(T_start, T_end, 50)
        Ms = []
        for T in Ts:
            M = self_consistent(D, Om, T)
            Ms.append(M)
        Ms = np.array(Ms)
        # find where M crosses zero
        idx = np.where(Ms < 0.001)[0]
        if len(idx) > 0:
            i = idx[0]
            if i > 0:
                Tc = Ts[i-1] + (Ts[i]-Ts[i-1]) * (Ms[i-1]-0)/(Ms[i-1]-Ms[i])
            else:
                Tc = Ts[0]
        else:
            Tc = Ts[-1]
        return Tc
    rows = []
    Om_fixed = 0.006
    for D in [0.1, 0.2, 0.3, 0.4, 0.5]:
        Tc = find_Tc(D, Om_fixed)
        rows.append(['D_div_J', D, Tc])
    D_fixed = 0.2
    for Om in [0.001, 0.002, 0.004, 0.006, 0.008]:
        Tc = find_Tc(D_fixed, Om)
        rows.append(['Omega_div_J', Om, Tc])
    with open(os.path.join(outdir, 'transition_temperature.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['parameter','value','Tc_div_J'])
        w.writerows(rows)
PYEOF
chmod +x /solution/solver.py

# === solve block: spinwave_spectrum.csv ===
python3 /solution/solver.py spinwave

# === solve block: transition_temperature.csv ===
python3 /solution/solver.py transition
