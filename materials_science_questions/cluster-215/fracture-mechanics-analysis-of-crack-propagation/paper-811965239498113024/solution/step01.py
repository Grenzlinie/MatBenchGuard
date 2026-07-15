import sys
sys.path.insert(0,'/solution')
import numpy as np
import eff_utils
import csv

outpath = '/app/outputs/step_01_err_data.csv'
C_b = eff_utils.C_b

def compute_error(k, h_f):
    C_f = k * C_b
    C_eff = eff_utils.generalized_effective_for_normal(C_b, C_f, h_f, axis=0)
    C_l_eff = eff_utils.linear_slip_effective_for_normal(C_b, k, h_f, axis=0)
    return eff_utils.error_percentage(C_b, C_eff, C_l_eff)

scenarios = []

# vary_k: h_f=1e-5
h_f_fixed = 1e-5
k_vals = np.logspace(-6, 0, 30)
for k in k_vals:
    scenarios.append(('vary_k', k, compute_error(k, h_f_fixed)))

# vary_hf: k=1e-5
k_fixed = 1e-5
hf_vals = np.logspace(-6, 0, 30)
for hf in hf_vals:
    scenarios.append(('vary_hf', hf, compute_error(k_fixed, hf)))

# cumul_Z10: k/h_f=10, h_f = k/10 (start k=1e-5 so h_f>=1e-6)
k_vals_Z10 = np.logspace(-5, 0, 30)
for k in k_vals_Z10:
    hf = k / 10.0
    if hf < 1e-6:
        hf = 1e-6
    scenarios.append(('cumul_Z10', k, compute_error(k, hf)))

# cumul_Z1: k/h_f=1, h_f=k
k_vals_Z1 = np.logspace(-6, 0, 30)
for k in k_vals_Z1:
    hf = k
    scenarios.append(('cumul_Z1', k, compute_error(k, hf)))

# cumul_Z05: k/h_f=0.5, h_f = 2*k
k_vals_Z05 = np.logspace(-6, 0, 30)
for k in k_vals_Z05:
    hf = 2.0 * k
    scenarios.append(('cumul_Z05', k, compute_error(k, hf)))

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scenario', 'parameter_value', 'err_percent'])
    for scen, param, err in scenarios:
        writer.writerow([scen, param, err])