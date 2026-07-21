#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash\nset -euo pipefail\nmkdir -p /app/outputs

# === solve block: results.csv ===
python3 <<'PYEOF'
import math, csv

params = [
    (2, 10, 10),
    (5, 10, 10),
    (2, 10, 30),
    (5, 10, 30),
    (5, 30, 10),
    (10, 30, 10),
    (5, 30, 30),
    (10, 30, 30),
    (2, 30, 10),
    (2, 30, 30),
]

KMAX = 3000

def compute_fg(sigma, t, xi):
    pref = 16.0 / (math.pi**4 * sigma)
    sum_f = 0.0
    sum_g = 0.0
    for k in range(KMAX+1):
        dk = (2*k + 1) ** 2
        for l in range(KMAX+1):
            dl = (2*l + 1) ** 2
            denom = dk * dl
            pkl = (math.pi / xi) * math.sqrt(dk + dl)
            e_pt   = math.exp(-pkl * t)
            e_p2s  = math.exp(-pkl * 2 * sigma)
            if t - 2*sigma >= 0:
                e_p_t2s = math.exp(-pkl * (t - 2*sigma))
            else:
                e_p_t2s = 0.0
            term_f = (1.0 - e_pt + e_p_t2s - e_p2s) / (pkl * denom)
            sum_f += term_f
            term_g = (t * e_pt - (t - 2*sigma) * e_p_t2s + 2*sigma * e_p2s) / denom
            sum_g += term_g
    f = pref * sum_f
    g = pref * sum_g
    return f, g

rows = []
for sigma, t, xi in params:
    f, g = compute_fg(sigma, t, xi)
    Bs_3333 = -(1.0 - g) * sigma / 2.0
    Bs_3311 = -(1.0 - 2*f + g) * sigma / 2.0
    Bs_1111 = -(math.pi * sigma * t) / (4.0 * xi)
    Bs_1122 =  (math.pi * sigma * t) / (4.0 * xi)
    Ks = -(3.0/4.0) * sigma * (1.0 - f)
    rows.append([sigma, t, xi, f, g, Bs_3333, Bs_3311, Bs_1111, Bs_1122, Ks])

# Save intermediate f, g
with open('/app/outputs/f_g.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['sigma','t','xi','f','g'])
    for row in rows:
        writer.writerow([f"{row[0]:.10f}", f"{row[1]:.10f}", f"{row[2]:.10f}", f"{row[3]:.10f}", f"{row[4]:.10f}"])

# Save final results
with open('/app/outputs/results.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['sigma','t','xi','f','g','Bs_3333','Bs_3311','Bs_1111','Bs_1122','Ks'])
    for row in rows:
        writer.writerow([f"{v:.10f}" for v in row])
PYEOF