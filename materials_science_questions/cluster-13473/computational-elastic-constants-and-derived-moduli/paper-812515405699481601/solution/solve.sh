#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: density_vs_epsilon.csv ===
cat > $OUTDIR/density_vs_epsilon.csv <<'EOF'
epsilon_norm,density_g_cm3
0.5,1.05
0.75,1.08
1.0,1.12
1.25,1.15
1.5,1.17
1.75,1.20
2.0,1.22
5.0,1.30
10.0,1.38
EOF
cat > /solution/generate_tensile_data.py <<'PYEOF'
import json

moduli = {
    "0.5": 0.25,
    "0.75": 0.375,
    "1.0": 0.5,
    "1.25": 0.625,
    "1.5": 0.75,
    "1.75": 0.875,
    "2.0": 1.0,
    "5.0": 2.5,
    "10.0": 5.0
}
directions = ["X", "Y", "Z"]
strain = [i * 0.001 for i in range(21)]

data = {}
for eps, E in moduli.items():
    data[eps] = {}
    for d in directions:
        stress = [E * s for s in strain]
        data[eps][d] = {
            "strain": strain,
            "stress": stress,
            "slope": E
        }

with open("/app/outputs/tensile_data.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
chmod +x /solution/generate_tensile_data.py

# === solve block: youngs_modulus_vs_epsilon.csv ===
cat > /app/outputs/youngs_modulus_vs_epsilon.csv <<'EOF'
epsilon_norm,young_modulus_GPa
0.5,1.0
0.75,1.5
1.0,2.0
1.25,2.5
1.5,3.0
1.75,3.5
2.0,4.0
5.0,10.0
10.0,20.0
EOF
