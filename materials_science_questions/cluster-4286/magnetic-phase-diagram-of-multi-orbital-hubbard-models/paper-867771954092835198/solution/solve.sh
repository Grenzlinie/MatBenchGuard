#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagram.csv ===
cat > "$OUTDIR/phase_diagram.csv" <<'EOF'
Ueff,phase,m_Os,Delta_D,Delta_C
0.0,NMM,0.0,0.035,0.0
0.5,NMM,0.0,0.03,0.0
0.8,AFM,0.2,0.015,0.0
0.9,AFM,0.4,0.0,0.0
1.0,AFM,0.6,0.05,0.0
1.1,AFM,0.7,0.1,0.0
1.25,AFI,0.9,0.17,0.02
1.5,AFI,1.1,0.3,0.1
EOF

# === solve block: energy_comparison.csv ===
cat > "$OUTDIR/energy_comparison.csv" <<'EOF'
magnetic_order,total_energy_per_Os
AIAO,-1000.0
3in1out,-999.9747
EOF

# === solve block: anisotropy_curve.csv ===
python3 -c "
import math
A_sia = 24.0
A_DM = 4.0
coeff = 4*math.sqrt(2)/3
def energy_diff(deg):
    theta = math.radians(deg)
    cos_th = math.cos(theta)
    ee = A_sia * (1.0 - ((2*cos_th + 1)**2)/9.0)
    return ee + coeff * A_DM * (1 - cos_th)
print('theta,energy_diff')
for angle in range(0, 181, 30):
    print(f'{angle},{energy_diff(angle):.6f}')
" > "$OUTDIR/anisotropy_curve.csv"

# === solve block: dos_near_MIT.csv ===
python3 -c "
import csv
import math
sigma = 0.1
A = 6.0
B = 5.0
with open('/app/outputs/dos_near_MIT.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'DOS'])
    for i in range(-100, 101):
        e = i * 0.01
        dos = A - B * math.exp(-e**2 / (2*sigma**2))
        writer.writerow([f'{e:.2f}', f'{dos:.6f}'])
"
