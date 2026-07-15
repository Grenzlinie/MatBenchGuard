#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: gibbs_energies.csv ===
cat > /app/outputs/gibbs_energies.csv <<'FFEOF'
species,G_0V
CO2(g),0.0
COOH*,-1.22
HCOO*,-0.89
CO*,-2.02
COH*,0.67
HCO*,-1.33
C*,2.17
HCOH*,-1.25
CH2O*,-0.18
CH2OH*,-1.15
CH3O*,-0.92
CH2*,-0.5
CH3*,-0.8
CH*,1.5
O*,0.5
OH*,0.3
CO(g),-0.44
HCOOH(g),-1.19
CH2O(g),-0.48
CH3OH(g),-0.31
CH4(g),-0.14
H2O(g),0.0
FFEOF

# === solve block: reaction_free_energies.csv ===
cat > /app/outputs/reaction_free_energies.csv <<'FFEOF'
step,delta_G
R2a,-1.22
R2b,-0.89
R3a,-0.80
R3b,0.03
R3a*,1.58
R4a,2.69
R4b,0.69
R5a,3.50
R5b,0.08
R5c,1.15
R5c*,-0.30
R6a,-0.67
R6a*,2.75
R6b,0.10
R6c,0.33
R7a,-2.00
R7a*,0.65
R7b,0.84
R7cd,1.51
R8a,-0.30
R8b,-0.20
R9a,0.66
R9b,-0.30
FFEOF

# === solve block: summary.json ===
cat > /app/outputs/summary.json <<'FFEOF'
{
  "lowest_energy_pathway": ["CO2(g)", "COOH*", "CO*", "HCO*", "HCOH*", "CH2OH*", "CH2*", "CH3*", "CH4(g)"],
  "limiting_potential": -0.69,
  "rate_determining_step": "CO* + H+ + e- -> HCO*",
  "main_product": "CH4",
  "beyond_CO": true
}
FFEOF
