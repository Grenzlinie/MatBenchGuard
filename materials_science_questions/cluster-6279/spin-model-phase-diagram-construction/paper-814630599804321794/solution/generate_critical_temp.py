import sys, os, csv
sys.path.insert(0, '/solution')
import numpy as np
from scipy.optimize import brentq
from common import J0, K0, D, solve_self

def M_zero_T(T, h, zeta, eta):
    s, l = solve_self(T, zeta)
    denom = K0 * zeta - J0
    if denom == 0:
        return np.nan, np.nan
    sin2chi = -h / (denom * (s + l))
    if abs(sin2chi) > 1.0:
        return np.nan, np.nan
    cos2chi = np.sqrt(1.0 - sin2chi**2)
    xi = 1.0
    A0 = h*sin2chi - D + (3.0*s - l)*K0 - (s+l)*(J0*sin2chi**2 + zeta*K0*cos2chi**2) - (s-l)*(xi*J0 + eta*K0)
    B0 = (s - l) * cos2chi * (xi*J0 - eta*K0)
    C0 = h*cos2chi - (s+l)*sin2chi*cos2chi * (J0 - zeta*K0)
    D0 = (s - l) * sin2chi * (eta*K0 - xi*J0)
    E0 = C0
    F0 = 2.0 * s * sin2chi * (eta*K0 - xi*J0)
    G0 = -h*sin2chi - D + (3.0*s - l)*K0 + (s+l)*(J0*sin2chi**2 + zeta*K0*cos2chi**2) - 2.0*s*(xi*J0 + eta*K0)
    H0 = 2.0 * s * cos2chi * (eta*K0 - xi*J0)
    mat = np.array([
        [A0,  B0,  C0,  D0],
        [-B0, -A0, -D0, -C0],
        [E0,  F0,  G0,  H0],
        [-F0, -E0, -H0, -G0]
    ])
    detM = np.linalg.det(mat)
    L0 = A0**2 - B0**2 + G0**2 - H0**2 + 2.0*C0*E0 - 2.0*D0*F0
    return detM, L0

def find_T_crit(h, zeta, eta, T_low=0.1, T_high=2.0):
    def f(T):
        det, _ = M_zero_T(T, h, zeta, eta)
        return det
    try:
        fl = f(T_low)
        fh = f(T_high)
        if np.isnan(fl) or np.isnan(fh):
            return None
        if fl * fh > 0:
            for Tl in [0.05, 0.02, 0.01]:
                fl2 = f(Tl)
                if not np.isnan(fl2) and fl2 * fh < 0:
                    T_low = Tl
                    break
            else:
                return None
        T_root = brentq(f, T_low, T_high, xtol=1e-8)
        _, L0 = M_zero_T(T_root, h, zeta, eta)
        if L0 < 0:
            return T_root
    except:
        pass
    return None

h_vals = [2.5, 3.2, 3.8]
eta_fixed = 2.0
zeta_vals = np.linspace(1.0, 5.0, 50)
rows = []
for h in h_vals:
    for zeta in zeta_vals:
        T_c = find_T_crit(h, zeta, eta_fixed)
        if T_c is not None:
            rows.append([eta_fixed, zeta, h, T_c])

zeta_fixed = 3.0
eta_vals = np.linspace(1.0, 5.0, 50)
for h in h_vals:
    for eta in eta_vals:
        T_c = find_T_crit(h, zeta_fixed, eta)
        if T_c is not None:
            rows.append([eta, zeta_fixed, h, T_c])

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'critical_temp_anisotropy.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['eta', 'zeta', 'field', 'critical_temperature'])
    for row in rows:
        writer.writerow(row)
