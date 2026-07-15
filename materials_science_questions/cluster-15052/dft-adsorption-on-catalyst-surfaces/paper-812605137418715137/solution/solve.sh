#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
cat > "$OUTDIR/adsorption_energies.json" <<'EOF'
{
  "NH3_V": -6.070,
  "NH3_Pd": -6.785,
  "Benzene_Pd": -6.335,
  "O2_V": -5.848,
  "O2_Pd": -7.286,
  "NO_V_N": -5.375,
  "NO_Pd_N": -8.447,
  "NO2_Pd_N": -7.593,
  "NO2_Pd_O": -7.068
}
EOF

# === solve finalize ===
true
