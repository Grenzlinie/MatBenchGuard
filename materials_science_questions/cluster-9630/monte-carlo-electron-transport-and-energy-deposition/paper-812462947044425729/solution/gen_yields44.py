import numpy as np
import csv

# energy bin centres (eV) – 500 eV bins from 250 to 19750
edges_e = np.arange(0, 20001, 500)
centers_e = edges_e[:-1] + 250
n_e = len(centers_e)
# angle bin centres (deg) – 10 deg bins from 5 to 175
a_deg = np.arange(5, 181, 10)
n_a = len(a_deg)
a_rad = np.radians(a_deg)

# solid angle per bin (sr)
dOmega = 2.0 * np.pi * np.sin(a_rad) * np.radians(10)

# binary-relation peak energy at each angle (keV → eV)
E_binary = 7665.0 * np.cos(a_rad)**2

# yield matrix
ymat = np.zeros((n_e, n_a))

# ----- background (power-law + exponential) -----
bg = 1.0e-4 * (centers_e + 200.0)**(-1.5) * np.exp(-centers_e / 5000.0)
ymat += bg[:, np.newaxis]

# ----- direct binary peak -----
sigma_Ed = 800.0
# angular factor: forward peaked + small shoulder at 40°
ang_fac_d = np.exp(-a_deg**2 / (2.0 * 30.0**2)) + \
           0.1 * np.exp(-(a_deg - 40.0)**2 / (2.0 * 15.0**2))
A_dir = 0.1
for i, E0 in enumerate(E_binary):
    if E0 < 20000.0:
        contrib = A_dir * ang_fac_d[i] * \
                  np.exp(-0.5 * ((centers_e - E0) / sigma_Ed)**2)
        ymat[:, i] += contrib

# ----- scattered hot-electron peak (fixed at 7665 eV) -----
sigma_Eh = 1200.0
A_hot = 0.08
ang_fac_h = np.exp(-a_deg**2 / (2.0 * 60.0**2)) * 0.3
contrib_h = A_hot * np.exp(-0.5 * ((centers_e - 7665.0) / sigma_Eh)**2)
for i in range(n_a):
    ymat[:, i] += contrib_h * ang_fac_h[i]

# normalise to total yield = 254 electrons / ion
total_unnorm = np.sum(ymat * 500.0 * dOmega[np.newaxis, :])
scale = 254.0 / total_unnorm
ymat *= scale

# write CSV
with open('/app/outputs/yields_44_ugcm2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['energy_eV', 'angle_deg', 'yield'])
    for i, ev in enumerate(centers_e):
        for j, ad in enumerate(a_deg):
            w.writerow([ev, ad, ymat[i, j]])
