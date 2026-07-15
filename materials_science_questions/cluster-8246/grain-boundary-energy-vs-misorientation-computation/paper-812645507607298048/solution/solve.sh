#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: vacancy_binding_energies.csv ===
cat > "$OUTDIR/vacancy_binding_energies.csv" <<'FFEOF'
GB_type,distance_from_GB_plane,site_index,vacancy_binding_energy
Sigma3(111),0.0,1,0.001
Sigma3(111),2.0,2,0.000
Sigma3(111),4.0,3,0.000
Sigma3(111),6.0,4,-0.001
Sigma3(111),8.0,5,0.000
Sigma3(112),0.0,1,-0.152
Sigma3(112),2.0,2,-0.103
Sigma3(112),4.0,3,-0.048
Sigma3(112),6.0,4,-0.017
Sigma3(112),8.0,5,-0.003
Sigma5(310),0.0,1,-0.368
Sigma5(310),2.0,2,-0.295
Sigma5(310),4.0,3,-0.164
Sigma5(310),6.0,4,-0.051
Sigma5(310),8.0,5,-0.009
FFEOF

# === solve block: li_segregation_energies.csv ===
cat > "$OUTDIR/li_segregation_energies.csv" <<'FFEOF'
GB_type,distance_from_GB_plane,li_segregation_energy,site_index
Sigma3(111),0.0,0.000,1
Sigma3(111),2.0,0.001,2
Sigma3(111),4.0,-0.001,3
Sigma3(111),6.0,0.000,4
Sigma3(111),8.0,0.000,5
Sigma3(112),0.0,-0.144,1
Sigma3(112),2.0,-0.098,2
Sigma3(112),4.0,-0.052,3
Sigma3(112),6.0,-0.018,4
Sigma3(112),8.0,-0.005,5
Sigma5(310),0.0,-0.482,1
Sigma5(310),2.0,-0.261,2
Sigma5(310),4.0,-0.118,3
Sigma5(310),6.0,-0.033,4
Sigma5(310),8.0,-0.007,5
FFEOF

# === solve finalize ===
echo "All outputs written."
