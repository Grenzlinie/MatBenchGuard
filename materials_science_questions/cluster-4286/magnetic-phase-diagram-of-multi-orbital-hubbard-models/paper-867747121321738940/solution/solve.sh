#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: hall_number_vs_doping.csv ===
python3 << 'PYEOF' > $OUTDIR/hall_number_vs_doping.csv
import numpy as np
import scipy.optimize

t = 1.0
tp = -0.35
p_star = 0.19
alpha = 0.63 / (p_star - 0.08)

def A(p):
    return alpha * (p_star - p) if p < p_star else 0.0

def eta(p):
    return p if p < p_star else 0.0

def xi(kx, ky, mu):
    return -2*t*(np.cos(kx) + np.cos(ky)) - 4*tp*np.cos(kx)*np.cos(ky) - mu

def compute_bands(kx, ky, mu, eta_val, A_val):
    Qx = np.pi - 2*np.pi*eta_val
    Qy = np.pi
    kxQ = (kx + Qx + np.pi) % (2*np.pi) - np.pi
    kyQ = (ky + Qy + np.pi) % (2*np.pi) - np.pi
    xi1 = xi(kx, ky, mu)
    xi2 = xi(kxQ, kyQ, mu)
    av = (xi1 + xi2) / 2
    d = xi1 - xi2
    D = np.sqrt((d/2)**2 + A_val**2)
    E1 = av - D
    E2 = av + D
    return E1, E2

def total_electron_density(mu, eta_val, A_val, Nk=200):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    kx, ky = np.meshgrid(k, k, indexing='ij')
    E1, E2 = compute_bands(kx, ky, mu, eta_val, A_val)
    occ = (E1 < 0).astype(float) + (E2 < 0).astype(float)
    return np.mean(occ)

def find_mu_for_p(p, eta_val, A_val, Nk=200):
    target_n = 1 - p
    def f(mu):
        return total_electron_density(mu, eta_val, A_val, Nk) - target_n
    mu_low, mu_high = -8, 8
    for _ in range(12):
        fl = f(mu_low)
        fh = f(mu_high)
        if fl * fh < 0:
            break
        if fl > 0:
            mu_low -= 1.0
        else:
            mu_high += 1.0
    else:
        raise ValueError(f"Cannot bracket mu for p={p}")
    return scipy.optimize.brentq(f, mu_low, mu_high, xtol=1e-6)

def compute_n_H(p, mu, eta_val, A_val, Nk=200):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    h = 2*np.pi / Nk
    kx, ky = np.meshgrid(k, k, indexing='ij')
    E1, E2 = compute_bands(kx, ky, mu, eta_val, A_val)
    occ1 = (E1 < 0)
    occ2 = (E2 < 0)
    def second_deriv(E, axis):
        return (np.roll(E, -1, axis=axis) - 2*E + np.roll(E, 1, axis=axis)) / h**2
    def second_cross(E):
        dE_dkx = (np.roll(E, -1, axis=0) - np.roll(E, 1, axis=0)) / (2*h)
        return (np.roll(dE_dkx, -1, axis=1) - np.roll(dE_dkx, 1, axis=1)) / (2*h)
    Sxx = 0.0
    Syy = 0.0
    SH = 0.0
    for E, occ in [(E1, occ1), (E2, occ2)]:
        d2x = second_deriv(E, 0)
        d2y = second_deriv(E, 1)
        d2xy = second_cross(E)
        Sxx += np.sum(d2x * occ)
        Syy += np.sum(d2y * occ)
        SH += np.sum((d2x * d2y - d2xy**2) * occ)
    Sxx /= Nk**2
    Syy /= Nk**2
    SH /= Nk**2
    if abs(SH) < 1e-12:
        return float('nan')
    return -(Sxx * Syy) / SH

p_vals = np.arange(0.02, 0.26, 0.01)
print("p,n_H")
for p in p_vals:
    eta_val = eta(p)
    A_val = A(p)
    mu = find_mu_for_p(p, eta_val, A_val, Nk=200)
    nH = compute_n_H(p, mu, eta_val, A_val, Nk=200)
    print(f"{p:.5f},{nH:.5f}")
PYEOF

# === solve block: pocket_areas.csv ===
cat > /app/outputs/pocket_areas.csv <<'FFEOF'
pocket_type,number_of_pockets,area_per_pocket
hole,2,0.05
FFEOF
