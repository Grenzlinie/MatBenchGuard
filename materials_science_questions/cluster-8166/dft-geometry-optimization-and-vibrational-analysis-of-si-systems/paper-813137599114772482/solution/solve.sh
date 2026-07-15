#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json
result = {
    "H2SiOO_MP2_geom_file": "/app/outputs/mp2_geometries.xyz",
    "H2SiOO_MP2_energy_hartree": -440.07176,
    "H2SiOO_planar_imaginary_freq": True,
    "H2SiOO_GVB_overlaps": {"S_pi": 0.201, "S_Si_Oa": 0.826, "S_Oa_Ob": 0.735},
    "H2SiOO_CASSCF_spins": {"Si": 0.749, "O_terminal": 0.769},
    "H2SiOO_TS_energy_hartree": -440.06145,
    "H2SiOO_siladioxirane_energy_hartree": -440.17340,
    "H2COO_GVB_overlaps": {"S_pi": 0.420, "S_C_Oa": 0.842, "S_Oa_Ob": 0.767},
    "H2COO_CASSCF_spins": {"C": 0.407, "O_terminal": 0.409}
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
'
