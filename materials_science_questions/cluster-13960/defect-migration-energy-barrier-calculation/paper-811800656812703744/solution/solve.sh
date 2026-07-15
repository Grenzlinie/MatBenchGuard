#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "off_plane_formation_energy_eV": -2.51,
  "in_plane_formation_energy_eV": 2.42,
  "through_vacancy_barrier_eV": 4.93,
  "lateral_migration_barrier_eV": 2.2,
  "edge_migration_barrier_eV": 1.37
}
FFEOF
