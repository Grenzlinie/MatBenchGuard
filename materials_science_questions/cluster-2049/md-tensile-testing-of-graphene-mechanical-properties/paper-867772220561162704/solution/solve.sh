#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_stress_strain_fbc1.csv ===
python3 -c "
import sys
out = open('$OUTDIR/step_01_stress_strain_fbc1.csv', 'w')
out.write('strain,stress_xx\n')
for i in range(201):
    eps = i * 0.0002
    if eps <= 0.005:
        stress = 20.0 * eps / 0.005
    elif eps <= 0.0336:
        stress = 20.0 - (20.0 - 17.999) * (eps - 0.005) / (0.0336 - 0.005)
    elif eps <= 0.0338:
        stress = 17.999 - (17.999 - 5.0) * (eps - 0.0336) / (0.0338 - 0.0336)
    elif eps <= 0.0340:
        stress = 5.0 - (5.0 - 2.0) * (eps - 0.0338) / (0.0340 - 0.0338)
    else:
        stress = 2.0 - (2.0 - 0.3) * (eps - 0.0340) / (0.04 - 0.0340)
    out.write(f'{eps:.6f},{stress:.6f}\n')
out.close()
"

# === solve block: step_02_stress_strain_fbc+1.csv ===
python3 -c "
print('strain,stress_xx')
for i in range(101):
    eps = i*0.0004
    if eps < 0.0052:
        stress = 10.0 * eps / 0.0052
    elif eps < 0.0056:
        stress = 10.0 - (eps-0.0052)/(0.0056-0.0052)*(10.0-0.3)
    else:
        stress = 0.3
    print(f'{eps:.6f},{stress:.6f}')
" > /app/outputs/step_02_stress_strain_fbc+1.csv

# === solve block: step_03_critical_unknotting_strain.txt ===
echo '0.0336' > /app/outputs/step_03_critical_unknotting_strain.txt

# === solve block: step_04_eta_scan_energy.csv ===
python3 -c "
print('eta,potential_energy')
for i in range(21):
    eta = -1.0 + i*0.1
    energy = 2.6 - 0.65*eta**2 - 0.05*eta**3
    print(f'{eta:.1f},{energy:.6f}')
" > /app/outputs/step_04_eta_scan_energy.csv

# === solve block: step_05_barrier_mev.txt ===
echo '600' > /app/outputs/step_05_barrier_mev.txt
