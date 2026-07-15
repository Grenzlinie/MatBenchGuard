#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs
export OUTDIR

# === solve block: optimized_lattice.json ===
# Write optimized_lattice.json
python3 -c '
import json, os
data = {
    "pseudocubic_110": {
        "a": 6.46,
        "b": 6.44,
        "c": 6.47,
        "alpha": 88.5,
        "beta": 89.7,
        "gamma": 89.6,
        "volume": 269.0
    },
    "pseudocubic_111": {
        "a": 6.452,
        "b": 6.452,
        "c": 6.452,
        "alpha": 89.4,
        "beta": 89.4,
        "gamma": 89.4,
        "volume": 268.52
    },
    "orthorhombic": {
        "a": 8.86,
        "b": 12.62,
        "c": 8.85,
        "alpha": 90.0,
        "beta": 90.0,
        "gamma": 90.0,
        "volume": 990.1
    }
}
with open(os.path.join(os.environ["OUTDIR"], "optimized_lattice.json"), "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: bandgaps_and_rashba.json ===
# Write bandgaps_and_rashba.json
python3 - <<'PYEOF'
import json

data = {
    "pseudocubic_110": {
        "Eg_nonSOC": 1.79,
        "nature_nonSOC": "indirect",
        "Eg_SOC": 0.76,
        "nature_SOC": "indirect",
        "Rashba_CB_splitting": 0.0647,
        "Rashba_VB_splitting": 0.017,
        "k0_CB": 0.052,
        "k0_VB": 0.035
    },
    "pseudocubic_111": {
        "Eg_nonSOC": 1.62,
        "nature_nonSOC": "direct",
        "Eg_SOC": 0.60,
        "nature_SOC": "direct",
        "Rashba_CB_splitting": 0.01328,
        "Rashba_VB_splitting": 0.00296,
        "k0_CB": 0.017,
        "k0_VB": 0.017
    },
    "orthorhombic": {
        "Eg_nonSOC": 1.84,
        "nature_nonSOC": "direct",
        "Eg_SOC": 0.94,
        "nature_SOC": "direct",
        "Rashba_CB_splitting": None,
        "Rashba_VB_splitting": None,
        "k0_CB": None,
        "k0_VB": None
    }
}
with open("/app/outputs/bandgaps_and_rashba.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: effective_masses.json ===
# Write effective_masses.json
python3 - <<'PYEOF'
import json

data = {
    "pseudocubic_110": {
        "mh_star_nonSOC": 0.50,
        "me_star_nonSOC": 0.60,
        "mh_star_SOC": 0.33,
        "me_star_SOC": 0.17
    },
    "pseudocubic_111": {
        "mh_star_nonSOC": 0.25,
        "me_star_nonSOC": 0.43,
        "mh_star_SOC": 0.18,
        "me_star_SOC": 0.13
    },
    "orthorhombic": {
        "mh_star_nonSOC": 0.37,
        "me_star_nonSOC": 0.32,
        "mh_star_SOC": 0.33,
        "me_star_SOC": 0.24
    }
}
with open("/app/outputs/effective_masses.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: binding_energies.json ===
# Write binding_energies.json
python3 - <<'PYEOF'
import json

# Conversion factor kcal/mol -> eV (1 eV = 23.060548 kcal/mol)
kcal_to_ev = 1.0 / 23.060548

entries = []

# Pseudocubic blocks from Figure 2 (C-G), using Def2-TZVPPD values where available
# Fig2C
entries.append({
    "system": "pseudocubic",
    "block_label": "Fig2C",
    "ΔE_BSSE_kcal_per_mol": -129.81,
    "ΔE_BSSE_eV": round(-129.81 * kcal_to_ev, 4)
})
# Fig2D
entries.append({
    "system": "pseudocubic",
    "block_label": "Fig2D",
    "ΔE_BSSE_kcal_per_mol": -121.03,
    "ΔE_BSSE_eV": round(-121.03 * kcal_to_ev, 4)
})
# Fig2E
entries.append({
    "system": "pseudocubic",
    "block_label": "Fig2E",
    "ΔE_BSSE_kcal_per_mol": -99.28,
    "ΔE_BSSE_eV": round(-99.28 * kcal_to_ev, 4)
})
# Fig2F
entries.append({
    "system": "pseudocubic",
    "block_label": "Fig2F",
    "ΔE_BSSE_kcal_per_mol": -96.49,
    "ΔE_BSSE_eV": round(-96.49 * kcal_to_ev, 4)
})
# Fig2G: Def2-TZVPPD failed; paper reports DZP value -64.98 kcal/mol and -2.818 eV
entries.append({
    "system": "pseudocubic",
    "block_label": "Fig2G",
    "ΔE_BSSE_kcal_per_mol": -64.98,
    "ΔE_BSSE_eV": -2.818
})

# Orthorhombic blocks from Figure 3 (A-C), using PBE/Def2-TZVPPD results
# Fig3A: strongest I...H hydrogen bond pair
entries.append({
    "system": "orthorhombic",
    "block_label": "Fig3A",
    "ΔE_BSSE_kcal_per_mol": -109.20,
    "ΔE_BSSE_eV": -4.737
})
# Fig3B: about 4.0 kcal/mol less stable than A (text: "4.0 kcal mol⁻¹ less stable")
entries.append({
    "system": "orthorhombic",
    "block_label": "Fig3B",
    "ΔE_BSSE_kcal_per_mol": -105.20,
    "ΔE_BSSE_eV": round(-105.20 * kcal_to_ev, 4)
})
# Fig3C: I...F halogen bond
entries.append({
    "system": "orthorhombic",
    "block_label": "Fig3C",
    "ΔE_BSSE_kcal_per_mol": -79.42,
    "ΔE_BSSE_eV": -3.444
})

with open("/app/outputs/binding_energies.json", "w") as f:
    json.dump(entries, f, indent=2)
PYEOF

# === solve finalize ===
echo "All reference outputs written."
