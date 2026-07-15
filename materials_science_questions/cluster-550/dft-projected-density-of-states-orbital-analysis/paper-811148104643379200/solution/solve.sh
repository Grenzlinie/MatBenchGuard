#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optical_properties.csv ===
cat > "/app/outputs/optical_properties.csv" <<'EOF'
material,polarization,optical_band_gap_eV,epsilon1_static,sigma_peak1_eV,sigma_peak1_s1,sigma_peak2_eV,sigma_peak2_s1
Nb3O7(OH),perpendicular,3.19,4.12,5.83,4.33e15,9.13,4.25e15
Nb3O7(OH),parallel,3.33,3.98,5.73,4.75e15,10.01,3.95e15
H-Nb2O5,perpendicular,3.40,4.30,5.83,4.44e15,8.96,4.08e15
H-Nb2O5,parallel,3.40,4.58,5.70,5.96e15,8.47,4.82e15
EOF

# === solve block: transport_properties.csv ===
cat > "/app/outputs/transport_properties.csv" <<'EOF'
material,sigma_ave_n_type,sigma_ave_p_type
Nb3O7(OH),1.26e20,0.57e20
H-Nb2O5,3.92e19,2.97e19
EOF
