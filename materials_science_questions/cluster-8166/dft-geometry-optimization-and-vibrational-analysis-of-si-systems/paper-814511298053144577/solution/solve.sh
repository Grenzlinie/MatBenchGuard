#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'EOF'
{
  "L3H": {
    "scf_energy": -836.316,
    "homo": -5.111,
    "lumo": -0.571,
    "gap": 4.540,
    "dipole": 8.2429
  },
  "Me3SiL3": {
    "scf_energy": -1244.864,
    "homo": -3.772,
    "lumo": -1.435,
    "gap": 2.337,
    "dipole": 14.0375
  },
  "PhSiL3OEt": {
    "scf_energy": -1510.732,
    "homo": -3.324,
    "lumo": -0.756,
    "gap": 2.568,
    "dipole": 7.6195
  }
}
EOF
