import sys, os
sys.path.insert(0, '/solution')
from fem_hc2 import *
import numpy as np
import csv

epsilonFtau_values = [1e6, 2.0, 1.5, 1.3, 1.0]
t_values = np.arange(0.1, 1.05, 0.05)

out_path = '/app/outputs/h_vs_t.csv'
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t', 'epsilonFtau', 'h_FEM', 'h_WHHM_fit'])
    for eps in epsilonFtau_values:
        D_ratio, Tc_ratio = compute_params(eps)
        if eps == 1e6:
            eps_label = 1e6  # write as 1e6
        else:
            eps_label = eps
        # compute FEM h(t)
        h_fem_list = []
        for t in t_values:
            h = fem_Hc2(t, eps, D_ratio, Tc_ratio)
            h_fem_list.append(h)
        h_fem_array = np.array(h_fem_list)
        # fit WHHM
        A_fit, B_fit = fit_whhm(t_values, h_fem_array)
        # compute WHHM fitted h(t)
        for i, t in enumerate(t_values):
            h_fem = h_fem_list[i]
            if t <= B_fit and h_fem > 0:
                h_whhm = whhm_model(t, A_fit, B_fit)
            else:
                h_whhm = 0.0
            writer.writerow([f"{t:.2f}", f"{eps_label}", f"{h_fem:.6f}", f"{h_whhm:.6f}"])
