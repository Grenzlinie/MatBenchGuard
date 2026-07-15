import numpy as np
import csv
import os

# Wavelengths (nm)
wl_all = np.array([195.75176, 194.45970, 193.88269, 193.00345, 192.97510, 192.21425, 191.60818])

# Fused silica measured indices (Table 2). None marks 'not obs.'
fused_data = {
    'A1': [1.55706, 1.55903, 1.55991, 1.56129, 1.56133, 1.56257, 1.56355],
    'A2': [1.55707, 1.55904, 1.55992, 1.56131, 1.56135, 1.56257, 1.56361],
    'A3': [1.55707, 1.55903, 1.55992, 1.56126, 1.56136, None,    1.56354],
    'B1': [1.55710, 1.55906, 1.55995, 1.56133, 1.56138, 1.56261, 1.56359],
    'B2': [1.55709, 1.55905, 1.55994, 1.56133, 1.56137, 1.56259, 1.56358],
    'B3': [1.55707, 1.55904, 1.55993, 1.56132, 1.56136, 1.56257, 1.56357],
    'C1': [1.55705, 1.55902, 1.55991, 1.56129, 1.56133, 1.56256, 1.56355],
    'C2': [1.55705, 1.55901, 1.55991, 1.56129, 1.56134, 1.56256, 1.56355],
}

# Calcium fluoride measured indices: list of (wavelength, index) pairs for observed lines
ca_data = {
    'A1': [
        (195.75176, 1.49964),
        (194.45970, 1.50087),
        (193.88269, 1.50152),
        (192.97510, 1.50229),
        (191.60818, 1.50369),
    ],
    'A2': [
        (194.45970, 1.50088),
        (192.97510, 1.50233),
        (191.60818, 1.50372),
    ],
    'B': [   # Sample B1 in Table 2 → named 'B' in the output contract
        (194.45970, 1.50088),
        (192.97510, 1.50232),
        (191.60818, 1.50371),
    ],
}

os.makedirs('/app/outputs', exist_ok=True)

indices_rows = []
coeff_rows = []

# Process fused silica
for sample, vals in fused_data.items():
    w = []
    n = []
    for i, v in enumerate(vals):
        if v is not None:
            w.append(wl_all[i])
            n.append(v)
    if len(w) < 3:
        continue
    c = np.polyfit(w, n, 2)   # returns a2, a1, a0
    a2, a1, a0 = c
    n_193 = np.polyval(c, 193.39)
    dn = a1 + 2 * a2 * 193.39
    indices_rows.append([sample, 'fused_silica', f'{n_193:.6f}', f'{dn:.6f}'])
    coeff_rows.append([sample, 'fused_silica', f'{a0:.7f}', f'{a1:.10e}', f'{a2:.10e}'])

# Process calcium fluoride
for sample, pts in ca_data.items():
    w = np.array([p[0] for p in pts])
    n = np.array([p[1] for p in pts])
    c = np.polyfit(w, n, 2)
    a2, a1, a0 = c
    n_193 = np.polyval(c, 193.39)
    dn = a1 + 2 * a2 * 193.39
    indices_rows.append([sample, 'calcium_fluoride', f'{n_193:.6f}', f'{dn:.6f}'])
    coeff_rows.append([sample, 'calcium_fluoride', f'{a0:.7f}', f'{a1:.10e}', f'{a2:.10e}'])

# Write fitted_indices.csv
with open('/app/outputs/fitted_indices.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sample', 'material', 'n_193.39', 'dn_dlambda'])
    w.writerows(indices_rows)

# Write fitted_coefficients.csv
with open('/app/outputs/fitted_coefficients.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sample', 'material', 'a0', 'a1', 'a2'])
    w.writerows(coeff_rows)
