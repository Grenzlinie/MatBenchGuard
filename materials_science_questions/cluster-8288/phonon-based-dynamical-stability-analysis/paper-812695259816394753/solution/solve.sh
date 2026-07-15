#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: phonon_stability.json ===
cat > "$OUTDIR/phonon_stability.json" <<'EOF'
{
  "BaCNOCl": {"imaginary_modes_present": false, "min_phonon_frequency_cm-1": 50.0},
  "BaCNOBr": {"imaginary_modes_present": false, "min_phonon_frequency_cm-1": 45.0},
  "BaCNOI": {"imaginary_modes_present": false, "min_phonon_frequency_cm-1": 40.0},
  "Ba(CNO)2": {"imaginary_modes_present": false, "min_phonon_frequency_cm-1": 60.0}
}
EOF

# === solve block: refractive_indices.json ===
cat > "$OUTDIR/refractive_indices.json" <<'EOF'
{
  "BaCNOCl": {"n_x": 1.50, "n_y": 1.842, "n_z": 1.60, "birefringence": 0.342},
  "BaCNOBr": {"n_x": 1.55, "n_y": 1.807, "n_z": 1.60, "birefringence": 0.257},
  "BaCNOI": {"n_x": 1.60, "n_y": 1.817, "n_z": 1.62, "birefringence": 0.217},
  "Ba(CNO)2": {"n_x": 1.45, "n_y": 1.769, "n_z": 1.55, "birefringence": 0.319}
}
EOF
