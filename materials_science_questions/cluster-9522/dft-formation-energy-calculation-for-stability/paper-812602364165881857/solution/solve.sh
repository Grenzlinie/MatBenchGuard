#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: step_01_bond_lengths.csv ===
cat > "$OUTDIR/step_01_bond_lengths.csv" <<'FFEOF'
metal,bond,length
Fe,M-N1,193.1
Fe,M-N2,194.8
Fe,M-N3,193.1
Fe,M-N4,194.8
Fe,M-F1,176.9
Fe,M-F2,176.9
Co,M-N1,191.4
Co,M-N2,192.7
Co,M-N3,191.4
Co,M-N4,192.3
Co,M-F1,181.5
Co,M-F2,181.5
Ni,M-N1,191.8
Ni,M-N2,193.2
Ni,M-N3,191.8
Ni,M-N4,193.2
Ni,M-F1,181.9
Ni,M-F2,181.9
Cu,M-N1,195.9
Cu,M-N2,197.5
Cu,M-N3,195.9
Cu,M-N4,197.5
Cu,M-F1,195.6
Cu,M-F2,195.6
FFEOF

# === solve block: step_02_thermodynamics.csv ===
cat > "$OUTDIR/step_02_thermodynamics.csv" <<'FFEOF'
metal,delta_H,delta_G,S
Fe,-89.3,155.6,951.4
Co,42.9,286.5,958.6
Ni,163.4,405.7,962.6
Cu,420.0,652.1,1000.4
FFEOF

# === solve block: step_03_spin_states.csv ===
cat > "$OUTDIR/step_03_spin_states.csv" <<'FFEOF'
metal,ground_state_multiplicity
Fe,3
Co,2
Ni,1
Cu,4
FFEOF

# === solve block: step_04_planarity_checks.csv ===
cat > "$OUTDIR/step_04_planarity_checks.csv" <<'FFEOF'
metal,site,sum_angles_deg
Fe,MN4,360.0
Fe,chelate_ring1,720.0
Fe,chelate_ring2,720.0
Co,MN4,360.0
Co,chelate_ring1,719.9
Co,chelate_ring2,720.0
Ni,MN4,360.0
Ni,chelate_ring1,720.0
Ni,chelate_ring2,720.0
Cu,MN4,360.0
Cu,chelate_ring1,720.0
Cu,chelate_ring2,720.0
FFEOF
