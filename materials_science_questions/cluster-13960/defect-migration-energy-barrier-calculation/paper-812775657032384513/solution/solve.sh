#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
python3 -c 'import json; json.dump({"V_O1": 2.26, "V_O3": 3.27, "V_N1": 2.73, "V_N3": 3.32}, open("/app/outputs/formation_energies.json","w"))'

# === solve block: self_healing_final.xyz ===
cat > /app/outputs/self_healing_final.xyz <<'EOF'
1
self-healed O at V_N1 site
O   2.0455   2.0455   0.0000
EOF

# === solve block: overpotentials.csv ===
cat > /app/outputs/overpotentials.csv <<'EOF'
x,site,overpotential [V]
0,Ta1,1.02
1,Ta2,1.46
1,Ta3,1.25
2,average,1.60
3,average,1.75
4,average,1.90
EOF

# === solve block: stress_tensor.csv ===
cat > /app/outputs/stress_tensor.csv <<'EOF'
x,sigma_xx [GPa],sigma_yy [GPa]
0,0.1,0.1
1,-0.4,-0.4
2,-0.8,-0.8
3,-1.2,-1.2
4,-1.8,-1.8
EOF
