#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
python3 -c '
import json

band_gap = 2.8
transition_level = 0.6  # eV below CBM
neutral_O_poor = 2.6

fermi_levels = [round(i*0.05, 2) for i in range(0, int(band_gap/0.05)+1)]  # 0 to 2.8 step 0.05

def H1_OP(ef): return 0.4 + ef
def H2_OP(ef): return -1.8 + 2*ef

def H0_OR(ef): return 4.5
def H1_OR(ef): return 2.3 + ef
def H2_OR(ef): return 0.1 + 2*ef

charges = [0, 1, 2]
formation = []
for q in charges:
    O_rich = []
    O_poor = []
    if q == 0:
        for ef in fermi_levels:
            O_poor.append(neutral_O_poor)
            O_rich.append(4.5)
    elif q == 1:
        for ef in fermi_levels:
            O_poor.append(round(H1_OP(ef), 4))
            O_rich.append(round(H1_OR(ef), 4))
    elif q == 2:
        for ef in fermi_levels:
            O_poor.append(round(H2_OP(ef), 4))
            O_rich.append(round(H2_OR(ef), 4))
    formation.append({
        "charge": q,
        "fermi_levels": fermi_levels,
        "O_rich": O_rich,
        "O_poor": O_poor
    })

data = {
    "bulk_band_gap": band_gap,
    "transition_level_plus2plus": transition_level,
    "transition_level_0plus": transition_level,
    "neutral_formation_energy_O_poor": neutral_O_poor,
    "formation_energies": formation
}
with open("/app/outputs/computed_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'
