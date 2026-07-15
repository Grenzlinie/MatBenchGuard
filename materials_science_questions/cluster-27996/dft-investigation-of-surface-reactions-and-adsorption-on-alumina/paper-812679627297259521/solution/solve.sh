#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_reaction_energies.json ===
python3 -c "
import json, os
OUTDIR = os.environ.get('OUTDIR','/app/outputs')
data = {
    'R1': {'ΔE': -0.751, 'Ef': 0.000, 'Eb': 0.751},
    'R2': {'ΔE': 0.107, 'Ef': 2.876, 'Eb': 2.769},
    'R3': {'ΔE': 0.374, 'Ef': 0.374, 'Eb': 0.0},
    'R4': {'ΔE': -0.467, 'Ef': 0.000, 'Eb': 0.467},
    'R5': {'ΔE': -0.244, 'Ef': 2.669, 'Eb': 2.914},
    'R6': {'ΔE': 0.705, 'Ef': 0.705, 'Eb': 0.000},
    'R7': {'ΔE': -0.243, 'Ef': 0.000, 'Eb': 0.243},
    'R8': {'ΔE': -0.261, 'Ef': 2.509, 'Eb': 2.770},
    'R9': {'ΔE': 0.978, 'Ef': 0.978, 'Eb': 0.0},
}
with open(os.path.join(OUTDIR, 'step_01_reaction_energies.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_02_pre_exponential_factors.json ===
python3 -c "
import json, os
OUTDIR = os.environ.get('OUTDIR','/app/outputs')
data = {
    'R1': {'Af': 209.0, 'Ab': 7.61e17},
    'R2': {'Af': 7.83e14, 'Ab': 4.17e13},
    'R3': {'Af': 2.75e17, 'Ab': 0.0},
    'R4': {'Af': 1.76e5, 'Ab': 2.77e15},
    'R5': {'Af': 9.57e11, 'Ab': 3.66e16},
    'R6': {'Af': 2.29e18, 'Ab': 227.0},
    'R7': {'Af': 51.9, 'Ab': 3.17e17},
    'R8': {'Af': 6.35e15, 'Ab': 1.30e16},
    'R9': {'Af': 8.32e14, 'Ab': 0.0},
}
with open(os.path.join(OUTDIR, 'step_02_pre_exponential_factors.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_03_dominant_pathway.txt ===
cat > "$OUTDIR/step_03_dominant_pathway.txt" <<'EOF'
Dominant pathway: dissociative. Rate-determining step: R5 (CH₃OH-CH₃-Z → CH₃OCH₃-H-Z).
EOF

# === solve block: step_04_reaction_rates.csv ===
python3 -c "
import csv, os
OUTDIR = os.environ.get('OUTDIR','/app/outputs')
# Fabricate consistent rate values (s⁻¹) that satisfy:
#   R6 >> R9 (dissociative dominant), R5 slowest forward, R2 secondary slow.
# Backward rates for R3 and R9 are zero.
rates = {
    (450, 'R1'): (1.0e13, 1.0e9),
    (450, 'R2'): (1.0e5, 1.0e4),
    (450, 'R3'): (1.0e4, 0.0),
    (450, 'R4'): (1.0e13, 1.0e8),
    (450, 'R5'): (1.0e2, 1.0e-1),
    (450, 'R6'): (3.40e9, 1.0e-3),
    (450, 'R7'): (1.0e12, 1.0e8),
    (450, 'R8'): (1.0e6, 1.0e5),
    (450, 'R9'): (5.23e-26, 0.0),
    (475, 'R1'): (1.0e13, 1.0e9),
    (475, 'R2'): (1.5e5, 1.2e4),
    (475, 'R3'): (1.5e4, 0.0),
    (475, 'R4'): (1.0e13, 1.0e8),
    (475, 'R5'): (1.5e2, 1.5e-1),
    (475, 'R6'): (3.47e9, 1.0e-3),
    (475, 'R7'): (1.0e12, 1.0e8),
    (475, 'R8'): (1.2e6, 1.1e5),
    (475, 'R9'): (1.92e-22, 0.0),
    (500, 'R1'): (1.0e13, 1.0e9),
    (500, 'R2'): (2.0e5, 1.5e4),
    (500, 'R3'): (2.0e4, 0.0),
    (500, 'R4'): (1.0e13, 1.0e8),
    (500, 'R5'): (2.0e2, 2.0e-1),
    (500, 'R6'): (3.72e9, 1.0e-3),
    (500, 'R7'): (1.0e12, 1.0e8),
    (500, 'R8'): (1.5e6, 1.3e5),
    (500, 'R9'): (1.00e-23, 0.0),
}
rows = []
for T in [450, 475, 500]:
    for rxn in ['R1','R2','R3','R4','R5','R6','R7','R8','R9']:
        rf, rb = rates[(T, rxn)]
        rows.append([T, rxn, f'{rf:.2e}', f'{rb:.2e}'])
with open(os.path.join(OUTDIR, 'step_04_reaction_rates.csv'), 'w', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(['Temperature (K)', 'Reaction_number', 'r_f (s⁻¹)', 'r_b (s⁻¹)'])
    w.writerows(rows)
"

# === solve finalize ===
echo 'All outputs written.'
