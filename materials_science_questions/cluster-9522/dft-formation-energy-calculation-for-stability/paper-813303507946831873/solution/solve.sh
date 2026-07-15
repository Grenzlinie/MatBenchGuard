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
cat > "$OUTDIR/results.json" << 'EOF'
{
  "lattice_optimizations": [
    {"compound": "Ti2FeAl", "a_opt_angstrom": 6.14, "total_moment_muB": 1.0, "minority_gap_eV": 0.53},
    {"compound": "Ti2CoAl", "a_opt_angstrom": 6.14, "total_moment_muB": 2.0, "minority_gap_eV": 0.68},
    {"compound": "Ti2NiAl", "a_opt_angstrom": 6.20, "total_moment_muB": 3.0, "minority_gap_eV": 0.46}
  ],
  "z_removal": {"a_angstrom": 6.14, "total_moment_muB": 0.5, "minority_gap_eV": 0.0},
  "lattice_parameter_effect": [
    {"a": 5.80, "gap": 0.65},
    {"a": 6.40, "gap": 0.66}
  ]
}
EOF
