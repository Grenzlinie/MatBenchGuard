#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bulk_surface.json ===
cat > "$OUTDIR/bulk_surface.json" << 'EOF'
{
  "bulk_lattice_constant": 5.42,
  "surface_energy": 0.62,
  "vacancy_formation_energy": 2.78
}
EOF

# === solve block: adsorption_perfect.csv ===
cat > "$OUTDIR/adsorption_perfect.csv" << 'EOF'
config,E_ads,C_Oa,C_Ob,O_C_O_angle,Bader_charge
P-1,-0.54,1.27,1.27,129,-0.35
P-2,-0.38,1.22,1.30,130,-0.30
P-3,-0.12,1.18,1.17,180,-0.003
EOF

# === solve block: adsorption_defective.csv ===
cat > "$OUTDIR/adsorption_defective.csv" << 'EOF'
config,E_ads,C_Oa,C_Ob,O_C_O_angle,Bader_charge
D-1,-0.69,1.21,1.43,122,-0.83
D-2,-0.88,1.28,1.25,128,-0.40
D-3,-1.12,1.27,1.27,129,-0.67
EOF

# === solve block: reaction_pathways.json ===
cat > "$OUTDIR/reaction_pathways.json" << 'EOF'
[
  {"pathway_label":"perfect_dissoc_P1","initial_state":"P-1","final_state":"CO+O","reaction_energy":3.62,"barrier":4.08},
  {"pathway_label":"perfect_dissoc_P2","initial_state":"P-2","final_state":"CO+O","reaction_energy":3.23,"barrier":3.70},
  {"pathway_label":"defective_dissoc_D1","initial_state":"D-1","final_state":"CO+O","reaction_energy":-0.52,"barrier":0.0},
  {"pathway_label":"defective_dissoc_D3","initial_state":"D-3","final_state":"CO+O","reaction_energy":-0.09,"barrier":0.27},
  {"pathway_label":"perfect_hydrogen_COOH_CH1","initial_state":"CH-1","final_state":"COOH*","reaction_energy":0.23,"barrier":0.36},
  {"pathway_label":"perfect_hydrogen_HCOO_CH2","initial_state":"CH-2","final_state":"HCOO*","reaction_energy":2.43,"barrier":2.72},
  {"pathway_label":"defective_hydrogen_COOH_CW1","initial_state":"CW-1","final_state":"COOH*","reaction_energy":0.53,"barrier":0.68},
  {"pathway_label":"defective_hydrogen_HCOO_CW2","initial_state":"CW-2","final_state":"HCOO*","reaction_energy":-1.27,"barrier":1.76}
]
EOF
