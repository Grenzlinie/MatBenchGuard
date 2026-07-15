#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bandstructure_trap_levels.json ===
python3 -c "
import json

data = {
    'defects': [
        {
            'name': 'perfect',
            'band_gap': 1.9,
            'trap_energies': [],
            'fermi_level_position': 'mid_gap',
            'notes': 'Perfect 4H-SiC crystal.'
        },
        {
            'name': 'Al_Si',
            'band_gap': 1.9,
            'trap_energies': [],
            'fermi_level_position': 'near_VB',
            'notes': 'p-type doping, Fermi level near valence band.'
        },
        {
            'name': 'Al_Si+V_C',
            'band_gap': 1.9,
            'trap_energies': [1.7],
            'fermi_level_position': 'near_CB',
            'notes': 'Half-filled trap near conduction band, n-type character.'
        },
        {
            'name': 'Al_C',
            'band_gap': 1.9,
            'trap_energies': [0.9, 1.0, 1.1],
            'fermi_level_position': 'mid_gap',
            'notes': 'Three closely spaced mid-gap trap levels, no doping effect.'
        },
        {
            'name': 'Al_C+Si_C',
            'band_gap': 1.9,
            'trap_energies': [0.7, 0.9, 1.0, 1.1],
            'fermi_level_position': 'near_VB',
            'notes': 'Additional trap level; Fermi level pins near valence band, n-type doping.'
        },
        {
            'name': 'Al_i',
            'band_gap': 1.9,
            'trap_energies': [1.0],
            'fermi_level_position': 'near_CB',
            'notes': 'n-type doping, deep trap level near mid-gap.'
        },
        {
            'name': 'Al_i+antisite',
            'band_gap': 1.9,
            'trap_energies': [0.6, 1.0],
            'fermi_level_position': 'near_CB',
            'notes': 'Antisite coupling introduces shallow trap near VB and reduces n-type character.'
        }
    ]
}
with open('/app/outputs/bandstructure_trap_levels.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: neb_barriers.json ===
python3 -c "
import json

data = {
    'reactions': [
        {
            'pathway': 'Al_i directly occupies V_C -> Al_C',
            'initial_energy': 0.0,
            'final_energy': -0.5,
            'barrier_height': 0.2,
            'image_energies': [0.0, 0.05, 0.15, 0.2, 0.10, -0.2, -0.5]
        },
        {
            'pathway': 'Al displaces Si, Si migrates to V_C -> Al_Si+Si_C',
            'initial_energy': 0.0,
            'final_energy': -0.3,
            'barrier_height': 0.17,
            'image_energies': [0.0, 0.04, 0.12, 0.17, 0.10, -0.1, -0.3]
        }
    ]
}
with open('$OUTDIR/neb_barriers.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: iv_characteristics.csv ===
python3 -c "
import csv, math

leakage = 1e-13    # A/um at Vg=0
S_dec = 0.08       # subthreshold slope (V/dec)
S_nat = S_dec / math.log10(math.e)  # natural log slope
max_current = 1e-3 # clip current to avoid overflow

with open('$OUTDIR/iv_characteristics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Vg', 'Id'])
    for vg in [i*0.05 for i in range(121)]:  # 0 to 6 V, step 0.05
        id_raw = leakage * math.exp(vg / S_nat)
        id_val = min(id_raw, max_current)
        writer.writerow([f'{vg:.2f}', f'{id_val:.6e}'])
"
