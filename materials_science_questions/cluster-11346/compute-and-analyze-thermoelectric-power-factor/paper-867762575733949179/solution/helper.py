import numpy as np
from scipy.integrate import quad
import csv
import os

# ---------- physical constants ----------
e = 1.602176634e-19          # C
h = 6.62607015e-34           # J s
hbar = h / (2 * np.pi)       # J s
k_B = 1.380649e-23            # J/K
meV_to_J = 1e-3 * e           # 1 meV -> J

# ---------- fixed model parameters ----------
kBT_meV = 30.0
kBT_J = kBT_meV * meV_to_J

l_qd = 6e-9        # m
d_sep = 6e-9       # m (distance between adjacent QDs)
xi = 2e-9          # m
l_b = 6e-9         # m
A = 1e-15          # m^2

alpha_ep_J = 10e-3 * e   # meV -> J
t0_J = 100e-3 * e        # meV -> J

# ---------- helper functions ----------
def f0(energy_J):
    "Fermi distribution with chemical potential 0."
    return 1.0 / (np.exp(energy_J / kBT_J) + 1.0)

def N_p(deltaE_J):
    "Phonon distribution function Eq.(2) at temperature T (kBT)."
    abs_dE = np.abs(deltaE_J)
    if abs_dE == 0.0:
        return 0.0   # avoid division by zero; not used for i!=j
    return (1.0 / (np.exp(abs_dE / kBT_J) - 1.0)) + 0.5 + 0.5 * np.sign(deltaE_J)

# ---------- dE and N values ----------
dE_list_meV = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
N_list = [2, 3, 5, 7, 10, 12, 15, 18, 21, 25, 30]

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "step_01_power_factor.csv")

rows = []

for dE_meV in dE_list_meV:
    dE_J = dE_meV * meV_to_J
    for N in N_list:
        # ---- geometry & energies ----
        DeltaE = (N - 1) * dE_J
        E = np.zeros(N)
        for i in range(N):
            E[i] = -DeltaE / 2.0 + i * dE_J
        # positions of left edge of each QD
        x = np.zeros(N)
        for i in range(N):
            x[i] = l_b + i * (l_qd + d_sep)
        L_tot = 2 * l_b + N * l_qd + (N - 1) * d_sep

        # ---- inelastic hopping conductances G_{ij} ----
        G_ij = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                deltaE = E[i] - E[j]
                n_p = N_p(deltaE)
                gamma_ij0 = 2.0 * alpha_ep_J \
                            * np.exp(-abs(x[i] - x[j]) / xi) \
                            * f0(E[i]) * (1.0 - f0(E[j])) \
                            * n_p
                G_ij[i, j] = (e**2 / kBT_J) * gamma_ij0

        # ---- electrode couplings ----
        G_iL = np.zeros(N)
        G_iR = np.zeros(N)
        # only first QD to left electrode, last QD to right electrode
        G0 = (2.0 * e**2) / (kBT_J * hbar) * t0_J * np.exp(-l_b / xi)
        G_iL[0] = G0
        G_iR[-1] = G0

        # ---- solve Miller-Abrahams network ----
        V = 0.01       # bias voltage (V)
        VL = V / 2.0
        VR = -V / 2.0
        A = np.zeros((N, N))
        z = np.zeros(N)
        for i in range(N):
            A[i, i] = G_iL[i] + G_iR[i] + np.sum(G_ij[i, :])
            for j in range(N):
                if i != j:
                    A[i, j] = -G_ij[i, j]
            z[i] = G_iL[i] * VL + G_iR[i] * VR
        V_local = np.linalg.solve(A, z)

        I_in = G_iL[0] * (VL - V_local[0])
        G_in = I_in / V

        # ---- elastic conductance G_el (resonant tunneling) ----
        max_abs_E = DeltaE / 2.0
        # integration range: at least +/- max_abs_E + 0.3 eV
        extra_range_J = 0.3 * e
        low_J = -max_abs_E - extra_range_J
        high_J = max_abs_E + extra_range_J

        G_el = 0.0
        for i in range(N):
            gamma_Li = t0_J * np.exp(-x[i] / xi)
            gamma_Ri = t0_J * np.exp(-(L_tot - x[i] - l_qd) / xi)
            def integrand(eps, Ei=E[i], gL=gamma_Li, gR=gamma_Ri):
                f = f0(eps)
                num = gL * gR
                denom = (eps - Ei)**2 + (gL + gR)**2 / 4.0
                return num / denom * f * (1.0 - f) / kBT_J
            res, _ = quad(integrand, low_J, high_J, limit=200,
                          epsabs=1e-30, epsrel=1e-8)
            G_i_val = (2.0 * e**2 / h) * res
            G_el += G_i_val

        # ---- total transport coefficients ----
        G = G_in + G_el
        sigma = G * L_tot / A
        S = (k_B / e) * (G_in * (N - 1) * dE_J) / (G * kBT_J)
        P = sigma * S**2

        rows.append([
            dE_meV,
            N,
            sigma,
            S,
            P
        ])

# ---------- write CSV ----------
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["dE(meV)", "N", "conductivity(S/m)",
                     "Seebeck_coefficient(V/K)", "power_factor(W/(K^2 m))"])
    writer.writerows(rows)
