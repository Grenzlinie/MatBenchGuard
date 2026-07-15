#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: interfacial_energies.csv ===
cat > "$OUTDIR/interfacial_energies.csv" <<'FFEOF'
surface,monolayer_density_fraction,ca_density_fraction,b_param_Angstrom,interfacial_energy_mJm2
(01.2),1.0,1.0,6.45,15.2
(01.2),0.8,0.9,8.06,19.8
(01.2),0.666667,0.833333,9.69,24.5
(00.1),1.0,1.0,8.31,10.5
(00.1),0.8,0.9,10.39,14.2
(00.1),0.666667,0.833333,12.46,18.0
FFEOF
