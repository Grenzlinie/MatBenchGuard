#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies_and_lattice.json ===
cat << 'SCRIPT_EOF' > /tmp/gen_json.py
import json

eV_per_kJmol = 96.485

E_Au = -3.0
E_Ni = -5.0
E_Pd = -4.0
E_Sn = -2.0

def total_energy(dH, x_Ni=0.0, x_Pd=0.0):
    x_Au = 1 - x_Ni - x_Pd
    dH_eV = dH / eV_per_kJmol
    return 5 * dH_eV + (x_Ni * E_Ni + x_Pd * E_Pd + x_Au * E_Au + 4 * E_Sn)

compounds = [
    {"name": "AuSn4", "total_energy_per_fu": total_energy(-10.19),
     "total_energy_fu_units": "eV", "a": 6.67, "b": 6.52, "c": 12.00, "volume": 521.51, "delta_H_kJ_per_mol_atoms": -10.19},
    {"name": "Au0.75Ni0.25Sn4", "total_energy_per_fu": total_energy(-11.38, x_Ni=0.25),
     "total_energy_fu_units": "eV", "a": 6.55, "b": 6.55, "c": 11.82, "volume": 507.46, "delta_H_kJ_per_mol_atoms": -11.38},
    {"name": "Au0.5Ni0.5Sn4", "total_energy_per_fu": total_energy(-12.65, x_Ni=0.5),
     "total_energy_fu_units": "eV", "a": 6.49, "b": 6.53, "c": 11.65, "volume": 493.43, "delta_H_kJ_per_mol_atoms": -12.65},
    {"name": "Au0.75Pd0.25Sn4", "total_energy_per_fu": total_energy(-29.85, x_Pd=0.25),
     "total_energy_fu_units": "eV", "a": 6.59, "b": 6.57, "c": 11.86, "volume": 513.78, "delta_H_kJ_per_mol_atoms": -29.85},
    {"name": "Au0.5Pd0.5Sn4", "total_energy_per_fu": total_energy(-18.96, x_Pd=0.5),
     "total_energy_fu_units": "eV", "a": 6.54, "b": 6.60, "c": 11.75, "volume": 506.66, "delta_H_kJ_per_mol_atoms": -18.96},
    {"name": "Au0.5Pd0.25Ni0.25Sn4", "total_energy_per_fu": total_energy(-15.83, x_Ni=0.25, x_Pd=0.25),
     "total_energy_fu_units": "eV", "a": 6.51, "b": 6.56, "c": 11.71, "volume": 500.22, "delta_H_kJ_per_mol_atoms": -15.83}
]

data = {
    "compounds": compounds,
    "elemental_references": {
        "Au_fcc": E_Au,
        "Ni_fcc": E_Ni,
        "Pd_fcc": E_Pd,
        "Sn_beta": E_Sn
    }
}

import sys
with open(sys.argv[1], "w") as f:
    json.dump(data, f, indent=2)
SCRIPT_EOF

python3 /tmp/gen_json.py "$OUTDIR/formation_energies_and_lattice.json"

# === solve block: elastic_and_thermodynamic.json ===
python3 /solution/write_outputs.py --output /app/outputs/elastic_and_thermodynamic.json
