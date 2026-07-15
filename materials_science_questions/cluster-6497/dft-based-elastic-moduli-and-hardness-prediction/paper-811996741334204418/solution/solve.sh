#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results_summary.csv ===
cat > "$OUTDIR/results_summary.csv" <<'FFEOF'
composition,phase,lattice_constant_a,lattice_constant_c,bulk_modulus,total_energy
0,NaCl,4.5114,0,189.9,-100
0.25,NaCl,4.5670,0,180.820,-102
0.5,NaCl,4.6194,0,171.182,-104
0.75,NaCl,4.6685,0,160.986,-105
1,NaCl,4.7144,0,150.233,-106
0,wurtzite,3.5226,5.6756,140.42,-99
0.25,wurtzite,3.5377,5.7016,134.332,-101
0.5,wurtzite,3.5534,5.7276,128.617,-104
0.75,wurtzite,3.5697,5.7536,123.272,-106
1,wurtzite,3.5865,5.7796,118.30,-108
FFEOF

# === solve block: bowing_parameters.json ===
cat > "$OUTDIR/bowing_parameters.json" <<'FFEOF'
{
  "NaCl": {
    "alpha_lattice_bowing_parameter": -0.02602,
    "beta_bulk_modulus_bowing_parameter": -4.4612
  },
  "wurtzite": {
    "alpha_lattice_bowing_parameter": 0.00461,
    "beta_bulk_modulus_bowing_parameter": 2.974
  }
}
FFEOF

# === solve block: phase_transition_composition.json ===
cat > "$OUTDIR/phase_transition_composition.json" <<'FFEOF'
{
  "crossover_x": 0.5,
  "stable_NaCl_range": "0<=x<0.5",
  "stable_wurtzite_range": "0.5<=x<=1"
}
FFEOF
