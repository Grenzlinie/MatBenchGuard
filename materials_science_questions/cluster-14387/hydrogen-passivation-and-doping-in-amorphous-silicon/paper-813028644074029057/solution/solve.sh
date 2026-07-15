#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
cat > /app/outputs/formation_energies.json <<'EOF'
{
  "silanol": 0.51,
  "Si-OOH+Si-H": 4.20
}
EOF

# === solve block: barriers.json ===
cat > /app/outputs/barriers.json <<'EOF'
{
  "O-O_cleavage": 1.31,
  "Si-O_cleavage": 3.72
}
EOF

# === solve block: absorption_spectra.csv ===
cat << 'PYEOF' | python3
import csv, math

peaks = {
    'POL': [(6.47, 0.5, 0.1), (7.66, 0.3, 0.1)],
    'silanol': [(7.07, 0.8, 0.1), (7.44, 0.7, 0.1), (8.03, 0.6, 0.1)],
    'SiOOH_SiH': [(6.37, 0.9, 0.1), (7.17, 0.8, 0.1), (7.51, 0.7, 0.1)]
}

def gauss(x, c, h, s):
    return h * math.exp(-((x - c) / s) ** 2 / 2)

with open('/app/outputs/absorption_spectra.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['energy_eV', 'absorption_POL', 'absorption_silanol', 'absorption_SiOOH_SiH'])
    for i in range(1001):
        x = i * 0.01
        pol = sum(gauss(x, c, h, s) for c, h, s in peaks['POL'])
        siol = sum(gauss(x, c, h, s) for c, h, s in peaks['silanol'])
        siooh = sum(gauss(x, c, h, s) for c, h, s in peaks['SiOOH_SiH'])
        w.writerow([f'{x:.2f}', f'{pol:.6f}', f'{siol:.6f}', f'{siooh:.6f}'])
PYEOF
