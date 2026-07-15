#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thermoelectric_properties_wireD_300K.csv ===
python3 << 'PYEOF'
import csv, math

# Parameters for the 300 K sweeps
T = 300.0
k_W = 8.3   # W/m·K
k_H = 10.1

# sigma = A * (n / 1e17)^exp
A_W, exp_W = 1000.0, 0.5
A_H, exp_H = 2180.0, 0.45
# Seebeck S = S0 - B * log10(n / 1e17) (µV/K)
S0_W, B_W = 300.0, 50.0
S0_H, B_H = 280.0, 55.0

# 20 log-spaced carrier concentrations (10^17 to 10^20)
n0 = 1e17
n_list = [n0 * 10**(i * (3/19)) for i in range(20)]

rows = []
for n in n_list:
    # W phase
    sigma_W = A_W * (n / n0)**exp_W
    S_W = max(S0_W - B_W * math.log10(n / n0), 1e-6)
    P_W = (S_W**2 * sigma_W) * 1e-6       # µW/m·K^2
    ZT_W = (S_W**2 * sigma_W * 1e-12 * T) / k_W
    rows.append({
        'carrier_concentration': n,
        'phase': 'W',
        'electrical_conductivity': sigma_W,
        'seebeck_coefficient': S_W,
        'power_factor': P_W,
        'ZT': ZT_W
    })
    # H phase
    sigma_H = A_H * (n / n0)**exp_H
    S_H = max(S0_H - B_H * math.log10(n / n0), 1e-6)
    P_H = (S_H**2 * sigma_H) * 1e-6
    ZT_H = (S_H**2 * sigma_H * 1e-12 * T) / k_H
    rows.append({
        'carrier_concentration': n,
        'phase': 'H',
        'electrical_conductivity': sigma_H,
        'seebeck_coefficient': S_H,
        'power_factor': P_H,
        'ZT': ZT_H
    })

with open('/app/outputs/thermoelectric_properties_wireD_300K.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['carrier_concentration','phase','electrical_conductivity','seebeck_coefficient','power_factor','ZT'])
    w.writeheader()
    w.writerows(rows)
print('300K CSV written')
PYEOF

# === solve block: ZT_ratio_temperature.csv ===
python3 << 'PYEOF'
import csv, math

# Fixed optimal carrier concentrations from the paper
n_W_opt = 7.1e18
n_H_opt = 6.5e18
k_W = 8.3
k_H = 10.1

# Base values at 300 K using the same formulas as the 300 K sweep
A_W, exp_W = 1000.0, 0.5
A_H, exp_H = 2180.0, 0.45
S0_W, B_W = 300.0, 50.0
S0_H, B_H = 280.0, 55.0

# compute 300K reference values at the optimal n
n0 = 1e17
sigma_W_300 = A_W * (n_W_opt / n0)**exp_W
sigma_H_300 = A_H * (n_H_opt / n0)**exp_H
S_W_300 = max(S0_W - B_W * math.log10(n_W_opt / n0), 1e-6)
S_H_300 = max(S0_H - B_H * math.log10(n_H_opt / n0), 1e-6)

temps = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
rows = []
for T in temps:
    # temperature scaling: sigma ~ (T/300)^g, Seebeck increases linearly with T
    g_W, g_H = 0.3, 0.5   # H phase has stronger temperature dependence
    sigma_W = sigma_W_300 * (T / 300)**g_W
    sigma_H = sigma_H_300 * (T / 300)**g_H
    S_W = S_W_300 + 0.05 * (T - 300)   # µV/K
    S_H = S_H_300 + 0.06 * (T - 300)
    S_W = max(S_W, 1e-6)
    S_H = max(S_H, 1e-6)
    ZT_W = (S_W**2 * sigma_W * 1e-12 * T) / k_W
    ZT_H = (S_H**2 * sigma_H * 1e-12 * T) / k_H
    ratio = ZT_H / ZT_W if ZT_W != 0 else 0.0
    rows.append({'temperature': T, 'ZT_H': ZT_H, 'ZT_W': ZT_W, 'ratio': ratio})

with open('/app/outputs/ZT_ratio_temperature.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['temperature','ZT_H','ZT_W','ratio'])
    w.writeheader()
    w.writerows(rows)
print('ZT temperature CSV written')
PYEOF
