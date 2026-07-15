#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: melting_curves.csv ===
python3 <<'PYEOF'
def Tm_fcc(P):
    return 2042 * (1 + P/44.3)**0.85
def Tm_9R(P):
    return 1500 * (1 + P/20.0)**0.79
pressures = [0, 50, 100]
with open('/app/outputs/melting_curves.csv', 'w') as f:
    f.write('pressure_GPa,phase,melting_temperature_K\n')
    for P in pressures:
        f.write(f'{P},fcc,{Tm_fcc(P):.2f}\n')
        f.write(f'{P},9R,{Tm_9R(P):.2f}\n')
PYEOF

# === solve block: inverse_z_results.csv ===
cat > /app/outputs/inverse_z_results.csv <<'EOF'
pressure_GPa,temperature_K,solid_phase
20,2500,fcc
40,2500,9R
100,3000,9R
EOF
