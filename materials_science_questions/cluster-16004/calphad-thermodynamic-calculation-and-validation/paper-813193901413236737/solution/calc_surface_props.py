#!/usr/bin/env python3
"""Compute ternary surface properties via Butler's equation for the Co-Cr-Ni system."""
import sys, math
import numpy as np
from scipy.optimize import fsolve

R = 8.314
T = 1873.0
N_A = 6.02214e23
beta_tilde = 0.75

# Pure component densities (g/cm3) and molar masses (g/mol)
rho = {'Co':7.75, 'Cr':6.3, 'Ni':7.9}
M   = {'Co':58.933, 'Cr':51.996, 'Ni':58.693}

# Pure surface tensions (mN/m) -> converted to J/m2
sigma_mNm = {}
sigma_mNm['Co'] = 866.0 - 0.15*(T-933.0)
sigma_mNm['Cr'] = 1672.0 - 0.20*(T-2178.0)
sigma_mNm['Ni'] = 1838.0 - 0.42*(T-1728.0)
sigma_pure = {k: v*1e-3 for k,v in sigma_mNm.items()}   # J/m2

# Molar surface areas (m2/mol)
def molar_surface_area(elem):
    s_cm2 = 1.091 * N_A * (M[elem]/rho[elem])**(2/3)
    return s_cm2 * 1e-4   # m2/mol
S = {e: molar_surface_area(e) for e in ['Co','Cr','Ni']}

# Redlich-Kister polynomial coefficients: list of (v, A, B)
RK = {}
RK['CoCr'] = [(0, -12008.6239, 2.2019), (1, -5836.4696, 1.1402)]
RK['CrNi'] = [(0,  318.0,    -7.33),   (1,  16941.0,    -6.37)]
RK['CoNi'] = [(0,  1331.0,    0.0)]     # no v=1 term

def Gxs_binary(xi, xj, coeffs):
    """Excess Gibbs energy of a binary pair + partial derivatives w.r.t xi,xj."""
    d = xi - xj
    poly = 0.0
    dpoly = 0.0   # d(poly)/dd
    for v, A, B in coeffs:
        L = A + B*T
        poly += L * (d**v)
        if v > 0:
            dpoly += L * v * (d**(v-1))
    G = xi * xj * poly
    dG_dxi = xj * poly + xi * xj * dpoly
    dG_dxj = xi * poly - xi * xj * dpoly
    return G, dG_dxi, dG_dxj

def Gxs_ternary(xCo, xCr, xNi):
    """Ternary excess Gibbs energy and its gradients w.r.t. the three mole fractions."""
    G = 0.0
    dG = np.zeros(3)   # dG/dx_Co, dG/dx_Cr, dG/dx_Ni
    # Co-Cr
    g, dg_Co, dg_Cr = Gxs_binary(xCo, xCr, RK['CoCr'])
    G += g
    dG[0] += dg_Co
    dG[1] += dg_Cr
    # Cr-Ni
    g, dg_Cr, dg_Ni = Gxs_binary(xCr, xNi, RK['CrNi'])
    G += g
    dG[1] += dg_Cr
    dG[2] += dg_Ni
    # Co-Ni
    g, dg_Co, dg_Ni = Gxs_binary(xCo, xNi, RK['CoNi'])
    G += g
    dG[0] += dg_Co
    dG[2] += dg_Ni
    return G, dG

def partial_excess(xCo, xCr, xNi):
    """Return partial excess Gibbs energies for Co, Cr, Ni (J/mol)."""
    G, dG = Gxs_ternary(xCo, xCr, xNi)
    x = np.array([xCo, xCr, xNi])
    Gex = np.zeros(3)
    for i in range(3):
        s = 0.0
        for j in range(3):
            delta = 1.0 if i==j else 0.0
            s += (delta - x[j]) * dG[j]
        Gex[i] = G + s
    return Gex

def surface_from_logratios(present, uvars):
    """Convert log-ratio variables to surface mole fractions (length-3 array)."""
    x_s = np.zeros(3)
    if len(present) == 1:
        x_s[present[0]] = 1.0
    elif len(present) == 2:
        i, j = present
        u = uvars[0]
        x_i = 1.0 / (1.0 + np.exp(-u))
        x_s[i] = x_i
        x_s[j] = 1.0 - x_i
    else:      # three component
        u1, u2 = uvars
        e1 = np.exp(u1)
        e2 = np.exp(u2)
        denom = 1.0 + e1 + e2
        x_s[present[0]] = e1 / denom
        x_s[present[1]] = e2 / denom
        x_s[present[2]] = 1.0 / denom
    return x_s

def butler_residual(vars, present, bulks):
    """Residuals for fsolve: (sigma, u1, ..., u_{k-1}) -> k equations."""
    sigma = vars[0]
    uvars = vars[1:]
    
    x_s = surface_from_logratios(present, uvars)
    # surface excess: G_ex_s (surface) = beta_tilde * G_ex^b evaluated at x_s
    Gex_b_s = partial_excess(x_s[0], x_s[1], x_s[2])
    # bulk excess
    Gex_b_b = partial_excess(bulks[0], bulks[1], bulks[2])
    
    eqs = []
    for i, comp_idx in enumerate(present):
        elem = ['Co','Cr','Ni'][comp_idx]
        ln_term = math.log(x_s[comp_idx] / bulks[comp_idx])
        sigma_i = sigma_pure[elem] + (R*T*ln_term + (beta_tilde * Gex_b_s[comp_idx] - Gex_b_b[comp_idx])) / S[elem]
        eqs.append(sigma_i - sigma)
    return eqs

# Composition grid
compositions = []
for i in range(10):      # X_Cr = 0.0, 0.1, ..., 0.9
    for j in range(10):  # X_Ni = 0.0, 0.1, ..., 0.9
        xCr = i * 0.1
        xNi = j * 0.1
        if xCr + xNi <= 1.0:
            xCo = 1.0 - xCr - xNi
            compositions.append((xCo, xCr, xNi))

# Solve
header = ['bulk_X_Cr','bulk_X_Ni','bulk_X_Co','surface_tension_mN_per_m','surface_X_Cr','surface_X_Ni','surface_X_Co']
print(','.join(header))

for xCo, xCr, xNi in compositions:
    bulks = (xCo, xCr, xNi)
    
    # determine present components
    present = []
    if xCo > 0:
        present.append(0)
    if xCr > 0:
        present.append(1)
    if xNi > 0:
        present.append(2)
    
    if len(present) == 1:
        # pure component
        sigma = sigma_pure[['Co','Cr','Ni'][present[0]]] * 1e3   # J/m2 -> mN/m
        x_s = np.zeros(3)
        x_s[present[0]] = 1.0
    else:
        # initial guess
        sigma0 = np.mean([sigma_pure[['Co','Cr','Ni'][p]] for p in present])
        n_u = len(present)-1
        uvars0 = [0.0] * n_u
        guess = [sigma0] + uvars0
        try:
            sol = fsolve(lambda v: butler_residual(v, present, bulks), guess, xtol=1e-8, maxfev=1000)
        except Exception as e:
            # fallback: keep initial guess but ensure positivity
            sol = guess
            print(f"Warning: solver failed at Co={xCo}, Cr={xCr}, Ni={xNi}: {e}", file=sys.stderr)
        sigma = sol[0] * 1e3   # J/m2 -> mN/m
        uvars = sol[1:]
        x_s = surface_from_logratios(present, uvars)
        # clip tiny negatives and re-normalize
        x_s = np.maximum(x_s, 0.0)
        x_s /= x_s.sum()
    
    row = [f'{xCr:.10f}', f'{xNi:.10f}', f'{xCo:.10f}', f'{sigma:.6f}', f'{x_s[1]:.10f}', f'{x_s[2]:.10f}', f'{x_s[0]:.10f}']
    print(','.join(row))
