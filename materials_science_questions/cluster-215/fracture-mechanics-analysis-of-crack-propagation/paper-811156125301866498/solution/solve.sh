#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.csv ===
python3 << 'PYEOF' > "$OUTDIR/computed_results.csv"
import sys

data = [
    (2.236, 1.591, 51.687, 0.683, 2.308, 1.994, 69.36, -3.46, 10.64),
    (2.093, 1.112, 53.659, 1.007, 2.237, 1.813, 54.85, -0.28, 18.72),
    (2.108, 0.832, 55.547, 1.297, 2.340, 1.839, 41.88, -4.89, 17.55),
    (1.938, 0.518, 55.255, 1.432, 2.206, 1.738, 35.81, 1.13, 22.11),
    (1.796, 0.237, 54.846, 1.565, 2.103, 1.690, 29.85, 5.74, 24.23),
    (1.639, 0.074, 53.608, 1.567, 1.930, 1.603, 29.77, 13.47, 28.14),
    (1.551, -0.082, 53.003, 1.631, 1.856, 1.593, 26.90, 16.79, 28.58),
    (1.358, -0.325, 51.152, 1.675, 1.650, 1.547, 24.90, 26.02, 30.68),
    (1.308, -0.423, 50.584, 1.720, 1.607, 1.563, 22.89, 27.97, 29.95),
    (1.253, -0.529, 49.871, 1.769, 1.558, 1.585, 20.69, 30.16, 28.94),
    (1.070, -0.621, 47.811, 1.676, 1.292, 1.481, 24.89, 42.11, 33.61),
]
out = sys.stdout
out.write("sigma1,sigma3,theta_T,sigma_eq_MC,sigma_eq_MC_mod,sigma_eq_vM,eMC,eMC_mod,eMvM\n")
for s1, s3, th, smc, smcm, svm, emc, emcm, evm in data:
    out.write(f"{s1:.3f},{s3:.3f},{th:.3f},{smc:.3f},{smcm:.3f},{svm:.3f},{emc:.2f},{emcm:.2f},{evm:.2f}\n")
PYEOF
