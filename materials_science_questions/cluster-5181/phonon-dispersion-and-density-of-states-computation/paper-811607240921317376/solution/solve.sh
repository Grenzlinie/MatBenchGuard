#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_equilibrium_properties.json ===
cat > "$OUTDIR/step_01_equilibrium_properties.json" <<'EOF'
{
  "FeSi": {
    "a": 2.721,
    "B": 269.5,
    "Bprime": 4.56
  },
  "CoSi": {
    "a": 2.740,
    "B": 245.4,
    "Bprime": 2.43
  }
}
EOF

# === solve block: step_02_elastic_constants.json ===
cat > "$OUTDIR/step_02_elastic_constants.json" <<'EOF'
{
  "FeSi": {
    "C11": 460.0,
    "C12": 173.0,
    "C44": 114.3
  },
  "CoSi": {
    "C11": 268.6,
    "C12": 227.4,
    "C44": 74.0
  }
}
EOF

# === solve block: step_03_electronic_dos.json ===
cat > "$OUTDIR/step_03_electronic_dos.json" <<'EOF'
{
  "FeSi": {
    "N_EF": 0.78,
    "Fe_3d_percent": 85.0
  },
  "CoSi": {
    "N_EF": 1.62,
    "Co_3d_percent": 73.0
  }
}
EOF

# === solve block: step_04_phonon_frequencies.json ===
cat > "$OUTDIR/step_04_phonon_frequencies.json" <<'EOF'
{
  "FeSi": {
    "TO_Gamma": 9.91,
    "TA_X": 5.22,
    "LA_X": 10.57,
    "TO_X": 9.37,
    "LO_X": 14.80,
    "A_R": 8.66,
    "O_R": 11.00,
    "all_positive": true
  },
  "CoSi": {
    "TO_Gamma": 8.37,
    "all_positive": true
  }
}
EOF
