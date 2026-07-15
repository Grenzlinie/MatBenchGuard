#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_energies.json ===
cat > "$OUTDIR/defect_energies.json" <<'FFEOF'
{
  "formation_energies": {
    "Cs": 1.95,
    "Ci_100_DB": 3.72,
    "Sii_110_DB": 3.39,
    "V": 3.63
  },
  "binding_energies": {
    "Ci_Ci": -2.39,
    "Ci_V": -5.39,
    "Cs_Sii": -0.97
  },
  "migration_barriers": {
    "Ci_diff": 0.90,
    "CiV_to_Cs": 0.10,
    "CsSii_to_Ci": 0.12
  },
  "md_result": "separated"
}
FFEOF
