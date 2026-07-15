#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: site_preference.json ===
cat > "$OUTDIR/site_preference.json" <<'EOF'
[
  {"metal": "Li", "preferred_site": "different_layers", "interlayer_distance_A": 5.9},
  {"metal": "Na", "preferred_site": "same_layer", "interlayer_distance_A": 6.4},
  {"metal": "Mg", "preferred_site": "different_layers", "interlayer_distance_A": 6.1}
]
EOF

# === solve block: bulk_moduli.json ===
cat > "$OUTDIR/bulk_moduli.json" <<'EOF'
[
  {"system": "pristine_BP", "bulk_modulus_GPa": 46},
  {"system": "Li2P", "bulk_modulus_GPa": 26},
  {"system": "Na2P", "bulk_modulus_GPa": 24},
  {"system": "Mg2P", "bulk_modulus_GPa": 53}
]
EOF

# === solve block: diffusion_barriers.json ===
cat > "$OUTDIR/diffusion_barriers.json" <<'EOF'
[
  {"metal": "Li", "path": "zigzag", "barrier_eV": 0.02},
  {"metal": "Li", "path": "armchair", "barrier_eV": 0.12},
  {"metal": "Na", "path": "zigzag", "barrier_eV": 0.18},
  {"metal": "Na", "path": "armchair", "barrier_eV": 0.76},
  {"metal": "Mg", "path": "zigzag", "barrier_eV": 0.41},
  {"metal": "Mg", "path": "armchair", "barrier_eV": 1.50}
]
EOF
