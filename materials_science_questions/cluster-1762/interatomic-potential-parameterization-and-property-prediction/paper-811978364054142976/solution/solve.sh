#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_fitted_coefficients.json ===
cat > /app/outputs/step_01_fitted_coefficients.json <<'FFEOF'
{
  "Si": {"C1": 0.1475, "C2": -0.3490, "C3": 0.1092},
  "Ge": {"C1": 0.2035, "C2": -0.6803, "C3": 0.3914},
  "alphaSn": {"C1": 0.2600, "C2": -0.6285, "C3": 0.3803}
}
FFEOF

# === solve block: step_02_transition_energies.csv ===
cat > /app/outputs/step_02_transition_energies.csv <<'FFEOF'
material,transition,energy
Si,"Γ2'-Γ25'",4.15
Si,"Γ15-Γ25'",3.35
Si,"L1-Γ25'",2.07
Si,"L1-L3'",3.31
Si,"L3-L3'",5.41
Si,"X1-X4",4.12
Ge,"Γ2'-Γ25'",0.97
Ge,"Γ15-Γ25'",3.18
Ge,"L1-Γ25'",1.00
Ge,"X1(Δ1)-Γ25'",1.49
Ge,"L1-L3'",2.19
Ge,"L3-L3'",5.39
Ge,"X1-X4",3.98
alphaSn,"Γ2'-Γ25'",-0.20
alphaSn,"Γ15-Γ25'",2.60
alphaSn,"L1-Γ25'",0.68
alphaSn,"X1(Δ1)-Γ25'",1.60
alphaSn,"L1-L3'",1.39
alphaSn,"L3-L3'",4.33
alphaSn,"X1-X4",3.29
FFEOF
