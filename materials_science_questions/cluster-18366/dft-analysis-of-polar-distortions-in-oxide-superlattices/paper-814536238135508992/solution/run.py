import sys
import numpy as np
from scipy.optimize import brentq
import csv
import os

# CGS constants
hbar = 1.054571817e-27   # erg·s
e    = 4.8032047e-10     # esu
m_e  = 9.10938356e-28    # g
kB   = 1.380649e-16      # erg/K
pi   = np.pi

# Input parameters (all in cgs, concentrations in cm^{-3})
m1 = 1.8 * m_e
m2 = 3.5 * m_e
m3 = 6.0 * m_e
n_c1 = 1.2e18
n_c2 = 2.5e19
n_s_max_exp = 2.0e18
T_C_max_exp  = 0.2
x_max        = 7.18

# Calibrated values (computed once)
a_B   = None
const = None
kappa_infty = None

def calibrate():
    global a_B, const, kappa_infty
    # Fermi momentum at the experimental first-band maximum
    p_F_max = hbar * (3.0*pi**2 * n_s_max_exp)**(1.0/3.0)
    # optical Bohr radius from x_max condition
    a_B = (x_max * hbar) / (pi * p_F_max)
    # effective optical dielectric constant
    kappa_infty = a_B * e**2 * m1 / hbar**2
    # lambda_1 at the maximum
    lam1_max = (1.0/x_max) * np.log(1.0 + x_max)
    # Fermi energy (erg) at the maximum
    E_F1_max = hbar**2 * p_F_max**2 / (2.0 * m1)
    # theoretical T_C without the constant prefactor (in K)
    T_C1_no_const = (E_F1_max / kB) * np.exp(-1.0/lam1_max)
    # calibrate the constant
    const = T_C_max_exp / T_C1_no_const

def compute_all():
    calibrate()
    # concentration grid (cm^{-3})
    n_s_arr = np.logspace(17, 21, 500)   # 1e17 to 1e21
    T_C1 = np.zeros_like(n_s_arr)
    T_C2 = np.zeros_like(n_s_arr)
    T_C3 = np.zeros_like(n_s_arr)

    # critical momenta (cgs)
    p_c1 = hbar * (3.0*pi**2 * n_c1)**(1.0/3.0)
    p_c2 = hbar * (3.0*pi**2 * n_c2)**(1.0/3.0)

    for i, ns in enumerate(n_s_arr):
        # ----------- solve for Fermi momenta -----------
        if ns < n_c1:
            # only band 1
            p_F1 = hbar * (3.0*pi**2 * ns)**(1.0/3.0)
            p_F2 = 0.0
            p_F3 = 0.0
        elif ns < n_c2:
            # bands 1 and 2
            def f2(p):
                if p <= p_c1:
                    p2 = 0.0
                else:
                    p2 = np.sqrt((m2/m1) * (p**2 - p_c1**2))
                return (p**3 + p2**3) / (3.0*pi**2) - ns * hbar**3
            # bracket
            lo = p_c1
            hi = p_c1 * 2.0
            while f2(hi) <= 0:
                hi *= 2.0
            p_F1 = brentq(f2, lo, hi)
            p_F2 = np.sqrt((m2/m1) * max(0.0, p_F1**2 - p_c1**2)) if p_F1 > p_c1 else 0.0
            p_F3 = 0.0
        else:
            # all three bands
            def f3(p):
                if p <= p_c1:
                    p2 = 0.0
                else:
                    p2 = np.sqrt((m2/m1) * (p**2 - p_c1**2))
                if p <= p_c2:
                    p3 = 0.0
                else:
                    p3 = np.sqrt((m3/m1) * (p**2 - p_c2**2))
                return (p**3 + p2**3 + p3**3) / (3.0*pi**2) - ns * hbar**3
            lo = p_c2
            hi = p_c2 * 2.0
            while f3(hi) <= 0:
                hi *= 2.0
            p_F1 = brentq(f3, lo, hi)
            p_F2 = np.sqrt((m2/m1) * max(0.0, p_F1**2 - p_c1**2)) if p_F1 > p_c1 else 0.0
            p_F3 = np.sqrt((m3/m1) * max(0.0, p_F1**2 - p_c2**2)) if p_F1 > p_c2 else 0.0

        # ----------- band 1 -----------
        x1 = pi * p_F1 * a_B / hbar
        lam1 = (1.0/x1) * np.log(1.0 + x1) if x1 > 0 else 0.0
        E_F1 = hbar**2 * p_F1**2 / (2.0 * m1)
        T_C1[i] = const * (E_F1 / kB) * np.exp(-1.0/lam1) if lam1 > 0 else 0.0

        # ----------- band 2 -----------
        if p_F2 > 0:
            arg2 = (p_F2**2 * pi * kappa_infty * hbar**3) / (e**2 * (m1*p_F1 + m2*p_F2))
            lam2 = (e**2 * m2 / (pi * p_F2 * kappa_infty)) * np.log(1.0 + arg2)
            E_F2 = hbar**2 * p_F2**2 / (2.0 * m2)
            T_C2[i] = const * (E_F2 / kB) * np.exp(-1.0/lam2) if lam2 > 0 else 0.0
        else:
            T_C2[i] = 0.0

        # ----------- band 3 -----------
        if p_F3 > 0:
            arg3 = (p_F3**2 * pi * kappa_infty * hbar**3) / (e**2 * (m1*p_F1 + m2*p_F2 + m3*p_F3))
            lam3 = (e**2 * m3 / (pi * p_F3 * kappa_infty)) * np.log(1.0 + arg3)
            E_F3 = hbar**2 * p_F3**2 / (2.0 * m3)
            T_C3[i] = const * (E_F3 / kB) * np.exp(-1.0/lam3) if lam3 > 0 else 0.0
        else:
            T_C3[i] = 0.0

    return n_s_arr, T_C1, T_C2, T_C3

def write_tc_csv(filepath):
    n_s, T_C1, T_C2, T_C3 = compute_all()
    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['n_s', 'T_C_1', 'T_C_2', 'T_C_3'])
        for i in range(len(n_s)):
            w.writerow([n_s[i], T_C1[i], T_C2[i], T_C3[i]])

def write_maxima_csv(filepath):
    n_s, T_C1, T_C2, T_C3 = compute_all()
    max1 = np.max(T_C1)
    idx1 = np.argmax(T_C1)
    n1 = n_s[idx1]
    max2 = np.max(T_C2)
    if max2 > 0:
        idx2 = np.argmax(T_C2)
        n2 = n_s[idx2]
    else:
        n2 = 0.0
        max2 = 0.0
    max3 = np.max(T_C3)
    if max3 > 0:
        idx3 = np.argmax(T_C3)
        n3 = n_s[idx3]
    else:
        n3 = 0.0
        max3 = 0.0
    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['band', 'n_s_max', 'T_C_max'])
        w.writerow([1, n1, max1])
        w.writerow([2, n2, max2])
        w.writerow([3, n3, max3])

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'tc'
    out = sys.argv[2] if len(sys.argv) > 2 else '/dev/null'
    if cmd == 'tc':
        write_tc_csv(out)
    elif cmd == 'maxima':
        write_maxima_csv(out)
    else:
        print("Usage: run.py tc|maxima <outfile>")
        sys.exit(1)
