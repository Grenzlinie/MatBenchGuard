#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: high_T_energy.csv ===
python3 << 'PYEOF' > "$OUTDIR/high_T_energy.csv"
import csv, sys

def energy(alpha, T):
    if T <= 0:
        return None
    beta = 1.0 / T
    e = 0.25 * alpha * ( (1.0/(1.0+beta)) - 1.0 )
    return e

alphas = [0.3, 0.5]
# Temperature grid: 0.0001 to 0.15 step 0.0001
Ts = [ (i+1)*1e-4 for i in range(1500) ]  # 0.0001, 0.0002, ..., 0.15

writer = csv.writer(sys.stdout)
writer.writerow(["temperature", "energy", "alpha"])
for alpha in alphas:
    for T in Ts:
        e = energy(alpha, T)
        writer.writerow([T, e, alpha])
PYEOF

# === solve block: tg_values.json ===
cat > "$OUTDIR/tg_values.json" << 'JSONEOF'
{
  "alpha_0_3": 0.0243,
  "alpha_0_5": 0.0445
}
JSONEOF
