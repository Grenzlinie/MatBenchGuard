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
model,adsorption_energy_eV
CN,-1.93
Nv-rich-CN,-3.66
EOF

# === solve block: step_02_bader_charges.json ===
python3 -c "
import json
data = {
    'CN': [-1.52, -1.5],
    'Nv-rich-CN': [-1.0, -0.99]
}
with open('$OUTDIR/step_02_bader_charges.json', 'w') as f:
    json.dump(data, f, indent=2)
"
