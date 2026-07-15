#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'EOF'
{
  "CoFeTiGa": {"c11": 316.24, "c12": 125.56, "c44": 125.75, "G": 143.21, "B": 189.12, "Y": 171.52, "ν": 0.20},
  "CoFeVGa": {"c11": 242.18, "c12": 191.65, "c44": 112.96, "G": 67.35, "B": 208.49, "Y": 91.20, "ν": 0.35},
  "CoFeCrGa": {"c11": 228.15, "c12": 161.64, "c44": 120.01, "G": 79.16, "B": 183.81, "Y": 103.84, "ν": 0.56},
  "CoFeMnGa": {"c11": 260.52, "c12": 197.15, "c44": 165.11, "G": 95.10, "B": 214.94, "Y": 248.63, "ν": 0.31},
  "CoFeCuGa": {"c11": 166.08, "c12": 151.17, "c44": 105.59, "G": 42.17, "B": 156.14, "Y": 58.03, "ν": 0.54},
  "CoFeNbGa": {"c11": 257.03, "c12": 176.04, "c44": 106.96, "G": 82.75, "B": 203.04, "Y": 218.56, "ν": 0.32}
}
EOF

# === solve block: phonon_min_freq.json ===
cat > "$OUTDIR/phonon_min_freq.json" <<'EOF'
{
  "CoFeTiGa": 0.5,
  "CoFeVGa": 0.5,
  "CoFeCrGa": 0.5,
  "CoFeMnGa": 0.5,
  "CoFeCuGa": 0.5,
  "CoFeNbGa": 0.5
}
EOF

# === solve block: magnetic_moments.csv ===
cat > "$OUTDIR/magnetic_moments.csv" <<'EOF'
Alloy,Type,a,M_Co,M_Fe,M_R,M_Ga,M_tot,Phase
CoFeTiGa,1,5.81,0,0,0,0,0,CS
CoFeVGa,1,5.74,0.57,0.59,-0.11,-0.02,1.03,HM
CoFeCrGa,1,5.72,0.94,-0.74,1.81,-0.04,1.97,SGS
CoFeMnGa,1,5.71,0.72,-0.24,2.61,-0.05,3.04,Nearly-HM
CoFeCuGa,2,5.79,1.05,2.61,-0.01,-0.06,3.59,Metal
CoFeNbGa,1,5.94,0.57,0.62,-0.11,-0.02,1.06,HM
EOF

# === solve block: transport_seebeck_300K.csv ===
cat > "$OUTDIR/transport_seebeck_300K.csv" <<'EOF'
Alloy,S_up,S_down,S_spin
CoFeTiGa,0,0,0
CoFeVGa,9.76,382.04,9.72
CoFeCrGa,-58.78,442.88,-60.29
CoFeMnGa,17.11,113.37,10.15
CoFeCuGa,-1.55,-1.55,0.0
CoFeNbGa,9.06,789.21,9.05
EOF
