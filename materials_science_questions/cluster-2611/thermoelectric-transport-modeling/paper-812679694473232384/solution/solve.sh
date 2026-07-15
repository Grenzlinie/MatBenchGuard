#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bandgap.json ===
cat > "$OUTDIR/bandgap.json" <<'FFEOF'
{
  "bandgap_eV": 1.06
}
FFEOF

# === solve block: adsorption_energy.json ===
cat > "$OUTDIR/adsorption_energy.json" <<'FFEOF'
{
  "adsorption_energy_eV": -0.92
}
FFEOF

# === solve block: power_factor_enhancement.json ===
cat > "$OUTDIR/power_factor_enhancement.json" <<'FFEOF'
{
  "temperature_K": 300,
  "GeSe_max_power_factor_W_per_mKs": 1.117e10,
  "GQD_GeSe_max_power_factor_W_per_mKs": 5.385e10,
  "power_factor_enhancement_ratio": 4.820
}
FFEOF
