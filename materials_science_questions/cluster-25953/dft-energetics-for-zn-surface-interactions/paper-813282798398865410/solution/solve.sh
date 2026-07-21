#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reaction_energies.json ===
cat > /app/outputs/reaction_energies.json <<'FFEOF'
{
  "H2S_a": { "relative_energy_kJmol": 0.0 },
  "TS1":   { "relative_energy_kJmol": 35.66 },
  "SH_H_a":{ "relative_energy_kJmol": 6.13 },
  "TS2":   { "relative_energy_kJmol": 57.60 },
  "S_2H_b":{ "relative_energy_kJmol": 26.88 },
  "TS3":   { "relative_energy_kJmol": 325.12 },
  "P1":    { "relative_energy_kJmol": 305.27 },
  "TS4":   { "relative_energy_kJmol": 246.85 },
  "S_2H_c":{ "relative_energy_kJmol": -110.70 },
  "TS5":   { "relative_energy_kJmol": 88.75 },
  "P2":    { "relative_energy_kJmol": 216.61 },
  "TS6":   { "relative_energy_kJmol": -13.15 },
  "P3":    { "relative_energy_kJmol": -166.47 }
}
FFEOF
