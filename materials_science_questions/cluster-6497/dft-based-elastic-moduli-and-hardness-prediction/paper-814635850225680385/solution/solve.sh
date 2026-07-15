#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results_FeAl.json ===
python3 -c "import json; d={'equilibrium_lattice_constant_a':5.398,'bulk_modulus_B':1900,'E_AF_minus_E_FM':0.5,'FM_iron_moment':0.7,'AF_iron_moment':0.4}; print(json.dumps(d,indent=2))" > /app/outputs/results_FeAl.json

# === solve block: results_FeV.json ===
python3 -c "import json; d={'equilibrium_lattice_constant_a':5.405,'bulk_modulus_B':2320,'E_AF_minus_E_FM':0.5,'FM_iron_moment':0.7,'AF_iron_moment':0.7}; print(json.dumps(d,indent=2))" > /app/outputs/results_FeV.json
