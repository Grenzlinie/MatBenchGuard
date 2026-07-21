#!/usr/bin/env python3
import numpy as np
import math

# Spin-1 operators
s_plus = np.array([[0, math.sqrt(2), 0],
                   [0, 0, math.sqrt(2)],
                   [0, 0, 0]], dtype=float)
s_minus = s_plus.T
sz = np.diag([1.0, 0.0, -1.0])
sz2 = np.diag([1.0, 0.0, 1.0])  # (Sz)^2
I3 = np.eye(3)

# full 9x9 operators
S1z = np.kron(sz, I3)
S2z = np.kron(I3, sz)
S1z2 = np.kron(sz2, I3)
S2z2 = np.kron(I3, sz2)
S1p = np.kron(s_plus, I3)
S1m = np.kron(s_minus, I3)
S2p = np.kron(I3, s_plus)
S2m = np.kron(I3, s_minus)

# precompute S1z dot S2z for speed
S1zS2z = np.dot(S1z, S2z)

def compute_eigenvalues(delta, D_JI, mu_sum):
    J_H = 1.0
    J_I = 1.0
    # XXZ term: -J_H [ (delta/2)(S1+S2- + S1-S2+) + S1z S2z ]
    term_xxz = -J_H * ((delta/2.0)*(np.dot(S1p, S2m) + np.dot(S1m, S2p)) + S1zS2z)
    # single-ion anisotropy: -D_JI * ((S1z)^2 + (S2z)^2)
    term_D = -D_JI * (S1z2 + S2z2)
    # Ising interaction: -J_I * mu_sum * (S1z + S2z)
    term_I = -J_I * mu_sum * (S1z + S2z)
    H = term_xxz + term_D + term_I
    # ensure real symmetric
    H = (H + H.T) / 2.0
    eigvals = np.linalg.eigvalsh(H)
    return eigvals

def ratio(beta, delta, D_JI):
    e_par = compute_eigenvalues(delta, D_JI, mu_sum=1)
    e_anti = compute_eigenvalues(delta, D_JI, mu_sum=0)
    # shift to avoid overflow
    emin = min(e_par.min(), e_anti.min())
    Z_par = np.sum(np.exp(-beta * (e_par - emin)))
    Z_anti = np.sum(np.exp(-beta * (e_anti - emin)))
    return Z_par / Z_anti

def find_critical_temperature(delta, D_JI):
    target = math.sqrt(3)
    f = lambda b: ratio(b, delta, D_JI) - target
    # search for root
    beta_max = 100.0
    if f(beta_max) <= 0:
        beta_max = 500.0
        if f(beta_max) <= 0:
            return 0.0
    beta_low = 0.01
    beta_high = beta_max
    for _ in range(50):
        beta_mid = (beta_low + beta_high) / 2
        fm = f(beta_mid)
        if fm == 0:
            break
        if fm > 0:
            beta_high = beta_mid
        else:
            beta_low = beta_mid
    beta_c = (beta_low + beta_high) / 2
    Tc = 1.0 / beta_c
    return Tc

def main():
    rows = []
    # Section 1: sweep Delta
    D_JI_vals = [-0.5, 0.0, 0.5, 1.0, 2.0]
    delta_vals = np.arange(0.0, 3.0 + 0.125, 0.25)   # ensures 3.0 is included
    for D_JI in D_JI_vals:
        for delta in delta_vals:
            Tc = find_critical_temperature(delta, D_JI)
            rows.append(('Delta', '{:.2f}'.format(delta), '{:.6f}'.format(Tc)))

    # Section 2: sweep D_JI
    delta_vals_fixed = [0.5, 1.0, 1.5, 2.0, 3.0]
    D_JI_vals_sweep = np.arange(-0.5, 2.0 + 0.125, 0.25)
    for delta in delta_vals_fixed:
        for D_JI in D_JI_vals_sweep:
            Tc = find_critical_temperature(delta, D_JI)
            rows.append(('D_J_I', '{:.2f}'.format(D_JI), '{:.6f}'.format(Tc)))

    with open('/app/outputs/critical_temperatures.csv', 'w') as f:
        f.write('param,param_value,T_c\n')
        for row in rows:
            f.write(','.join(row) + '\n')

if __name__ == '__main__':
    main()
