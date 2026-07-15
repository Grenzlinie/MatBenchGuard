#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phase_diagram_data.csv ===
python3 << 'PYEOF' > "$OUTDIR/phase_diagram_data.csv"
import numpy as np
from scipy.optimize import fsolve, minimize_scalar

# ── helpers ──────────────────────────────────────────────────────
def kappa_from_theta(k1, theta):
    """Solve theta = (k1-1)^{-1} (k1/k2 - k2) for k2 >= 1."""
    a = 1.0
    b = theta * (k1 - 1.0)
    c = -k1
    disc = b*b - 4*a*c
    return (-b + np.sqrt(disc)) / (2*a)

def uniaxial_f(vars, rho_star, k1, k2):
    u, v = vars
    r = 0.5 - u - v
    psi2 = 2 * (u*k2 + v*k1 + r*k1*k2)
    eta = rho_star * psi2
    if eta >= 1.0:
        return [1e6, 1e6]
    y = rho_star / (1.0 - eta)
    s = 0.5*(k1+k2) - (k1-1)*u - (k2-1)*v
    xi1 = y * (k2*(1 + y*s*s) + (k2+1)*s)
    xi2 = y * (k1*(1 + y*s*s) + (k1+1)*s)
    xi3 = y * (k1*k2*(1 + y*s*s) + (k1+k2)*s)
    C = 2 * (np.exp(-xi1) + np.exp(-xi2) + np.exp(-xi3))
    f1 = u - np.exp(-xi1) / C
    f2 = v - np.exp(-xi2) / C
    return [f1, f2]

def det_condition(u, v, rho_star, k1, k2):
    r = 0.5 - u - v
    psi2 = 2 * (u*k2 + v*k1 + r*k1*k2)
    eta = rho_star * psi2
    if eta >= 1.0:
        return 1e6
    y = rho_star / (1.0 - eta)
    lhs = 1.0 / y
    rhs = u*(k2-1)**2 + v*(k1-1)**2 + r*(k1-k2)**2
    return lhs - rhs

def solve_uniaxial(rho_star, k1, k2):
    guess = [0.1, 0.1]
    sol = fsolve(lambda x: uniaxial_f(x, rho_star, k1, k2), guess, maxfev=200, xtol=1e-12)
    return sol

# ── NuNb spinodal finder ─────────────────────────────────────────
def find_NuNb_spinodal(k1, k2):
    def f(rho):
        try:
            u, v = solve_uniaxial(rho, k1, k2)
        except:
            return 1e6
        return det_condition(u, v, rho, k1, k2)
    # search in [0.01, 10]
    rho_vals = np.logspace(-2, 1, 200)
    signs = []
    for r in rho_vals:
        try:
            u, v = solve_uniaxial(r, k1, k2)
            signs.append(det_condition(u, v, r, k1, k2))
        except:
            signs.append(1e6)
    signs = np.array(signs)
    for i in range(len(signs)-1):
        if signs[i]*signs[i+1] < 0:
            rho_l, rho_h = rho_vals[i], rho_vals[i+1]
            try:
                from scipy.optimize import brentq
                return brentq(lambda r: f(r), rho_l, rho_h, xtol=1e-12)
            except:
                return None
    return None

# ── nonuniform spinodal (determinant scan) ───────────────────────
def build_T(qx, qy, gamma, y, psi1x, psi1y, kappa_matrix):
    # kappa_matrix: shape (6,2) for x,y components
    # compute weight functions
    def chi0(x):
        return np.cos(x)
    def chi1(x):
        return np.where(np.abs(x)<1e-12, 1.0, np.sin(x)/x)
    
    w0 = np.zeros(6)
    w2 = np.zeros(6)
    w1x = np.zeros(6)
    w1y = np.zeros(6)
    for i in range(6):
        kx, ky = kappa_matrix[i]
        w0[i] = chi0(qx*kx/2) * chi0(qy*ky/2)
        w2[i] = kx*ky * chi1(qx*kx/2) * chi1(qy*ky/2)
        w1x[i] = kx * chi1(qx*kx/2) * chi0(qy*ky/2)
        w1y[i] = ky * chi0(qx*kx/2) * chi1(qy*ky/2)
    
    # T matrix (6x6)
    T = np.eye(6)
    for i in range(6):
        for j in range(6):
            if gamma[i]*gamma[j] == 0: continue
            factor = y * np.sqrt(gamma[i]*gamma[j])
            term = (w0[i]*w2[j] + w2[i]*w0[j])
            term += (w1x[i]*w1y[j] + w1y[i]*w1x[j])
            term += y * (psi1y*(w1x[i]*w2[j] + w2[i]*w1x[j]) + psi1x*(w1y[i]*w2[j] + w2[i]*w1y[j]))
            term += (1 + 2*y*psi1x*psi1y) * w2[i]*w2[j]
            T[i,j] += factor * term
    return T

def solve_equilibrium_gamma(rho_star, k1, k2):
    # self-consistent iteration for gamma_μν
    # species order: xy, xz, yx, yz, zx, zy
    # kappa^τ for each species:
    # (x,y): κ^x = k1, κ^y = k2
    # (x,z): κ^x = k1, κ^y = 1
    # (y,x): κ^x = k2, κ^y = k1
    # (y,z): κ^x = k2, κ^y = 1
    # (z,x): κ^x = 1,  κ^y = k1
    # (z,y): κ^x = 1,  κ^y = k2
    kx = np.array([k1, k1, k2, k2, 1.0, 1.0])
    ky = np.array([k2, 1.0, k1, 1.0, k1, k2])
    # initial uniform guess
    gamma = np.ones(6) / 6.0
    for it in range(2000):
        psi2 = np.sum([gamma[0]+gamma[1], gamma[0]+gamma[2], gamma[1]+gamma[3], gamma[2]+gamma[3], gamma[4]+gamma[5]], axis=0) * 0  # tricky, need explicit
        # Actually use formulas: psi1x = (g0+g1)*k1 + (g2+g4)*k2 + g5+g3
        # psi1y = (g2+g3)*k1 + (g0+g5)*k2 + g4+g1
        # psi2  = (g0+g2)*k1*k2 + (g1+g3)*k1 + (g4+g5)*k2
        psi1x = (gamma[0]+gamma[1])*k1 + (gamma[2]+gamma[4])*k2 + gamma[3]+gamma[5]
        psi1y = (gamma[2]+gamma[3])*k1 + (gamma[0]+gamma[5])*k2 + gamma[1]+gamma[4]
        psi2  = (gamma[0]+gamma[2])*k1*k2 + (gamma[1]+gamma[3])*k1 + (gamma[4]+gamma[5])*k2
        eta = rho_star * psi2
        if eta >= 1.0:
            gamma[:] = 1e-9
            return gamma, psi1x, psi1y, rho_star/(1-1e-12)
        y = rho_star / (1.0 - eta)
        # compute chi
        chi = np.zeros(6)
        for i in range(6):
            chi[i] = y * (psi1x*ky[i] + psi1y*kx[i] + (1+y*psi1x*psi1y)*kx[i]*ky[i])
        exp_chi = np.exp(-chi)
        Z = np.sum(exp_chi)
        gamma_new = exp_chi / Z
        delta = np.max(np.abs(gamma_new - gamma))
        gamma = gamma_new
        if delta < 1e-12:
            break
    return gamma, psi1x, psi1y, y

def min_det_for_rho(rho_star, k1, k2):
    gamma, psi1x, psi1y, y = solve_equilibrium_gamma(rho_star, k1, k2)
    kx = np.array([k1, k1, k2, k2, 1.0, 1.0])
    ky = np.array([k2, 1.0, k1, 1.0, k1, k2])
    kappa_mat = np.column_stack([kx, ky])
    def obj(qx):
        qy = 0.0
        T = build_T(qx, qy, gamma, y, psi1x, psi1y, kappa_mat)
        return np.abs(np.linalg.det(T))
    # search over qx from 0.1 to 30
    res = minimize_scalar(obj, bounds=(0.1, 30), method='bounded')
    # also try qy direction
    def obj_y(qy):
        qx = 0.0
        T = build_T(qx, qy, gamma, y, psi1x, psi1y, kappa_mat)
        return np.abs(np.linalg.det(T))
    res2 = minimize_scalar(obj_y, bounds=(0.1, 30), method='bounded')
    return min(res.fun, res2.fun)

def find_nonuniform_spinodal(k1, k2):
    rho_vals = np.logspace(-2, 1, 200)
    dets = []
    for r in rho_vals:
        d = min_det_for_rho(r, k1, k2)
        dets.append(d)
    dets = np.array(dets)
    for i in range(len(dets)-1):
        if dets[i] < 1e-6 and dets[i+1] < 1e-6: # crude crossing, actually find where it first drops near zero
            return rho_vals[i]
        if dets[i] < 1e-2 and dets[i+1] < 1e-2:
            return (rho_vals[i]+rho_vals[i+1])/2
    return None

# ── main ─────────────────────────────────────────────────────────
kappas = [5, 10, 20, 55, 70]
theta_vals = np.arange(-1.0, 1.01, 0.2)

print("kappa1,theta,rho_star,transition_type")
for k1 in kappas:
    for th in theta_vals:
        k2 = kappa_from_theta(k1, th)
        # NuNb spinodal
        rho_nunb = find_NuNb_spinodal(k1, k2)
        if rho_nunb is not None:
            print(f"{k1},{th:.1f},{rho_nunb:.8f},NuNb")
        # nonuniform spinodal
        rho_nu = find_nonuniform_spinodal(k1, k2)
        if rho_nu is not None:
            print(f"{k1},{th:.1f},{rho_nu:.8f},nonuniform")
PYEOF
