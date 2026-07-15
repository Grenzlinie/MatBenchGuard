#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants_mgo.csv ===
python3 << 'PYEOF'
import csv, math
alphaD = 4.42e-5
delta11 = 5.38
delta44 = 2.49
T_D = 900
C11_0 = 261.9
C44_0 = 148.1
temps = range(900, 2801, 100)
rows = []
for T in temps:
    dt = T - T_D
    C11_mur1 = C11_0 * (1 + alphaD*dt + 0.5*alphaD**2*delta11*dt**2) ** (-delta11)
    C11_mur2 = C11_0 * (1 + alphaD*dt + 0.5*alphaD**2*delta11*dt**2 + (1/3)*alphaD**3*delta11**2*dt**3) ** (-delta11)
    C11_tal1 = C11_0 * math.exp(-delta11 * (alphaD*dt + 0.5*alphaD**2*delta11*dt**2))
    C11_tal2 = C11_0 * math.exp(-delta11 * (alphaD*dt + 0.5*alphaD**2*delta11*dt**2 + (1/3)*alphaD**3*delta11**2*dt**3))
    C44_mur1 = C44_0 * (1 + alphaD*dt + 0.5*alphaD**2*delta44*dt**2) ** (-delta44)
    C44_mur2 = C44_0 * (1 + alphaD*dt + 0.5*alphaD**2*delta44*dt**2 + (1/3)*alphaD**3*delta44**2*dt**3) ** (-delta44)
    C44_tal1 = C44_0 * math.exp(-delta44 * (alphaD*dt + 0.5*alphaD**2*delta44*dt**2))
    C44_tal2 = C44_0 * math.exp(-delta44 * (alphaD*dt + 0.5*alphaD**2*delta44*dt**2 + (1/3)*alphaD**3*delta44**2*dt**3))
    rows.append([T, C11_mur1, C11_mur2, C11_tal1, C11_tal2, C44_mur1, C44_mur2, C44_tal1, C44_tal2])
with open('/app/outputs/elastic_constants_mgo.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Temperature(K)','C11_Mur1','C11_Mur2','C11_Tal1','C11_Tal2','C44_Mur1','C44_Mur2','C44_Tal1','C44_Tal2'])
    w.writerows(rows)
PYEOF
