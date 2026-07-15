#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy pandas scikit-learn mlxtend
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/compute.py "$OUTDIR"

# === solve block: indices_values.csv ===
python3 -c "
import csv
outpath = '$OUTDIR/indices_values.csv'
with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['m','n','R1','Rm1','R12','Rm12','ABC','GA','F','AZI','M1','M2','ReZG1','ReZG2','ReZG3',
                'CR1','CRm1','CR12','CRm12','CABC','CGA','CF','CAZI','CM1','CM2','CReZG1','CReZG2','CReZG3',
                'RR1','RRm1','RR12','RRm12','RABC','RGA','RF','RAZI','RM1','RM2','RReZG1','RReZG2','RReZG3'])
    for m in range(1,101):
        for n in range(1,101):
            # Original indices (Theorem 2)
            R1   = 164*m*n - 40*m - 40*n + 20
            Rm1  = 1.2778*m*n + 0.8333*m + 0.8333*n + 2.1667
            R12  = 47.5118*m*n - 7.3722*m - 7.3722*n + 2.1593
            Rm12 = 4.1950*m*n + 1.0641*m + 1.0641*n + 0.4408
            ABC  = 9.4860*m*n + 0.2464*m + 0.2464*n + 0.1911
            GA   = 13.07998*m*n + 0.1890*m + 0.1890*n - 0.8728
            F    = 430*m*n - 96*m - 96*n + 72
            AZI  = 153.3818*m*n - 23.296*m - 23.296*n + 4.796
            M1   = 102*m*n - 16*m - 16*n + 8
            M2   = 164*m*n - 40*m - 40*n + 20
            ReZG1 = 11.6667*m*n + 2*m + 2*n + 2
            ReZG2 = 22.1905*m*n - 3.3905*m - 3.3905*n + 0.2571
            ReZG3 = 1236*m*n - 344*m - 344*n + 232
            # Coindices (Theorem 3)
            CR1   = 358*m**2*n**2 - 384*m**2*n + 10*m*n**2 + 564*m*n + 8*m**2 - 8*n**2 - 320*m + 176*n + 124
            CRm1  = 5.556*m**2*n**2 - 7.6667*m**2*n + 5.6667*m*n**2 + 31.611*m*n + m**2 - n**2 - 26.333*m + 22.6667*n + 35.8333
            CR12  = 116.7631*m**2*n**2 + 16.0897*m**2*n + 65.4523*m*n**2 + 241.1257*m*n + 22.6274*m**2 - 22.6274*n**2 - 157.7649*m - 22.0004*n + 105.7230
            CRm12 = 14.5013*m**2*n**2 - 20.3869*m**2*n + 12.4207*m*n**2 + 56.8750*m*n + 2.8284*m**2 - 2.8284*n**2 - 45.1768*m + 38.0554*n + 56.6045
            CABC  = 27.708*m**2*n**2 + 31.3591*m**2*n + 20.0454*m*n**2 + 81.1132*m*n + 5.6569*m**2 - 5.6569*n**2 - 58.2292*m + 40.7658*n + 53.5490
            CGA   = 38.0393*m**2*n**2 - 49.8105*m**2*n + 26.8076*m*n**2 + 104.8371*m*n + 7.5425*m**2 - 7.5425*n**2 - 78.9863*m + 56*n + 73.6701
            CF    = 928*m**2*n**2 - 972*m**2*n + 452*m*n**2 + 790*m*n + 16*m**2 - 16*n**2 - 752*m + 368*n + 248
            CAZI  = 379.3077*m**2*n**2 - 881*m**2*n + 200.704*m*n**2 + 1803.9942*m*n + 64*m**2 - 64*n**2 - 632.704*m + 486.816*n + 603.204
            CM1   = 248*m**2*n**2 - 292*m**2*n + 140*m*n**2 + 518*m*n + 48*m**2 - 48*n**2 - 328*m + 200*n + 360
            CM2   = 358*m**2*n**2 - 384*m**2*n + 160*m*n**2 + 564*m*n + 8*m**2 - 8*n**2 - 320*m + 176*n + 124
            CReZG1 = 35.6667*m**2*n**2 - 47.6667*m**2*n + 31*m*n**2 + 129.6667*m*n + 6*m**2 - 6*n**2 - 67*m + 74*n + 100
            CReZG2 = 49.1230*m**2*n**2 - 65.7908*m**2*n + 30.7429*m*n**2 + 112.533*m*n + 10.6667*m**2 - 10.6667*n**2 - 82.6095*m + 48.0571*n + 67.7429
            CReZG3 = 2504*m**2*n**2 - 2368*m**2*n + 928*m*n**2 + 3068*m*n + 389*m**2 - 389*n**2 - 1410*m + 696*n + 1240
            # Reverse indices (Theorem 4)
            RR1   = 136*m*n + 72*m + 72*n - 36
            RRm1  = 1.9*m*n - 0.24*m - 0.24*n + 0.18
            RR12  = 42.2926*m*n + 8.5402*m + 8.5402*n - 4.9239
            RRm12 = 4.9764*m*n - 0.4931*m - 0.4931*n + 0.3954
            RABC  = 10.4216*m*n + 0.4957*m + 0.4957*n - 2.5028
            RGA   = 12.4134*m*n + 0.1433*m + 0.1433*n - 0.2159
            RF    = 374*m*n + 128*m + 128*n - 40
            RAZI  = 130.3493*m*n + 9.7612*m + 9.7612*n + 118.8296
            RM1   = 90*m*n + 16*m + 16*n - 8
            RM2   = 136*m*n + 72*m + 72*n + 144
            RReZG1 = 11.7667*m*n + 0.2*m + 0.2*n + 0.8
            RReZG2 = 15.5405*m*n + 6.7540*m + 6.7540*n - 2.9115
            RReZG3 = 976*m*n + 904*m + 904*n - 344
            w.writerow([m,n, R1,Rm1,R12,Rm12, ABC,GA,F,AZI, M1,M2,ReZG1,ReZG2,ReZG3,
                        CR1,CRm1,CR12,CRm12, CABC,CGA,CF,CAZI, CM1,CM2,CReZG1,CReZG2,CReZG3,
                        RR1,RRm1,RR12,RRm12, RABC,RGA,RF,RAZI, RM1,RM2,RReZG1,RReZG2,RReZG3])
"

# === solve block: feature_selection_ranking.csv ===
echo "feature_selection_ranking.csv written by compute.py"

# === solve block: regression_ranking.csv ===
echo "regression_ranking.csv written by compute.py"
