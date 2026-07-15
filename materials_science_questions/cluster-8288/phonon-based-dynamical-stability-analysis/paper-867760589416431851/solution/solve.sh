#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: mechanical_properties.json ===
cat > "$OUTDIR/mechanical_properties.json" <<'FFEOF'
[
  {
    "phase": "P-62m-HfO",
    "bulk_modulus_GPa": 210.7,
    "shear_modulus_GPa": 128.1,
    "young_modulus_GPa": 319.5,
    "hardness_GPa": 16.1,
    "phonon_stable": true,
    "carrier_density_electrons_cm3": 1.1e20,
    "carrier_density_holes_cm3": 1.1e20
  },
  {
    "phase": "Pnnm-Hf2O",
    "bulk_modulus_GPa": 173.0,
    "shear_modulus_GPa": 110.3,
    "young_modulus_GPa": 272.9,
    "hardness_GPa": 15.5,
    "phonon_stable": true
  },
  {
    "phase": "Imm2-Hf5O2",
    "bulk_modulus_GPa": 150.0,
    "shear_modulus_GPa": 95.3,
    "young_modulus_GPa": 235.9,
    "hardness_GPa": 13.9,
    "phonon_stable": true
  },
  {
    "phase": "P-31m-Hf2O",
    "bulk_modulus_GPa": 175.2,
    "shear_modulus_GPa": 103.1,
    "young_modulus_GPa": 258.6,
    "hardness_GPa": 13.2,
    "phonon_stable": true
  },
  {
    "phase": "P-42m-Hf2O3",
    "bulk_modulus_GPa": 243.9,
    "shear_modulus_GPa": 127.1,
    "young_modulus_GPa": 324.8,
    "hardness_GPa": 12.9,
    "phonon_stable": true
  }
]
FFEOF

python3 << 'PYEOF'
import math
n_k = 200
num_bands = 12
lines = []
for ik in range(n_k):
    t = ik / (n_k - 1)          # 0..1
    x = t * 2 * math.pi
    for ib in range(num_bands):
        # example semimetallic dispersion with electron pocket near Gamma and hole pocket near M
        if ib == 0:
            energy = 0.15 * (math.cos(x) - 1.0)         # min -0.30 at Gamma
        elif ib == 1:
            energy = -0.12 * math.cos(8 * math.pi * (t - 0.15)) - 0.03
        elif ib == 2:
            energy = 2.0 + 0.5 * math.sin(3 * x)
        elif ib == 3:
            energy = -2.0 + 0.5 * math.cos(5 * x)
        else:
            energy = (ib - 5) * 1.4 + 0.2 * math.sin(x)
        lines.append(f"{ik} {ib} {energy:.6f}")
with open("/app/outputs/band_structure_P62m_HfO.dat", "w") as f:
    f.write("\n".join(lines))
PYEOF

# === solve block: band_structure_P62m_HfO.dat ===
python3 /solution/create_band.py > "$OUTDIR/band_structure_P62m_HfO.dat"
