#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.csv ===
cat > /app/outputs/band_gaps.csv <<'EOF'
gap_type,energy_eV
indirect_no_scissor,1.87
direct_no_scissor,2.24
indirect_with_scissor,3.2
direct_with_scissor,3.57
EOF

# === solve block: epsilon2_peaks.csv ===
cat > /app/outputs/epsilon2_peaks.csv <<'EOF'
peak_label,energy_eV
A,5.68
B,6.42
C,8.74
D,9.64
E,10.98
F,12.48
G,15.68
H,21.78
I,24.80
EOF

# === solve block: optical_constants.json ===
cat > /app/outputs/optical_constants.json <<'EOF'
{
  "epsilon1_at_0": 5.35,
  "plasma_peak_energy_eV": 28
}
EOF
