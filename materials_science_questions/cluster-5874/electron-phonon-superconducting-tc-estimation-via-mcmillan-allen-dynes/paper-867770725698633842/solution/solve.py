import sys
import csv
import math
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

def main():
    outpath = sys.argv[1] if len(sys.argv) > 1 else "/app/outputs/results.csv"

    # Fixed parameters (energies in meV, temperatures in K with 1 K = 1 meV)
    T_c = 22.0
    Omega0 = 2 * T_c / 5           # 8.8 meV
    Y = Omega0 / 2                 # half-width
    T_SG = 15.0
    nu12 = 0.8333
    w1, w2 = 0.72, 0.28

    # Electron–spin-fluctuation coupling constants
    lam11 = 1.00
    lam12 = -0.17
    lam22 = 2.65
    lam21 = lam12 * nu12

    k22_vals = [0.0, 1.0, 2.0, 3.0, 3.5, 4.0, 4.05, 5.0]
    betas = [1, 2]
    T_min = 0.125
    T_max = 30.0
    N_T = 60                      # >50 temperature points
    T_vals = np.linspace(T_min, T_max, N_T)

    N_matsu = 200                 # positive Matsubara frequencies

    # ---------- universal integrals ----------
    def integrand_I(Om):
        if Om == 0:
            Om = 1e-30
        return (1/Om) * ( 1/((Om+Omega0)**2 + Y**2) - 1/((Om-Omega0)**2 + Y**2) )
    I_val = quad(integrand_I, 0, np.inf, limit=200, epsabs=1e-10)[0]
    C_scale = 1.0 / (2 * I_val)

    # Precompute F(omega) = ∫_0^∞ dΩ Ω * [L(Ω+Ω₀,Y)-L(Ω-Ω₀,Y)] / (ω²+Ω²)   on a log-spaced grid
    omega_grid = np.logspace(-2, 2.7, 2000)   # ≈0.01–500 meV
    F_grid = np.zeros_like(omega_grid)
    def integrand_F(Om, om):
        return Om * ( 1/((Om+Omega0)**2 + Y**2) - 1/((Om-Omega0)**2 + Y**2) ) / (om**2 + Om**2)
    for idx, om in enumerate(omega_grid):
        res = quad(integrand_F, 0, np.inf, args=(om,), limit=200, epsabs=1e-10)
        F_grid[idx] = res[0]
    F_interp = interp1d(omega_grid, F_grid, kind='linear', fill_value='extrapolate')

    # C_{jk} for each channel
    C = np.zeros((2,2))
    C[0,0] = lam11 * C_scale
    C[0,1] = lam12 * C_scale
    C[1,0] = lam21 * C_scale
    C[1,1] = lam22 * C_scale

    # ---------- iterative solver ----------
    def solve_T(T, k22, beta, init=None):
        # spin‑glass scattering rates
        k12_val = 0.2 * k22
        k11_val = k12_val
        k21_val = k12_val * nu12
        if T < T_SG:
            temp_factor = 1.0 - (T / T_SG) ** beta
        else:
            temp_factor = 0.0
        GM = np.zeros((2,2))
        GM[0,0] = k11_val * temp_factor
        GM[0,1] = k12_val * temp_factor
        GM[1,0] = k21_val * temp_factor
        GM[1,1] = k22     * temp_factor

        M = 2 * N_matsu
        m_indices = np.arange(-N_matsu, N_matsu)
        omega_arr = (2 * m_indices + 1) * np.pi * T

        # pre‑compute Lambda^{sf} for all differences l = |n-m|
        omega_diff_l = 2 * np.arange(M) * np.pi * T
        F_vals = F_interp(omega_diff_l)
        Lambda_sf_l = np.zeros((2, 2, M))
        for j in range(2):
            for k in range(2):
                Lambda_sf_l[j, k] = 2 * C[j, k] * F_vals

        alpha = 0.3
        max_iter = 1000
        tol = 1e-5

        if init is None:
            Z = np.ones((2, M))
            Delta = np.ones((2, M)) * 0.5
        else:
            Z = init[0].copy()
            Delta = init[1].copy()

        for it in range(max_iter):
            Z_old = Z.copy()
            Delta_old = Delta.copy()

            denom = np.sqrt(omega_arr[None,:]**2 + Delta**2)
            denom = np.maximum(denom, 1e-12)
            NZ = omega_arr[None,:] / denom
            NDelta = Delta / denom

            Z_new = Z.copy()
            Delta_new = Delta.copy()

            for j in range(2):
                for n in range(N_matsu, M):        # positive frequencies only
                    om_n = omega_arr[n]
                    sum_Z = 0.0
                    sum_D = 0.0
                    for k in range(2):
                        for m in range(M):
                            l = abs(n - m)
                            LamZ = Lambda_sf_l[j, k, l]
                            LamD = -LamZ
                            sum_Z += LamZ * NZ[k, m]
                            sum_D += LamD * NDelta[k, m]
                    imp_Z = GM[j,0] * NZ[0, n] + GM[j,1] * NZ[1, n]
                    imp_D = - (GM[j,0] * NDelta[0, n] + GM[j,1] * NDelta[1, n])
                    Z_new[j, n] = 1.0 + (np.pi * T * sum_Z + imp_Z) / om_n
                    Delta_new[j, n] = (np.pi * T * sum_D + imp_D) / Z_new[j, n]

            # enforce Z(-ω) = Z(ω), Δ(-ω) = Δ(ω)
            for n in range(N_matsu):
                i_pos = N_matsu + n
                i_neg = N_matsu - 1 - n
                Z_new[:, i_neg] = Z_new[:, i_pos]
                Delta_new[:, i_neg] = Delta_new[:, i_pos]

            Z = alpha * Z_new + (1 - alpha) * Z
            Delta = alpha * Delta_new + (1 - alpha) * Delta

            diff = max(np.max(np.abs(Z - Z_old)), np.max(np.abs(Delta - Delta_old)))
            if diff < tol:
                break

        # lowest-Matsubara-frequency gaps
        Delta1_0 = Delta[0, N_matsu]
        Delta2_0 = Delta[1, N_matsu]

        # raw superfluid density (before normalization)
        ns_raw = 0.0
        for j in range(2):
            w = w1 if j == 0 else w2
            term_sum = 0.0
            D_j = Delta[j]
            Z_j = Z[j]
            for m in range(M):
                D_val = D_j[m]
                Z_val = Z_j[m]
                om = omega_arr[m]
                den = (om**2 * Z_val**2 + D_val**2 * Z_val**2) ** 1.5
                if den < 1e-30:
                    den = 1e-30
                term_sum += (D_val**2 * Z_val**2) / den
            ns_raw += w * np.pi * T * term_sum

        return Delta1_0, Delta2_0, ns_raw, (Z, Delta)

    # ---------- reference for normalization (k22=0, T=T_min) ----------
    _, _, ns_ref, _ = solve_T(T_min, 0.0, 1)

    # ---------- produce CSV ----------
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k22', 'beta', 'T', 'Delta1', 'Delta2', 'ns'])
        for k22 in k22_vals:
            for beta in betas:
                # temperature sweep from high to low; use previous solution as initial guess
                T_sorted = np.sort(T_vals)[::-1]
                state = None
                for T in T_sorted:
                    D1, D2, ns_raw, state = solve_T(T, k22, beta, init=state)
                    ns_norm = ns_raw / ns_ref if ns_ref != 0 else 0.0
                    writer.writerow([k22, beta, T, D1, D2, ns_norm])

if __name__ == '__main__':
    main()
