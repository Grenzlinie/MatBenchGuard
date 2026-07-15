#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: free_energies.csv ===
# Write the scored free_energies.csv using only shell heredoc.
cat > "$OUTDIR/free_energies.csv" <<'FFEOF'
comment,free_energy_eV,intermediate,pH,surface
,0.0,*NO3,1,TiO2
,-0.5,*NO2,1,TiO2
,-1.0,*NO,1,TiO2
,-0.8,*NOH,1,TiO2
,-1.3,*NH2OH,1,TiO2
,-1.79,*NH3,1,TiO2
NH3 desorption barrier,1.29,RDS,1,TiO2
,0.0,*NO3,1,FePc/TiO2
,-0.7,*NO2,1,FePc/TiO2
,-1.2,*NO,1,FePc/TiO2
,-0.46,*NOH,1,FePc/TiO2
,-1.5,*NH2OH,1,FePc/TiO2
,-2.0,*NH3,1,FePc/TiO2
*NO to *NOH barrier,0.74,RDS,1,FePc/TiO2
FFEOF
