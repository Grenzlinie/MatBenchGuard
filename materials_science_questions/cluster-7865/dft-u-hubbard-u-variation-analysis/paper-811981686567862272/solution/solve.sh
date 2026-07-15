#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: metals_properties.json ===
cat > "$OUTDIR/metals_properties.json" <<'EOF'
{
  "Th": {
    "LDA": {"V": 27, "Ecoh": -5.96, "B": 100},
    "GC": {"V": 27.46, "Ecoh": -5.73, "B": 102}
  },
  "Pa": {
    "LDA": {"V": 22.01, "Ecoh": -4.90, "B": 147},
    "GC": {"V": 22.48, "Ecoh": -4.55, "B": 141}
  },
  "U": {
    "LDA": {"V": 19.14, "Ecoh": -4.08, "B": 212},
    "GC": {"V": 19.67, "Ecoh": -3.50, "B": 181}
  }
}
EOF

# === solve block: uo2_properties.json ===
cat > "$OUTDIR/uo2_properties.json" <<'EOF'
{
  "LDA": {"a0": 5.25, "B": 261, "Ecoh": -1.63},
  "GC": {"a0": 5.27, "B": 252, "Ecoh": -1.37}
}
EOF

# === solve block: tho2_properties.json ===
cat > "$OUTDIR/tho2_properties.json" <<'EOF'
{
  "LDA": {"a0": 5.636, "B": 209, "Ecoh": -1.70},
  "GC": {"a0": 5.662, "B": 200, "Ecoh": -1.53}
}
EOF

# === solve block: vacancy_formation_energy.json ===
cat > "$OUTDIR/vacancy_formation_energy.json" <<'EOF'
{
  "formation_energy": 10.0
}
EOF
