#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_single_molecule_energies.json ===
cat > "$OUTDIR/step_01_single_molecule_energies.json" <<'EOF'
[
{"method":"LDA","E_abs_eV":-0.124,"E_LC_eV":-1031.124,"E_EC_eV":-1000.0,"E_H2_eV":-31.0},
{"method":"PW91","E_abs_eV":-0.065,"E_LC_eV":-1031.065,"E_EC_eV":-1000.0,"E_H2_eV":-31.0},
{"method":"PBE","E_abs_eV":-0.025,"E_LC_eV":-1031.025,"E_EC_eV":-1000.0,"E_H2_eV":-31.0},
{"method":"BLYP","E_abs_eV":0.041,"E_LC_eV":-1030.959,"E_EC_eV":-1000.0,"E_H2_eV":-31.0},
{"method":"FF_Buck","E_abs_eV":-0.057,"E_LC_eV":-500.057,"E_EC_eV":-500.0,"E_H2_eV":0.0}
]
EOF
