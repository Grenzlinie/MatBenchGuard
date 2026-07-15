#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: formation_energies.csv ===
cat > $OUTDIR/formation_energies.csv << 'FFEOF'
element,defect_type,formation_energy_eV
W,111,10.16
W,110,10.59
W,bridge,10.17
Ti,sub,-0.81
Ti,bridge,8.73
Ti,111,8.83
Ti,110,8.99
V,sub,-0.60
V,bridge,7.77
V,111,8.00
V,110,8.10
Zr,sub,0.07
Zr,bridge,11.21
Zr,111,11.21
Zr,110,11.74
Nb,sub,-0.32
Nb,bridge,10.19
Nb,111,10.22
Nb,110,10.74
Hf,sub,-0.20
Hf,bridge,10.14
Hf,111,9.99
Hf,110,11.53
Ta,sub,-0.47
Ta,bridge,10.33
Ta,111,10.34
Ta,110,11.01
Re,sub,0.17
Re,bridge,9.49
Re,111,9.53
Re,110,9.55
FFEOF

# === solve block: binding_energies.csv ===
python3 -c "
import csv
fe = {
    'W': {'111': 10.16, '110': 10.59, 'bridge': 10.17},
    'Ti': {'sub': -0.81, 'bridge': 8.73, '111': 8.83, '110': 8.99},
    'V': {'sub': -0.60, 'bridge': 7.77, '111': 8.00, '110': 8.10},
    'Zr': {'sub': 0.07, 'bridge': 11.21, '111': 11.21, '110': 11.74},
    'Nb': {'sub': -0.32, 'bridge': 10.19, '111': 10.22, '110': 10.74},
    'Hf': {'sub': -0.20, 'bridge': 10.14, '111': 9.99, '110': 11.53},
    'Ta': {'sub': -0.47, 'bridge': 10.33, '111': 10.34, '110': 11.01},
    'Re': {'sub': 0.17, 'bridge': 9.49, '111': 9.53, '110': 9.55}
}
W_111 = fe['W']['111']
with open('$OUTDIR/binding_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['element', 'binding_energy_eV'])
    for el in ['Ti', 'V', 'Zr', 'Nb', 'Hf', 'Ta', 'Re']:
        d = fe[el]
        e_sub = d['sub']
        mixed = min(d['bridge'], d['111'], d['110'])
        binding = mixed - W_111 - e_sub
        writer.writerow([el, round(binding, 2)])
"
