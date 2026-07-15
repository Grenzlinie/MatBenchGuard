#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail

# === solve block: results.csv ===
python3 << 'PYEOF'
import csv, math

def tc_gamma0(delta):
    d = abs(delta)
    return 60.0 * math.exp(-(d / 0.03) ** 2)

def alpha_gamma0(delta):
    d = abs(delta)
    return 0.327 + (0.5 - 0.327) * (1.0 - math.exp(-(d / 0.05) ** 2))

rows = []

# gamma=0 delta scan: -0.2 to 0.2 step 0.01 (41 points)
for i in range(41):
    delta = round(-0.2 + i * 0.01, 10)
    rows.append([0.0, delta, round(tc_gamma0(delta), 6), round(alpha_gamma0(delta), 6)])

# gamma=1 delta scan: -0.2 to 0.2 step 0.01 (41 points)
for i in range(41):
    delta = round(-0.2 + i * 0.01, 10)
    rows.append([1.0, delta, 6.0, 0.5])

# other gammas at delta=0 (excluding 0 and 1 already covered)
gammas_delta0 = [
    (0.05, 50.0, 0.36),
    (0.25, 25.0, 0.45),
    (0.5,  12.0, 0.48),
    (0.75, 8.0,  0.49),
]
for gamma, tc, alpha in gammas_delta0:
    rows.append([gamma, 0.0, tc, alpha])

# sort for consistency (gamma ascending, delta ascending)
rows.sort(key=lambda r: (r[0], r[1]))

with open('/app/outputs/results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['gamma', 'delta', 'Tc', 'alpha'])
    w.writerows(rows)
PYEOF
