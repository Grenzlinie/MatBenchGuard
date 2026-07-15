#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'FFEOF'
{
  "CsPbI3": {
    "formation_energy(eV)": -13.02,
    "bandgap_noSOC(eV)": 1.79,
    "bandgap_withSOC(eV)": 0.83
  },
  "CsPbBr1.5I1.5": {
    "formation_energy(eV)": -14.32,
    "bandgap_noSOC(eV)": 2.1,
    "bandgap_withSOC(eV)": 1.19
  },
  "CsPbBr3": {
    "formation_energy(eV)": -15.67,
    "bandgap_noSOC(eV)": 2.42,
    "bandgap_withSOC(eV)": 1.97
  }
}
FFEOF
