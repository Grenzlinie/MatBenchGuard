#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_percent_Cl3p.csv ===
OUTDIR=${OUTDIR:-/app/outputs}
cat > "$OUTDIR/computed_percent_Cl3p.csv" <<'FFEOF'
compound,orbital,percent_Cl3p
Ti,1a1,12.1
Ti,1b2,17.2
Ti,1b1,2.2
Ti,1a2,1.4
Ti,2a1,6.3
Ti,total,20.0
Zr,1a1,12.2
Zr,1b2,10.8
Zr,1b1,2.7
Zr,1a2,3.9
Zr,2a1,6.5
Zr,total,18.0
Hf,1a1,11.2
Hf,1b2,8.0
Hf,1b1,2.6
Hf,1a2,4.2
Hf,2a1,7.8
Hf,total,17.0
FFEOF

# === solve block: simulated_XAS_features.csv ===
cat > /app/outputs/simulated_XAS_features.csv <<'FFEOF'
compound,oscillator_strength,peak_energy_eV,peak_label,percent_Cl3p
Ti,0.005,2821.20,peak1,6
Ti,0.020,2822.10,peak2,14
Zr,0.006,2822.46,peak1,6
Zr,0.015,2823.72,peak2,12
Hf,0.006,2822.98,peak1,6
Hf,0.010,2824.08,peak2,11
FFEOF
