#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: free_energy_diagram.json ===
cat > "$OUTDIR/free_energy_diagram.json" <<'HEREDOC_END'
[
  {
    "system": "Zn(100)",
    "steps": [
      {"label": "CO2(g)", "energy_eV": 0.0},
      {"label": "*COOH", "energy_eV": -0.83},
      {"label": "*CO", "energy_eV": -0.03},
      {"label": "CO(g)+*", "energy_eV": -0.20}
    ]
  },
  {
    "system": "CuZn(100)",
    "steps": [
      {"label": "CO2(g)", "energy_eV": 0.0},
      {"label": "*COOH", "energy_eV": -0.61},
      {"label": "*CO", "energy_eV": -0.04},
      {"label": "CO(g)+*", "energy_eV": -0.20}
    ]
  }
]
HEREDOC_END
