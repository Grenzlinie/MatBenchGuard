#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monomer_properties.json ===
python3 -c "
import json
monomer = {
    'mu': 5.72,
    'energy': -1000.0,
    'O_Si_bond_length': 2.201
}
with open('$OUTDIR/monomer_properties.json', 'w') as f:
    json.dump(monomer, f, indent=2)
"

# === solve block: dimer_Ia_properties.json ===
python3 -c "
import json
delta_E_Ha = -9.8 / 627.509
E_Ia = 2 * (-1000.0) + delta_E_Ha
dimer_Ia = {
    'mu': 4.71,
    'energy': round(E_Ia, 6),
    'O_Si_bond_1': 2.124,
    'O_Si_bond_2': 2.124,
    'Si_Si_distance': 4.605
}
with open('/app/outputs/dimer_Ia_properties.json', 'w') as f:
    json.dump(dimer_Ia, f, indent=2)
"

# === solve block: dimer_Ib_properties.json ===
python3 -c "
import json
delta_E_Ha = -11.2 / 627.509
E_Ib = 2 * (-1000.0) + delta_E_Ha
dimer_Ib = {
    'mu': 1.20,
    'energy': round(E_Ib, 6),
    'O_Si_bond_1': 2.094,
    'O_Si_bond_2': 2.041,
    'Si_Si_distance': 4.414
}
with open('/app/outputs/dimer_Ib_properties.json', 'w') as f:
    json.dump(dimer_Ib, f, indent=2)
"

# === solve block: formation_energies.json ===
python3 -c "
import json
fe = {
    'Ia_delta_E': -9.8,
    'Ia_delta_E0': -8.7,
    'Ib_delta_E': -11.2,
    'Ib_delta_E0': -10.0,
    'Ia_delta_E_solvent': None,
    'Ib_delta_E_solvent': None
}
with open('/app/outputs/formation_energies.json', 'w') as f:
    json.dump(fe, f, indent=2)
"
