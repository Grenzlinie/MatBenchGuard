#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_adsorption_energies.csv ===
cat > "$OUTDIR/step_01_adsorption_energies.csv" <<'EOF'
species,Eads_ev
O2,-2.48
OOH,-3.04
O,-5.88
OH,-4.05
H2O,-0.90
EOF

# === solve block: step_02_activation_barriers.csv ===
cat > "$OUTDIR/step_02_activation_barriers.csv" <<'EOF'
reaction,Ea_ev
O2_dissoc,1.46
O2_to_OOH,0.96
OOH_to_O_H2O,0.16
OOH_to_2OH,0.07
OOH_to_O_OH,0.03
O_to_OH,0.26
OH_to_H2O,0.64
EOF

# === solve block: step_03_free_energy_diagram.csv ===
cat > "$OUTDIR/step_03_free_energy_diagram.csv" <<'EOF'
step,dG_ev
O2->OOH,-0.55
OOH->O+H2O,-3.05
O->OH,-1.45
OH->H2O,0.78
EOF

# === solve finalize ===
# Check that all outputs exist
for f in step_01_adsorption_energies.csv step_02_activation_barriers.csv step_03_free_energy_diagram.csv; do
  if [ ! -f "$OUTDIR/$f" ]; then
    echo "ERROR: missing output $f" >&2
    exit 1
  fi
done
echo "Oracle outputs written successfully."
