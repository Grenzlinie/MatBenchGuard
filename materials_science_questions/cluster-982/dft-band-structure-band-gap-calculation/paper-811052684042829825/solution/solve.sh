#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.txt ===
cat > "$OUTDIR/band_gaps.txt" <<'EOF'
PBE_bandgap_eV = 1.72
HSE06_bandgap_eV = 2.81
EOF

# === solve block: defect_formation_energies.csv ===
cat > /app/outputs/defect_formation_energies.csv <<'EOF'
defect_type,formation_energy_eV
V_Li-,0.77
V_S2_2+,2.35
p-,1.40
p+,0.77
EOF

# === solve block: diffusion_barriers.csv ===
cat > /app/outputs/diffusion_barriers.csv <<'EOF'
defect_type,orientation,barrier_eV
V_Li-,[001],0.148
V_Li-,[010],0.83
V_Li-,[100],0.95
V_S2_2+,[001],0.46
V_S2_2+,[010],1.20
V_S2_2+,[100],0.71
p-,[001],0.69
p-,[010],0.89
p-,[100],0.71
p+,[001],0.013
p+,[010],0.006
p+,[100],0.006
EOF

# === solve block: conductivity_summary.csv ===
cat > /app/outputs/conductivity_summary.csv <<'EOF'
charge_carrier,conductivity_S_cm,mobility_cm2_Vs,temperature_K
p+,1.5e-12,1.0e-01,300
V_Li-,1.5e-25,1.5e-16,300
EOF
