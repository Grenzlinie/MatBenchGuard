import sys, os
sys.path.insert(0, '/solution')
from fem_hc2 import *
import numpy as np
import csv

epsilonFtau_values = [1e6, 2.0, 1.5, 1.3, 1.0]
t_values = np.arange(0.1, 1.05, 0.05)

out_path = '/app/outputs/ratios.csv'
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['epsilonFtau', 'alpha_H_over_alpha_0', 'dTc_over_Tc0', 'max_rel_diff_h_vs_WHHM_fit'])
    for eps in epsilonFtau_values:
        if eps == 1e6:
            eps_label = 1e6
        else:
            eps_label = eps
        D_ratio, Tc_ratio = compute_params(eps)
        # compute FEM h(t) again (could store, but fast enough)
        h_fem_list = []
        for t in t_values:
            h = fem_Hc2(t, eps, D_ratio, Tc_ratio)
            h_fem_list.append(h)
        h_fem_array = np.array(h_fem_list)
        # fit WHHM
        A_fit, B_fit = fit_whhm(t_values, h_fem_array)
        # compute alpha_H/alpha_0 = (D/D0) / (D_fit/D0) = D_ratio / A_fit
        alpha_ratio = D_ratio / A_fit if A_fit > 0 else 1.0
        # dTc = 1 - Tc/Tc0 = 1 - Tc_ratio
        dTc = 1.0 - Tc_ratio
        # max relative difference (only where h_FEM > 0)
        h_whhm_list = []
        for t in t_values:
            if t <= B_fit:
                h_whhm_list.append(whhm_model(t, A_fit, B_fit))
            else:
                h_whhm_list.append(0.0)
        h_whhm_array = np.array(h_whhm_list)
        mask = h_fem_array > 0
        if np.any(mask):
            rel_diff = np.max(np.abs((h_fem_array[mask] - h_whhm_array[mask]) / h_fem_array[mask]))
        else:
            rel_diff = 0.0
        writer.writerow([f"{eps_label}", f"{alpha_ratio:.6f}", f"{dTc:.6f}", f"{rel_diff:.6f}"])
