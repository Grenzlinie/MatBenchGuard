#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
python3 <<'PYEOF'
import csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ['surface', 'species', 'adsorption_energy_eV'],
    ['Pd(211)',    'CO',     '-1.95'],
    ['Pd(211)',    'H',      '-0.48'],
    ['Pd(211)',    'CH3OH',  '-0.36'],
    ['Pd(211)',    'H2O',    '-0.21'],
    ['Pd(211)',    'CH2O',   '-0.84'],
    ['Pd(211)-B',  'CO',     '-1.32'],
    ['Pd(211)-B',  'H',      '-0.31'],
    ['Pd(211)-B',  'CH3OH',  '-0.34'],
    ['Pd(211)-B',  'H2O',    '-0.20'],
    ['Pd(211)-B',  'CH2O',   '-0.59'],
]

with open(f'{outdir}/adsorption_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: reaction_barriers.csv ===
python3 <<'PYEOF'
import csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ['surface',   'reaction_step',     'activation_energy_eV', 'reaction_energy_eV'],
    ['Pd(211)',   'CO+H→CHO',         '1.21',                  '1.20'],
    ['Pd(211)',   'CHO+H→CHOH',       '0.55',                  '0.28'],
    ['Pd(211)',   'CHOH+H→CH2OH',     '0.84',                  '0.60'],
    ['Pd(211)',   'CH2OH+H→CH3OH',    '0.90',                  '0.27'],
    ['Pd(211)',   'COH→C+OH',         '1.34',                  '-0.10'],
    ['Pd(211)-B', 'CO+H→CHO',         '1.03',                  '0.81'],
    ['Pd(211)-B', 'CHO+H→CHOH',       '0.84',                  '0.48'],
    ['Pd(211)-B', 'CHOH+H→CH2OH',     '0.49',                  '0.04'],
    ['Pd(211)-B', 'CH2OH+H→CH3OH',    '0.64',                  '-0.30'],
    ['Pd(211)-B', 'COH→C+OH',         '1.14',                  '0.14'],
]

with open(f'{outdir}/reaction_barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: effective_barriers.csv ===
python3 <<'PYEOF'
import csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    ['surface',   'product',  'effective_barrier_eV'],
    ['Pd(211)',   'methanol', '2.97'],
    ['Pd(211)',   'methane',  '2.47'],
    ['Pd(211)-B', 'methanol', '1.98'],
    ['Pd(211)-B', 'methane',  '2.22'],
]

with open(f'{outdir}/effective_barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF
