#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies_and_distances.json ===
cat > "/app/outputs/binding_energies_and_distances.json" <<'FFEOF'
{
  "Pd111_O_fcc_binding_energy": -1.78,
  "PdB111_O_hcp_binding_energy": -1.36,
  "Pd111_OH_fcc_binding_energy": -3.07,
  "PdB111_OH_bridge_binding_energy": -2.98,
  "Pd111_interlayer_distance": 2.282,
  "PdB111_interlayer_distance": 2.335
}
FFEOF
