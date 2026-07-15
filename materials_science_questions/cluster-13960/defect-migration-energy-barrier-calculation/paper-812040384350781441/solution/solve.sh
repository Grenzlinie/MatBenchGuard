#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energies.json ===
cat > "$OUTDIR/step_01_formation_energies.json" <<'FFEOF'
{
  "tetrahedral": 6.18,
  "octahedral": 6.40
}
FFEOF

# === solve block: step_02_migration_energy.json ===
cat > "$OUTDIR/step_02_migration_energy.json" <<'FFEOF'
{
  "migration_energy": 0.06
}
FFEOF

# === solve block: step_03_binding_energy.json ===
cat > "$OUTDIR/step_03_binding_energy.json" <<'FFEOF'
{
  "binding_energy_config_C": 0.98
}
FFEOF
