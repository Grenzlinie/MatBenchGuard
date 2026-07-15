#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: elastic_dielectric_properties.json ===
cat > "$OUTDIR/elastic_dielectric_properties.json" <<'FFEOF'
{
  "c11": 371,
  "c12": 116,
  "c44": 127,
  "eps_s": 115.5,
  "eps_inf": 1.80,
  "phonon_frequencies": [
    {"mode": "TO1", "frequency": 96},
    {"mode": "LO1", "frequency": 488},
    {"mode": "TO2", "frequency": 194},
    {"mode": "LO2", "frequency": 194},
    {"mode": "TO3", "frequency": 492},
    {"mode": "LO3", "frequency": 777}
  ]
}
FFEOF

# === solve block: vacancy_formation_energies.json ===
cat > "$OUTDIR/vacancy_formation_energies.json" <<'FFEOF'
{
  "V_O": 20.44,
  "V_K": 5.76,
  "V_Nb": 122.83
}
FFEOF

# === solve block: o_migration_energy.json ===
cat > "$OUTDIR/o_migration_energy.json" <<'FFEOF'
{
  "energy": 0.68
}
FFEOF
