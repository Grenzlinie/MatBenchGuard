#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'EOF'
defect,condition,substrate,formation_energy_eV
Sevac,W-rich,isolated,2.31
Sevac,W-rich,supported,2.20
Sevac,Se-rich,isolated,2.92
Sevac,Se-rich,supported,2.82
Wvac,W-rich,isolated,5.01
Wvac,W-rich,supported,5.09
Wvac,Se-rich,isolated,3.78
Wvac,Se-rich,supported,3.87
Sew,W-rich,isolated,5.34
Sew,W-rich,supported,5.51
Sew,Se-rich,isolated,3.49
Sew,Se-rich,supported,3.66
2Sevac,W-rich,isolated,3.86
2Sevac,W-rich,supported,3.78
2Sevac,Se-rich,isolated,5.09
2Sevac,Se-rich,supported,5.01
EOF

# === solve block: gap_state_passivation.csv ===
cat > "/app/outputs/gap_state_passivation.csv" <<'FFEOF'
system,has_gap_states
pristine,false
Sevac,true
Sevac+O,false
FFEOF
