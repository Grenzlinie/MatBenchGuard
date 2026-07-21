import sys
import numpy as np

hbar_eVs = 6.582119569e-16
vF_ms = 5.8e5
vF_evang = hbar_eVs * vF_ms * 1e10

param_sets = {
    'sb': {'mstar': -0.2, 'alphaR': 0.5, 't': 0.05, 'delta': 0.05},
    'bi': {'mstar': -0.12, 'alphaR': 0.2, 't': 0.1, 'delta': 0.4},
}

if len(sys.argv) != 3:
    sys.exit("Usage: compute_bands.py <output_csv> <system_code>")

outpath = sys.argv[1]
sys_code = sys.argv[2].lower()
params = param_sets[sys_code]
mstar = params['mstar']
alphaR = params['alphaR']
t = params['t']
delta = params['delta']

k_vals = np.linspace(0.0, 1.2, 200)

sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)

def H_k(k):
    H_TI = vF_evang * k * sigma_y
    c = k**2 / (2 * mstar) + delta
    H_BI = c * np.eye(2) + alphaR * k * sigma_y
    T_mat = t * np.diag([1, -1])
    top = np.hstack((H_TI, T_mat))
    bot = np.hstack((T_mat.conj().T, H_BI))
    return np.vstack((top, bot))

data_rows = []
for k in k_vals:
    H = H_k(k)
    ev = np.linalg.eigvalsh(H)
    data_rows.append([k, ev[0], ev[1], ev[2], ev[3]])

with open(outpath, 'w') as f:
    f.write("k,E1,E2,E3,E4\n")
    for row in data_rows:
        f.write(f"{row[0]:.6f},{row[1]:.6f},{row[2]:.6f},{row[3]:.6f},{row[4]:.6f}\n")
