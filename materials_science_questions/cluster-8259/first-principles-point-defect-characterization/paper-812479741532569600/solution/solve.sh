#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: transition_levels_2D1L.json ===
cat > "$OUTDIR/transition_levels_2D1L.json" <<'EOF'
{
  "V_I_LA": {"transition_type": "(0/1+)", "value_eV": -0.020, "reference": "CBM"},
  "V_I_LB": {"transition_type": "(0/1+)", "value_eV": -0.198, "reference": "CBM"},
  "I_i_LA": {"transition_type": "(0/1-)", "value_eV": 0.115, "reference": "VBM"},
  "I_i_LB": {"transition_type": "(0/1-)", "value_eV": 0.131, "reference": "VBM"}
}
EOF

# === solve block: deep_defect_formation_energies.json ===
cat > "$OUTDIR/deep_defect_formation_energies.json" <<'EOF'
{
  "Pb_i_0": 1.4,
  "Pb_I_0": 3.0,
  "I_M_0": 4.2,
  "I_Pb_0": 3.2
}
EOF
