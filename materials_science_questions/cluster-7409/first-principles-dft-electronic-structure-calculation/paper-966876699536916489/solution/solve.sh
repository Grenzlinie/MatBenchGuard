#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_summary.json ===
cat > /app/outputs/electronic_summary.json <<'EOF'
{
  "bandgap_PBEpU": 2.08,
  "bandgap_HSEscaled": 2.48,
  "midgap_states": [
    {"spin": "up", "state_label": "d1", "energy_rel_VBM": 0.10, "occupied": true},
    {"spin": "up", "state_label": "d2", "energy_rel_VBM": 0.55, "occupied": true},
    {"spin": "up", "state_label": "d3", "energy_rel_VBM": 1.00, "occupied": true},
    {"spin": "down", "state_label": "d1", "energy_rel_VBM": 0.09, "occupied": true},
    {"spin": "down", "state_label": "d2", "energy_rel_VBM": 0.51, "occupied": true},
    {"spin": "down", "state_label": "d3", "energy_rel_VBM": 1.20, "occupied": true}
  ]
}
EOF

# === solve block: table1_energy_nac.csv ===
cat > /app/outputs/table1_energy_nac.csv <<'EOF'
orbitals,energy,scaled_energy,NAC,scaled_NAC
VBM-d1,0.09,0.11,42.08,34.93
d1-d2,0.42,0.76,24.31,13.37
d2-d3,0.69,0.60,14.44,16.61
d3-CBM,0.86,1.00,8.41,7.23
VBM-CBM,2.08,2.48,2.10,1.66
EOF

# === solve block: table2_timescales.csv ===
cat > /app/outputs/table2_timescales.csv <<'EOF'
spin,process,timescale_ps,uncertainty_ps
up,ES_decay,1.40,0.22
up,trapped_hole_rise,1.43,0.56
up,GS_rise,23.52,2.90
down,ES_decay,0.32,0.06
down,trapped_hole_rise,0.34,0.08
down,GS_rise,12.18,1.89
EOF
