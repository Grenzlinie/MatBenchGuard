#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_functions.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 << 'HEREDOC'
import numpy as np
from scipy.interpolate import UnivariateSpline
import csv

# Experimental data from Table 1 (all rows, sorted)
data = [
    (5.26, 0.006), (5.80, 0.008), (6.37, 0.012), (7.02, 0.015), (7.73, 0.019),
    (8.51, 0.026), (9.36, 0.036), (10.30, 0.051), (11.29, 0.075), (12.37, 0.108),
    (13.60, 0.147), (14.98, 0.188), (16.52, 0.238), (18.20, 0.308), (19.78, 0.382),
    (21.27, 0.472), (22.91, 0.606), (24.68, 0.771), (26.58, 0.989), (28.63, 1.244),
    (30.84, 1.536), (33.24, 1.906), (35.84, 2.362), (38.67, 2.983), (41.74, 3.795),
    (45.08, 4.833), (48.72, 6.022), (52.68, 7.448), (56.99, 9.329),
    (50.19, 6.665), (54.08, 8.024), (58.47, 10.214), (63.21, 12.176), (68.37, 14.976),
    (74.03, 18.116), (80.20, 21.875), (86.93, 26.102), (94.29, 30.880), (102.34, 36.241),
    (110.87, 42.001), (119.53, 47.915), (128.26, 53.804), (137.13, 59.766), (146.12, 65.764),
    (155.15, 71.630), (164.23, 77.381), (173.29, 83.040), (182.32, 88.668), (191.35, 94.039),
    (200.42, 99.236), (209.52, 104.350), (218.59, 109.154), (227.60, 113.926), (236.47, 118.557),
    (245.13, 122.645), (253.58, 126.329), (261.85, 130.187), (270.00, 133.657), (277.98, 137.383),
    (285.86, 140.471), (293.70, 143.374), (301.49, 146.224),
    (81.15, 22.463), (85.35, 25.090), (92.70, 29.927), (100.51, 35.041), (108.81, 40.648),
    (117.35, 46.452), (125.99, 52.315), (134.72, 58.167), (143.53, 64.047), (152.42, 69.860),
    (347.15, 154.010), (397.15, 167.509), (447.15, 174.755), (497.15, 181.115),
    (547.15, 188.678), (597.15, 191.929), (647.15, 198.632), (697.15, 202.837),
    (747.15, 204.018), (797.15, 207.994), (847.15, 209.344), (897.15, 212.217),
    (947.15, 215.308), (997.15, 218.416), (1047.15, 222.181)
]
data.sort(key=lambda x: x[0])
T_data = np.array([p[0] for p in data])
Cp_data = np.array([p[1] for p in data])

# Smoothing spline (small smoothing to follow data closely)
spline = UnivariateSpline(T_data, Cp_data, s=1e-7)

# Low‑temperature extrapolation: fit Cp/T vs T^2 for T < 10 K
mask_low = T_data < 10
T_low = T_data[mask_low]
Cp_low = Cp_data[mask_low]
Cp_over_T_low = Cp_low / T_low
coeff = np.polyfit(T_low**2, Cp_over_T_low, 1)
a_low = coeff[0]  # Cp/T ≈ a * T^2   →   Cp ≈ a * T^3

# Dense integration grid
T_dense = np.linspace(0, max(T_grid := np.array([5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,273.15,280,290,298.15,300,325,350,375,400,425,450,475,500,550,600,650,700,750,800,850,900,950,1000])), 20000)
Cp_dense = np.zeros_like(T_dense)
# Analytical T^3 law below the first data point
mask_low_dense = T_dense <= T_data[0]
Cp_dense[mask_low_dense] = a_low * T_dense[mask_low_dense]**3
# Spline above
mask_high = T_dense > T_data[0]
Cp_dense[mask_high] = spline(T_dense[mask_high])
Cp_dense = np.maximum(Cp_dense, 0.0)

# Integrate
with np.errstate(divide='ignore', invalid='ignore'):
    Cp_over_T_dense = np.where(T_dense > 0, Cp_dense / T_dense, 0.0)
dT = T_dense[1] - T_dense[0]
S_dense = np.cumsum(Cp_over_T_dense) * dT
H_J_dense = np.cumsum(Cp_dense) * dT  # J/mol

# Interpolate to target grid
Cp_grid = spline(T_grid)
S_grid = np.interp(T_grid, T_dense, S_dense)
H_J_grid = np.interp(T_grid, T_dense, H_J_dense)
H_grid = H_J_grid / 1000.0   # kJ/mol
neg_G_grid = S_grid - H_J_grid / T_grid

# Write CSV
with open('/app/outputs/thermodynamic_functions.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'Cp', 'S', 'neg_G_over_T', 'H'])
    for i in range(len(T_grid)):
        w.writerow([T_grid[i], Cp_grid[i], S_grid[i], neg_G_grid[i], H_grid[i]])
HEREDOC
