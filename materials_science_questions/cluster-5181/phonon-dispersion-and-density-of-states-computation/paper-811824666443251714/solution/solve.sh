#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: equilibrium_properties.json ===
cat > "$OUTDIR/equilibrium_properties.json" <<'EOF'
{
  "HgSe_V0": 56.23,
  "HgSe_B0": 57,
  "HgTe_V0": 67.03,
  "HgTe_B0": 47
}
EOF

# === solve block: phonon_frequencies.json ===
cat > "$OUTDIR/phonon_frequencies.json" <<'EOF'
{
  "HgSe_TO_Gamma_0GPa": 4.00,
  "HgSe_TA_X_0GPa": 0.70,
  "HgSe_TA_X_3GPa": -0.35,
  "HgTe_TO_Gamma_0GPa": 3.54,
  "HgTe_TA_X_0GPa": 0.50,
  "HgTe_TA_X_3GPa": -0.20
}
EOF

# === solve block: c2221_parameters.json ===
cat > "$OUTDIR/c2221_parameters.json" <<'EOF'
{
  "HgSe_x": 0.304,
  "HgSe_y": 0.210,
  "HgSe_b_over_a": 0.984,
  "HgSe_c_over_a": 0.998,
  "HgTe_x": 0.301,
  "HgTe_y": 0.211,
  "HgTe_b_over_a": 0.982,
  "HgTe_c_over_a": 0.994
}
EOF
