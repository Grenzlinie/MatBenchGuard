#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
cat > /app/outputs/energies.json <<'FFEOF'
{
  "halfML_2x1": -1000.0,
  "halfML_2x2": -1000.09,
  "fullML_2x1_aligned": -2000.0,
  "fullML_2x2_antiparallel": -2000.12,
  "halfML_energy_diff_per_1x1": -0.09,
  "fullML_energy_diff_per_2x2": -0.12
}
FFEOF

# === solve block: geometries.csv ===
cat > /app/outputs/geometries.csv <<'FFEOF'
structure,parameter,value,unit
halfML_2x1,C-C dimer length,1.62,Angstrom
halfML_2x1,C-C subsurface length (C_H-C),1.54,Angstrom
halfML_2x1,C-C subsurface length (C_OH-C),1.55,Angstrom
halfML_2x1,C-H bond length,1.09,Angstrom
halfML_2x1,C-O bond length,1.43,Angstrom
halfML_2x1,O-H bond length,0.99,Angstrom
halfML_2x1,H···OH hydrogen bond distance,1.64,Angstrom
halfML_2x1,H-O-C angle,107,degree
halfML_2x1,H-C_S-C_S angle,112,degree
halfML_2x1,O-C_S-C_S angle,113,degree
halfML_2x2,C-C dimer length (C_H-C_H),1.62,Angstrom
halfML_2x2,C-C dimer length (C_OH-C_OH),1.63,Angstrom
halfML_2x2,C-C subsurface length (C_H-C),1.54,Angstrom
halfML_2x2,C-C subsurface length (C_OH-C),1.55,Angstrom
halfML_2x2,C-H bond length,1.08,Angstrom
halfML_2x2,C-O bond length (top site),1.41,Angstrom
halfML_2x2,C-O bond length (bridge site),1.42,Angstrom
halfML_2x2,O-H bond length,1.00,Angstrom
halfML_2x2,H···OH hydrogen bond distance (bridge site),1.59,Angstrom
halfML_2x2,H···OH hydrogen bond distance (dimer site),1.74,Angstrom
halfML_2x2,H-O-C angle (bridge site OH),112,degree
halfML_2x2,H-O-C angle (dimer site OH),105,degree
halfML_2x2,H-C_S-C_S angle,113,degree
halfML_2x2,O-C_S-C_S angle (C_H),106,degree
halfML_2x2,O-C_S-C_S angle (C_OH),108,degree
fullML_2x1_aligned,C-C dimer length,1.64,Angstrom
fullML_2x1_aligned,C-C subsurface length,1.55,Angstrom
fullML_2x1_aligned,C-O bond length (top site),1.39,Angstrom
fullML_2x1_aligned,C-O bond length (bridge site),1.41,Angstrom
fullML_2x1_aligned,O-H bond length,1.00,Angstrom
fullML_2x1_aligned,H···OH hydrogen bond distance (bridge site),1.60,Angstrom
fullML_2x1_aligned,H···OH hydrogen bond distance (dimer site),1.74,Angstrom
fullML_2x1_aligned,H-O-C angle (bridge site OH),112,degree
fullML_2x1_aligned,H-O-C angle (dimer site OH),105,degree
fullML_2x1_aligned,O-C_S-C_S angle (bridge site),106,degree
fullML_2x1_aligned,O-C_S-C_S angle (dimer site),109,degree
fullML_2x2_antiparallel,C-C dimer length,1.63,Angstrom
fullML_2x2_antiparallel,C-C subsurface length (a),1.54,Angstrom
fullML_2x2_antiparallel,C-C subsurface length (b),1.57,Angstrom
fullML_2x2_antiparallel,C-O bond length (top site),1.39,Angstrom
fullML_2x2_antiparallel,C-O bond length (bridge site),1.41,Angstrom
fullML_2x2_antiparallel,O-H bond length (a),0.99,Angstrom
fullML_2x2_antiparallel,O-H bond length (b),0.98,Angstrom
fullML_2x2_antiparallel,H···OH hydrogen bond distance (bridge site),1.60,Angstrom
fullML_2x2_antiparallel,H···OH hydrogen bond distance (dimer site),1.79,Angstrom
fullML_2x2_antiparallel,H-O-C angle (bridge site OH),112,degree
fullML_2x2_antiparallel,H-O-C angle (dimer site OH),105,degree
fullML_2x2_antiparallel,O-C_S-C_S angle (bridge site),104,degree
fullML_2x2_antiparallel,O-C_S-C_S angle (dimer site),111,degree
FFEOF
