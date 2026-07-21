#!/usr/bin/env python3
"""Helper to compute engineering model outputs."""
import sys, csv
import numpy as np
from scipy.optimize import fsolve, brentq
from scipy.special import arccosh

def g_func(omega):
    if omega > 1.0:
        return arccosh(omega) / (omega * np.sqrt(omega*omega - 1.0))
    else:
        return np.arccos(omega) / (omega * np.sqrt(1.0 - omega*omega))

# Powers constants
rho_a = 3.13
kappa_w = 1.31
kappa_h = 2.13

# Engineering model parameters
E_h = 25.3   # GPa
nu_h = 0.29
k_h = E_h / (3.0 * (1.0 - 2.0*nu_h))
mu_h = E_h / (2.0 * (1.0 + nu_h))
omega_h = 0.013        # oblate

omega_cp = 6.0          # prolate

# Clinker
E_a = 135.0
nu_a = 0.3
k_a = E_a / (3.0 * (1.0 - 2.0*nu_a))
mu_a = E_a / (2.0 * (1.0 + nu_a))

# Diffusivity
D_h_over_Dbulk = 5.04e-4
D_cp_over_Dbulk = 1.0
D_a_over_Dbulk = 0.0

def powers_volumes(wc, alpha):
    denom = 1.0 + rho_a * wc
    f_a = (1.0 - alpha) / denom
    f_h = kappa_h * alpha / denom
    f_cp = (rho_a * wc + (1.0 - kappa_h) * alpha) / denom
    return f_a, f_h, f_cp

def alpha_max_external(wc):
    crit = (kappa_h - 1.0) / rho_a  # ~0.36
    if wc <= crit:
        return min(1.0, (rho_a * wc) / (kappa_h - 1.0))
    else:
        return 1.0

# Elasticity self-consistent helpers
def S_elastic_components(omega, nu):
    gv = g_func(omega)
    w2 = omega * omega
    denom = 2.0 * (w2 - 1.0)
    F0 = w2 * (1.0 - gv) / denom
    F1 = w2 * ((2.0*w2 + 1.0)*gv - 3.0) / (8.0 * (w2 - 1.0)**2)
    Sp = np.zeros(6)
    Sp[0] = F0 + 2.0*F1
    Sp[1] = (1.0 - nu)*(1.0 - 2.0*F0) + 4.0*F1
    Sp[2] = (1.5 - 2.0*nu)*F0 + F1
    Sp[3] = (1.0 - nu)*(1.0 - F0) - 4.0*F1
    Sp[4] = nu*(1.0 - 2.0*F0) - 2.0*F1
    Sp[5] = nu*F0 - 2.0*F1
    S = Sp / (1.0 - nu)
    return S

def compute_A_components(kr, mur, S):
    # Walpole double contraction and inverse
    delta_kr = kr - 1.0
    delta_mur = mur - 1.0
    J = np.array([2.0/3, 1.0/3, 0.0, 0.0, 1.0/3, 1.0/3])
    K = np.array([1.0/3, 2.0/3, 1.0, 1.0, -1.0/3, -1.0/3])
    T = delta_kr * J + delta_mur * K
    ST = np.zeros(6)
    ST[0] = S[0]*T[0] + 2.0*S[5]*T[4]
    ST[1] = S[1]*T[1] + 2.0*S[4]*T[5]
    ST[2] = S[2]*T[2]
    ST[3] = S[3]*T[3]
    ST[4] = S[4]*T[0] + S[1]*T[4]
    ST[5] = S[5]*T[1] + S[0]*T[5]
    I_comp = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0])
    B = I_comp + ST
    delta = B[0]*B[1] - 2.0*B[4]*B[5]
    A = np.zeros(6)
    A[0] = B[1] / delta
    A[1] = B[0] / delta
    A[2] = 1.0 / B[2] if abs(B[2])>1e-15 else 0.0
    A[3] = 1.0 / B[3] if abs(B[3])>1e-15 else 0.0
    A[4] = -B[4] / delta
    A[5] = -B[5] / delta
    return A

# coefficients a_c, b_c from (A.11)
a_c = np.array([2.0/3, 1.0/3, 0.0, 0.0, 2.0/3, 2.0/3])   # a1=2/3, a2=1/3? wait: a1=2/3, a2=1/3, a5=a6=2/3. let's check: a1=2 a2 = a5=a6=2/3, so a2=1/3. correct.
b_c = np.array([2.0/15, 2.0/15, 2.0/5, 2.0/5, -2.0/15, -2.0/15])  # b1=2/15, b2=2/15, b3=2/5, b4=2/5, b5=-2/15, b6=-2/15. Actually b2=2 b1=-b5=-b6=2/15. So b2=2/15? Wait b2=2*2/15=4/15? Let's check: b2=2 b1=-b5=-b6=2/15 => b1=2/15? No: b2=2 b1, and b1=2/15? Let's re-derive: They give b2=2 b1=-b5=-b6=2/15. That means b2=2/15? Actually it says b2=2 b1=-b5=-b6=2/15. So b2 = 2/15, b1 = 1/15? But later b3=b4=2/5. So correct: b1=1/15? Wait reading: b2=2 b1 = -b5 = -b6 = 2/15. So b2=2/15, b1= b2/2 = 1/15? But then b2=2/15, b1=1/15, b5=-2/15, b6=-2/15. But they also say b2=2 b1, so 2/15 = 2*(1/15). Yes. So b1=1/15. But then -b5=2/15 => b5=-2/15. So b = [1/15, 2/15, 2/5, 2/5, -2/15, -2/15]? Let's double-check the paper: b2=2 b1=-b5=-b6=2/15. So b2 = 2/15, b1 = b2/2 = 1/15. b5 = -2/15, b6 = -2/15. That's consistent. And b3=b4=2/5. So final b array = [1/15, 2/15, 2/5, 2/5, -2/15, -2/15]. But earlier I wrote [2/15, 2/15,...] which is wrong. I'll correct.
# Actually from the paper: b2=2 b1 = -b5 = -b6 = 2/15. So b2 = 2/15, b1 = 1/15. And b3=b4=2/5. So:
b_c = np.array([1.0/15, 2.0/15, 2.0/5, 2.0/5, -2.0/15, -2.0/15])
# But wait, re-evaluate: The text: "b2=2 b1=-b5=-b6=2/15 ; b3=b4=2/5". So that gives b1 = (2/15)/2 = 1/15. So yes.

# However, I'll re-check with symmetry: The sums we compute should give correct percolation? Let's trust the paper.

# Now foam elastic solver
def elastic_foam_residual(vars, phi, kh, muh, omegah, omegap, kp=0.0, mup=0.0):
    ksc, musc = vars
    if ksc <= 0 or musc <= 0:
        return [1e6, 1e6]
    nu_sc = (3*ksc - 2*musc) / (2*(3*ksc + musc)) if (3*ksc+musc)!=0 else 0.5
    Sh = S_elastic_components(omegah, nu_sc)
    Sp = S_elastic_components(omegap, nu_sc)
    # hydrates
    krh = kh / ksc
    murh = muh / musc
    Ah = compute_A_components(krh, murh, Sh)
    f1_h_sum = np.sum(a_c * Ah)
    f2_h_sum = np.sum(b_c * Ah)
    # pores (stiffness zero; handle small)
    krp = 0.0   # kp/ksc
    murp = 0.0  # mup/musc
    Ap = compute_A_components(krp, murp, Sp)
    f1_p_sum = np.sum(a_c * Ap)
    f2_p_sum = np.sum(b_c * Ap)

    f1 = (1-phi) * (kh - ksc) * f1_h_sum + phi * (kp - ksc) * f1_p_sum
    f2 = (1-phi) * (muh - musc) * f2_h_sum + phi * (mup - musc) * f2_p_sum
    return [f1, f2]

def solve_elastic_foam(phi):
    if phi >= 1.0:
        return 0.0, 0.0
    if phi <= 0.0:
        return kh, muh
    k0 = (1-phi) * kh + 1e-6
    mu0 = (1-phi) * muh + 1e-6
    try:
        sol = fsolve(lambda x: elastic_foam_residual(x, phi, kh, muh, omegah, omegap), [k0, mu0],
                     maxfev=1000, xtol=1e-12)
        kf, muf = sol
        if kf <= 0 or muf <= 0 or not np.isfinite(kf) or not np.isfinite(muf):
            return (1-phi)*kh, (1-phi)*muh
        return kf, muf
    except Exception:
        return (1-phi)*kh, (1-phi)*muh

def mori_tanaka_elastic(kf, muf, fa):
    if fa <= 0:
        return kf, muf
    alpha_f = 3*kf / (3*kf + 4*muf) if (3*kf+4*muf)!=0 else 0.0
    beta_f = 6.0/5.0 * (kf + 2*muf) / (3*kf + 4*muf) if (3*kf+4*muf)!=0 else 0.0
    kcem = kf * (1 + fa * (ka - kf) / (kf + (1-fa)*alpha_f*(ka - kf))) if abs(kf+(1-fa)*alpha_f*(ka-kf))>1e-15 else kf
    mucem = muf * (1 + fa * (mu_a - muf) / (muf + (1-fa)*beta_f*(mu_a - muf))) if abs(muf+(1-fa)*beta_f*(mu_a-muf))>1e-15 else muf
    return kcem, mucem

def young_from_bulk_shear(k, mu):
    if k <= 0 or mu <= 0:
        return 0.0
    return 9*k*mu / (3*k + mu)

# Diffusivity self-consistent
def diff_self_consistent(phi, D_h, D_cp, omegah, omegacp):
    sh1, sh2 = S_diff(omegah)
    sp1, sp2 = S_diff(omegacp)
    def f(x):
        term_h = (D_h - x) * ( (1/3)/(x + sh1*(D_h - x)) + (2/3)/(x + sh2*(D_h - x)) )
        term_p = (D_cp - x) * ( (1/3)/(x + sp1*(D_cp - x)) + (2/3)/(x + sp2*(D_cp - x)) )
        return (1-phi)*term_h + phi*term_p
    low = max(1e-12, D_h*0.5, 0.0)
    high = D_cp*1.1
    if f(low)*f(high) < 0:
        return brentq(f, low, high, xtol=1e-12)
    else:
        # fallback
        return (D_h * (1-phi) + D_cp * phi)  # approximate

def S_diff(omega):
    gv = g_func(omega)
    w2 = omega*omega
    if abs(w2-1.0)<1e-12:
        S2 = 1.0/3.0
    else:
        S2 = (w2/(w2-1.0)) * (1.0 - gv) / 2.0
    S1 = 1.0 - 2.0*S2
    return S1, S2

def mori_tanaka_diff(D_f, fa, D_a):
    # Eq. 6, clinker spherical
    if fa <= 0:
        return D_f
    # For D_a=0, formula: D_cement = (1 - fa) / (1 + fa/2) * D_f
    if abs(D_a) < 1e-12:
        return (1.0 - fa) / (1.0 + fa/2.0) * D_f
    else:
        alpha = 1.0/3.0  # for spheres
        return D_f * (1 + fa*(D_a - D_f)/(D_f + (1-fa)*alpha*(D_a - D_f)))

# ----- Main -----
def main():
    if len(sys.argv) < 3:
        print("Usage: helper.py [youngs|diffusivity] <output.csv>")
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]

    if mode == "youngs":
        wc = 0.4
        alpha_max = alpha_max_external(wc)  # 1.0
        npts = 101
        alphas = np.linspace(0, alpha_max, npts)
        rows = []
        for alpha in alphas:
            if alpha < 1e-12:
                rows.append((alpha, 0.0))
                continue
            fa, fh, fcp = powers_volumes(wc, alpha)
            if fh + fcp < 1e-12:
                rows.append((alpha, 0.0))
                continue
            phi = fcp / (fcp + fh)
            kf, muf = solve_elastic_foam(phi)
            if fa + 1e-12 >= 1.0:  # no foam
                kcem, mucem = (0.0, 0.0)
            else:
                # effective foam volume fraction in paste is 1-fa, but Mori-Tanaka needs fa only
                kcem, mucem = mori_tanaka_elastic(kf, muf, fa)
            E = young_from_bulk_shear(kcem, mucem)
            rows.append((alpha, E))
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['hydration_degree', 'young_modulus_GPa'])
            writer.writerows(rows)

    elif mode == "diffusivity":
        wc_vals = np.arange(0.23, 0.81, 0.01)
        rows = []
        for wc in wc_vals:
            amax = alpha_max_external(wc)
            fa, fh, fcp = powers_volumes(wc, amax)
            if fh + fcp < 1e-12:
                D_rel = 0.0
            else:
                phi = fcp / (fcp + fh)
                D_f = diff_self_consistent(phi, D_h_over_Dbulk, D_cp_over_Dbulk, omegah, omegacp)
                D_rel = mori_tanaka_diff(D_f, fa, D_a_over_Dbulk)
            rows.append((D_rel, wc))  # match scaffold: normalized_diffusivity first
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['normalized_diffusivity', 'wc_ratio'])
            writer.writerows(rows)
    else:
        print("Unknown mode")
        sys.exit(1)

if __name__ == '__main__':
    main()
