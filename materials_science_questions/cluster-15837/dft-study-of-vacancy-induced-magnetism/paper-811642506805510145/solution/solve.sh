#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mhdnnp_vs_acsf_errors.csv ===
cat > "$OUTDIR/mhdnnp_vs_acsf_errors.csv" << 'EOF'
potential,split,metric,value
ACSF-only,train,E_RMSE_meV_per_atom,11.0
ACSF-only,test,E_RMSE_meV_per_atom,11.5
ACSF-only,train,F_RMSE_eV_per_angstrom,0.50
ACSF-only,test,F_RMSE_eV_per_angstrom,0.55
mHDNNP,train,E_RMSE_meV_per_atom,0.86
mHDNNP,test,E_RMSE_meV_per_atom,1.11
mHDNNP,train,F_RMSE_eV_per_angstrom,0.067
mHDNNP,test,F_RMSE_eV_per_angstrom,0.066
EOF

# === solve block: optimized_lattice_params.json ===
python3 << 'EOF'
import json
data = {
    "AFM-II": {"a": 4.433, "alpha": 90.77},
    "FM": {"a": 4.461}
}
with open("/app/outputs/optimized_lattice_params.json", "w") as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: exchange_neel.json ===
python3 << 'EOF'
import json
data = {
    "J1": -14.0,
    "J2": -14.6,
    "T_N": 256.0,
    "T_N_MC": 300.0
}
with open("/app/outputs/exchange_neel.json", "w") as f:
    json.dump(data, f, indent=2)
EOF
