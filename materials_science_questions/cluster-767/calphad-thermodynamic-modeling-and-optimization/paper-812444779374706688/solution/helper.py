import numpy as np
from scipy.optimize import fsolve
import csv
import sys
import os

R = 8.314462618  # J/mol·K

# ------------- binary mixing parameters (Zn-Sn, Zn-Se, Sn-Se) -------------
def M_H_ZnSn(xZn, xSn):
    if xZn <= 0 or xSn <= 0: return 0.0
    d = xZn - xSn
    poly = 2.360 + 0.907*d + 0.216*d**2
    return xZn * xSn * poly * 4.184 * 1000  # J/mol

def xs_S_ZnSn(xZn, xSn):
    if xZn <= 0 or xSn <= 0: return 0.0
    d = xZn - xSn
    poly = 1.42 + 0.58*d + 0.12*d**2
    return xZn * xSn * poly * 4.184  # J/mol·K

def M_H_ZnSe(xZn, xSe):
    if xZn <= 0 or xSe <= 0: return 0.0
    d = xZn - xSe
    poly = 17.663 - 8.782*d + 8.525*d**2
    return xZn * xSe * poly * 4.184 * 1000

def xs_S_ZnSe(xZn, xSe):
    if xZn <= 0 or xSe <= 0: return 0.0
    d = xZn - xSe
    poly = 4.10 - 0.73*d
    return xZn * xSe * poly * 4.184

def M_H_SnSe(xSn, xSe):
    if xSn <= 0 or xSe <= 0: return 0.0
    d = xSn - xSe
    poly = 5.086 + 2.936*d - 3.846*d**2
    return xSn * xSe * poly * 4.184 * 1000

def xs_S_SnSe(xSn, xSe):
    if xSn <= 0 or xSe <= 0: return 0.0
    d = xSn - xSe
    poly = -0.05 + 0.63*d
    return xSn * xSe * poly * 4.184

# ------------- ternary interaction coefficients (Table 2) ------------
alpha_Zn = 2742 * 4.184 * 1000  # J/mol
alpha_Sn = 3787 * 4.184 * 1000
alpha_Se = -3885 * 4.184 * 1000
beta_Zn = -60.6 * 4.184 * 1000   # J/mol·K
beta_Sn = 2.9 * 4.184 * 1000
beta_Se = 55.8 * 4.184 * 1000

def ternary_term(xZn, xSn, xSe, T):
    s = ( (alpha_Zn - beta_Zn*T)*xZn +
          (alpha_Sn - beta_Sn*T)*xSn +
          (alpha_Se - beta_Se*T)*xSe )
    return xZn * xSn * xSe * s

# ------------- total excess Gibbs energy per mole of atoms ------------
def G_ex_total(xZn, xSn, T):
    xSe = 1.0 - xZn - xSn
    # clamp small negative values
    if xZn < -1e-12 or xSn < -1e-12 or xSe < -1e-12:
        return 0.0
    xZn = max(0.0, min(1.0, xZn))
    xSn = max(0.0, min(1.0, xSn))
    xSe = 1.0 - xZn - xSn
    if xSe < 0.0:
        xSe = 0.0
    G_ZnSn = M_H_ZnSn(xZn, xSn) - T * xs_S_ZnSn(xZn, xSn)
    G_ZnSe = M_H_ZnSe(xZn, xSe) - T * xs_S_ZnSe(xZn, xSe)
    G_SnSe = M_H_SnSe(xSn, xSe) - T * xs_S_SnSe(xSn, xSe)
    G_tern = ternary_term(xZn, xSn, xSe, T)
    return G_ZnSn + G_ZnSe + G_SnSe + G_tern

# ------------- excess chemical potentials via numerical differentiation ------------
def mu_excess(xZn, xSn, T):
    xSe = 1.0 - xZn - xSn
    eps = 1e-6
    G0 = G_ex_total(xZn, xSn, T)
    dGdx1 = (G_ex_total(xZn+eps, xSn, T) - G_ex_total(xZn-eps, xSn, T)) / (2*eps)
    dGdx2 = (G_ex_total(xZn, xSn+eps, T) - G_ex_total(xZn, xSn-eps, T)) / (2*eps)
    dGdx3 = -dGdx1 - dGdx2
    common = xZn*dGdx1 + xSn*dGdx2 + xSe*dGdx3
    mu1 = G0 + dGdx1 - common
    mu2 = G0 + dGdx2 - common
    mu3 = G0 + dGdx3 - common
    return mu1, mu2, mu3

# ------------- solid reference states ------------
T_Zn_melt = 692.73
L_Zn_F = 1750.0  # J/mol
S_Zn_F = L_Zn_F / T_Zn_melt  # J/mol·K
T_Sn_melt = 505.08
L_Sn_F = 1720.0  # J/mol
S_Sn_F = L_Sn_F / T_Sn_melt

# ZnSe solid
S_ZnSe_F = 4.47   # J/mol·K (per ZnSe formula unit)
T_ZnSe_F = 1788.0  # K
def G_ZnSe_solid(T):
    return S_ZnSe_F * (T - T_ZnSe_F)  # J per mole ZnSe

# ------------- binary eutectic ------------
def equations_binary_eutectic(p):
    xZn, T = p[0], p[1]
    xSn = 1.0 - xZn
    mu_Zn_ex, mu_Sn_ex, _ = mu_excess(xZn, xSn, T)
    # chemical potential of Zn in liquid vs solid Zn
    eq1 = R*T*np.log(xZn) + mu_Zn_ex - (-S_Zn_F*(T - T_Zn_melt))
    # chemical potential of Sn in liquid vs solid Sn
    eq2 = R*T*np.log(xSn) + mu_Sn_ex - (-S_Sn_F*(T - T_Sn_melt))
    return [eq1, eq2]

def solve_eutectic():
    # initial guess
    guess = [0.15, 460.0]
    sol = fsolve(equations_binary_eutectic, guess, maxfev=1000, xtol=1e-12)
    xZn, T = sol
    return T, xZn

# ------------- ternary liquidus point for given x (x_Zn=x_Se=x) ------------
def liquidus_ternary_eq(T, x):
    xZn = x
    xSn = 1.0 - 2*x
    mu_Zn_ex, _, mu_Se_ex = mu_excess(xZn, xSn, T)
    lhs = 2.0 * R * T * np.log(x) + mu_Zn_ex + mu_Se_ex
    rhs = G_ZnSe_solid(T)
    return lhs - rhs

def solve_ternary_liquidus(x):
    # initial temperature guess
    T_guess = 1100.0 + 2000.0 * x
    T_sol, = fsolve(lambda T: liquidus_ternary_eq(T, x), T_guess, maxfev=1000, xtol=1e-12)
    return T_sol

# =============== main ===============
if __name__ == '__main__':
    mode = sys.argv[1]
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)

    if mode == 'binary':
        T_eut, x_eut = solve_eutectic()
        with open(os.path.join(outdir, 'step_01_binary_eutectic.csv'), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['eutectic_temperature_K', 'eutectic_Zn_mole_fraction'])
            writer.writerow([T_eut, x_eut])
    elif mode == 'ternary':
        x_list = np.arange(0.005, 0.051, 0.0025)
        temps = []
        for x in x_list:
            T = solve_ternary_liquidus(x)
            temps.append(T)
        with open(os.path.join(outdir, 'step_01_ternary_liquidus.csv'), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['temperature_K', 'mole_fraction_ZnSe'])
            for x, T in zip(x_list, temps):
                writer.writerow([T, x])
    else:
        raise ValueError("Unknown mode")
