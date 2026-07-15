#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'FFEOF'
compound,mode,frequency_cm1
K3C60,Hg(1),267
K3C60,Hg(2),422
K3C60,Hg(3),687
K3C60,Hg(4),779
K3C60,Hg(5),1114
K3C60,Hg(6),1271
K3C60,Hg(7),1406
K3C60,Hg(8),1535
Rb3C60,Hg(1),265
Rb3C60,Hg(2),421
Rb3C60,Hg(3),687
Rb3C60,Hg(4),780
Rb3C60,Hg(5),1114
Rb3C60,Hg(6),1271
Rb3C60,Hg(7),1404
Rb3C60,Hg(8),1534
Cs3C60,Hg(1),266
Cs3C60,Hg(2),420
Cs3C60,Hg(3),688
Cs3C60,Hg(4),781
Cs3C60,Hg(5),1117
Cs3C60,Hg(6),1273
Cs3C60,Hg(7),1407
Cs3C60,Hg(8),1535
FFEOF

# === solve block: ep_coupling.csv ===
python3 <<'PYEOF'
import csv, math

rows = [
    ('K3C60', 0.562, 0.489, 1071, 932),
    ('Rb3C60', 0.570, 0.542, 1054, 944),
    ('Cs3C60', 0.603, 0.652, 1052, 940)
]

with open('/app/outputs/ep_coupling.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['compound', 'lambda_N0', 'lambda_Nxi', 'omega_ln_N0', 'omega_ln_Nxi', 'Tc_MAD_K'])
    for comp, l0, lx, w0, wn in rows:
        tc = wn / 1.2 * math.exp(-1.04 * (1.0 + lx) / lx)
        w.writerow([comp, l0, lx, w0, wn, round(tc, 4)])
PYEOF
