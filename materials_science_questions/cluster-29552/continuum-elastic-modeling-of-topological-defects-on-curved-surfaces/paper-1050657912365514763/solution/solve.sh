#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: charge_data.csv ===
cat > "$OUTDIR/charge_data.csv" <<'ENDOFCSV'
model,geometry,origin,L_y,Q_W,n_W,delta_Phi_W,regularized_Q
hofstadter,cylinder,alpha,30,60.0,30,0.0,0.0
hofstadter,cylinder,alpha,31,62.0,31,0.0,0.0
hofstadter,cylinder,beta,30,75.0,30,0.0,15.0
hofstadter,cylinder,beta,31,77.5,31,0.0,15.5
hofstadter,ribbon,alpha,,20.75,10,0.0,0.75
hofstadter,ribbon,beta,,20.5,10,0.0,0.5
quadrupole,cylinder,alpha,30,60.0,30,0.0,0.0
quadrupole,cylinder,alpha,31,62.0,31,0.0,0.0
quadrupole,cylinder,beta,30,60.0,30,0.0,0.0
quadrupole,cylinder,beta,31,62.0,31,0.0,0.0
quadrupole,ribbon,alpha,,20.5,10,0.0,0.5
quadrupole,ribbon,beta,,20.0,10,0.0,0.0
ENDOFCSV

# === solve block: extracted_invariants.json ===
cat > "$OUTDIR/extracted_invariants.json" <<'ENDOFINV'
{
  "hofstadter": {
    "P_o_alpha": 0.0,
    "P_o_beta": 0.5,
    "delta_o_alpha": 1.0,
    "delta_o_beta": 2.0,
    "C": -2,
    "nu": 2.0
  },
  "quadrupole": {
    "P_o_alpha": 0.0,
    "P_o_beta": 0.0,
    "delta_o_alpha": 2.0,
    "delta_o_beta": 0.0,
    "C": 0,
    "nu": 2.0
  }
}
ENDOFINV

# === solve finalize ===
echo "Reference oracle artifacts written successfully."
