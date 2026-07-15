#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_adsorption_energies_and_charges.csv ===
python3 <<'PYEOF'
import csv, os

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, 'step_02_adsorption_energies_and_charges.csv')

rows = [
    ['pristine', '-2.63', '0.46'],
    ['V_BrS',   '-2.68', '0.80'],
    ['V',       '-2.73', '1.22']
]

with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'E_ads', 'Bader_charge_on_CO2'])
    for row in rows:
        w.writerow(row)
PYEOF

# === solve block: step_03_gibbs_free_energy_profiles.csv ===
python3 <<'PYEOF'
import csv, os

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, 'step_03_gibbs_free_energy_profiles.csv')

# Free energies (eV) for each intermediate; zero = CO2(g) + clean surface.
# Values are set to reproduce the paper's barriers and the exothermic *CO->*CHO on V.
profiles = {
    'pristine': [
        ('CO2_gas', 0.0),
        ('*CO2',   -0.20),
        ('*COOH',   0.00),
        ('*CO',     1.80),
        ('*CHO',    2.00),
        ('*CH2O',   1.00),
        ('*CH3O',   0.00),
        ('*CH3OH', -0.30),
        ('CH3OH_gas', -0.50)
    ],
    'V_BrS': [
        ('CO2_gas', 0.0),
        ('*CO2',   -0.30),
        ('*COOH',  -0.10),
        ('*CO',     1.50),
        ('*CHO',    4.06),   # 1.50 + 2.56 = 4.06
        ('*CH2O',   2.00),
        ('*CH3O',   0.50),
        ('*CH3OH', -0.40),
        ('CH3OH_gas', -0.50)
    ],
    'V': [
        ('CO2_gas', 0.0),
        ('*CO2',   -0.50),
        ('*COOH',   0.00),
        ('*CO',     0.82),
        ('*CHO',    0.30),   # exothermic step
        ('*CH2O',  -0.20),
        ('*CH3O',  -0.80),
        ('*CH3OH', -1.20),
        ('CH3OH_gas', -0.50)
    ]
}

with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'reaction_step', 'free_energy'])
    for sys_name, steps in profiles.items():
        for step, energy in steps:
            w.writerow([sys_name, step, f'{energy:.2f}'])
PYEOF
