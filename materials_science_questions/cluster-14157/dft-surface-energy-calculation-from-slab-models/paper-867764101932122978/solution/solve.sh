#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# This script generates the expected output files with the correct reference values
# from the paper. It is used by the verifier to obtain gold-standard scores.
# The agent must implement the DFT workflow; this file is hidden from the agent
# and is only used for grading.

# slab_energies.csv
cat > "$OUTDIR/slab_energies.csv" << EOF
surface,slab_total_energy,E_VBM
(001),-1000.0,-2.6358
(100),-1000.0,-1.8181
EOF

# mu_O2.txt
echo "-10.4857" > "$OUTDIR/mu_O2.txt"

# formation_energies.csv
cat > "$OUTDIR/formation_energies.csv" << 'EOF'
surface,site,charge,geometry_type,E_form,magnetic_moment_ground_state,is_LEMS
(001),site1,0,Si-Si dimer,5.1378,0.0,False
(001),site1,1,Si-Si dimer,5.3593,1.0,True
(001),site1,2,Si-Si dimer,5.9628,1.0,True
(001),site2,0,Si-Si dimer,5.2306,0.0,False
(001),site2,1,Si-Si dimer,5.3537,1.0,True
(001),site2,2,Si-Si dimer,5.9717,1.0,True
(001),subsurface,0,Si-Si dimer,5.5779,0.0,False
(001),subsurface,1,Si-Si dimer,5.5137,1.0,True
(001),subsurface,2,Si-Si dimer,2.7874,0.0,False
(100),bridge,0,puckered configuration,5.2099,0.0,False
(100),bridge,1,puckered configuration,3.6295,1.0,True
(100),bridge,2,puckered configuration,3.6239,1.0,True
(100),metastable ring,0,puckered configuration,5.3224,0.0,False
(100),metastable ring,1,puckered configuration,3.1666,1.0,True
(100),metastable ring,2,puckered configuration,1.2963,0.0,False
(100),ring 2III-O,0,2III-O,3.4193,0.0,False
(100),ring 2III-O,1,2III-O,0.6417,1.0,True
(100),ring 2III-O,2,2III-O,-1.1842,0.0,False
EOF

echo "[+] reference outputs generated."