#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: intrinsic_defect_energies.csv ===
cat > "$OUTDIR/intrinsic_defect_energies.csv" <<'FFEOF'
polymorph,defect_type,energy_eV
monoclinic,Li_Frenkel,2.55
monoclinic,Mn_Frenkel,6.41
monoclinic,O_Frenkel,8.11
monoclinic,Schottky,34.84
monoclinic,Li_Mn_antisite,1.38
monoclinic,Li_deficiency_oxidation,14.36
monoclinic,O_excess_oxidation,12.43
orthorhombic,Li_Frenkel,3.90
orthorhombic,Mn_Frenkel,7.79
orthorhombic,O_Frenkel,11.78
orthorhombic,Schottky,43.73
orthorhombic,Li_Mn_antisite,1.65
orthorhombic,Li_deficiency_oxidation,16.12
orthorhombic,O_excess_oxidation,14.75
FFEOF

# === solve block: li_migration_energies.csv ===
cat > "$OUTDIR/li_migration_energies.csv" <<'FFEOF'
polymorph,path_label,jump_distance_A,energy_eV
monoclinic,A,2.69,0.60
monoclinic,B,2.90,0.54
monoclinic,C,3.50,1.58
monoclinic,D,3.53,0.94
orthorhombic,X,3.10,0.95
orthorhombic,Y,3.22,1.29
FFEOF

# === solve block: dopant_incorporation_energies.csv ===
cat > "$OUTDIR/dopant_incorporation_energies.csv" <<'FFEOF'
polymorph,dopant,site,energy_eV
monoclinic,Al,Li,9.60
monoclinic,Al,Mn,4.95
monoclinic,Al,Si,2.70
monoclinic,Ga,Li,11.79
monoclinic,Ga,Mn,5.09
monoclinic,Ga,Si,3.90
orthorhombic,Al,Li,9.13
orthorhombic,Al,Mn,5.15
orthorhombic,Al,Si,3.51
orthorhombic,Ga,Li,9.16
orthorhombic,Ga,Mn,5.10
orthorhombic,Ga,Si,4.74
FFEOF
