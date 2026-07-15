#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: vibrational_frequencies.csv ===
cat > /app/outputs/vibrational_frequencies.csv <<'FFEOF'
intermediate,site_label,mode,frequency_cm-1
*OCHCH2,OD-Cu-297,CCO symmetric stretching,1182
*OCHCH2,OD-Cu-297,CCO antisymmetric stretching,1318
*OCHCH2,OD-Cu-297,C-C stretching,1453
*OCHCH2,OD-Cu-297,C-O stretching,1595
FFEOF

# === solve block: binding_energies.csv ===
cat > /app/outputs/binding_energies.csv <<'FFEOF'
intermediate,site_label,binding_energy_eV,formation_energy_eV
*OCHCH2,OD-Cu-297,-1.2,-1.2
FFEOF
