#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_energetics.json ===
cat > "$OUTDIR/dft_energetics.json" <<'FFEOF'
{
  "reaction_energy_bulk_Zn_oxidation_eV_per_O": -3.85,
  "exothermicity_epoxide_migration_Zn_eV": -5.5,
  "energy_barrier_O_transfer_vacancy_eV": 0.0,
  "exothermicity_hydroxyl_transfer_Zn_eV": -4.0
}
FFEOF
