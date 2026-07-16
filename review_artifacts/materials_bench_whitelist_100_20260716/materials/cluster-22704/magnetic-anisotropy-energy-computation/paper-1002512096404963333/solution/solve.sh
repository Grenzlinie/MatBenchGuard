#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_ground_states.csv ===
cat > "$OUTDIR/magnetic_ground_states.csv" <<'EOF'
compound,stacking,ground_state,M_I_moment,M_II_moment,N_moment
Sc2NF2,ABC,NM,0.0,0.0,0.0
Sc2NF2,ABA,FM,0.44,0.44,0.05
Sc2NO2,ABC,NM,0.0,0.0,0.03
Sc2NO2,ABA,FM,0.0,0.0,0.56
Ti2NF2,ABC,AFM2,1.3,1.0,0.02
Ti2NF2,ABA,FM,0.40,0.40,0.04
V2NF2,ABC,AFM2,2.4,2.0,0.01
V2NF2,ABA,AFM2,1.78,1.78,0.07
V2NO2,ABC,AFM1,1.75,1.11,0.00
V2NO2,ABA,AFM2,0.50,0.50,0.03
Cr2NF2,ABC,AFM3,3.65,3.11,0.0
Cr2NF2,ABA,AFM1,3.70,3.10,0.07
Cr2NO2,ABC,FM,2.87,2.87,0.23
Cr2NO2,ABA,FM,2.91,2.91,0.45
Mn2NF2,ABC,AFM3,4.5,4.5,0.05
Mn2NF2,ABA,FM,4.50,4.50,0.37
EOF

# === solve block: electronic_ground_states.csv ===
cat > "$OUTDIR/electronic_ground_states.csv" <<'EOF'
compound,stacking,electronic_state
Sc2NF2,ABC,metal
Sc2NF2,ABA,spin-gapless_semiconductor
Sc2NO2,ABC,metal
Sc2NO2,ABA,half-metal
Ti2NF2,ABC,semiconductor
Ti2NF2,ABA,half-metal
V2NF2,ABC,semiconductor
V2NF2,ABA,metal
V2NO2,ABC,semiconductor
V2NO2,ABA,metal
Cr2NF2,ABC,semiconductor
Cr2NF2,ABA,semiconductor
Cr2NO2,ABC,half-metal
Cr2NO2,ABA,half-metal
Mn2NF2,ABC,metal
Mn2NF2,ABA,half-metal
EOF

# === solve block: magnetic_anisotropy_energies.csv ===
cat > "$OUTDIR/magnetic_anisotropy_energies.csv" <<'EOF'
compound,stacking,MAE_microeV
Sc2NF2,ABA,-2.28
Sc2NO2,ABA,23.80
Ti2NF2,ABA,19.38
Ti2NF2,ABC,-4.76
V2NF2,ABA,-148.40
V2NF2,ABC,1.5
V2NO2,ABA,6.4
V2NO2,ABC,-55.5
Cr2NF2,ABA,148.50
Cr2NF2,ABC,-48.51
Cr2NO2,ABA,-166.40
Cr2NO2,ABC,36.95
Mn2NF2,ABA,-13.50
Mn2NF2,ABC,19.87
EOF
