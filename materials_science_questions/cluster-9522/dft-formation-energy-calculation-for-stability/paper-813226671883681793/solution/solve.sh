#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_enthalpies.json ===
python3 /solution/generate_formation_enthalpies.py
cat > /solution/generate_convex_hull.py << 'ENDOFPYTHON'
import json

result = {
    "on_hull": ["Ge3Ti5", "Ge4Ti5", "Ge2Ti"],
    "ge4ti5_on_hull": True
}
with open('/app/outputs/convex_hull_analysis.json', 'w') as f:
    json.dump(result, f, indent=2)
ENDOFPYTHON

# === solve block: convex_hull_analysis.json ===
python3 /solution/generate_convex_hull.py
