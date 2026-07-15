#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
# No network fetch needed; all values are hardcoded from the paper's Fig. 5(a).

# === solve block: na_lattice_energies.csv ===
cat > "$OUTDIR/na_lattice_energies.csv" <<'EEOF'
lattice_constant,total_free_energy_per_atom
7.3,-0.238595
7.4,-0.238845
7.5,-0.238995
7.6,-0.239045
7.7,-0.238995
7.8,-0.238845
7.9,-0.238595
EEOF

# === solve finalize ===
# No additional steps.
