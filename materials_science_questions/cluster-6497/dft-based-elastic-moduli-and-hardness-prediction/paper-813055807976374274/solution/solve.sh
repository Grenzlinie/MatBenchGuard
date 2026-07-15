#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: candidate_energies.json ===
cat > "$OUTDIR/candidate_energies.json" <<'FFEOF'
{
  "B1N5-I": -1.20,
  "B1N5-II": 0.0,
  "B5N1-I": 0.0,
  "B5N1-II": -0.08,
  "B2N4-I": 0.0,
  "B2N4-II": 1.60,
  "B2N4-III": 2.96,
  "B2N4-IV": 4.37,
  "B4N2-I": 0.0,
  "B4N2-II": 1.78,
  "B4N2-III": -2.39,
  "B4N2-IV": -2.72,
  "B3N3-I": 0.0,
  "B3N3-II": 1.89,
  "B3N3-III": 2.32
}
FFEOF

# === solve block: phonon_summary.json ===
cat > "$OUTDIR/phonon_summary.json" <<'FFEOF'
{
  "B1N5-I": {"stable": false},
  "B5N1-II": {"stable": false},
  "B2N4-I": {"stable": true},
  "B4N2-I": {"stable": false},
  "B4N2-III": {"stable": false},
  "B4N2-IV": {"stable": false},
  "B3N3-I": {"stable": true}
}
FFEOF

# === solve block: stable_structures.txt ===
cat > "$OUTDIR/stable_structures.txt" <<'FFEOF'
B2N4-I
B3N3-I
FFEOF

# === solve block: mechanical_properties.json ===
cat > "$OUTDIR/mechanical_properties.json" <<'FFEOF'
{
  "B2N4-I": {
    "biaxial": {"E_GPa": 415, "Y_N_m": 194, "tau_c_GPa": 36, "epsilon_c": 0.13},
    "X-axial": {"E_GPa": 441, "Y_N_m": 206, "tau_c_GPa": 40, "epsilon_c": 0.13},
    "Y-axial": {"E_GPa": 441, "Y_N_m": 206, "tau_c_GPa": 40, "epsilon_c": 0.14}
  },
  "B3N3-I": {
    "biaxial": {"E_GPa": 267, "Y_N_m": 127, "tau_c_GPa": 27, "epsilon_c": 0.16},
    "X-axial": {"E_GPa": 271, "Y_N_m": 129, "tau_c_GPa": 17, "epsilon_c": 0.08},
    "Y-axial": {"E_GPa": 271, "Y_N_m": 129, "tau_c_GPa": 17, "epsilon_c": 0.08}
  }
}
FFEOF

# === solve block: band_gap_strain.csv ===
cat > "$OUTDIR/band_gap_strain.csv" <<'FFEOF'
strain_percent,band_gap_eV,band_type
0,0.060,direct
1,0.090,direct
2,0.130,direct
3,0.170,direct
4,0.220,direct
5,0.280,direct
6,0.350,indirect
7,0.460,indirect
8,0.570,indirect
FFEOF
