#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transition_and_elastic_properties.json ===
mkdir -p /app/outputs
cat > /app/outputs/transition_and_elastic_properties.json <<'EOF'
{
  "compounds": [
    {"name": "ZnTe", "P_t_GPa": 10.0, "volume_collapse_percent": 8.1, "B_T_GPa": 129.8, "C44_GPa": 103.1, "C_s_GPa": 39.9},
    {"name": "ZnSe0.2Te0.8", "P_t_GPa": 11.0, "volume_collapse_percent": 8.5, "B_T_GPa": 132.0, "C44_GPa": 104.0, "C_s_GPa": 40.9},
    {"name": "ZnSe0.55Te0.45", "P_t_GPa": 12.2, "volume_collapse_percent": 7.8, "B_T_GPa": 146.5, "C44_GPa": 114.2, "C_s_GPa": 41.1},
    {"name": "ZnSe0.81Te0.19", "P_t_GPa": 12.8, "volume_collapse_percent": 8.4, "B_T_GPa": 154.9, "C44_GPa": 118.8, "C_s_GPa": 41.4},
    {"name": "ZnSe0.93Te0.07", "P_t_GPa": 13.0, "volume_collapse_percent": 8.3, "B_T_GPa": 163.3, "C44_GPa": 122.6, "C_s_GPa": 41.7},
    {"name": "ZnSe", "P_t_GPa": 13.8, "volume_collapse_percent": 7.6, "B_T_GPa": 156.5, "C44_GPa": 104.2, "C_s_GPa": 52.5}
  ]
}
EOF
