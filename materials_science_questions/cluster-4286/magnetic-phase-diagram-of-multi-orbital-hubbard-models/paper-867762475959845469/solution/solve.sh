#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# Install required packages
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# Run core computation
python3 <<'PYEOF'
import numpy as np
from scipy.optimize import minimize, brentq

# ----- parameters -----
t = 0.3
E1 = -0.125
E2 = -0.25
S = 1.5
Sbar = S + 0.5  # 2.0

# ----- k-mesh -----
Nk = 18
kpts = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
kx, ky, kz = np.meshgrid(kpts, kpts, kpts, indexing='ij')

def dispersion(kx, ky, kz):
    cosx = np.cos(kx)
    cosy = np.cos(ky)
    cosz = np.cos(kz)
    term = cosx + cosy + cosz
    sq = np.sqrt(np.maximum(cosx**2 + cosy**2 + cosz**2 - cosx*cosy - cosy*cosz - cosz*cosx, 0.0) + 1e-12)
    eps_p = -2*t * (term + sq)
    eps_m = -2*t * (term - sq)
    return eps_p, eps_m

eps_p, eps_m = dispersion(kx, ky, kz)
eps0 = np.stack([eps_p, eps_m], axis=-1)  # (Nk,Nk,Nk,2)
Nk_tot = Nk**3

# Save band dispersion
np.save('/app/outputs/band_dispersion.npy', {'k': np.stack([kx, ky, kz], axis=-1), 'eps0': eps0})

# ----- helper functions -----
def coth(x):
    return 1.0 / np.tanh(x)

def B_a(z, a):
    if abs(z) < 1e-10:
        return (a+1)/(3*a) * z
    return (2*a+1)/(2*a) * coth((2*a+1)/(2*a)*z) - 1/(2*a) * coth(z/(2*a))

def gamma_Sbar(z, Sbar):
    if abs(z) < 1e-10:
        return 1.0
    return 0.5 + Sbar/(2*Sbar+1) * coth((2*Sbar+1)/(2*Sbar)*z) * (coth(z) - 1/(2*Sbar)*coth(z/(2*Sbar)))

def ferm(x):
    return 1.0/(1.0+np.exp(-np.clip(x, -100, 100)))

def log1pexp(x):
    out = np.empty_like(x)
    mask = x < 50
    out[mask] = np.log1p(np.exp(x[mask]))
    out[~mask] = x[~mask]
    return out

def ln_nu(z, Sbar):
    if abs(z) < 1e-10:
        return 0.0   # lim_{z->0} nu = 1, ln=0
    v = np.sinh(z)*coth(z/(2*Sbar)) + np.cosh(z)
    return np.log(v)

def ion_spin_entropy(lmbda, p_f, x, S, Sbar):
    p_p = 1.0 - p_f
    z_bar = lmbda * Sbar
    z_S = lmbda * S
    term_f = p_f * ( (1-x)*(ln_nu(z_bar, Sbar) - lmbda*Sbar*B_a(z_bar, Sbar)) + x*(ln_nu(z_S, S) - lmbda*S*B_a(z_S, S)) )
    term_p = p_p * ((1-x)*ln_nu(0.0, Sbar) + x*ln_nu(0.0, S))
    return -(term_f + term_p)

def free_energy(mu, lmbda, p_f, beta, x, eps0_flat, eps_p, S, Sbar):
    gamma_f = gamma_Sbar(lmbda*Sbar, Sbar)
    eps_bar = p_f * gamma_f * eps0_flat
    tmp = beta*(mu - eps_bar)
    omega_f = -0.5/beta * np.mean(np.sum(log1pexp(tmp), axis=1))
    omega_p = -1.0/beta * log1pexp(beta*(mu - eps_p))
    F = x*mu + omega_f + omega_p - (1.0/beta)*ion_spin_entropy(lmbda, p_f, x, S, Sbar)
    return F

def eq_x(mu, lmbda, p_f, beta, x, eps0_flat, eps_p):
    gamma_f = gamma_Sbar(lmbda*Sbar, Sbar)
    eps_bar = p_f * gamma_f * eps0_flat
    occ_f = 0.5 * np.mean(ferm(eps_bar - mu))
    occ_p = ferm(eps_p - mu)
    return occ_f + occ_p - x

def objective(params, beta, x, eps0_flat, eps_p, S, Sbar):
    lmbda, p_f = params
    if lmbda < 0 or not (0 <= p_f <= 1):
        return 1e9
    mu_low = -30.0
    mu_high = 30.0
    f_low = eq_x(mu_low, lmbda, p_f, beta, x, eps0_flat, eps_p)
    f_high = eq_x(mu_high, lmbda, p_f, beta, x, eps0_flat, eps_p)
    if f_low*f_high > 0:
        return 1e9
    mu = brentq(lambda mu: eq_x(mu, lmbda, p_f, beta, x, eps0_flat, eps_p), mu_low, mu_high, xtol=1e-6)
    return free_energy(mu, lmbda, p_f, beta, x, eps0_flat, eps_p, S, Sbar)

# ----- main loop -----
dopings = [0.175, 0.2, 0.25, 0.3, 0.35, 0.4]
T_vals = np.linspace(0.005, 0.06, 40)
eps0_flat = eps0.reshape(-1, 2)
eps_p_list = {x: (1/x - 1)*E1 + E2 for x in dopings}

all_x = []
all_T = []
all_M = []
all_pf = []

for x in dopings:
    eps_p = eps_p_list[x]
    Ms = []
    pfs = []
    for T in T_vals:
        beta = 1.0 / T
        res = minimize(lambda p: objective(p, beta, x, eps0_flat, eps_p, S, Sbar),
                       [1.5, 0.8], bounds=[(0, None), (0, 1)], method='L-BFGS-B',
                       options={'ftol':1e-8, 'maxiter':100})
        lmbda_opt, p_f_opt = res.x
        # find mu for optimal params
        mu_low=-30; mu_high=30
        mu_opt = brentq(lambda mu: eq_x(mu, lmbda_opt, p_f_opt, beta, x, eps0_flat, eps_p),
                        mu_low, mu_high, xtol=1e-6)
        M0 = Sbar - x/2
        Bsb = B_a(lmbda_opt*Sbar, Sbar)
        Bs = B_a(lmbda_opt*Sbar, S)
        M = (1-x)*Sbar*(p_f_opt*Bsb + (1-p_f_opt)*B_a(0,Sbar)) + x*S*(p_f_opt*Bs + (1-p_f_opt)*B_a(0,S))
        M_norm = M / M0
        Ms.append(M_norm)
        pfs.append(p_f_opt)
    all_x.append(x)
    all_T.append(T_vals.copy())
    all_M.append(Ms)
    all_pf.append(pfs)

# save raw results
np.savez('/app/outputs/raw_results.npz', x=all_x, T=all_T, M=all_M, p_f=all_pf)

# extract Tc (max -dM/dT)
Tc_vals = []
for i, x in enumerate(dopings):
    M_arr = np.array(all_M[i])
    T_arr = all_T[i]
    dM = -np.gradient(M_arr, T_arr)
    idx = np.argmax(dM)
    Tc_vals.append(T_arr[idx])

# save data for CSV generation
np.savez('/app/outputs/solve_results.npz', x=dopings, T=all_T, M=all_M, p_f=all_pf, Tc=Tc_vals)

print("Computation finished.")
PYEOF

# === solve block: magnetization_curves.csv ===
python3 <<'PYEOF'
import numpy as np, csv
data = np.load('/app/outputs/solve_results.npz')
x_vals = data['x']
T_vals = data['T']
M_vals = data['M']
out = '/app/outputs/magnetization_curves.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','T','M'])
    for i, x in enumerate(x_vals):
        for j, t in enumerate(T_vals[i]):
            w.writerow([x, t, M_vals[i][j]])
print('magnetization_curves.csv written')
PYEOF

# === solve block: phase_diagram.csv ===
python3 <<'PYEOF'
import numpy as np, csv
data = np.load('/app/outputs/solve_results.npz')
x_vals = data['x']
Tc_vals = data['Tc']
out = '/app/outputs/phase_diagram.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','Tc'])
    for i, x in enumerate(x_vals):
        w.writerow([x, Tc_vals[i]])
print('phase_diagram.csv written')
PYEOF

# === solve block: zener_fraction.csv ===
python3 <<'PYEOF'
import numpy as np, csv
data = np.load('/app/outputs/solve_results.npz')
x_vals = data['x']
T_vals = data['T']
p_f_vals = data['p_f']
target_x = 0.3
idx = list(x_vals).index(target_x)
T_arr = T_vals[idx]
pf_arr = p_f_vals[idx]
out = '/app/outputs/zener_fraction.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T','p_f'])
    for t, pf in zip(T_arr, pf_arr):
        w.writerow([t, pf])
print('zener_fraction.csv written')
PYEOF
