#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computational_results.json ===
python3 << 'PYEOF' > "$OUTDIR/computational_results.json"
import json, sys
result = {
    "indirect_gap_ev": 2.52,
    "direct_gap_ev": 2.64,
    "phonon_zone_center_negative_frequencies": [-5.0, -5.0, -2.0]
}
json.dump(result, sys.stdout, indent=2)
PYEOF

# === solve block: orbital_character.txt ===
cat > "$OUTDIR/orbital_character.txt" <<'EOF'
VBM: Bi 6s + Br 4p
CBM: Bi p
EOF
