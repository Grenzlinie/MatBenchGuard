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
cat > "$OUTDIR"/mechanical_properties.json << 'EOF'
{
  "x": {"Young_modulus_GPa": 204.0, "ultimate_strain": 0.25, "breaking_strength_GPa": 21.85},
  "y": {"Young_modulus_GPa": 210.0, "ultimate_strain": 0.19, "breaking_strength_GPa": 14.35},
  "xy": {"Young_modulus_GPa": 259.0, "ultimate_strain": 0.24, "breaking_strength_GPa": 25.20}
}
EOF

# === solve block: diffusion_barriers.json ===
python3 << 'PYEOF' > "$OUTDIR"/diffusion_barriers.json
import json, sys
data = {
    "Se_side_pathI_barrier_eV": 0.035,
    "S_side_pathI_barrier_eV": 0.052
}
json.dump(data, sys.stdout, indent=2)
PYEOF

# === solve block: adsorption_energies.json ===
python3 << 'PYEOF' > "$OUTDIR"/adsorption_energies.json
import json, sys
data = {
    "1": {"capacity_mAh_g": 129.5, "E_avg_eV": -1.520, "E_layer_eV": -1.520, "voltage_V": 1.520, "volume_expansion_percent": 1.43},
    "2": {"capacity_mAh_g": 258.9, "E_avg_eV": -1.493, "E_layer_eV": -1.466, "voltage_V": 0.733, "volume_expansion_percent": 3.53},
    "3": {"capacity_mAh_g": 388.5, "E_avg_eV": -1.445, "E_layer_eV": -1.348, "voltage_V": 0.449, "volume_expansion_percent": 3.87},
    "4": {"capacity_mAh_g": 517.9, "E_avg_eV": -1.422, "E_layer_eV": -1.354, "voltage_V": 0.338, "volume_expansion_percent": 4.51},
    "5": {"capacity_mAh_g": 647.5, "E_avg_eV": -1.406, "E_layer_eV": -1.341, "voltage_V": 0.268, "volume_expansion_percent": 4.72},
    "6": {"capacity_mAh_g": 776.9, "E_avg_eV": -1.375, "E_layer_eV": -1.308, "voltage_V": 0.218, "volume_expansion_percent": 5.12},
    "7": {"capacity_mAh_g": 906.5, "E_avg_eV": -1.366, "E_layer_eV": -1.305, "voltage_V": 0.186, "volume_expansion_percent": 5.62},
    "8": {"capacity_mAh_g": 1035.9, "E_avg_eV": -1.329, "E_layer_eV": -1.299, "voltage_V": 0.143, "volume_expansion_percent": 6.08}
}
json.dump(data, sys.stdout, indent=2)
PYEOF
