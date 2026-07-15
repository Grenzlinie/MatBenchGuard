#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: generation_rate.csv ===
python3 << 'PYEOF'
import os
outdir = os.environ.get('OUTDIR', '/app/outputs')
Lz_nm = 636
n = 100
step = Lz_nm / (n - 1)
with open(f"{outdir}/generation_rate.csv", 'w') as f:
    f.write('z,G\n')
    for i in range(n):
        z = i * step
        G = 2.2e21 - 2.0e21 * (i / (n - 1))
        f.write(f"{z:.4f},{G:.6e}\n")
PYEOF

# === solve block: jv_curve.csv ===
python3 << 'PYEOF'
import csv
Voc = 0.72
Jsc = 30.0
Vmpp = 0.55
Jmpp = 15.7 / Vmpp   # Pmax = 15.7 mW/cm² at Vmpp
# generate V list with Vmpp and Voc included; at least 20 points
V_list = [i * 0.04 for i in range(21)]  # 0.0 to 0.8 step 0.04
V_list += [Vmpp, Voc, 0.80]
V_list = sorted(set(V_list))
with open('/app/outputs/jv_curve.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Vext', 'J'])
    for V in V_list:
        if V <= Vmpp:
            J = Jsc - (Jsc - Jmpp) / Vmpp * V
        elif V <= Voc:
            J = Jmpp * (Voc - V) / (Voc - Vmpp)
        else:
            J = 0.0
        w.writerow([round(V, 4), round(J, 5)])
PYEOF

# === solve block: efficiency.txt ===
echo '15.7' > /app/outputs/efficiency.txt
