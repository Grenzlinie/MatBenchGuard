#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_results.csv ===
export OUTFILE="$OUTDIR/step_01_results.csv"
python3 << 'PYEOF'
import csv, os
alphas = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100]
outfile = os.environ["OUTFILE"]
with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["alpha","p","E0","m_star_over_m"])
    for a in alphas:
        p = max(1.0, 2*a/3.0 + 0.5)
        for _ in range(50):
            fp = p**4 - (2*a/3)*p**3 - 1
            dfp = 4*p**3 - 2*a*p**2
            if dfp == 0:
                break
            pnew = p - fp/dfp
            if abs(pnew - p) < 1e-15 * pnew:
                p = pnew
                break
            p = pnew
        E0 = -3*(p*p-1)*(p*p+3)/(4*p*p)
        mstar = ((p*p-1)*(p**4+2*p*p-2)/(p*p+1)) + 1
        writer.writerow([a, p, E0, mstar])
PYEOF
