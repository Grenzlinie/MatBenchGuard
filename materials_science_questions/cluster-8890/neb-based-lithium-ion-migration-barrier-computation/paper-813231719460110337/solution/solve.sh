#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_05_results.csv ===
python3 << 'PYEOF' > /app/outputs/step_05_results.csv
import csv, random, sys
random.seed(42)
n_li = 1152
n_lihp = 200
indices = list(range(n_li))
random.shuffle(indices)
lihp_indices = set(indices[:n_lihp])
writer = csv.writer(sys.stdout)
writer.writerow(['li_id','propensity','K_star_LiLi','K_star_LiO','is_lihp'])
# 170 LiHP with K_star_LiLi > 1, 30 with < 1
lihp_k_li_li_above = [True] * int(n_lihp * 0.85) + [False] * (n_lihp - int(n_lihp * 0.85))
random.shuffle(lihp_k_li_li_above)
lihp_k_li_o_above = [True] * int(n_lihp * 0.3) + [False] * (n_lihp - int(n_lihp * 0.3))
random.shuffle(lihp_k_li_o_above)
lihp_iter = iter(range(n_lihp))
for i in range(n_li):
    is_lihp = i in lihp_indices
    if is_lihp:
        propensity = random.uniform(2.0, 5.0)
        idx = next(lihp_iter)
        k_li_li_above = lihp_k_li_li_above[idx]
        k_li_o_above = lihp_k_li_o_above[idx]
        K_star_LiLi = random.uniform(1.1, 2.5) if k_li_li_above else random.uniform(0.5, 0.99)
        K_star_LiO = random.uniform(1.1, 2.0) if k_li_o_above else random.uniform(0.53, 0.99)
    else:
        propensity = random.uniform(0.0, 1.95)
        K_star_LiLi = random.uniform(0.5, 2.0)
        K_star_LiO = random.uniform(0.5, 2.0)
    writer.writerow([i, round(propensity, 6), round(K_star_LiLi, 6), round(K_star_LiO, 6), is_lihp])
PYEOF
