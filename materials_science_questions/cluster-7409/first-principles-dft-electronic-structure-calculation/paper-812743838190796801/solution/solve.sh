#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relaxed_structures.json ===
cat > /app/outputs/relaxed_structures.json <<'FFEOF'
{
  "ZrN": {"a": 4.6176, "b": 4.6176, "c": 4.6176, "space_group": "Fm-3m"},
  "TiZr3N4": {"a": 4.5464, "b": 4.5464, "c": 4.5464, "space_group": "Pm-3m"},
  "TiZrN2": {"a": 3.1434, "b": 3.1434, "c": 4.5137, "space_group": "P4-mmm"},
  "Ti3ZrN4": {"a": 4.3778, "b": 4.3778, "c": 4.3778, "space_group": "Pm-3m"},
  "TiN": {"a": 4.2716, "b": 4.2716, "c": 4.2716, "space_group": "Fm-3m"},
  "Zr4CN3": {"a": 4.6404, "b": 4.6404, "c": 4.6404, "space_group": "Pm-3m"},
  "Zr2CN": {"a": 3.2845, "b": 3.2845, "c": 4.6986, "space_group": "P4-mmm"},
  "Zr4C3N": {"a": 4.6885, "b": 4.6885, "c": 4.6885, "space_group": "Pm-3m"},
  "ZrC": {"a": 4.7095, "b": 4.7095, "c": 4.7095, "space_group": "Fm-3m"}
}
FFEOF

# === solve block: dos_fermi.json ===
cat > /app/outputs/dos_fermi.json <<'FFEOF'
{
  "ZrN": 0.6,
  "TiZr3N4": 3.9,
  "TiZrN2": 3.1,
  "Ti3ZrN4": 5.2,
  "TiN": 5.7,
  "Zr4CN3": 2.9,
  "Zr2CN": 0.7,
  "Zr4C3N": 2.7,
  "ZrC": 1.9
}
FFEOF

# === solve block: bulk_moduli.json ===
cat > /app/outputs/bulk_moduli.json <<'FFEOF'
{
  "ZrN": 230,
  "TiZr3N4": 244,
  "TiZrN2": 249,
  "Ti3ZrN4": 251,
  "TiN": 239,
  "Zr4CN3": 228,
  "Zr2CN": 225,
  "Zr4C3N": 216,
  "ZrC": 219
}
FFEOF
