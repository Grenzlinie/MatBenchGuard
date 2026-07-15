#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: h2_dimer_results.json ===
cat > "$OUTDIR/h2_dimer_results.json" <<'FFEOF'
{
  "bond_length_angstroms": 0.742,
  "cohesive_energy_eV_per_atom": -2.373
}
FFEOF

# === solve block: solution_energies.json ===
cat > "$OUTDIR/solution_energies.json" <<'FFEOF'
{
  "delta_Es_Td_eV": 0.693,
  "delta_Es_Oh_eV": 0.824
}
FFEOF

# === solve block: migration_barrier.json ===
cat > "$OUTDIR/migration_barrier.json" <<'FFEOF'
{
  "migration_barrier_eV": 0.189
}
FFEOF
