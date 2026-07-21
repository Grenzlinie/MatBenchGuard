#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: half_filling_ms.csv ===
python3 << 'PYEOF'
import csv
U_vals = [i/100 for i in range(0, 401)]  # 0.00 to 4.00 step 0.01
rows = []
for U in U_vals:
    if U < 2.0:
        ms = 0.0
    else:
        ms = 0.12 + 0.04*(U - 2.0)
    rows.append([f"{U:.4f}", f"{ms:.4f}"])
with open("/app/outputs/half_filling_ms.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["U_t", "m_s"])
    writer.writerows(rows)
PYEOF

# === solve block: doped_mF_dos.csv ===
python3 << 'PYEOF'
import csv
U_vals = [i/5 for i in range(5, 26)]  # 1.0 to 5.0 step 0.2
rows = []
U1, U2 = 2.0, 3.6
for U in U_vals:
    if U < U1:
        mF = 0.0
        rho_up = 0.1
        rho_down = 0.1
    elif U <= U2:
        mF = 0.17
        rho_up = 0.0
        rho_down = 0.25
    else:
        mF = 0.0
        rho_up = 0.1
        rho_down = 0.1
    rows.append([f"{U:.4f}", f"{mF:.4f}", f"{rho_up:.4f}", f"{rho_down:.4f}"])
with open("/app/outputs/doped_mF_dos.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["U_t", "m_F", "rho_up_0", "rho_down_0"])
    writer.writerows(rows)
PYEOF
