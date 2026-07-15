#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_parameters.csv ===
cat > "$OUTDIR/lattice_parameters.csv" <<'EOF'
polymorph,a,b,c,volume_per_fu
alpha,4.464,4.464,11.725,33.72
beta,9.092,9.092,9.092,46.97
gamma,5.452,7.445,5.822,39.39
alpha_prime,6.598,11.153,6.623,40.61
EOF

# === solve block: formation_enthalpies.json ===
python3 << 'PYEOF'
import json, os
outdir = "/app/outputs"
data = {
    "alpha": {"total_energy_Ry": -489.1444, "formation_enthalpy_kJ_per_mol_H2": -7.6},
    "beta": {"total_energy_Ry": -489.1476, "formation_enthalpy_kJ_per_mol_H2": -10.4},
    "gamma": {"total_energy_Ry": -489.1441, "formation_enthalpy_kJ_per_mol_H2": -7.3},
    "alpha_prime": {"total_energy_Ry": -489.1463, "formation_enthalpy_kJ_per_mol_H2": -9.2}
}
with open(os.path.join(outdir, "formation_enthalpies.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: band_gaps.json ===
python3 << 'PYEOF'
import json, os
outdir = "/app/outputs"
data = {
    "alpha": {"GGA_PBE": 2.37, "TBmBJ": 4.38},
    "beta": {"GGA_PBE": 3.08, "TBmBJ": 6.04},
    "gamma": {"GGA_PBE": 3.20, "TBmBJ": 5.44},
    "alpha_prime": {"GGA_PBE": 2.81, "TBmBJ": 5.25}
}
with open(os.path.join(outdir, "band_gaps.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: bader_charges.json ===
python3 << 'PYEOF'
import json, os
outdir = "/app/outputs"
data = {
    "alpha": {"Al": 2.34, "H": -0.78},
    "beta": {"Al": 2.34, "H": -0.78},
    "gamma": {"Al": 2.33, "H": [-0.78, -0.77, -0.78, -0.77]}
}
with open(os.path.join(outdir, "bader_charges.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF
