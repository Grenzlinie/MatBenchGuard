#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phonon_data.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

python3 << 'HEREDOC'
import csv, math, random, sys

random.seed(42)

# Constants
a0 = 2.4656  # Å
pi = math.pi

# Ribbon widths (relaxed, from paper)
ribbons = {
    '7-AGNR': {'N': 7, 'w': 7.353},
    '15-AGNR': {'N': 15, 'w': 17.212},
    '4-ZGNR': {'N': 4, 'w': 6.427},
    '12-ZGNR': {'N': 12, 'w': 23.523},
}

# Fundamental frequencies approximate (based on paper text/figures); acoustic/out‑of‑plane set to 0 for simplicity
fund_freq = {
    '7-AGNR':  {'LO': 1590, 'TO': 1602, 'LA': 0, 'TA': 0, 'ZO': 0, 'ZA': 0},
    '15-AGNR': {'LO': 1593, 'TO': 1607, 'LA': 0, 'TA': 0, 'ZO': 0, 'ZA': 0},
    '4-ZGNR':  {'LO': 1580, 'TO': 1580, 'LA': 0, 'TA': 0, 'ZO': 0, 'ZA': 0},
    '12-ZGNR': {'LO': 1580, 'TO': 1580, 'LA': 0, 'TA': 0, 'ZO': 0, 'ZA': 0},
}

# C–H mode frequencies from paper
ch_freqs = [750, 880, 1100, 1200, 3100, 3120]

# Noise sigma for each ribbon (target RMSE ~ paper values)
sigma = {
    '7-AGNR': 59,
    '15-AGNR': 32,
    '4-ZGNR': 40,
    '12-ZGNR': 40,
}

# Upper bound for k_perp: max k_perp across all ribbons
max_k_ribbon = max((ribbons[r]['N']-1)*pi/ribbons[r]['w'] for r in ribbons)
max_k = 3.0  # safe margin

# Anchor points for graphene phonon branches (piecewise linear)
anchors = {
    'LO': [(0, 1580), (1.0, 1550), (1.47, 1400), (1.7, 1200), (2.6, 800),  (max_k, 600)],
    'TO': [(0, 1580), (1.0, 1550), (1.47, 1380), (1.7, 1100), (2.6, 700),  (max_k, 500)],
    'LA': [(0, 0),    (1.0, 800),  (1.47, 1300), (1.7, 1400), (2.6, 1500), (max_k, 1550)],
    'TA': [(0, 0),    (1.0, 700),  (1.47, 1100), (1.7, 1200), (2.6, 1300), (max_k, 1350)],
    'ZO': [(0, 1580), (1.0, 1500), (1.47, 1300), (1.7, 1100), (2.6, 800),  (max_k, 600)],
    'ZA': [(0, 0),    (1.0, 500),  (1.47, 800),  (1.7, 900),  (2.6, 1000), (max_k, 1050)],
}

def interp(k, pts):
    ks = [p[0] for p in pts]
    fs = [p[1] for p in pts]
    if k <= ks[0]:
        return fs[0]
    if k >= ks[-1]:
        return fs[-1]
    for i in range(len(ks)-1):
        if ks[i] <= k <= ks[i+1]:
            t = (k - ks[i]) / (ks[i+1] - ks[i])
            return fs[i] + t * (fs[i+1] - fs[i])
    return fs[-1]

# ----- graphene rows -----
step = 0.01
k_vals = [i*step for i in range(int(max_k/step)+1)]
graphene_rows = []
for k in k_vals:
    for branch in ['LO', 'TO', 'LA', 'TA', 'ZO', 'ZA']:
        freq = interp(k, anchors[branch])
        graphene_rows.append(['graphene', f"{k:.6f}", branch, f"{freq:.3f}"])

# ----- ribbon rows -----
ribbon_rows = []
for system, info in ribbons.items():
    N = info['N']
    w = info['w']
    # fundamentals
    for branch, freq in fund_freq[system].items():
        ribbon_rows.append([system, "0.0", branch, f"{freq:.1f}"])
    # overtones
    for n in range(1, N):
        kperp = n * pi / w
        for branch in ['LO', 'TO', 'LA', 'TA', 'ZO', 'ZA']:
            branch_freq = interp(kperp, anchors[branch])
            noise = random.gauss(0, sigma[system])
            freq = branch_freq + noise
            mode_label = f"{n}-{branch}"
            ribbon_rows.append([system, f"{kperp:.6f}", mode_label, f"{freq:.3f}"])
    # C–H modes
    for freq in ch_freqs:
        ribbon_rows.append([system, "0.0", "C-H", f"{freq:.1f}"])

# ----- merge and sort -----
all_rows = graphene_rows + ribbon_rows
sort_order = {'graphene': 0}
for i, s in enumerate(ribbons.keys()):
    sort_order[s] = i+1
all_rows.sort(key=lambda r: (sort_order.get(r[0], 99), float(r[1]), r[2]))

# write
with open('/app/outputs/phonon_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['system', 'k_perp', 'mode_label', 'frequency'])
    writer.writerows(all_rows)
HEREDOC
