#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: phonon_irrep_decomposition.json ===
cat > "$OUTDIR/phonon_irrep_decomposition.json" << 'EOF'
{
  "janus_C3v": {
    "point_group": "C3v",
    "total_vibrational": "5A1⊕3A2⊕8E",
    "acoustic": "A1⊕E",
    "optic": "4A1⊕3A2⊕7E",
    "ir_active": "4A1⊕7E",
    "raman_active": "4A1⊕7E",
    "silent": "3A2"
  },
  "symmetric_D3d": {
    "point_group": "D3d",
    "total_vibrational": "2A1g⊕2A2g⊕A1u⊕3A2u⊕4Eg⊕4Eu",
    "acoustic": "A2u⊕Eu",
    "optic": "2A1g⊕2A2g⊕A1u⊕2A2u⊕4Eg⊕3Eu",
    "ir_active": "2A2u⊕3Eu",
    "raman_active": "2A1g⊕4Eg",
    "silent": "2A2g⊕A1u"
  }
}
EOF
