#!/usr/bin/env python3
import sys, math, csv
import numpy as np

def main():
    Jx = 1.0
    N = 100
    # momentum grid for even fermion sector
    ks = np.pi * np.arange(1, N) / N   # k_1...k_{N-1}

    # parameter sweeps
    Jy_ratios = [-2.0, -1.0, 0.0, 1.0, 2.0]
    h_vals = np.arange(-3.0, 3.01, 0.1)
    # We'll store all data in a dict (jy,h) -> (C13, Mz, I13, D13, E_global)
    results = {}

    for jyr in Jy_ratios:
        Jy = jyr
        for h_idx, h in enumerate(h_vals):
            A = -h + (Jx + Jy) * np.cos(2.0*ks)
            B = (Jx - Jy) * np.sin(2.0*ks)
            omega = np.sqrt(A**2 + B**2)
            zero_mask = omega == 0.0
            omega_safe = omega.copy()
            omega_safe[zero_mask] = 1e-15
            A_safe = A.copy()
            B_safe = B.copy()
            A_safe[zero_mask] = 0.0
            B_safe[zero_mask] = 0.0

            sin2 = 0.5 * (1.0 - A_safe / omega_safe)
            sin2[zero_mask] = 0.5   # limit at degeneracy
            sin_theta = -B_safe / omega_safe
            sin_theta[zero_mask] = 0.0

            # single-site occupation
            n = (2.0 / N) * np.sum(sin2)
            Mz = 2.0 * n - 1.0

            # auxiliary sums
            def gamma(p):
                return (2.0 / N) * np.sum(np.cos(p * ks) * sin2)
            def xi(p):
                return -(1.0 / N) * np.sum(np.sin(p * ks) * sin_theta)

            g0 = n      # gamma(0)
            g1 = gamma(1)
            g2 = gamma(2)
            xi1 = xi(1)
            xi2 = xi(2)

            # next-nearest neighbour correlation functions
            z13 = g2 * (1.0 - 2.0*n) + 2.0 * g1**2
            x13 = xi2 * (1.0 - 2.0*n)

            # reduced density matrix elements for distance 2
            r_sq = g2**2 + xi2**2
            u = n**2 - r_sq
            w = n - u
            v = (1.0 - n)**2 - r_sq

            # concurrence C13
            sqrt_uv = math.sqrt(max(0.0, u*v))
            cand1 = abs(x13) - w
            cand2 = abs(z13) - sqrt_uv
            C13 = 2.0 * max(0.0, cand1, cand2)

            # von Neumann entropy (natural logarithm, as in the paper)
            def entropy_ln(p):
                if p <= 0.0 or p >= 1.0:
                    return 0.0
                return -p*math.log(p) - (1.0-p)*math.log(1.0-p)

            S_single = entropy_ln(n)

            # two-qubit eigenvalues (X-form)
            x_abs = abs(x13)
            z_abs = abs(z13)
            disc = (u - v)**2 + 4.0*x_abs**2
            sqrt_disc = math.sqrt(max(0.0, disc))
            lam1 = (u + v + sqrt_disc) / 2.0
            lam2 = (u + v - sqrt_disc) / 2.0
            lam3 = w + z_abs
            lam4 = w - z_abs
            evals = np.array([lam1, lam2, lam3, lam4])
            evals = np.clip(evals, 0.0, 1.0)
            evals /= evals.sum()
            S_pair = -np.sum(evals * np.log(np.maximum(evals, 1e-15)))

            # quantum mutual information
            I13 = 2.0 * S_single - S_pair

            # quantum discord (Eqs. 26, 27) with natural log
            zeta = 0.5 + math.sqrt(((u - v)/2.0)**2 + (x_abs + z_abs)**2)
            zeta = max(1e-12, min(zeta, 1.0 - 1e-12))
            H_zeta = -zeta*math.log(zeta) - (1.0-zeta)*math.log(1.0-zeta)
            D13 = H_zeta + S_single - S_pair

            # global entanglement
            E_global = 4.0 * n * (1.0 - n)

            key = (jyr, h)
            results[key] = (Mz, C13, I13, D13, E_global)

    # compute derivatives via finite differences
    # store C13 values for easy access
    C13_dict = {}
    for jyr in Jy_ratios:
        for h in h_vals:
            C13_dict[(jyr, h)] = results[(jyr, h)][1]

    rows = []
    for jyr in Jy_ratios:
        for h in h_vals:
            Mz, C13, I13, D13, E_global = results[(jyr, h)]
            C12 = 0.0

            # dC_dh
            if h == h_vals[0]:
                dC_dh = (C13_dict[(jyr, h+0.1)] - C13_dict[(jyr, h)]) / 0.1
            elif h == h_vals[-1]:
                dC_dh = (C13_dict[(jyr, h)] - C13_dict[(jyr, h-0.1)]) / 0.1
            else:
                dC_dh = (C13_dict[(jyr, h+0.1)] - C13_dict[(jyr, h-0.1)]) / 0.2

            # dC_dJ_y (step = 1 in Jy_ratio)
            idx = Jy_ratios.index(jyr)
            if idx == 0:
                jyr_plus = Jy_ratios[idx+1]
                dC_dJy = (C13_dict[(jyr_plus, h)] - C13_dict[(jyr, h)]) / 1.0
            elif idx == len(Jy_ratios)-1:
                jyr_minus = Jy_ratios[idx-1]
                dC_dJy = (C13_dict[(jyr, h)] - C13_dict[(jyr_minus, h)]) / 1.0
            else:
                jyr_plus = Jy_ratios[idx+1]
                jyr_minus = Jy_ratios[idx-1]
                dC_dJy = (C13_dict[(jyr_plus, h)] - C13_dict[(jyr_minus, h)]) / 2.0

            rows.append([
                jyr, h, Mz, C12, C13, dC_dJy, dC_dh, I13, D13, E_global
            ])

    # write CSV
    writer = csv.writer(sys.stdout)
    writer.writerow([
        'J_y_over_J_x', 'h_over_J_x', 'magnetization', 'C_12', 'C_13',
        'dC_dJ_y', 'dC_dh', 'I_13', 'D_13', 'E_global'
    ])
    for row in rows:
        writer.writerow(row)

if __name__ == '__main__':
    main()
