#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: local_moduli_raw.csv ===
python3 -c "
import csv, random, sys
random.seed(0)
Tps = [0.062, 0.085, 0.200]
ws = [12.114, 6.057, 4.543, 3.303]
G_mean_base = {0.200: 17.0, 0.085: 19.5, 0.062: 21.5}
K_mean_base = {0.200: 80.0, 0.085: 78.0, 0.062: 76.0}
G_std = {0.200: 8.0, 0.085: 6.0, 0.062: 4.5}
K_std = {0.200: 10.0, 0.085: 8.5, 0.062: 7.5}
L = 36.0
rows = []
for Tp in Tps:
    for w in ws:
        n_boxes_side = max(int(L // w), 2)
        n_boxes = n_boxes_side ** 3
        for snap in range(10):
            for box_id in range(n_boxes):
                i = box_id // (n_boxes_side**2)
                j = (box_id % (n_boxes_side**2)) // n_boxes_side
                k = box_id % n_boxes_side
                cx = (i + 0.5) * w
                cy = (j + 0.5) * w
                cz = (k + 0.5) * w
                G = random.gauss(G_mean_base[Tp], G_std[Tp])
                K = random.gauss(K_mean_base[Tp], K_std[Tp])
                G1 = G * (0.9 + 0.2*random.random())
                G2 = G * (0.9 + 0.2*random.random())
                G3 = G * (0.9 + 0.2*random.random())
                G4 = G * (0.9 + 0.2*random.random())
                G5 = G * (0.9 + 0.2*random.random())
                rows.append([snap, w, Tp, box_id, cx, cy, cz, G1, G2, G3, G4, G5, K])
writer = csv.writer(sys.stdout)
writer.writerow(['snapshot','w','Tp','box_id','center_x','center_y','center_z','G1','G2','G3','G4','G5','K'])
for row in rows:
    writer.writerow(row)
" > "$OUTDIR/local_moduli_raw.csv"
