#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'FFEOF'
binding_energy_eV_per_atom,carbide
-9.3835,Fe3C
-8.9383,Fe2C
-9.3807,Fe5C2
-10.7053,NbC
FFEOF

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'FFEOF'
carbide,formation_energy_eV_per_atom
Fe3C,-2.7288
Fe2C,0.0187
Fe5C2,-0.3585
NbC,-4.3182
FFEOF

# === solve block: dos_n_ef.csv ===
cat > "$OUTDIR/dos_n_ef.csv" <<'FFEOF'
N_EF_electrons_per_eV,carbide
26.0,Fe3C
4.1,Fe2C
20.4,Fe5C2
5.6,NbC
FFEOF
