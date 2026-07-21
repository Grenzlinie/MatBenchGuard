import csv
import sys
import numpy as np
from scipy.special import i0, i1
from scipy.optimize import fsolve
from numpy.polynomial.laguerre import laggauss

Btilde = 1.0
Jtilde = 3.0
ns = [2.0, 5.0]
Tmin = 0.1
Tmax = 2.0
nT = 50
T_list = np.linspace(Tmax, Tmin, nT)
deg = 80
y_nodes, y_weights = laggauss(deg)
x_nodes = np.sqrt(2*y_nodes)
z_nodes = np.sqrt(2*y_nodes)
z_weights = y_weights

def compute_new(q0_guess, q1_guess, n, beta):
    if q0_guess <= 0 and q1_guess <= 0:
        return 0.0, 0.0
    Xi_sq = 0.5*(Jtilde+Btilde)*q1_guess - 0.5*Btilde*q0_guess
    if Xi_sq <= 0:
        return 0.0, 0.0
    Xi = np.sqrt(Xi_sq) * beta
    term = beta * np.sqrt(0.5*Btilde*q0_guess) / Xi
    I0_zXi = i0(z_nodes * Xi)
    I1_zXi = i1(z_nodes * Xi)
    I0_zXi_pow_n = I0_zXi**n
    arg = (z_nodes[:, None] * term) * x_nodes[None, :]
    I0_arg = i0(arg)
    D = np.dot(z_weights, I0_zXi_pow_n[:, None] * I0_arg)
    I0_zXi_pow_n2 = I0_zXi**(n-2)
    I1_sq = I1_zXi**2
    num_q1 = np.dot(z_weights, (I0_zXi_pow_n2 * I1_sq)[:, None] * I0_arg)
    q1_new = np.dot(y_weights, num_q1 / D)
    I1_arg = i1(arg)
    num_q0_inner = np.dot(z_weights, (I0_zXi**(n-1) * I1_zXi)[:, None] * I1_arg)
    A = num_q0_inner / D
    q0_new = np.dot(y_weights, A**2)
    return q0_new, q1_new

results = []
for n in ns:
    beta_array = 1.0 / T_list
    q0, q1 = 0.0, 0.0
    for i, T in enumerate(T_list):
        b = beta_array[i]
        def resid(vars):
            q0v, q1v = vars
            q0n, q1n = compute_new(q0v, q1v, n, b)
            return [q0n - q0v, q1n - q1v]
        try:
            sol = fsolve(resid, [q0, q1], xtol=1e-12, maxfev=1000)
            q0_new, q1_new = sol
            q0_new = max(0.0, q0_new)
            q1_new = max(0.0, q1_new)
            results.append([n, T, q0_new, q1_new])
            q0, q1 = q0_new, q1_new
        except Exception:
            results.append([n, T, q0, q1])

with open(sys.argv[1], 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['n', 'T', 'q0', 'q1'])
    writer.writerows(results)
