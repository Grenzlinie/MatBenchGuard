#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_stable_phases.csv ===
python3 << 'EOF'
import csv, math

phi_vals = [round(0.15 + 0.05*i, 2) for i in range(15)]  # 0.15 .. 0.85
chiN_vals = [12.0 + 0.5*i for i in range(17)]  # 12.0 .. 20.0

def melting_chiN(phi):
    # double lobe with peaks near phi=0.33 and phi=0.65, eutectic near 0.5
    base = 13.0
    lobe1_amp = 5.0
    lobe2_amp = 5.0
    width = 0.08
    lobe1 = lobe1_amp * math.exp(-((phi - 0.33) / width) ** 2)
    lobe2 = lobe2_amp * math.exp(-((phi - 0.65) / width) ** 2)
    # add a slight V shape to deepen the eutectic
    v_shape = 2.0 * abs(phi - 0.5)
    return base + lobe1 + lobe2 + v_shape

with open('/app/outputs/step_01_stable_phases.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['phi_A_tot', 'chiN', 'phase'])
    for phi in phi_vals:
        chi_melt = melting_chiN(phi)
        for chiN in chiN_vals:
            if chiN < chi_melt:
                phase = 'Dis'
            else:
                if phi <= 0.45:
                    phase = 'Hex_II'
                elif phi <= 0.55:
                    phase = 'Lam'
                else:
                    phase = 'Hex'
            writer.writerow([phi, chiN, phase])
EOF

# === solve block: step_02_grand_potentials.json ===
python3 /solution/gen_output.py grand_json > /app/outputs/step_02_grand_potentials.json
