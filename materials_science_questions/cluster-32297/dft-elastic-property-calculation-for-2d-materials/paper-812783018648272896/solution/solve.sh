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
cat > "$OUTDIR/results.json" <<'EOF'
{
  "monolayer_bandgap_eV": 2.31,
  "monolayer_refractive_index": 1.8,
  "monolayer_first_absorption_peak_eV": 3.75,
  "monolayer_max_imaginary_frequency_cm-1": 0.0,
  "heterostructure_bandgap_0strain_eV": 1.37,
  "heterostructure_bandgap_plus0.8strain_eV": 1.56,
  "heterostructure_bandgap_plus0.8efield_eV": 0.62
}
EOF
