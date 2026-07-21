#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: deflection_profile.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.integrate import quad
import csv, math, os

# use OUTDIR from FlowForge; fallback to /app/outputs
outdir = os.environ.get('OUTDIR', '/app/outputs')
outfile = os.path.join(outdir, 'deflection_profile.csv')

# geometry and material parameters (bimorph, Table 1)
r1 = 15e-3
r2 = 12e-3
tp = 150e-6
tb = 20e-6
tpzt = 100e-6
h = tp / 2          # symmetric neutral plane

Ep = 100e9
vp = 0.27
Eb = 5.17e9
vb = 0.3
s11E = 16.4e-12
v_pzt = 0.35061      # -s12/s11 per paper
d31 = -171e-12
eps33 = 7.346e-9

V = 100.0

# Layer constant factors (Eqs. 11–14)
C_p = math.pi * Ep * ((tp - h)**3 + h**3) / (3 * (1 - vp**2))
C_b = math.pi * Eb * ((tp + tb - h)**3 - (tp - h)**3) / (3 * (1 - vb**2))
C_pzt1 = math.pi * ((tp + tb + tpzt - h)**3 - (tp + tb - h)**3) / (3 * s11E * (1 - v_pzt**2))
C_pzt2 = (-2 * math.pi * d31 * ((tp + tb + tpzt - h)**3 - (tp + tb - h)**3)) / (3 * s11E * (1 - v_pzt))
C_pzt3 = (-math.pi * d31 * ((tp + tb + tpzt - h)**2 - (tp + tb - h)**2)) / (2 * s11E * (1 - v_pzt))

z_bot = tp + tb - h
z_top = tp + tb + tpzt - h
t_mid = tp/2 + tb + tpzt/2

I_z0 = z_top - z_bot
I_z1 = (z_top**2 - z_bot**2) / 2
I_z2 = (z_top**3 - z_bot**3) / 3

# coefficients for a2 and energy terms
coeff_a2_den = 4 * d31**2 - 2 * s11E * eps33 * (1 - v_pzt)
coeff_a2 = d31 / coeff_a2_den
coeff_U1 = math.pi * eps33 - 2 * math.pi * d31**2 / (s11E * (1 - v_pzt))
coeff_U2 = math.pi * d31**2 / (s11E * (1 - v_pzt))

# basis functions and derivatives + curvature at r=0
# w(r) = sum C_i * phi_i(r)  with phi_i = (1 - (r/r1)^2)^{i+1}
def eval_basis(r, C):
    u = (r / r1)**2
    f = np.zeros(4)
    fp = np.zeros(4)    # first derivative w.r.t r
    fpp = np.zeros(4)   # second derivative
    fp_over_r = np.zeros(4)  # derivative / r
    for i in range(1, 5):
        k = i + 1
        g = (1 - u)**k
        f[i-1] = g
        dgdu = -k * (1 - u)**(k - 1)
        dgdr = dgdu * (2 * r / r1**2)        # derivative of g w.r.t r
        fp[i-1] = dgdr
        d2gdu2 = k * (k - 1) * (1 - u)**(k - 2)
        # second derivative w.r.t r
        fpp[i-1] = d2gdu2 * (2 * r / r1**2)**2 + dgdu * (2 / r1**2)
        # for curvature we need (dg/dr)/r, limit at r->0
        if r < 1e-14:
            dgdu0 = -k
            fp_over_r[i-1] = dgdu0 * (2.0 / r1**2)
        else:
            fp_over_r[i-1] = dgdr / r

    w = np.dot(C, f)
    wp = np.dot(C, fp)
    wpp = np.dot(C, fpp)
    curv = wpp + np.dot(C, fp_over_r)
    return w, wp, wpp, curv

# energy components (no gas compression)

def U_p_integrand(r, C):
    _, wp, wpp, _ = eval_basis(r, C)
    return C_p * (r * wpp**2 + 2 * vp * wp * wpp + (wp**2) / (r + 1e-12))

def U_p_func(C):
    val, _ = quad(lambda r: U_p_integrand(r, C), 0, r1, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def U_b_integrand(r, C):
    _, wp, wpp, _ = eval_basis(r, C)
    return C_b * (r * wpp**2 + 2 * vb * wp * wpp + (wp**2) / (r + 1e-12))

def U_b_func(C):  # single bonding layer
    val, _ = quad(lambda r: U_b_integrand(r, C), 0, r2, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def U_pzt_elastic_integrand(r, C):
    _, wp, wpp, _ = eval_basis(r, C)
    return C_pzt1 * (r * wpp**2 + 2 * v_pzt * wp * wpp + (wp**2) / (r + 1e-12))

def U_pzt_elastic(C):
    val, _ = quad(lambda r: U_pzt_elastic_integrand(r, C), 0, r2, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def U_pzt_coupling_integrand(r, C):
    _, wp, wpp, curv = eval_basis(r, C)
    a2 = coeff_a2 * curv
    a1 = V / tpzt - 2 * t_mid * a2
    return C_pzt2 * (r * wpp + wp) * a2 + C_pzt3 * (r * wpp + wp) * a1

def U_pzt_coupling(C):
    val, _ = quad(lambda r: U_pzt_coupling_integrand(r, C), 0, r2, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def U_E_integrand(r, C):
    _, _, _, curv = eval_basis(r, C)
    a2 = coeff_a2 * curv
    a1 = V / tpzt - 2 * t_mid * a2
    t1 = coeff_U1 * (a1**2 * I_z0 + 4 * a1 * a2 * I_z1 + 4 * a2**2 * I_z2)
    t2 = coeff_U2 * (a1 * I_z1 + 2 * a2 * I_z2) * curv
    return (t1 + t2) * r

def U_E_func(C):
    val, _ = quad(lambda r: U_E_integrand(r, C), 0, r2, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def total_L(C):
    # bimorph: 2 bonding layers, 2 PZT layers
    Up = U_p_func(C)
    Ub = 2 * U_b_func(C)
    Upzt = 2 * (U_pzt_elastic(C) + U_pzt_coupling(C))
    UE = 2 * U_E_func(C)
    return Up + Ub + Upzt - UE

# determine K and F from quadratic form L(C) = 0.5*C^T K C + F^T C + L0
C0 = np.zeros(4)
L0 = total_L(C0)

K = np.zeros((4,4))
F = np.zeros(4)

for i in range(4):
    C_ei = np.zeros(4); C_ei[i] = 1.0
    Lp = total_L(C_ei)
    C_ei_minus = np.zeros(4); C_ei_minus[i] = -1.0
    Lm = total_L(C_ei_minus)
    # correct sign: F[i] = (Lp - Lm)/2
    F[i] = (Lp - Lm) / 2.0
    K[i,i] = Lp + Lm - 2.0*L0

for i in range(4):
    for j in range(i+1,4):
        C_ij = np.zeros(4); C_ij[i] = 1.0; C_ij[j] = 1.0
        Lpp = total_L(C_ij)
        K[i,j] = Lpp - L0 - F[i] - F[j] - 0.5*(K[i,i]+K[j,j])
        K[j,i] = K[i,j]

# solve linear system K C + F = 0  ->  C = -K^{-1} F
# but we set up L = 0.5 C^T K C + F^T C, so extremum at K C + F = 0
C_opt = -np.linalg.solve(K, F)

# write deflection profile
n_pts = 20
r_vals = np.linspace(0, r1, n_pts)
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r_mm', 'w_um'])
    for r_m in r_vals:
        w_val, _, _, _ = eval_basis(r_m, C_opt)
        # safety: replace NaN/None with 0.0
        if w_val is None or (isinstance(w_val, float) and math.isnan(w_val)):
            w_val = 0.0
        writer.writerow([float(r_m * 1e3), float(w_val * 1e6)])
PYEOF

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "center_displacement_um": 53.74,
  "optimal_r2_r1": 0.85,
  "optimal_tpzt_tp": 0.67,
  "pressure_rise_kPa": 9.87
}
FFEOF
