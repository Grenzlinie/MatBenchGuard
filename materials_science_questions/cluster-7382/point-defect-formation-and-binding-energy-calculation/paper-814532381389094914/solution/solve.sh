#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: vacancy_formation_energies.json ===
mkdir -p /app/outputs
python3 <<'PYEOF'
import math, json

k_B = 8.617333262e-5
c = 0.5
Ef0 = 1.9
V1 = 0.082

S_all = - (c * math.log(c) + (1-c) * math.log(1-c))  # = math.log(2)

probs = [1,12,66,220,495,792,924,792,495,220,66,12,1]
g = [p / 4096.0 for p in probs]
Es = [Ef0 + n * V1 for n in range(13)]

results = {}
for T_K in [500, 1000, 1500]:
    T_eV = k_B * T_K
    Z = sum(g[n] * math.exp(-Es[n] / T_eV) for n in range(13))
    Ef = -T_eV * math.log(Z)
    tildeEf = Ef + T_eV * S_all
    results[f"T_{T_K}_Ef"] = Ef
    results[f"T_{T_K}_tildeEf"] = tildeEf

with open('/app/outputs/vacancy_formation_energies.json', 'w') as f:
    json.dump(results, f, indent=2)
PYEOF
