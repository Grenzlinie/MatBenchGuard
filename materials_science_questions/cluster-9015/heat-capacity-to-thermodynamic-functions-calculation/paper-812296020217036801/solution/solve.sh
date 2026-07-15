#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: recovered_parameters.csv ===
python3 << 'EOF'
import csv, math, os
import numpy as np

os.makedirs('/app/outputs', exist_ok=True)

# Hardcoded K1, K2, K3, K4 from the paper's Table XI (21 entries, 0 °C to 100 °C in 5 °C steps)
K1_list = [
    36.60992e-4, 35.95182e-4, 35.31697e-4, 34.70415e-4, 34.11223e-4,
    33.54016e-4, 32.98697e-4, 32.45173e-4, 31.93358e-4, 31.43171e-4,
    30.94538e-4, 30.47387e-4, 30.01651e-4, 29.57267e-4, 29.14177e-4,
    28.72325e-4, 28.31658e-4, 27.92126e-4, 27.53683e-4, 27.16284e-4,
    26.79887e-4
]
K2_list = [
    3.94918e-3, 2.46747e-3, 1.35553e-3, 0.58861e-3, 0.14382e-3,
    0.00000e-3, 0.13753e-3, 0.53823e-3, 1.18523e-3, 2.06282e-3,
    3.15644e-3, 4.45250e-3, 5.93834e-3, 7.60217e-3, 9.43297e-3,
    11.42045e-3, 13.55499e-3, 15.82761e-3, 18.22986e-3, 20.75386e-3,
    23.39221e-3
]
K3_list = [
    -33.38872e-3, -16.63971e-3, -6.83587e-3, -1.97317e-3, -0.24038e-3,
    0.00000e-3, 0.22858e-3, 1.78424e-3, 5.87757e-3, 13.60305e-3,
    25.94980e-3, 43.81140e-3, 67.99462e-3, 99.22728e-3, 138.16544e-3,
    185.39973e-3, 241.46122e-3, 306.82666e-3, 381.92323e-3, 467.13286e-3,
    562.79613e-3
]
K4_list = [
    -19.48868, -9.75471, -4.02469, -1.16670, -0.14274,
    0.00000, 0.13688, 1.07283, 3.54866, 8.24664,
    15.79563, 26.77561, 41.72189, 61.12880, 85.45310,
    115.11704, 150.51118, 191.99691, 239.90878, 259.55657,
    356.22725
]

temps_C = list(range(0, 105, 5))

sets = {
    'A': {'DS': -20.0, 'DH': -1000.0, 'DCp': -15.0, 'Db': 4.0, 'Dc': -0.0055},
    'B': {'DS': -20.0, 'DH': 0.0, 'DCp': -15.0, 'Db': 0.6, 'Dc': -0.0008},
}

rng = np.random.RandomState(42)
intervals = [(0,20),(20,40),(40,60),(60,80),(80,100)]

out_rows = []
for name, params in sets.items():
    DS = params['DS']
    DH = params['DH']
    DCp = params['DCp']
    Db = params['Db']
    Dc = params['Dc']
    # exact RlnK using precomputed K values
    R_exact = [
        DS - DH*k1 + DCp*k2 + Db*k3 + Dc*k4
        for k1,k2,k3,k4 in zip(K1_list, K2_list, K3_list, K4_list)
    ]
    # add noise
    R_noisy = [v + rng.normal(0, abs(v)/1500.0) for v in R_exact]

    # method of intervals
    Q = []
    dK2oK1 = []
    dK3oK1 = []
    dK4oK1 = []
    for t1, t2 in intervals:
        i1 = temps_C.index(t1)
        i2 = temps_C.index(t2)
        dR = R_noisy[i2] - R_noisy[i1]
        dK1 = K1_list[i2] - K1_list[i1]
        dK2 = K2_list[i2] - K2_list[i1]
        dK3 = K3_list[i2] - K3_list[i1]
        dK4 = K4_list[i2] - K4_list[i1]
        Q.append(dR / dK1)
        dK2oK1.append(dK2 / dK1)
        dK3oK1.append(dK3 / dK1)
        dK4oK1.append(dK4 / dK1)

    Z = []
    xv = []
    yv = []
    for i in range(len(intervals) - 1):
        dQ = Q[i+1] - Q[i]
        d2 = dK2oK1[i+1] - dK2oK1[i]
        d3 = dK3oK1[i+1] - dK3oK1[i]
        d4 = dK4oK1[i+1] - dK4oK1[i]
        Z.append(dQ / d2)
        xv.append(d3 / d2)
        yv.append(d4 / d2)

    A_mat = np.column_stack([np.ones_like(xv), xv, yv])
    b_vec = np.array(Z)
    DCp_rec, Db_rec, Dc_rec = np.linalg.lstsq(A_mat, b_vec, rcond=None)[0]

    # corrected RlnK
    R_corr = [
        R_noisy[j] - (DCp_rec*K2_list[j] + Db_rec*K3_list[j] + Dc_rec*K4_list[j])
        for j in range(len(temps_C))
    ]
    X2 = np.column_stack([np.ones_like(K1_list), [-k for k in K1_list]])
    y2 = np.array(R_corr)
    DS_rec, DH_rec = np.linalg.lstsq(X2, y2, rcond=None)[0]

    out_rows.append([name, DS_rec, DH_rec, DCp_rec, Db_rec, Dc_rec])

outpath = '/app/outputs/recovered_parameters.csv'
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['set', 'DeltaS', 'DeltaH', 'DeltaCp', 'Delta_b', 'Delta_c'])
    for row in out_rows:
        writer.writerow([row[0],
                         f"{row[1]:.6f}",
                         f"{row[2]:.6f}",
                         f"{row[3]:.6f}",
                         f"{row[4]:.6f}",
                         f"{row[5]:.6f}"])
EOF
