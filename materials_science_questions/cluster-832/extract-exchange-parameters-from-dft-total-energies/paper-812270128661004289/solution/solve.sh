#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_D_over_Tp.json ===
python3 -c "
import json
k_B = 8.617333262e-2  # meV/K (correct conversion from eV/K: 8.617333262e-5 eV/K * 1000)
S = 3.5
def D_over_Tp(r0, z, dr=0.0, dJ=0.0):
    factor = k_B * r0 * r0 / (2 * (S + 1))
    if dr == 0.0 and dJ == 0.0:
        return factor
    else:
        return factor * (1 - 2 * z * (dr / r0) * dJ)

amorphous = D_over_Tp(3.47, 6, 0.37, 0.25)
crystalline_GdAl2 = D_over_Tp(3.422, 4)
crystalline_Gd = D_over_Tp(3.573, 12)

result = {
    'amorphous': round(amorphous, 10),
    'crystalline_GdAl2': round(crystalline_GdAl2, 10),
    'crystalline_Gd': round(crystalline_Gd, 10)
}
with open('/app/outputs/computed_D_over_Tp.json', 'w') as f:
    json.dump(result, f, indent=2)
"
