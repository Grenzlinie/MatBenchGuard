#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'JSONEOF'
{
  "Ir210_atop": {
    "binding_energy_eV": 2.95,
    "frequency_cm-1": 1869
  },
  "Ir210_bridge": {
    "binding_energy_eV": 2.42,
    "frequency_cm-1": 1650
  },
  "Ir110_atop": {
    "binding_energy_eV": 2.35,
    "frequency_cm-1": 1793
  },
  "Ir110_bridge": {
    "binding_energy_eV": 2.31,
    "frequency_cm-1": 1665
  },
  "Ir311_atop": {
    "binding_energy_eV": 2.34,
    "frequency_cm-1": 1864
  },
  "Ir311_bridge": {
    "binding_energy_eV": 2.51,
    "frequency_cm-1": 1676
  }
}
JSONEOF
