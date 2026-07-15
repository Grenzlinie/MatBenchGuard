#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results.csv ===
cat <<'PYEOF' > /tmp/calc.py
import numpy as np, math, csv, os

mu0 = 4.0*math.pi*1e-7
R = 1.25e-6
Vp = 4.0/3.0*math.pi*R**3
phi = 0.11
mu_e = 1.0
mu_p = 1000.0
beta = (mu_p - mu_e)/(mu_p + 2.0*mu_e)
Ms = 1.7e6
C = 3.0*mu_e*mu0*beta*Vp   # factor in Fröhlich‑Kennelly law

eps = 1e-6   # finite‑difference step for gamma derivative

def index_range(length):
    """Return integer range for chain index according to paper parity rules."""
    if length % 2 == 1:
        return range(-(length-1)//2, (length-1)//2 + 1)
    else:
        return range(-(length//2-1), (length//2-1) + 1)

class BCTSum:
    def __init__(self, b, l):
        self.b = b
        self.l = l
        self.A_ranges = self._A_indices()
        self.B_ranges = self._B_indices()

    def _A_indices(self):
        return index_range(self.b), index_range(self.b), index_range(self.l)

    def _B_indices(self):
        b = self.b
        l = self.l
        B1 = [i for i in range(-((b-1)//2), ((b-1)//2)+1) if i != 0] if b%2==1 else [i for i in range(-(b//2-1), (b//2-1)+1) if i != 0]
        B2 = B1
        B3 = []
        if l%2==1:
            half = (l-1)//2
            B3 = [i for i in range(-half, half+1) if i != 0]
        else:
            half = l//2-1
            B3 = [i for i in range(-half, half+1) if i != 0]
        return B1, B2, B3

    def sum_f(self, gamma):
        s = 0.0
        sg, cg = math.sin(gamma), math.cos(gamma)
        # A chain
        for i, j, k in [(i,j,k) for i in self.A_ranges[0] for j in self.A_ranges[1] for k in self.A_ranges[2]]:
            if i==0 and j==0 and k==0:
                continue
            x = math.sqrt(6.0)*R*i + 2.0*R*k*sg
            y = math.sqrt(6.0)*R*j
            z = 2.0*R*k*cg
            r2 = x*x + y*y + z*z
            s += (2.0*z*z - x*x - y*y) / (4.0*math.pi*mu0 * r2**2.5)
        # B chain
        B1r, B2r, B3r = self.B_ranges
        for B1 in B1r:
            for B2 in B2r:
                for B3 in B3r:
                    x = (math.sqrt(6.0)/2.0)*(2*B1-1)*R + 2.0*(B3-1)*R*sg
                    y = (math.sqrt(6.0)/2.0)*(2*B2-1)*R
                    z = 2.0*(B3-1)*R*cg
                    r2 = x*x + y*y + z*z
                    s += (2.0*z*z - x*x - y*y) / (4.0*math.pi*mu0 * r2**2.5)
        return s

    def f_and_k(self, gamma, eps=1e-6):
        f0 = self.sum_f(gamma)
        f_plus = self.sum_f(gamma+eps)
        f_minus = self.sum_f(gamma-eps)
        k = (f_plus - f_minus)/(2.0*eps)
        return f0, k

# Precompute f,k for required b,gamma pairs
gammas_needed = [0.001, 0.003, 0.005]
bs_needed = [2,3,4,5,6,7]
Lmax = 200

f_cache = {}
k_cache = {}
for b in bs_needed:
    for gam in gammas_needed:
        flist = []
        klist = []
        for l in range(1, Lmax+1):
            summ = BCTSum(b, l)
            f, k = summ.f_and_k(gam, eps)
            flist.append(f)
            klist.append(k)
        f_cache[(b,gam)] = flist
        k_cache[(b,gam)] = klist

def solve_pz(H0, f):
    pz = 0.0
    for _ in range(100):
        Htot = H0 + f * pz
        p_new = C * Htot / (1.0 + C * Htot / Ms)
        if abs(p_new - pz) < 1e-20:
            break
        pz = p_new
    return pz

def compute_DeltaG(L, sigma, b, H0, gamma):
    sigma2 = sigma**2
    lvals = np.arange(1, 2*L+1)
    weights = lvals * np.exp(-(lvals - L)**2 / (2*sigma2))
    S = np.sum(weights)
    flist = f_cache[(b,gamma)]
    klist = k_cache[(b,gamma)]
    eps_f = 1e-8
    pz_list = np.zeros(2*L)
    dpz_df_list = np.zeros(2*L)
    for idx, l in enumerate(range(1, 2*L+1)):
        f0 = flist[l-1]
        pz0 = solve_pz(H0, f0)
        pz_list[idx] = pz0
        pz1 = solve_pz(H0, f0 + eps_f)
        dpz_df_list[idx] = (pz1 - pz0)/eps_f
    nll = b*b * lvals + (b-1)*(b-1) * (lvals - 1)
    n_over_V = (phi * np.exp(-(lvals - L)**2 / (2*sigma2))) / (Vp * (b*b + (b-1)*(b-1)) * S)
    J = np.sum(pz_list * nll * n_over_V)
    chi_eff = J / (mu0 * H0)
    k_vals = np.array(klist[:2*L])
    dchi_dgamma = np.sum(nll * n_over_V * dpz_df_list * k_vals) / (mu0 * H0)
    tau = -0.5 * mu0 * (H0/(1.0+chi_eff))**2 * dchi_dgamma
    DeltaG = tau / gamma
    return DeltaG

# Generate all conditions
rows = []
cond_id_num = 0

# (a) L variation
for L in range(10, 101, 10):
    for sigma in [3,6,9]:
        b = 2
        H0 = 1e6
        gamma = 0.003
        DeltaG = compute_DeltaG(L, sigma, b, H0, gamma)
        rows.append((f"a_L{L}_sigma{sigma}", L, sigma, b, H0/1e6, gamma, DeltaG/1e6))

# (b) b variation, sigma=9
sigma = 9
pairs = [(10,2), (20,3), (30,4), (40,5)]
for L,b in pairs:
    H0 = 1e6
    gamma = 0.003
    DeltaG = compute_DeltaG(L, sigma, b, H0, gamma)
    rows.append((f"b_exp_L{L}_b{b}", L, sigma, b, 1.0, gamma, DeltaG/1e6))
L = 30
for b in range(2,8):
    H0 = 1e6
    gamma = 0.003
    DeltaG = compute_DeltaG(L, sigma, b, H0, gamma)
    rows.append((f"b_cont_L30_b{b}", L, sigma, b, 1.0, gamma, DeltaG/1e6))

# (c) H0 variation, gamma variation
L = 30
sigma = 3
b = 2
for H0_MA in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]:
    H0 = H0_MA * 1e6
    for gamma in [0.001,0.003,0.005]:
        DeltaG = compute_DeltaG(L, sigma, b, H0, gamma)
        rows.append((f"c_H0_{H0_MA}_gamma_{gamma}", L, sigma, b, H0_MA, gamma, DeltaG/1e6))

os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["condition_id", "L", "sigma", "b", "H0", "gamma", "Delta_G"])
    for r in rows:
        w.writerow(r)
print("results.csv written")
PYEOF
python3 /tmp/calc.py
