#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_adsorption_free_energies.json ===
cat > "$OUTDIR/step_01_adsorption_free_energies.json" <<'FFEOF'
{
  "site1": 2.03,
  "site2": 1.43,
  "site3": 1.09,
  "site4": 0.90,
  "site5": 0.74,
  "site6": 0.85
}
FFEOF

# === solve block: step_02_charge_occupancy.json ===
cat > "$OUTDIR/step_02_charge_occupancy.json" <<'FFEOF'
{
  "site1": {"sigma": 3.10, "pi": 1.08},
  "site2": {"sigma": 3.09, "pi": 1.06},
  "site3": {"sigma": 3.05, "pi": 1.03},
  "site4": {"sigma": 3.00, "pi": 1.00},
  "site5": {"sigma": 2.98, "pi": 1.00},
  "site6": {"sigma": 2.97, "pi": 1.00}
}
FFEOF
