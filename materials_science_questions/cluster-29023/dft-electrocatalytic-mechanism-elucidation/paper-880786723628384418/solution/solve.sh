#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_dissociation_energy.csv ===
cat > "$OUTDIR/step_01_dissociation_energy.csv" <<'EOF'
dissociation_energy_eV,system
-1.44,Fe1-NC
-1.98,Fe1Co1-NC
EOF

# === solve block: step_02_bader_charge.csv ===
cat > "$OUTDIR/step_02_bader_charge.csv" <<'EOF'
charge_e,system
-0.90,Fe1-NC
-0.83,Fe1Co1-NC
EOF

# === solve block: step_03_d_band_center.csv ===
cat > "$OUTDIR/step_03_d_band_center.csv" <<'EOF'
d_band_center_eV,system
-2.0,Fe1-NC
-1.5,Fe1Co1-NC
EOF
