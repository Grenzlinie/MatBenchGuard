#!/usr/bin/env python3
import csv
import math
import sys

k_B = 8.617333262145e-2   # meV/K
N_atoms = 3

# Zero-point energies from the paper (meV per unit cell) – T=0 internal/free energy
compounds = [
    ("ZrB2", 285.60),
    ("NbB2", 276.63),
    ("MoB2", 248.29),
]

def debye_temperature(U0):
    """Debye temperature from U0 = (9/8)*N*k_B*theta_D  =>  U0 = (27/8)*k_B*theta_D for N=3"""
    return (8.0 * U0) / (27.0 * k_B)

def cv_debye(theta_D, T):
    """Debye heat capacity C_v(T) per unit cell (meV/K)"""
    if T == 0.0:
        return 0.0
    x_max = theta_D / T
    # numerical integration of  x^4 * exp(x) / (exp(x)-1)^2  from 0 to x_max
    steps = 1000
    dx = x_max / steps
    integral = 0.0
    for i in range(steps + 1):
        x = i * dx
        if x == 0.0:
            continue
        exp_x = math.exp(x)
        denom = exp_x - 1.0
        if denom == 0.0:
            continue
        f = x**4 * exp_x / (denom * denom)
        if i == 0 or i == steps:
            integral += 0.5 * f * dx
        else:
            integral += f * dx
    Cv = 9.0 * N_atoms * k_B * (T / theta_D)**3 * integral
    # high-T limit: 3*N*k_B = 9*k_B
    return max(0.0, min(Cv, 3.0 * N_atoms * k_B))

def thermodynamic_functions(U0, T_max=2000, step=100):
    theta_D = debye_temperature(U0)
    # compute on a fine temperature grid for accurate integration
    dT = 0.5
    n_points = int(T_max / dT) + 1
    T_fine = [i * dT for i in range(n_points)]
    Cv_fine = [cv_debye(theta_D, Ti) for Ti in T_fine]
    # integrate Cv to get U-U0 and S
    U_fine = [U0]
    S_fine = [0.0]
    for i in range(1, n_points):
        T_prev = T_fine[i-1]
        T_curr = T_fine[i]
        C_prev = Cv_fine[i-1]
        C_curr = Cv_fine[i]
        delta_T = T_curr - T_prev
        # trapezoidal integration for U
        delta_U = 0.5 * (C_prev + C_curr) * delta_T
        U_fine.append(U_fine[-1] + delta_U)
        # entropy integration: S = int_0^T (Cv/T') dT'
        if T_curr == 0.0:
            S_fine.append(0.0)
        else:
            delta_S = 0.5 * (C_prev / T_prev if T_prev > 0 else 0.0 + C_curr / T_curr) * delta_T
            # careful: at T_prev=0, C_prev=0 => term 0
            S_fine.append(S_fine[-1] + delta_S)
    # sample at requested temperatures
    rows = []
    for T in range(0, T_max + 1, step):
        if T == 0:
            idx = 0
        else:
            idx = int(round(T / dT))
        if idx >= n_points:
            idx = n_points - 1
        U = U_fine[idx]
        S = S_fine[idx]
        F = U - T * S
        Cv = Cv_fine[idx]
        rows.append((T, U, F, S, Cv))
    return rows

def main():
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(['compound', 'T_K', 'internal_energy_meV_per_cell',
                     'free_energy_meV_per_cell', 'entropy_meV_per_K',
                     'heat_capacity_meV_per_K'])
    for name, U0 in compounds:
        rows = thermodynamic_functions(U0, T_max=2000, step=100)
        for T, U, F, S, Cv in rows:
            writer.writerow([name, T, f"{U:.4f}", f"{F:.4f}", f"{S:.6f}", f"{Cv:.6f}"])

if __name__ == "__main__":
    main()
