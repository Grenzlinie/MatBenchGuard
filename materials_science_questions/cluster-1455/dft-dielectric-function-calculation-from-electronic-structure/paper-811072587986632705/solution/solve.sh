#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: uvvis_peaks.csv ===
OUTDIR=/app/outputs
cat > "$OUTDIR/uvvis_peaks.csv" << 'EOF'
wavelength_nm,oscillator_strength,transition_label
194.5,0.574,"39(HOMO-4) → 44(LUMO), 40(HOMO-3) → 45(LUMO+1), 42(HOMO-1) → 55(LUMO+11), 43(HOMO) → 54(LUMO+10)"
224.7,0.047,"43(HOMO) → 60(LUMO+16), 42(HOMO-1) → 61(LUMO+17)"
EOF

# === solve block: nbo_e2.csv ===
cat > /app/outputs/nbo_e2.csv << 'EOF'
donor,acceptor,E2_kcal_mol
Fe(d),LP*(C6)/LP*(C4),190.97
Fe(d),LP*(C13)/LP*(C15),133.84
C4-C5/C2-C3,Fe(s)/Fe(d),57.95
C14-C15/C13-C14,Fe(s)/Fe(d),57.95
EOF

# === solve block: nbo_charges.csv ===
cat > /app/outputs/nbo_charges.csv << 'EOF'
atom_or_moiety,natural_charge
Fe,0.212
C,-0.247
H,0.226
Cp_ring_1,-0.100
Cp_ring_2,-0.100
EOF
