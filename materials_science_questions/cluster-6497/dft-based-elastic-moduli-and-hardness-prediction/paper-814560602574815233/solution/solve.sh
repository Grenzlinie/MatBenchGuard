#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bulk_moduli.json ===
cat > "$OUTDIR/bulk_moduli.json" <<'FFEOF'
{
  "carbonates": [
    {"carbonate": "NiCO3", "K0_GPa": 131, "K0_err": 1},
    {"carbonate": "MgCO3", "K0_GPa": 107, "K0_err": 1},
    {"carbonate": "CoCO3", "K0_GPa": 125, "K0_err": 1},
    {"carbonate": "ZnCO3", "K0_GPa": 124, "K0_err": 1},
    {"carbonate": "MnCO3", "K0_GPa": 107, "K0_err": 1},
    {"carbonate": "CdCO3", "K0_GPa": 97, "K0_err": 1},
    {"carbonate": "CaCO3", "K0_GPa": 67, "K0_err": 2}
  ]
}
FFEOF

# === solve block: axial_compressibilities.json ===
cat > "$OUTDIR/axial_compressibilities.json" <<'FFEOF'
{
  "carbonates": [
    {"carbonate": "NiCO3", "ba": 1.74, "bc": 3.48, "bV": 6.86},
    {"carbonate": "MgCO3", "ba": 2.13, "bc": 4.03, "bV": 8.15},
    {"carbonate": "CoCO3", "ba": 1.67, "bc": 3.87, "bV": 7.10},
    {"carbonate": "ZnCO3", "ba": 1.60, "bc": 4.07, "bV": 7.18},
    {"carbonate": "MnCO3", "ba": 1.71, "bc": 4.96, "bV": 8.25},
    {"carbonate": "CdCO3", "ba": 1.28, "bc": 6.51, "bV": 8.95},
    {"carbonate": "CaCO3", "ba": 2.42, "bc": 9.34, "bV": 14.10}
  ]
}
FFEOF

# === solve block: subset_classification.json ===
cat > "$OUTDIR/subset_classification.json" <<'FFEOF'
{
  "alkaline_earth": ["MgCO3", "CaCO3"],
  "3d_transition_metal": ["NiCO3", "CoCO3", "MnCO3", "ZnCO3"],
  "4d_transition_metal": ["CdCO3"]
}
FFEOF
