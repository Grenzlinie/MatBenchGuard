#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_power_factor.csv ===
python3 - "$OUTDIR" << 'PYEOF'
import numpy as np
from scipy.integrate import quad
import sys, os, csv

outdir = sys.argv[1]
filepath = os.path.join(outdir, 'step_01_power_factor.csv')

e = 1.602176634e-19
k_B = 1.380649e-23
h = 6.62607015e-34
hbar = h/(2*np.pi)
T = 30e-3 * e / k_B
kT_J = k_B * T

l_qd = 6e-9
d_spacing = 6e-9
xi = 2e-9
l_b = 6e-9
A_area = 1e-15
V = 0.01
alpha_ep = 10e-3 * e
t0 = 100e-3 * e

dE_vals = [10,20,30,40,50,60,70,80,90,100,110,120]
N_vals = [2,3,5,7,10,12,15,18,21,25,30]

def n_p0(delta_E_J):
    if delta_E_J == 0:
        return 0.5
    absDE = abs(delta_E_J)
    sgn = np.sign(delta_E_J)
    return 1/(np.exp(absDE/kT_J)-1) + 0.5 + 0.5*sgn

def f0(energy_J):
    return 1/(np.exp(energy_J/kT_J)+1)

def elastic_G_i(E_i_J, gamma_L, gamma_R):
    def integrand(eps):
        f = 1/(np.exp(eps/kT_J)+1)
        window = f*(1-f)
        denom = (eps - E_i_J)**2 + ((gamma_L + gamma_R)/2)**2
        return window * gamma_L * gamma_R / denom
    integral, _ = quad(integrand, -np.inf, np.inf, limit=1000)
    return (2*e**2/h) * (1/kT_J) * integral

with open(filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['dE(meV)', 'N', 'conductivity(S/m)', 'Seebeck_coefficient(V/K)', 'power_factor(W/(K^2 m))'])
    for dE_mev in dE_vals:
        dE_J = dE_mev * 1e-3 * e
        for N in N_vals:
            x = np.array([l_b + i*(l_qd + d_spacing) for i in range(N)])
            L_tot = N*l_qd + (N-1)*d_spacing + 2*l_b
            delta_E_total = (N-1)*dE_J
            E = np.array([-delta_E_total/2 + i*dE_J for i in range(N)])
            G1L = (2*e**2)/(kT_J*hbar) * t0 * np.exp(-l_b/xi)
            G_iL = np.zeros(N)
            G_iR = np.zeros(N)
            G_iL[0] = G1L
            G_iR[-1] = G1L
            Gij = np.zeros((N,N))
            for i in range(N):
                for j in range(N):
                    if i == j: continue
                    dist = abs(x[i]-x[j])
                    deltaE = E[i]-E[j]
                    f_i0 = f0(E[i])
                    f_j0 = f0(E[j])
                    Gamma0 = 2 * alpha_ep * np.exp(-dist/xi) * f_i0 * (1-f_j0) * n_p0(deltaE)
                    Gij[i,j] = (e**2)/(kT_J) * Gamma0
            A = np.empty((N,N))
            for i in range(N):
                A[i,i] = G_iL[i] + G_iR[i] + np.sum(Gij[i,:])
                for j in range(N):
                    if i != j:
                        A[i,j] = -Gij[i,j]
            z = np.empty(N)
            for i in range(N):
                z[i] = G_iL[i] * (V/2) + G_iR[i] * (-V/2)
            V_vec = np.linalg.solve(A, z)
            I_in = G1L * (V/2 - V_vec[0])
            G_in = I_in / V
            G_el = 0.0
            for i in range(N):
                gamma_L = t0 * np.exp(-x[i]/xi)
                gamma_R = t0 * np.exp(-(L_tot - x[i] - l_qd)/xi)
                G_i = elastic_G_i(E[i], gamma_L, gamma_R)
                G_el += G_i
            G_total = G_in + G_el
            sigma = G_total * L_tot / A_area
            S = (k_B/e) * (G_in * (N-1)*dE_J) / (G_total * kT_J)
            PF = sigma * S**2
            writer.writerow([dE_mev, N, sigma, S, PF])
PYEOF
