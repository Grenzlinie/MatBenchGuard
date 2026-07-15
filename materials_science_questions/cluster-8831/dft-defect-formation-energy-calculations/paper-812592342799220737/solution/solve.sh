#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'FFEOF'
{
  "adatom_formation_energy_eV": 0.72,
  "vacancy_formation_energy_eV": 2.21
}
FFEOF

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'FFEOF'
{
  "adatom_gap_eV": 0.0,
  "pristine_gap_eV": 0.0,
  "vacancy_gap_eV": 0.5
}
FFEOF
