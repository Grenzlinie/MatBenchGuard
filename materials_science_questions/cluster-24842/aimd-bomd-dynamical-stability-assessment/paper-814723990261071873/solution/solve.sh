#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_results.csv ===
cat > /app/outputs/simulation_results.csv <<'FFEOF'
System,Temperature_K,L_ave_A,L_max_A,CED_kJ_cm3,vdW_kJ_cm3,Electrostatic_kJ_cm3,E_bind_kJ_mol,E_modulus_GPa,bulk_modulus_K_GPa,shear_modulus_G_GPa,K_G_ratio
epsilon-CL-20,245,1.396,1.574,,,,,13.4,10.7,5.2,2.1
epsilon-CL-20,295,1.397,1.594,,,,,12.4,10.0,4.8,2.1
epsilon-CL-20,345,1.398,1.618,,,,,11.8,9.4,4.6,2.1
epsilon-CL-20,395,1.399,1.622,,,,,11.0,8.7,4.3,2.0
epsilon-CL-20,445,1.399,1.652,,,,,9.7,7.8,3.8,2.1
composite,245,1.395,1.562,0.74,0.33,0.41,3198.8,5.6,6.1,2.1,2.9
composite,295,1.396,1.591,0.71,0.32,0.40,3115.2,4.3,4.8,1.6,3.0
composite,345,1.396,1.611,0.69,0.31,0.38,2994.9,3.6,4.6,1.5,3.0
composite,395,1.397,1.621,0.68,0.31,0.37,2970.1,3.1,4.2,1.1,3.7
composite,445,1.398,1.644,0.65,0.30,0.35,2860.6,2.6,3.6,0.9,3.9
cocrystal,245,1.392,1.547,0.84,0.38,0.46,5506.0,9.0,8.6,3.4,2.5
cocrystal,295,1.393,1.572,0.81,0.37,0.45,5373.3,8.6,8.3,3.3,2.5
cocrystal,345,1.394,1.603,0.79,0.36,0.43,5328.7,8.0,7.7,3.0,2.5
cocrystal,395,1.395,1.608,0.77,0.35,0.42,5161.4,7.4,7.1,2.8,2.6
cocrystal,445,1.396,1.640,0.74,0.34,0.40,4993.3,6.3,5.8,2.4,2.4
beta-HMX,245,,,,,,,11.1,8.1,4.4,1.9
beta-HMX,295,,,,,,,10.2,7.4,4.0,1.8
beta-HMX,345,,,,,,,9.6,6.7,3.8,1.8
beta-HMX,395,,,,,,,8.7,5.9,3.5,1.7
beta-HMX,445,,,,,,,8.0,5.3,3.2,1.6
FFEOF
