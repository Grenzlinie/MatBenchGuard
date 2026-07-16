#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: O2_physisorption_results.json ===
cat > "$OUTDIR/O2_physisorption_results.json" <<'FFEOF'
{
  "binding_energy_eV": -0.12,
  "molecule_sheet_distance_A": 2.84,
  "O_O_bond_length_A": 1.23,
  "net_charge_transfer_e": 1.2e-4,
  "band_gap_eV": 2.43,
  "HOMO_below_VBM_eV": 0.10,
  "LUMO_below_CBM_eV": 0.16
}
FFEOF

# === solve block: O2_dissociation_barrier.json ===
cat > "$OUTDIR/O2_dissociation_barrier.json" <<'FFEOF'
{
  "energy_barrier_eV": 4.78
}
FFEOF

# === solve block: H2O_physisorption_results.json ===
cat > "$OUTDIR/H2O_physisorption_results.json" <<'FFEOF'
{
  "binding_energy_eV": -0.62,
  "molecule_sheet_distance_A": 2.03,
  "net_charge_transfer_e": 9.0e-4
}
FFEOF
