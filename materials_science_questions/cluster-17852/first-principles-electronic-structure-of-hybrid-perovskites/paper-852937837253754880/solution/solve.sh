#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'EOF'
interface,termination,composition,E_LHP_Spiro,E_LHP,E_Spiro,E_LHP_star,E_Spiro_star,Eb,Ea,Ed_spiro,Ed_lhp
MAPI_MAI,AX,MAPI,-2.5,0,0,0.03,0.12,-2.5,-2.65,0.12,0.03
MAPI_PbI2,PbX2,MAPI,-1.5,0,0,0.03,0.12,-1.5,-1.65,0.12,0.03
triLHP_FAMAX,AX,triLHP,-2.3,0,0,0.03,0.12,-2.3,-2.45,0.12,0.03
triLHP_CsFAMAX,AX,triLHP,-1.7,0,0,0.03,0.12,-1.7,-1.85,0.12,0.03
triLHP_CsFAMAX_OCs,AX,triLHP,-2.3,0,0,0.03,0.12,-2.3,-2.45,0.12,0.03
triLHP_PbX2,PbX2,triLHP,-3.5,0,0,0.03,0.12,-3.5,-3.65,0.12,0.03
triLHP_PbX2_Cs,PbX2,triLHP,-4.5,0,0,0.03,0.12,-4.5,-4.65,0.12,0.03
EOF

# === solve block: hole_injection_times.csv ===
cat > "$OUTDIR/hole_injection_times.csv" <<'EOF'
interface,donor_state,tau_ps
MAPI_MAI,HOMO,11.7
MAPI_MAI,HOMO-1,1.80
MAPI_PbI2,HOMO,31.6
MAPI_PbI2,HOMO-1,4.93
triLHP_FAMAX,HOMO,38.7
triLHP_FAMAX,HOMO-1,1.65
triLHP_CsFAMAX,HOMO,5.70
triLHP_CsFAMAX,HOMO-1,12.9
triLHP_CsFAMAX_OCs,HOMO,16.7
triLHP_CsFAMAX_OCs,HOMO-1,2.50
triLHP_PbX2,HOMO,5.24
triLHP_PbX2,HOMO-1,13.1
triLHP_PbX2_Cs,HOMO,14.3
triLHP_PbX2_Cs,HOMO-1,2.68
EOF

# === solve finalize ===
echo "Reference artifacts written successfully."
