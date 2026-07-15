#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: final_orbital_spacings.json ===
cat > "/app/outputs/final_orbital_spacings.json" <<'FFEOF'
{
  "models": [
    {
      "model_name": "CH3O/Li9(5,4) on-top",
      "total_energy": -179.00144,
      "relative_orbital_energies": [0.0, 4.56, 6.86, 6.86]
    },
    {
      "model_name": "CH3O/Li9(4,5) symmetric double-bridge",
      "total_energy": -179.03651,
      "relative_orbital_energies": [0.0, 0.008, 4.46, 7.0]
    }
  ]
}
FFEOF
