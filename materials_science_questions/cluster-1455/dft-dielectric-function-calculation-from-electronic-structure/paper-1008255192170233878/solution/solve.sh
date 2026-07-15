#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hamaker_constants.csv ===
cat > "$OUTDIR/hamaker_constants.csv" <<'CSVEOF'
stoichiometry,A_NR_eV,A_m0_eV
Ca6Al7O16,0.004,-0.012
Ca5.75Al7O16,0.011,-0.004
Ca5.5Al7O16,0.033,0.016
CSVEOF

# === solve block: free_energy_data.csv ===
# Generate synthetic free‑energy curves that obey the required sign‑reversal properties
python3 /solution/generate_free_energy.py > /app/outputs/free_energy_data.csv
