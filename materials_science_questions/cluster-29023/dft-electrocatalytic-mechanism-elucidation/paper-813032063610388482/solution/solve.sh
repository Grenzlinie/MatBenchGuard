#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: homolumo_gaps.csv ===
cat > "$OUTDIR/homolumo_gaps.csv" <<'FFEOF'
config_name,homo,lumo,gap
Graphitic N-inside,-4.0,-3.757,0.243
Graphitic N-edge,-4.0,-3.754,0.246
Pyridinic N-inside,-4.0,-2.324,1.676
Pyridinic N-edge,-4.0,-3.749,0.251
Pyrrolic N-edge,-4.0,-2.108,1.892
FFEOF

# === solve block: active_sites.json ===
cat > "$OUTDIR/active_sites.json" <<'FFEOF'
{
  "Graphitic N-inside": [
    {"atom_label": "C27", "element": "C", "charge": 0.1295, "spin": 0.0687},
    {"atom_label": "C28", "element": "C", "charge": 0.0265, "spin": 0.1191},
    {"atom_label": "C29", "element": "C", "charge": -0.1583, "spin": 0.1594},
    {"atom_label": "C40", "element": "C", "charge": 0.1475, "spin": -0.0095},
    {"atom_label": "N37", "element": "N", "charge": -0.0095, "spin": 0.1102}
  ],
  "Graphitic N-edge": [
    {"atom_label": "C11", "element": "C", "charge": -0.0842, "spin": 0.1920},
    {"atom_label": "C12", "element": "C", "charge": -0.1642, "spin": 0.1014},
    {"atom_label": "C15", "element": "C", "charge": 0.1325, "spin": 0.0312},
    {"atom_label": "C18", "element": "C", "charge": 0.0264, "spin": 0.1128}
  ],
  "Pyridinic N-inside": [
    {"atom_label": "C43", "element": "C", "charge": 0.1754, "spin": -0.0010},
    {"atom_label": "C49", "element": "C", "charge": 0.1777, "spin": -0.0007}
  ],
  "Pyridinic N-edge": [
    {"atom_label": "N11", "element": "N", "charge": -0.2365, "spin": 0.1155},
    {"atom_label": "C12", "element": "C", "charge": -0.1292, "spin": 0.1025},
    {"atom_label": "C14", "element": "C", "charge": 0.1539, "spin": 0.0666},
    {"atom_label": "C17", "element": "C", "charge": 0.1539, "spin": 0.0666},
    {"atom_label": "C19", "element": "C", "charge": -0.1292, "spin": 0.1025},
    {"atom_label": "C21", "element": "C", "charge": -0.1442, "spin": 0.1004},
    {"atom_label": "C24", "element": "C", "charge": 0.0345, "spin": 0.1071},
    {"atom_label": "C30", "element": "C", "charge": -0.1442, "spin": 0.1005}
  ],
  "Pyrrolic N-edge": [
    {"atom_label": "C12", "element": "C", "charge": 0.1425, "spin": -0.0006},
    {"atom_label": "C13", "element": "C", "charge": 0.1425, "spin": -0.0006}
  ]
}
FFEOF
