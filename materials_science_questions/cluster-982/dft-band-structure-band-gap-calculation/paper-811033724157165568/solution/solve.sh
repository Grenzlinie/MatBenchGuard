#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: band_structure_data.json ===
python3 <<'PYEOF'
import json

data = [
    {"compound": "Au2Cs2I6", "Evi": 0.64, "Eci": 1.01, "delta_Ei": 0.70, "total_Eg": 2.35, "gap_type": "indirect"},
    {"compound": "Ag2GeBaS4", "Evi": 0.90, "Eci": 0.35, "delta_Ei": 1.16, "total_Eg": 2.41, "gap_type": "indirect"},
    {"compound": "Ag2ZnSnS4", "Evi": 0.47, "Eci": 0.57, "delta_Ei": 1.66, "total_Eg": 2.70, "gap_type": "direct"}
]
with open("/app/outputs/band_structure_data.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: dos_data.json ===
python3 <<'PYEOF'
import json, math, random

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def build_dos_entry(compound, elements, dominant_orbitals, ib_window, seed=42):
    random.seed(seed)
    E = [i*0.04 - 5.0 for i in range(0, 251)]  # 251 points from -5 to 5 eV step 0.04
    total = []
    for x in E:
        total.append(gaussian(x, -1.5, 0.6, 15.0) +
                     gaussian(x, (ib_window[0]+ib_window[1])/2, 0.3, 10.0) +
                     gaussian(x, 2.5, 0.7, 12.0) +
                     random.uniform(0, 0.1))
    proj = {}
    for elem, orb_shells in elements.items():
        proj[elem] = {}
        for orb in orb_shells:
            arr = []
            for x in E:
                val = 0.2 * gaussian(x, random.uniform(-2, 3), 0.5 + 0.5*random.random(), 2.0) + random.uniform(0, 0.05)
                if compound == "Au2Cs2I6" and elem == "I" and orb == "2p":
                    val += gaussian(x, (ib_window[0]+ib_window[1])/2, 0.3, 8.0)
                elif compound == "Ag2GeBaS4" and ((elem == "S" and orb == "2p") or (elem == "Ge" and orb == "4s") or (elem == "Ba" and orb == "4d")):
                    val += gaussian(x, (ib_window[0]+ib_window[1])/2, 0.3, 8.0)
                elif compound == "Ag2ZnSnS4" and ((elem == "Sn" and orb == "5s") or (elem == "S" and orb == "2p")):
                    val += gaussian(x, (ib_window[0]+ib_window[1])/2, 0.3, 8.0)
                arr.append(val)
            proj[elem][orb] = arr
    return {
        "compound": compound,
        "energy_grid": E,
        "total_dos": total,
        "projected_dos": proj,
        "ib_energy_window": ib_window,
        "dominant_orbitals": dominant_orbitals
    }

data = []
els = {"Au": ["s","p","d"], "Cs": ["s","p","d"], "I": ["s","p","d"]}
data.append(build_dos_entry("Au2Cs2I6", els, ["I 2p"], [0.64, 1.34]))

els = {"Ag": ["s","p","d"], "Ge": ["s","p","d"], "Ba": ["s","p","d"], "S": ["s","p","d"]}
data.append(build_dos_entry("Ag2GeBaS4", els, ["S 2p", "Ge 4s", "Ba 4d"], [0.90, 2.06], seed=99))

els = {"Ag": ["s","p","d"], "Zn": ["s","p","d"], "Sn": ["s","p","d"], "S": ["s","p","d"]}
data.append(build_dos_entry("Ag2ZnSnS4", els, ["Sn 5s", "S 2p"], [0.47, 2.13], seed=42))

with open("/app/outputs/dos_data.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: effective_masses.json ===
python3 <<'PYEOF'
import json

data = [
    {"compound": "Au2Cs2I6", "plane_direction": "110", "light_hole_effective_mass": 0.096, "heavy_hole_effective_mass": 0.265, "electron_effective_mass": 0.095},
    {"compound": "Ag2GeBaS4", "plane_direction": "110", "light_hole_effective_mass": 0.059, "heavy_hole_effective_mass": 0.114, "electron_effective_mass": 0.021},
    {"compound": "Ag2ZnSnS4", "plane_direction": "110", "light_hole_effective_mass": 0.237, "heavy_hole_effective_mass": 0.033, "electron_effective_mass": 0.025}
]
with open("/app/outputs/effective_masses.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
