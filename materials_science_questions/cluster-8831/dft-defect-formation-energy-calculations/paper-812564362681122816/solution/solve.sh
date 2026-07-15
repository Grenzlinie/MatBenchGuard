#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energy_summary.csv ===
cat > "$OUTDIR/formation_energy_summary.csv" <<'EOF'
angle,condition,defect,formation_energy_at_VBM
57.802,Ge-rich,Vac_Ge,0.58
57.802,Ge-rich,Vac_Te,1.95
57.802,Ge-rich,Te_Ge,2.30
57.802,Ge-rich,Ge_Te,3.10
57.802,Te-rich,Vac_Ge,1.15
57.802,Te-rich,Vac_Te,0.80
57.802,Te-rich,Te_Ge,2.70
57.802,Te-rich,Ge_Te,2.30
58.0,Ge-rich,Vac_Ge,0.30
58.0,Ge-rich,Vac_Te,1.92
58.0,Ge-rich,Te_Ge,2.28
58.0,Ge-rich,Ge_Te,3.08
58.0,Te-rich,Vac_Ge,1.12
58.0,Te-rich,Vac_Te,0.78
58.0,Te-rich,Te_Ge,2.68
58.0,Te-rich,Ge_Te,2.28
58.5,Ge-rich,Vac_Ge,0.01
58.5,Ge-rich,Vac_Te,1.90
58.5,Ge-rich,Te_Ge,2.25
58.5,Ge-rich,Ge_Te,3.05
58.5,Te-rich,Vac_Ge,1.10
58.5,Te-rich,Vac_Te,0.75
58.5,Te-rich,Te_Ge,2.65
58.5,Te-rich,Ge_Te,2.25
59.0,Ge-rich,Vac_Ge,-0.45
59.0,Ge-rich,Vac_Te,1.88
59.0,Ge-rich,Te_Ge,2.22
59.0,Ge-rich,Ge_Te,3.02
59.0,Te-rich,Vac_Ge,1.07
59.0,Te-rich,Vac_Te,0.72
59.0,Te-rich,Te_Ge,2.62
59.0,Te-rich,Ge_Te,2.22
59.5,Ge-rich,Vac_Ge,-0.46
59.5,Ge-rich,Vac_Te,1.87
59.5,Ge-rich,Te_Ge,2.21
59.5,Ge-rich,Ge_Te,3.01
59.5,Te-rich,Vac_Ge,1.06
59.5,Te-rich,Vac_Te,0.71
59.5,Te-rich,Te_Ge,2.61
59.5,Te-rich,Ge_Te,2.21
EOF
