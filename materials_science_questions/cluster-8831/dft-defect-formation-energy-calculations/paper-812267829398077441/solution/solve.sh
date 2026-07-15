#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cohesive_energies.csv ===
cat > "$OUTDIR/cohesive_energies.csv" << 'FFEOF'
cohesive_energy_eV,system
-10.0,bulk_GaN
-5.0,bulk_Ga
-5.0,N2
-5.0,Mg3N2
-368.49,type_I_NI_+3
-368.63,type_II_NI_+3
-368.89,type_I_NI_+2
-369.19,type_II_NI_+2
-369.63,type_I_NI_+1
-369.99,type_II_NI_+1
-370.73,type_I_NI_0
-371.20,type_II_NI_0
-372.24,type_I_NI_-1
-372.49,type_II_NI_-1
-377.91,channel_NI_-3
-362.7833333333333,MgGaN_I_a_+2
-362.6233333333333,MgGaN_I_b_+2
-362.5433333333333,MgGaN_I_c_+2
-362.7233333333333,MgGaN_I_d_+2
-362.7033333333333,MgGaN_I_e_+2
-362.4333333333333,MgGaN_I_f_+2
-363.2533333333333,MgGaN_I_a_+1
-363.1233333333333,MgGaN_I_b_+1
-363.1333333333333,MgGaN_I_c_+1
-363.4733333333333,MgGaN_I_d_+1
-363.6433333333333,MgGaN_I_e_+1
-363.0533333333333,MgGaN_I_f_+1
-364.2033333333333,MgGaN_I_a_0
-364.0833333333333,MgGaN_I_b_0
-364.1133333333333,MgGaN_I_c_0
-364.6733333333333,MgGaN_I_d_0
-364.7333333333333,MgGaN_I_e_0
-363.9733333333333,MgGaN_I_f_0
FFEOF
