#!/usr/bin/env python3
import sys, csv, math, numpy as np, scipy.integrate as integrate

def main():
    outpath = sys.argv[1]
    R = 8.314
    A_e1_C = 727.0
    A_e1_K = A_e1_C + 273.15  # 1000.15 K
    s_cem = 25e-9  # m

    # Arrhenius parameters for C diffusion in austenite (gamma) and ferrite (alpha)
    D0_gamma = 2.3e-5
    Q_gamma  = 137700.0
    D0_alpha = 1.1e-6
    Q_alpha  = 87500.0

    def D_func(T, D0, Q):
        return D0 * np.exp(-Q / (R * T))

    T_max_C_list = [750, 800, 850, 900]
    candidate_labels = ['Dγ_avg', 'Dγ_Tmax', 'Dα_avg', 'Dα_Tmax', 'D_mixed']

    tau_values = np.logspace(np.log10(1e-5), np.log10(0.5), 200)

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_max_C', 'D_candidate', 'tau_s', 'f_p_gamma'])
        for T_max_C in T_max_C_list:
            T_max_K = T_max_C + 273.15
            # Compute diffusion coefficients for this T_max
            # average over [A_e1, T_max]
            T_range = T_max_K - A_e1_K
            if T_range <= 0:
                # should not happen for valid T_max > 727°C
                continue
            # gamma average
            I_gamma, _ = integrate.quad(lambda T: D_func(T, D0_gamma, Q_gamma), A_e1_K, T_max_K)
            D_bar_gamma = I_gamma / T_range
            # gamma at T_max
            D_Tmax_gamma = D_func(T_max_K, D0_gamma, Q_gamma)
            # alpha average
            I_alpha, _ = integrate.quad(lambda T: D_func(T, D0_alpha, Q_alpha), A_e1_K, T_max_K)
            D_bar_alpha = I_alpha / T_range
            # alpha at T_max
            D_Tmax_alpha = D_func(T_max_K, D0_alpha, Q_alpha)
            # mixed average
            D_mixed = (D_bar_gamma + D_bar_alpha) / 2.0

            D_dict = {
                'Dγ_avg': D_bar_gamma,
                'Dγ_Tmax': D_Tmax_gamma,
                'Dα_avg': D_bar_alpha,
                'Dα_Tmax': D_Tmax_alpha,
                'D_mixed': D_mixed
            }

            prefactor = (T_max_K / A_e1_K) - 1.0

            for label in candidate_labels:
                D = D_dict[label]
                f_p = prefactor * np.sqrt(D * tau_values) / s_cem
                for tau, fp in zip(tau_values, f_p):
                    writer.writerow([T_max_C, label, tau, fp])

if __name__ == '__main__':
    main()
