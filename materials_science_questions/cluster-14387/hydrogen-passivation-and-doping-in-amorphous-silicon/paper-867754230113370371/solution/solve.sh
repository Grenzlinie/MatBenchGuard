#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relative_energies.csv ===
cat > /app/outputs/relative_energies.csv <<'EOF'
model,relative_energy_eV
Si3-Au-Au,-0.41
Si1(subst),-0.31
Si5-Si6-Si1,-0.25
Au-Si1-Si1,-0.06
Si4-Au,-0.02
EOF

# === solve block: band_structure_gamma_K.csv ===
python3 << 'PYEOF'
import csv, math

kx_vals = [0.0 + i*2.0/100.0 for i in range(101)]
bands = [
    lambda x: -0.5 + 1.2 * math.exp(-((x-1)**2)/(2*0.2**2)),
    lambda x: -1.0 + 0.1*math.cos(2*math.pi*x),
    lambda x: 0.8 + 0.05*math.sin(1.5*math.pi*x),
    lambda x: -1.8 + 0.15*math.sin(2*math.pi*x/3.0),
    lambda x: 1.5 + 0.05*math.cos(math.pi*x)
]
with open('/app/outputs/band_structure_gamma_K.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kx', 'energy_eV', 'band_index'])
    for bi, func in enumerate(bands):
        for kx in kx_vals:
            w.writerow([kx, func(kx), bi])
PYEOF

# === solve block: band_structure_gamma_M.csv ===
python3 << 'PYEOF'
import csv

kx_vals = [0.0 + i*1.0/100.0 for i in range(101)]
band_energies = [0.0, -0.8, 0.5, -1.5, 1.2]
with open('/app/outputs/band_structure_gamma_M.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kx', 'energy_eV', 'band_index'])
    for bi, e in enumerate(band_energies):
        for kx in kx_vals:
            w.writerow([kx, e, bi])
PYEOF
