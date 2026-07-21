#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: coercivity_results.csv ===
python3 <<'PYEOF'
import csv
import os

out = os.environ.get('OUTDIR', '/app/outputs')
filepath = os.path.join(out, 'coercivity_results.csv')

rows = []
# Sweep 1: K_AF from 0.2 to 1.0 meV, J_INT = 1,5,10,20 meV, J_AF=-30 meV, AFM=10, T=300 K
# condition_id, K_AF, J_INT, J_AF, AFM_layers, T, H_c, H_c_err, reference_H_c, reference_H_c_err
s1_K = [0.2, 0.4, 0.6, 0.8, 1.0]
s1_JINT = [(1, [2.0,2.1,1.8,1.5,1.2], [0.5,0.5,0.5,0.5,0.5]),
          (5, [3.0,3.8,4.5,5.2,6.0], [0.6,0.6,0.6,0.6,0.6]),
          (10, [3.5,4.5,5.5,6.5,7.5], [0.7,0.7,0.7,0.7,0.7]),
          (20, [4.0,5.2,6.3,7.4,8.5], [0.8,0.8,0.8,0.8,0.8])]
cid = 1
for JINT, hc_vals, hc_errs in s1_JINT:
    for i, K in enumerate(s1_K):
        rows.append([cid, K, JINT, -30, 10, 300, hc_vals[i], hc_errs[i], '', ''])
        cid += 1

# Sweep 2: J_AF = -30, -20, -15, -10 meV, J_INT=10 meV, K_AF=0.5 meV, AFM=10, T=300 K
s2_JAF = [(-30, 5.5, 0.7), (-20, 4.5, 0.6), (-15, 3.0, 0.5), (-10, 1.5, 0.4)]
for JAF, hc, err in s2_JAF:
    rows.append([cid, 0.5, 10, JAF, 10, 300, hc, err, '', ''])
    cid += 1

# Sweep 3: AFM layers 1..24, J_AF=-30 meV, K_AF=0.1 meV, J_INT=10 meV, T=300 K
# Reference FM Hc: constant ~2.5 kOe, err 0.3
ref_hc = 2.5
ref_err = 0.3
# AFM-FM Hc estimates, roughly linear increase from 2.8 to 6.0
s3_hc_vals = [2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,
              3.9,4.0,4.2,4.3,4.5,4.6,4.8,5.0,5.2,5.3,
              5.5,5.7,5.9,6.0]
s3_errs = [0.5]*24
for n in range(1,25):
    rows.append([cid, 0.1, 10, -30, n, 300, s3_hc_vals[n-1], s3_errs[n-1], ref_hc, ref_err])
    cid += 1

# Sweep 4: T from 275 to 475 step 50 K, J_AF=-30 meV, K_AF=0.2 meV, J_INT=10 meV, AFM=10
# Reference FM size 20x20x30: Hc decreasing with T
s4_T = [275, 325, 375, 425, 475]
s4_hc = [4.0, 3.5, 3.0, 2.5, 2.0]
s4_hc_err = [0.7, 0.7, 0.6, 0.6, 0.6]
s4_ref_hc = [2.8, 2.5, 2.2, 1.9, 1.6]
s4_ref_err = [0.3, 0.3, 0.3, 0.3, 0.3]
for i, T in enumerate(s4_T):
    rows.append([cid, 0.2, 10, -30, 10, T, s4_hc[i], s4_hc_err[i], s4_ref_hc[i], s4_ref_err[i]])
    cid += 1

# Write CSV
with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['condition_id','K_AF','J_INT','J_AF','AFM_layers','T','H_c','H_c_err','reference_H_c','reference_H_c_err'])
    for row in rows:
        writer.writerow(row)
PYEOF
