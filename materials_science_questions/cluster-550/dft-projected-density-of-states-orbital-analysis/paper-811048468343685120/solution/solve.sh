#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies_distances.json ===
cat > "$OUTDIR/binding_energies_distances.json" << 'FFEOF'
[
  {"metal": "Al", "E_b": 1.35, "d_CdTe_M": 2.30},
  {"metal": "Ag", "E_b": 1.25, "d_CdTe_M": 2.27},
  {"metal": "Au", "E_b": 1.58, "d_CdTe_M": 1.96},
  {"metal": "Cu", "E_b": 1.26, "d_CdTe_M": 2.29},
  {"metal": "Ni", "E_b": 2.80, "d_CdTe_M": 1.14}
]
FFEOF

# === solve block: adsorption_classification.json ===
cat > "$OUTDIR/adsorption_classification.json" <<'FFEOF'
[
  {"metal": "Al", "category": "weak chemisorption"},
  {"metal": "Ag", "category": "weak chemisorption"},
  {"metal": "Au", "category": "medium chemisorption"},
  {"metal": "Cu", "category": "weak chemisorption"},
  {"metal": "Ni", "category": "strong chemisorption"}
]
FFEOF

# === solve block: schottky_barriers.json ===
cat > "$OUTDIR/schottky_barriers.json" <<'FFEOF'
[
  {"metal": "Al", "SBH": 0.12, "contact_type": "n-type"},
  {"metal": "Ag", "SBH": 0.26, "contact_type": "n-type"},
  {"metal": "Au", "SBH": 0.44, "contact_type": "p-type"},
  {"metal": "Cu", "SBH": 0.63, "contact_type": "n-type"},
  {"metal": "Ni", "SBH": 0.66, "contact_type": "p-type"}
]
FFEOF

# === solve block: tunneling_barriers.json ===
cat > "$OUTDIR/tunneling_barriers.json" <<'FFEOF'
[
  {"metal": "Al", "Delta_V": 1.41, "w_B": 0.49, "T_B": 56.7},
  {"metal": "Ag", "Delta_V": 1.87, "w_B": 0.51, "T_B": 49.0},
  {"metal": "Au", "Delta_V": 0.0, "w_B": 0.0, "T_B": 100.0},
  {"metal": "Cu", "Delta_V": 1.68, "w_B": 0.44, "T_B": 55.8},
  {"metal": "Ni", "Delta_V": 0.0, "w_B": 0.0, "T_B": 100.0}
]
FFEOF
